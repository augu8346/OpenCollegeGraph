import requests
import bs4
from collections import defaultdict

def parser():
	basicUrl = "http://localhost/basic.html"
	response = requests.get(basicUrl)
	soup = bs4.BeautifulSoup(response.text)

	d = defaultdict(list)
	tableRows = soup('table')[2].findAll('tr')
	for row in tableRows[1:]:
		rowColoumns = row.findAll('td')
		key = rowColoumns[0].string
		for col in rowColoumns[1:]:
			d[key].append(col.string.encode('utf-8'))
	return d

#print soup('table')[2].findAll('tr')[1].findAll('td')[0].string

