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

def compare(str1, str2):
	str1 = str1.strip()
	str2 = str2.strip()
	str1_arr = str1.splitlines()
	str2_arr = str2.splitlines()
	if (len(str1_arr) != len(str2_arr)):
		return False
	for i in xrange(len(str1_arr)):
		if (str1_arr[i].strip() != str2_arr[i].strip()):
			return False
	return True

if str(sys.argv[1]) == '1':
	f_expected_1 = open("/home/cse/dual/cs5120284/sparse_matrix_testcases_lab4/testcase1/resultant_vector.txt")
	f_expected_1_str = f_expected_1.read()
	f_actual_1 = open("output1.txt")
	f_actual_1_str = f_actual_1.read()
	if (compare(f_actual_1_str, f_expected_1_str)):
		data = urllib.urlencode({'fileName':fileName,'O1':comp_out_str, 'E1':comp_err_str, 'status':1})
	else:
		data = urllib.urlencode({'fileName':fileName,'O1':comp_out_str, 'E1':comp_err_str, 'status':0})
	req = urllib.urlopen("http://10.194.47.139:8000/COL380/API/SendStatus1/", data)
elif str(sys.argv[1]) == '2':
	data = urllib.urlencode({'fileName':fileName,'O2':comp_out_str, 'E2':comp_err_str})
	req = urllib.urlopen("http://10.194.47.139:8000/COL380/API/SendStatus2/", data)
elif str(sys.argv[1]) == '3':
	data = urllib.urlencode({'fileName':fileName,'O3':comp_out_str, 'E3':comp_err_str})
	req = urllib.urlopen("http://10.194.47.139:8000/COL380/API/SendStatus3/", data)
elif str(sys.argv[1]) == '4':
	data = urllib.urlencode({'fileName':fileName,'O4':comp_out_str, 'E4':comp_err_str})
	req = urllib.urlopen("http://10.194.47.139:8000/COL380/API/SendStatus4/", data)
elif str(sys.argv[1]) == '5':
	data = urllib.urlencode({'fileName':fileName,'O5':comp_out_str, 'E5':comp_err_str})
	req = urllib.urlopen("http://10.194.47.139:8000/COL380/API/SendStatus5/", data)