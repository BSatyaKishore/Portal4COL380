import os
#import requests
import sys, urllib2, urllib

#time.sleep(9000)
score = 0

fileName = str(sys.argv[1])
comp_out_file = open("1.txt")
comp_out_str = comp_out_file.read()
comp_err_file = open("1.txt")
comp_err_str = comp_err_file.read()

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


f_expected_1 = open("/home/cse/dual/cs5120284/sparse_matrix_testcases_lab4/testcase1/resultant_vector.txt")
f_expected_1_str = f_expected_1.read()
f_actual_1 = open("output1.txt")
f_actual_1_str = f_actual_1.read()

f_expected_2 = open("/home/cse/dual/cs5120284/sparse_matrix_testcases_lab4/testcase2/resultant_vector.txt")
f_expected_2_str = f_expected_2.read()
f_actual_2 = open("output2.txt")
f_actual_2_str = f_actual_2.read()

f_expected_3 = open("/home/cse/dual/cs5120284/sparse_matrix_testcases_lab4/testcase3/resultant_vector.txt")
f_expected_3_str = f_expected_3.read()
f_actual_3 = open("output3.txt")
f_actual_3_str = f_actual_3.read()

f_expected_4 = open("/home/cse/dual/cs5120284/sparse_matrix_testcases_lab4/testcase4/resultant_vector.txt")
f_expected_4_str = f_expected_4.read()
f_actual_4 = open("output4.txt")
f_actual_4_str = f_actual_4.read()

f_expected_5 = open("/home/cse/dual/cs5120284/sparse_matrix_testcases_lab4/testcase5/resultant_vector.txt")
f_expected_5_str = f_expected_5.read()
f_actual_5 = open("output5.txt")
f_actual_5_str = f_actual_5.read()

if (compare(f_actual_1_str, f_expected_1_str)):
	score += 1
if (compare(f_actual_2_str, f_expected_2_str)):
	score += 1
if (compare(f_actual_3_str, f_expected_3_str)):
	score += 1
if (compare(f_actual_4_str, f_expected_4_str)):
	score += 1
if (compare(f_actual_5_str, f_expected_5_str)):
	score += 1
if (score > 0):
	data = urllib.urlencode({'fileName':fileName,'O1':comp_out_str, 'E1':comp_err_str, 'status':1, 'score':score})
else:
	data = urllib.urlencode({'fileName':fileName,'O1':comp_out_str, 'E1':comp_err_str, 'status':0, 'score':0})
req = urllib.urlopen("http://10.194.47.139:8000/COL380/API/SendStatus/", data)