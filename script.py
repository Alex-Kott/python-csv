import csv
import requests as req
import sys

url = "https://requestb.in/"

with open(sys.argv[1], 'r') as csvfile:
	reader = csv.reader(csvfile)
	args = next(reader)
	n = len(args)
	for row in reader:
		params = dict()
		for i in range(n):
			params[args[i]] = row[i]
		r = req.post(url, params)
		if r.status_code != 200:
			print("Error")
			exit()