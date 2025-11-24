import json
from selenium import webdriver

with open("browserstack_config.json") as f:
    config = json.load(f)

def test_safari_title():
    options = webdriver.SafariOptions()
    options.set_capability('bstack:options', {
        "os": "OS X",
        "osVersion": "Ventura",
        "browserVersion": "latest",
        "sessionName": "Safari Test"
    })

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options,
        desired_capabilities={
            "browserName": "safari",
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