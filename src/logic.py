from datetime import datetime, timezone

def calculate_health_score(repo_data: dict) -> dict:
    """
    Analyzes raw repository data and calculates health scores.
    Returns a dictionary with scores and status flags. 
    """

    last_pushed_raw = repo_data.get("last_pushed")
    last_pushed_str = last_pushed_raw.replace("Z", "+00:00") if last_pushed_raw else ""

    is_abandoned = False
    days_inactive = 0
    activity_status = "unknown"

    if last_pushed_str:
        last_pushed_date = datetime.fromisoformat(last_pushed_str)
        now = datetime.now(timezone.utc)
        days_inactive = (now - last_pushed_date).days

        if days_inactive > 365:
            activity_status = "critical"
            is_abandoned = True

        elif days_inactive > 60:
            activity_status = "warning"

        else:
            activity_status = "good"

    community = repo_data.get("community", {})
    community_score = 0

    if community.get("has_readme"):
        community_score += 25
    if community.get("has_license"):
        community_score += 25
    if community.get("has_contributing"):
        community_score += 30 
    if community.get("has_coc"):
        community_score += 20

    friendly_status = "good" if community_score >= 75 else "warning"
    if community_score < 50:
        friendly_status = "critical"

    
    stars = repo_data.get("stars", 0)
    forks = repo_data.get("forks", 0)

    if stars == 0:
        engagement_rate = 0.0
        engagement_status = "critical"
    
    else:
        engagement_rate = round((forks/stars) * 100, 1)
        
        if engagement_rate > 10.0:
            engagement_status = "good"
        elif engagement_rate >= 5.0:
            engagement_status = "warning"
        else: 
            engagement_status = "critical"



    return {
        "activity": {
            "status": activity_status,
            "days_inactive": days_inactive,
            "is_abandoned": is_abandoned
        },

        "community": {
            "score": community_score,
            "status": friendly_status
        },

        "engagement": {
            "rate": engagement_rate, 
            "status": engagement_status
        }
    }

if __name__ == "__main__":

    mock_api_data = {
        "last_pushed": "2022-01-01T10:00:00Z", 
        "community": {
            "has_readme": True,
            "has_license": False,
            "has_contributing": False,
            "has_coc": False
        }
    }
    
    print(calculate_health_score(mock_api_data))
