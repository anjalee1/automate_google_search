from selenium import webdriver

search = input("Input the URL or string you want to search for:")
search_string = search.replace(' ', '+')
browser = webdriver.Chrome('chromedriver')

for i in range(1):
	matched_elements = browser.get("https://www.google.com/search?q=" +
									search_string + "&start=" + str(i))
