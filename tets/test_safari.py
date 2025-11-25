from selenium import webdriver

USERNAME = "aleksturnitin_G6Kx1d"
ACCESS_KEY = "KT81txcpLzPmjFpQ1DMT"

options = webdriver.SafariOptions()

bstack_options = {
    "os": "OS X",
    "osVersion": "Sonoma",
    "sessionName": "Safari Test"
}

options.set_capability('bstack:options', bstack_options)
options.set_capability('browserVersion', 'latest')

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)
driver.get("https://google.com")
print(driver.title)

driver.quit()
