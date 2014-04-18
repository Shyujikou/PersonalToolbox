# Description:	This is a script for auto filling the survey form of Burger King (China).
# Author:		Shyujikou(http://weibo.com/shyujikou)
# Usage:		Input the number printed on the receipt, hit enter and wait the script doing its job.
# 				If no error occurs you will see the validation code after the 17th request.
# 				Write down the validation code on your receipt and take it to get small coke and fries for free.
# Notes:		Requires Python 3.x to work
#				Massive use of this script may spoil the result of the survey campaign, use with caution.

import urllib.request
import urllib.parse
import http.cookiejar
import ssl
import re

# entrydata is used to submit the receipt number in a specific format
entrydata = 'JavaScriptEnabled=1&FIP=True&CN1={0}&CN2={1}&CN3={2}&CN4={3}&CN5={4}&CN6={5}&NextButton=%E5%BC%80%E5%A7%8B'

# Answers to survey questions
# Not recommend to change the values because survey questions may change correspondingly and cause unexpected results
answers  = {'R001000':2, 'R002000':1, 'S001000':'',
			'R004000':5,
			'R014000':5, 'R021000':5, 'R012000':5, 'R013000':5, 'R010000':5,
			'R009000':5, 'R107000':5, 'R020000':5, 'R017000':5, 'R011000':5,
			'R008000':5, 'R007000':5, 'R015000':5, 'R023000':5,
			'R031000':5, 'R108000':5, 'R029000':5, 'R030000':5,
			'R041000':2,
			'R045000':5, 'R044000':5,
			'R047000':5, 'R046000':5,
			'S081000':'',
			'R049000':1, 'R051000':1, 'R048000':1, 'R055000':1, 'R050000':1, 'R054000':1,
			'R057000':3, 'R058000':5,
			'R060000':2,
			'R068000':2,
			'R069000':9, 'R070000':9,
			'S076000':''}

# Some general parameters
domain = 'https://www.tellburgerking.com.cn/'
path = ''
rh = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'}

# Prepare cookie handler
cookie = urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())

# Workaround of SSL in Windows as by default TLS1.0 is disabled in the OpenSSL packed with Python for Windows
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

# Setup cookie and SSL workaround for urllib
opener = urllib.request.build_opener(cookie, urllib.request.HTTPSHandler(context=ssl_context))
urllib.request.install_opener(opener)

# Ask user to input the 16-digit receipt number and format the entry data string
rn = input('Receipt Number: ')
if not re.match(r'\d{16}', rn):
	print('Receipt number must be a 16-digit number.')
	exit()
rns = [rn[i:i+3] for i in range(0, len(rn), 3)]
entrydata = entrydata.format(*rns)

# Some initialization code
i = 0
data = b''
url = ''

# Main loop
while True:
	print('Requesting survey page {0}...'.format(i), end='', flush=True)
	
	# Something is different when requesting for page 0 (top page, which contains the survey entry form)
	pattern = r'form method="post" id="surveyEntryForm" action="(Survey.aspx\?c=\d+)"' if i == 0 else r'form method="post" id="surveyForm" action="(Survey.aspx\?c=\d+)"'
	
	# Setup request parameters and send the request
	rh['Referer'] = url
	url = domain + path
	req = urllib.request.Request(url, headers=rh, data=data)
	res = urllib.request.urlopen(req).read().decode('utf-8')
	
	# Check if the response contains a valid survey form
	match = re.search(pattern, res)
	if match:
		# Response contains a valid survey form, prepare answers to submit
		if i > 0:
			# Extract necessary data from response to build the data submitted for survey questions
			d = dict()
			d['IoNF'] = re.search(r'input type="hidden" name="IoNF" value="(\d+)"', res).group(1)
			d['PostedFNS'] = re.search(r'input type="hidden" name="PostedFNS" value="([^"]+)"', res).group(1)
			for op in d['PostedFNS'].split('|'):
				d[op] = answers[op]
			data = str.encode(urllib.parse.urlencode(d))
		else:
			# Request for page 1 requires data filled in the entry form, use the pre-built entrydata string 
			data = str.encode(entrydata)
		
		# Extract path using the match pattern, which contains a random session code for identifying the next URL to request
		path = match.group(1)
		
		# Counter increment
		i += 1
		print('OK')
	else:
		# Response doesn't contain a valid survey form, check if we have already reached the finish page
		match = re.search(r'<p class="ValCode">验证代码：(\d+)</p>', res)
		if match:
			# Reached the finish page, extract the validation code and exit the main loop
			vcode = match.group(1)
			print('OK')
			break
		else:
			# Neither a valid survey form nor a finish page, throw an error and exit
			print('Invalid response!')
			exit()

# Print the validation code
print('Validation Code: {0}'.format(vcode))
