import pytest

print("=== Running Chrome tests ===")
pytest.main(["tests/test_chrome.py", "-v"])

print("=== Running Firefox tests ===")
pytest.main(["tests/test_firefox.py", "-v"])

print("=== Running Safari tests ===")
pytest.main(["tests/test_safari.py", "-v"])

print("=== Running functional tests ===")
pytest.main(["tests/test1.py", "tests/test2.py", "-v"])