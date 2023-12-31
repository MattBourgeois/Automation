from selenium import webdriver

def get_driver():
	options = webdriver.ChromeOptions()
	options.add_argument("disable-infobars")
	options.add_argument("start-maximized")
	options.add_argument("disable-dev-shm-usage") # avoids lynix problems
	options.add_argument("no-sandbox")
	options.add_experimental_option(excludeSwitches,["enable-automation"])
	options.add_argument("disable-blink-AutomationControlled")

	driver = webdriver.Chrome()

	driver = webdriver.Chrome(options = options)
	driver.get("http://automated.pythonanywhere.com")
	return driver

def main():
	driver = get_driver()
	element = driver.element_by_xpath("/html/body/div[1]/div/h1[1]")
	return element

print(main())