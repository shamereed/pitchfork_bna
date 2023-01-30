import requests, json, time
from bs4 import BeautifulSoup
from datetime import datetime
from random import randint

url = 'https://pitchfork.com/reviews/best/albums/?page='
outputFile = 'best_albums.json'
start_time = time.time()
now = datetime.now()
dt_string = now.strftime("%B %d %Y")

def getBestNewAlbums():

	bestAlbums = []
	pageNum = 1

	for pageNum in range(2) :
		data = requests.get(url + str(pageNum))

		soup = BeautifulSoup(data.text, 'lxml')

		reviews = soup.find_all('div', { 'class': 'review'})
		
		for review in reviews:
			
			newAlbum = createAlbumDict()
			
			getAlbumDetails(newAlbum, review)
			bestAlbums.append(newAlbum)		
		
		#added pause to avoid ip blacklist
		#time.sleep(randint(2,5))

	writeToJsonFile(bestAlbums)

	print("--- %s seconds ---" % (time.time() - start_time))

def createAlbumDict():
		return	{
				"artistName" : "",
				"albumTitle" : "",
				"updateDate" : dt_string,
				"reviewDate" : "",
				"genre" : ""
			}

def getAlbumDetails(newAlbum, review):

	artist = review.find('ul', { 'class': 'artist-list review__title-artist'})
	tempArtist = ""
	if(len(artist.find_all('li'))) > 1:
		tempArtist = ", ".join(n.text for n in artist.find_all('li'))
	else:
		tempArtist = artist.text;
	newAlbum.update({"artistName":tempArtist.strip()})
	
	album = review.find('h2', { 'class': 'review__title-album' })
	newAlbum.update({"albumTitle":album.text.strip()})

	reviewDate = review.find('time', {'class': 'pub-date'})
	newAlbum.update({"reviewDate":reviewDate.text})
	
	genre = review.find('li', {'class': 'genre-list__item'})
	newAlbum.update({"genre":genre.text})

def writeToJsonFile(bestAlbums):
	json_object = json.dumps(bestAlbums, indent=4, ensure_ascii=False)
	 
	with open(outputFile, "w", encoding='utf8') as outfile:
	    outfile.write(json_object)

if __name__ == "__main__":   
	getBestNewAlbums()