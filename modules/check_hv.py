#...HealthVerity Check flags
import time

# Check text in header after selecting 'RDS' tab
def	test_rds_tab(browser):
	browser.get(('https://ec2instances.info/'))
	time.sleep(2)
	rdstab = browser.find_element_by_css_selector('body > div.page-header > ul > li:nth-child(2) > a')
	rdstab.click() #...click on the RDS tab
			
	element = browser.find_element_by_xpath('/html/body/div[1]/h1')
	RDStext = element.text #...grab text string of RDS tab header
	assert RDStext == 'EC2Instances.info Easy Amazon RDS Instance Comparison'

# Check color attribute of a row when selected	
def	test_bk_color(browser):
	browser.get(('https://ec2instances.info/'))
	time.sleep(2)
	rdstab = browser.find_element_by_css_selector('body > div.page-header > ul > li:nth-child(2) > a')
	rdstab.click() #...click on the RDS tab
	element = browser.find_element_by_xpath("//*[@id='db.t2.small']/td[1]")
	bkclr = browser.find_element_by_id('db.t2.small')
	element.click() #...click on row under RDS tab
	bkclr = browser.find_element_by_id('db.t2.small')
	colorBK = bkclr.value_of_css_property('background-color')
	assert colorBK == "rgb(211, 255, 255)"

# Check for 'End Compare' button on RDS tab	and row info
def	test_cmp_btn(browser):
	browser.get(('https://ec2instances.info/rds/'))
	element = browser.find_element_by_xpath("//*[@id='db.t2.small']/td[1]")
	element.click() #...click on row under RDS tab to enable the "Compare Selected" button at top

	comparebtn = browser.find_element_by_xpath("//*[@id='menu']/div/button[1]")
	comparebtn.click() #...Click on the 'now visible' Compare Selected" button
	time.sleep(2)
	assert comparebtn.text == "End Compare"

