import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

bestAlbums = {}
albumCount = 1
x = 1

for x in range(6) :
	data = requests.get('https://pitchfork.com/reviews/best/albums/?page=' + str(x))

	soup = BeautifulSoup(data.text, 'html.parser')

	reviews = soup.find_all('div', { 'class': 'review'})
	for review in reviews:
		now = datetime.now()
		dt_string = now.strftime("%B %d %Y")
		newAlbum = {
			"artist" : "",
			"album" : "",
			"updateDate" : dt_string,
			"reviewDate" : ""
		}
		for title in review.find_all('ul', { 'class': 'artist-list review__title-artist'}):
			newAlbum.update({"artist":title.text})
		for album in review.find_all('h2', { 'class': 'review__title-album' }):
			newAlbum.update({"album":album.text})
		for reviewDate in review.find_all('time', {'class': 'pub-date'}):
			newAlbum.update({"reviewDate":reviewDate.text})
		bestAlbums.update({"album" + str(albumCount) : newAlbum})
		albumCount = albumCount + 1

print(bestAlbums)

# Serializing json
json_object = json.dumps(bestAlbums, indent=4, ensure_ascii=False)
 
# Writing to sample.json
with open("best_albums.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)