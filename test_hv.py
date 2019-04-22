#import  "C:\PythonScripts\pytest_framework\my_hv\modules\check_hv.py"  # Checks: text in RDS header;  row's background color attribute; 'Compare' button on RDS tab 
from modules import check_hv  #....import our test scripts from the 'modules' sub-directory
###################
import time
import	pytest
#
from selenium import webdriver

###################
from selenium.webdriver.firefox.options import Options
options = Options()
#options.headless = True
options.headless = False
print("Browser is NOT Headless")
#..................	V E R Y   I M P O R T A N T   M E S S A G E   B E L O W  ..........
###....The 'pytest' framework execution (THIS) file, along with all functions defined within it 'MUST' start with 'test_'  
#@pytest.fixture  #....Default fixture setup...Note: This module gets called every time its invoked as a parameter in our function calls(
@pytest.fixture(scope="module")  #....if we set scope="module", it only gets called once no matter how many times its invoked(more efficient)
def browser():
#	browse = webdriver.Firefox()
	browse = webdriver.Firefox(options=options)  #..Run firefox 'headless' (no browser opens to user)
	yield browse  #...The 'yield' keyword will return 'browser pointer' to all test cases that called 'browser' fixture
	browse.quit()   #...After addressing test cases that called curs, it will clean up/close connection to database
	
def	test_for_rds(browser):
	tab = check_hv.test_rds_tab(browser)
#	assert tab == 'EC2Instances.info Easy Amazon RDS Instance Comparison'

def	test_for_bkc(browser):
	color = check_hv.test_bk_color(browser)
#	assert color == "rgb(211, 255, 255)"

def	test_for_btn(browser):
	button = check_hv.test_cmp_btn(browser)
#	assert button == "End Compare"

