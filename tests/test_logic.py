import pytest
from datetime import datetime, timedelta, timezone
from src.logic import calculate_health_score

def generate_past_date(days_ago: int) -> str:
    """
    Generate ISO-string, going back through requirement number of days.
    """

    past_date = datetime.now(timezone.utc) - timedelta(days=days_ago)
    return past_date.isoformat().replace("+00:00", "Z")

@pytest.mark.parametrize("days_ago, expected_status, expected_abandoned",
                         [
                             (10, "good", False),
                             (100, "warning", False),
                             (400, "critical", True),
                         ])
def test_activity_logic(days_ago, expected_status, expected_abandoned):
    mock_data = {"last_pushed": generate_past_date(days_ago)}

    result = calculate_health_score(mock_data)

    assert result["activity"]["status"] == expected_status
    assert result["activity"]["is_abandoned"] == expected_abandoned


def test_activity_missing_date():
    result = calculate_health_score({"last_pushed": None})
    assert result["activity"]["status"] == "unknown"


@pytest.mark.parametrize("community_files, expected_score, expected_status", [
    ({"has_readme": True, "has_license": True, "has_contributing": True, "has_coc": True}, 100, "good"),
    
    ({"has_readme": True, "has_license": True, "has_contributing": False, "has_coc": False}, 50, "warning"),
    
    ({"has_readme": True, "has_license": False, "has_contributing": False, "has_coc": False}, 25, "critical"),
    
    ({"has_readme": False, "has_license": False, "has_contributing": False, "has_coc": False}, 0, "critical"),
])
def test_community_logic(community_files, expected_score,
                         expected_status):
    mock_data = {"community": community_files}
    result = calculate_health_score(mock_data)

    assert result["community"]["score"] == expected_score
    assert result["community"]["status"] == expected_status


@pytest.mark.parametrize("stars, forks, expected_rate, expected_status", [
    (1000, 150, 15.0, "good"),
    (1000, 70, 7.0, "warning"),
    (1000, 10, 1.0, "critical"),
    (0, 0, 0.0, "critical"),
])
def test_engagement_logic(stars, forks, expected_rate, expected_status):
    mock_data = {
        "stars": stars,
        "forks": forks
    }
    result = calculate_health_score(mock_data)
    
    assert result["engagement"]["rate"] == expected_rate
    assert result["engagement"]["status"] == expected_status