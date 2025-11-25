import json
from selenium import webdriver

with open("browserstack_config.json") as f:
    config = json.load(f)


USERNAME = config["user"]
ACCESS_KEY = config["key"]

options = webdriver.FirefoxOptions()

bstack_options = {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Firefox Test"
}

options.set_capability('bstack:options', bstack_options)
options.set_capability('browserVersion', 'latest')

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=webdriver.ChromeOptions()
)

driver.get("https://google.com")
print(driver.title)

driver.quit()
