import requests, json, time, pitchfork_best_new_albums
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint

url = 'https://pitchfork.com'
inputFile = 'best_albums.json'
ratingClass = 'ScoreCircle-cIILhI hHVylS'
updatedAlbums = []
start_time = time.time()

def getAlbumRating():
	bestNewAlbums = open(inputFile)
	data = json.load(bestNewAlbums)

	for album in data :
		scraper = requests.get(url + album['reviewLink'])

		soup = BeautifulSoup(scraper.text, 'lxml')
		
		reviewRating = soup.find('div', { 'class': ratingClass})
		
		if(reviewRating) :
			album.update({"reviewRating" : reviewRating.text})

		print(album)
		updatedAlbums.append(album)
		#added pause to avoid ip blacklist
		#time.sleep(randint(2,5))
	
	bestNewAlbums.close()
	print("--- %s seconds ---" % (time.time() - start_time))
	return True

if __name__ == "__main__":   
	if(getAlbumRating()):
		pitchfork_best_new_albums.writeToJsonFile(updatedAlbums)