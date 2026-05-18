import streamlit as st
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from api import fetch_basic_repo_info
from url_parser import extract_repo_path


st.title("GitPulse")
st.markdown("""
Welcome to the **GitPulse**! 
Enter a GitHub repository URL below to find out if the project is active, healthy, and beginner-friendly.
""")

st.set_page_config(
    page_title="GitPulse",
    layout="centered"
)

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
                
            st.subheader(f"📊 Repository Stats:")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Stars ⭐", value=f"{data['stars']:,}")
            with col2:
                st.metric(label="Forks 🔜", value=f"{data['forks']:,}")
            with col3:
                st.metric(label="Open Issues 🪲", value=f"{data['open_issues']:,}")

            st.divider()

            