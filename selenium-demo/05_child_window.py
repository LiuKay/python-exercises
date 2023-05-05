from selenium import webdriver

driver = webdriver.Chrome()
# get method to launch the URL
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
# prints the window handle in focus
prev = driver.current_window_handle
print(driver.current_window_handle)
# to fetch the first child window handle
chwnd = driver.window_handles[1]
# to switch focus the first child window handle
driver.switch_to.window(chwnd)
print(driver.current_window_handle)

driver.switch_to.window(prev)

print(driver.find_element_by_tag_name("h3").text)
# to close the browser
# driver.quit()
