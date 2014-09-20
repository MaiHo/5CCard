from bs4 import BeautifulSoup
import re
import mechanize

br = mechanize.Browser()
response = br.open('https://cards.cuc.claremont.edu/index.php')
responseStr = response.read()
#br = mechanize.Browser()
#response2 = br.open('https://cards.cuc.claremont.edu/login.php')
#response2Str = response2.read()
#print responseStr

def parser(text):
	soup = BeautifulSoup(text) # Makes a Soup object, assuming text is a string

	# Finds all instances of Current Balance in text.
	# Not an exact find because re.compile creates a regular expression
	currentBalances = soup.findAll(text = re.compile("Current Balance"))
	mealBalances = soup.findAll(attrs = {'class' : "tablecolnum"})
	
	# The first find should be the flex because it shows up first in the html
	# The second find should be claremont cash balance
	flexBalance = currentBalances[0]
	cCashBalance = currentBalances[1]

	# The final amount of meals left should be the last find
	mealsLeft = mealBalances[-1].string

	return float(onlyNumbers(flexBalance)), float(onlyNumbers(cCashBalance)), int(mealsLeft)

def onlyNumbers(s):
	result = ""
	for character in s:
		if (character.isdigit() or character == "."):
			result += character

	return result

flex, cCash, numMeals = parser(responseStr)