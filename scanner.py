import os
import sys
import time

# USAGE
# $ python scanner.py url-list.txt /wp-content/
# This outputs url-list.output.log with only positive reponses

def get_response(url):
	command = "curl -m 5 -s -I "+url
	process = os.popen(command)
	response = str(process.read())
	seek = response.find('HTTP/') + 9
	if response.find('HTTP/') != -1:
		return response[seek:].splitlines()[0]
	else:
		return "no"

target = open(sys.argv[1]+".output.log", 'w')

f = open(sys.argv[1])
for line in f:
	output = line.replace('\n','')
	fullurl = output + sys.argv[2]
	responded = get_response(fullurl)
	if responded == "404 Not Found" or responded == "400 Bad Request" or responded == "no" or responded == "301 Moved Permanently" or responded == "302 Found" or responded == "301 Moved Permamently":
		print("\033[1m\033[91m" + output+sys.argv[2]+","+responded + "\033[1m\033[91m")
	else:
		print("\033[1m\033[93m" + output+sys.argv[2]+","+responded + "\033[1m\033[93m")
		target.write(fullurl+","+responded+"\n")


f.close()
target.close()








