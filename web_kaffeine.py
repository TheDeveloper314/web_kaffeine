import time, csv, requests

def read_csv():
	csv_path = "links.csv"
	with open(csv_path) as file:
		links = [line[0].replace(";", "") for line in csv.reader(file)]
	return links

def ping_sites(links):
	for link in links:
		response = requests.get(link)

while True:
	links = read_csv()
	ping_sites(links)
	sleep(randint(360, 780))