import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

with open("browserstack_config.json") as f:
    config = json.load(f)

capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",
    "bstack:options": {
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "Chrome Test"
    }
}

driver = webdriver.Remote(
    command_executor=f"https://{config.user}:{config.key}@hub.browserstack.com/wd/hub",
    options=webdriver.ChromeOptions()
)

driver.capabilities.update(capabilities)

driver.get("https://google.com")
print(driver.title)

driver.quit()
