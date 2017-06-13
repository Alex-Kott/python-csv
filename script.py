import csv
try:
	import requests as req
except ImportError:
	print("У вас не установлен модуль requests. Установите модуль.")
import sys

url = "https://requestb.in/"

if len(sys.argv) == 1:
	print('Вы не указали файл. Укажите файл аргументом в команде "python3 script.py <filename>"')
	exit()

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