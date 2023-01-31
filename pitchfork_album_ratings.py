import requests, json, time
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint

url = 'https://pitchfork.com'
inputFile = 'best_albums.json'
ratingClass = 'ScoreCircle-cIILhI hHVylS'

def getAlbumRating():
	bestNewAlbums = open(inputFile)
	data = json.load(bestNewAlbums)

	for album in data :
		data = requests.get(url + album['reviewLink'])

		soup = BeautifulSoup(data.text, 'lxml')
		
		reviewRating = soup.find('div', { 'class': ratingClass})
		
		if(reviewRating) :
			album.update({"reviewRating" : reviewRating.text})

		print(album)
	
	bestNewAlbums.close()

if __name__ == "__main__":   
	getAlbumRating()