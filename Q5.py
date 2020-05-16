import requests as req

def getAllData(author):
	allData = []

	authorName = author
	page = 1
	url = (f'https://jsonmock.hackerrank.com/api/articles?author={authorName}&page={page}')
	resp = req.get(url).json()
	totalPage = resp['total_pages']

	for page in range(1,totalPage+1):
		url = (f'https://jsonmock.hackerrank.com/api/articles?author={authorName}&page={page}')
		resp = req.get(url).json()
		allData.extend( resp["data"] )

	return allData

def filterTitle(data):
	titleList = []
	for i in data:
		titleList.append(i['title'])
	return titleList

def main():
	# authorName = "epaga"
	authorName = str(input())
	data = getAllData(authorName)
	data = filterTitle(data)
	for i in data:
		print(i)

if __name__ == '__main__':
	main()