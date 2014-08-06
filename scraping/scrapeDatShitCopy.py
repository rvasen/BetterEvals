from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from parseDatShit import htmlParse

def main():
	evalPagesNew = []
	evalPagesOld = []
	evals = []
	driver = webdriver.Firefox()
	driver.implicitly_wait(20)
	driver.get("https://edu-apps.mit.edu/ose-rpt/?Search+Online+Reports=Search+Subject+Evaluation+Reports")
	#Authentication
	driver.find_element_by_name("j_username").send_keys("USERNAME")
	driver.find_element_by_name("j_password").send_keys("PASSWORD")
	driver.find_element_by_name("Submit").click()
	#Wait until next page loads
	checkProgress = False
	while(not checkProgress):
		checkProgress = "Subject Evaluation Report Search" in driver.title
	checkProgress = False
	#Iterate through each term; start at index 1 because index 0 is Any Term
	numTerms = len(driver.find_elements_by_xpath("//select[@id='term']/option"))
	for i in range(1, 50):
		old = False
		#Subject eval forms changed after Fall Term 2009-2010 (except January Term 2009-2010)
		if(i == 17 or i > 18):
			old = True
		select = Select(driver.find_element_by_xpath("//select[@id='term']"))
		select.select_by_index(i)
		driver.find_element_by_name("search").click()
		while(not checkProgress):
			checkProgress = "Search Results" in driver.title
		checkProgress = False
		#Three p tags before links to subject evals start
		numClassesPlus3 = len(driver.find_elements_by_xpath("//div[@id='rh-col']/p"))
		#Iterate through each class
		for j in range(4, numClassesPlus3):
			driver.find_element_by_xpath("//div[@id='rh-col']/p[%i]/a" % j).click()
			while(not checkProgress):
				checkProgress = "Report for" in driver.title
			checkProgress = False
			if(old == False):
				evalPagesNew.append(BeautifulSoup(driver.page_source))
			elif(old == True):
				evalPagesOld.append(BeautifulSoup(driver.page_source))
			driver.back()
			if(j>7):
				break
		driver.back()
		if(i>2):
			break
	driver.close()

	#Parse enew vals
	for evalPage in evalPagesOld:
		evals.append(htmlParse(evalPage))
	for evalPage in evalPagesNew:
		evals.append(htmlParse(evalPage))

	

	for Eval in evals:


if __name__ == '__main__':
	main()