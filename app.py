import streamlit as st
import time
import sys
import os
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from api import fetch_basic_repo_info
from url_parser import extract_repo_path
from logic import calculate_health_score

st.set_page_config(
    page_title="GitPulse",
    layout="centered"
)

st.title("GitPulse")
st.markdown("""
Welcome to the **GitPulse**! 
Enter a GitHub repository URL below to find out if the project is active, healthy, and beginner-friendly.
""")

url_input = st.text_input(
    "GitHub Repository URL:", 
    placeholder="https://github.com/ol1xy/GitPulse"
)

if st.button("Pulse Project", type="primary"):
    if not url_input:
        st.warning("Please enter a valid GitHub URL")
    else:
        repo_path = extract_repo_path(url_input)

        with st.spinner(f"Scanning '{repo_path}' via GitHub API..."):
            data = fetch_basic_repo_info(repo_path)
            health_scores = calculate_health_score(data)
                
            st.subheader(f"Repository Stats:")
            
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### Stars ⭐") # Это крупный заголовок
                st.markdown(f"<p style='font-size: 40px; font-weight: bold;'>{data['stars']:,}</p>", unsafe_allow_html=True)

            with col2:
                st.markdown("### Forks 🔜")
                st.markdown(f"<p style='font-size: 40px; font-weight: bold;'>{data['forks']:,}</p>", unsafe_allow_html=True)

            with col3:
                st.markdown("### Open Issues 🪲")
                st.markdown(f"<p style='font-size: 40px; font-weight: bold;'>{data['open_issues']:,}</p>", unsafe_allow_html=True)


            st.divider()

            st.subheader(f"Activity:")

            pushed_str = data.get("last_pushed")
            if pushed_str:
                pushed_date = datetime.strptime(pushed_str, "%Y-%m-%dT%H:%M:%SZ")
                st.write(f"**📤 Last Pushed:** `{pushed_date.strftime('%Y-%m-%d %H:%M UTC')}`")

            commit_data = data.get("latest_commit", {})
            commit_date_str = commit_data.get("date")
            
            days_ago = 0
            
            if commit_date_str:
                commit_date = datetime.strptime(commit_date_str, "%Y-%m-%dT%H:%M:%SZ")
                days_ago = (datetime.utcnow() - commit_date).days
                
                st.write(f"**💻 Latest Commit:** {days_ago} days ago by *{commit_data.get('author')}*")
                st.write(f"**📝 Message:**")
                st.markdown(f"```text\n{commit_data.get('message')}\n```")
            
            st.divider()

            st.subheader("Health & Community Report")

            community = health_scores["community"]
            engagement = health_scores["engagement"]
            activity = health_scores["activity"]

            if community["status"] == "good":
                st.success(f"🤝 **Community Score: {community['score']}/100** - Excellent! The project is welcoming and well-documented for beginners.")
            elif community["status"] == "warning":
                st.warning(f"⚠️ **Community Score: {community['score']}/100** - Acceptable, but lacks some key guidelines.")
            else:
                st.error(f"❌ **Community Score: {community['score']}/100** - Poor. Missing essential files. Might be hard for newcomers to contribute.")

            comm_files = data.get("community", {})
            
            def check_icon(found):
                return "✅" if found else "❌"

            st.markdown(f"""
            **Documentation Checklist:**
            * README {check_icon(comm_files.get('has_readme'))}
            * LICENSE {check_icon(comm_files.get('has_license'))}
            * CONTRIBUTING.md {check_icon(comm_files.get('has_contributing'))}
            * CODE_OF_CONDUCT.md {check_icon(comm_files.get('has_coc'))}
            """)
            
            st.write("")

            if engagement["status"] == "good":
                st.success(f"🔥 **Engagement Rate: {engagement['rate']}%** - High! A lot of users are actively forking and contributing.")
            elif engagement["status"] == "warning":
                st.warning(f"📊 **Engagement Rate: {engagement['rate']}%** - Average. Some users fork the project, but many just star it.")
            else:
                st.error(f"📉 **Engagement Rate: {engagement['rate']}%** - Low. Users like the project but rarely fork it to contribute.")

            if activity["is_abandoned"]:
                st.error(f"💀 **Activity Status:** Critical. Project seems abandoned. Last push was {activity['days_inactive']} days ago.")
            elif activity["status"] == "warning":
                st.warning(f"⏳ **Activity Status:** Slowing down. Last push was {activity['days_inactive']} days ago.")
            else:
                st.success(f"✅ **Activity Status:** Active and healthy! Last push was {activity['days_inactive']} days ago.")

            