import json
from selenium import webdriver

with open("browserstack_config.json") as f:
    config = json.load(f)

def test_chrome_title():
    options = webdriver.ChromeOptions()
    options.set_capability('bstack:options', {
        "os": "OS X",
        "osVersion": "Ventura",
        "browserVersion": "latest",
        "sessionName": "Chrome Test"
    })

    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=options,
        desired_capabilities={
            "browserName": "chrome",
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