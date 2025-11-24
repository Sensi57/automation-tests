import json
from selenium import webdriver

with open("browserstack_config.json") as f:
    config = json.load(f)

def test_firefox_title():
    options = webdriver.FirefoxOptions()
    options.set_capability('bstack:options', {
        "os": "Windows",
        "osVersion": "11",
        "browserVersion": "latest",
        "sessionName": "Firefox Test"
    })

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options,
        desired_capabilities={
            "browserName": "firefox",
            "browserVersion": "latest",
            "bstack:options": {
                "userName": config["user"],
                "accessKey": config["key"]
            }
        }
    )

    driver.get("https://google.com")
    assert "Google" in driver.title
    driver.quit()