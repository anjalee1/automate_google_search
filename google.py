from selenium import webdriver

search = input("Input the URL or string you want to search for:")
search_string = search.replace(' ', '+')
#create an instance of Chrome with the path of the driver
browser = webdriver.Chrome('chromedriver')

for i in range(1):
	#used to load a website
	matched_elements = browser.get("https://www.google.com/search?q=" +
									search_string + "&start=" + str(i))
