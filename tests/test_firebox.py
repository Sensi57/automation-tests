import json
from selenium import webdriver

with open("browserstack_config.json") as f:
    config = json.load(f)


options = webdriver.FirefoxOptions()

bstack_options = {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Firefox Test"
}

options.set_capability('bstack:options', bstack_options)
options.set_capability('browserVersion', 'latest')

driver = webdriver.Remote(
    command_executor=f"https://{config.user}:{config.key}@hub.browserstack.com/wd/hub",
    options=webdriver.ChromeOptions()
)

driver.get("https://google.com")
print(driver.title)

driver.quit()
