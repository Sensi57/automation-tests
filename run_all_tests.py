import pytest

# Запуск всех тестов одновременно
pytest.main([
    "tests/test_chrome.py",
    "tests/test_firefox.py",
    "tests/test_safari.py",
    "tests/test1.py",
    "tests/test2.py",
    "-v"
])