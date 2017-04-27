import os
#import requests
import sys, urllib2, urllib

#time.sleep(9000)

E = str(sys.argv[1])+'.e'
O = str(sys.argv[1])+'.o'
comp_err_file = open(E, 'r')
comp_err_str = comp_err_file.read()
comp_out_file = open(O, 'r')
comp_out_str = comp_out_file.read()
fileName = str(sys.argv[2])

if str(sys.argv[1]) == '1':
	data = urllib.urlencode({'fileName':fileName,'O1':comp_out_str, 'E1':comp_err_str})
	req = urllib.urlopen("http://10.201.136.134:8000/COL380/API/SendStatus1/", data)
elif str(sys.argv[1]) == '2':
	data = urllib.urlencode({'fileName':fileName,'O2':comp_out_str, 'E2':comp_err_str})
	req = urllib.urlopen("http://10.201.136.134:8000/COL380/API/SendStatus2/", data)
elif str(sys.argv[1]) == '3':
	data = urllib.urlencode({'fileName':fileName,'O3':comp_out_str, 'E3':comp_err_str})
	req = urllib.urlopen("http://10.201.136.134:8000/COL380/API/SendStatus3/", data)
elif str(sys.argv[1]) == '4':
	data = urllib.urlencode({'fileName':fileName,'O4':comp_out_str, 'E4':comp_err_str})
	req = urllib.urlopen("http://10.201.136.134:8000/COL380/API/SendStatus4/", data)
elif str(sys.argv[1]) == '5':
	data = urllib.urlencode({'fileName':fileName,'O5':comp_out_str, 'E5':comp_err_str})
	req = urllib.urlopen("http://10.201.136.134:8000/COL380/API/SendStatus5/", data)