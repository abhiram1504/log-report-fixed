import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """Success criterion 1: the agent writes a file to /app/report.json."""
    assert REPORT.exists(), "no report.json found"


def test_report_is_valid_json():
    """Success criterion 2: the file contains valid JSON."""
    try:
        json.loads(REPORT.read_text())
    except json.JSONDecodeError:
        assert False, "report.json is not valid JSON"


def test_total_requests_is_positive_integer():
    """Success criterion 3: total_requests is a positive integer."""
    data = json.loads(REPORT.read_text())
    assert "total_requests" in data, "missing key: total_requests"
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert data["total_requests"] > 0, "total_requests must be greater than 0"


def test_unique_ips_is_positive_integer():
    """Success criterion 4: unique_ips is a positive integer."""
    data = json.loads(REPORT.read_text())
    assert "unique_ips" in data, "missing key: unique_ips"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert data["unique_ips"] > 0, "unique_ips must be greater than 0"


def test_top_path_is_nonempty_string():
    """Success criterion 5: top_path is a non-empty string."""
    data = json.loads(REPORT.read_text())
    assert "top_path" in data, "missing key: top_path"
    assert isinstance(data["top_path"], str), "top_path must be a string"
    assert data["top_path"].strip() != "", "top_path must not be empty"

def test_total_requests_correct_value():
    """Success criterion 3: total_requests matches actual line count in access.log."""
    expected = sum(1 for line in open("/app/access.log") if line.strip())
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == expected