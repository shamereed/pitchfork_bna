import requests, json
from bs4 import BeautifulSoup

data = requests.get('https://pitchfork.com/reviews/best/albums/?page=1')

soup = BeautifulSoup(data.text, 'html.parser')

bestAlbums = {}
albumCount = 1
reviews = soup.find_all('div', { 'class': 'review__title'})
for review in reviews:
	newAlbum = {
		"artist" : "",
		"album" : ""
	}
	for title in review.find_all('li'):
		newAlbum.update({"artist":title.text})
	for album in review.find_all('h2'):
		newAlbum.update({"album":album.text})
	bestAlbums.update({"ablum" + str(albumCount) : newAlbum})
	albumCount = albumCount + 1

print(bestAlbums)

# Serializing json
json_object = json.dumps(bestAlbums, indent=4)
 
# Writing to sample.json
with open("best_albums.json", "w") as outfile:
    outfile.write(json_object)