import requests, json
from bs4 import BeautifulSoup
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

data = requests.get('https://pitchfork.com/reviews/best/albums/?page=1')

soup = BeautifulSoup(data.text, 'html.parser')

bestAlbums = {}
albumCount = 1
reviews = soup.find_all('div', { 'class': 'review__title'})
for review in reviews:
	newAlbum = {
		"artist" : "",
		"album" : "",
		"updateDate" : dt_string
	}
	for title in review.find_all('li'):
		newAlbum.update({"artist":title.text})
	for album in review.find_all('h2'):
		newAlbum.update({"album":album.text})
	bestAlbums.update({"ablum" + str(albumCount) : newAlbum})
	albumCount = albumCount + 1

print(bestAlbums)

# Serializing json
json_object = json.dumps(bestAlbums, indent=4, ensure_ascii=False)
 
# Writing to sample.json
with open("best_albums.json", "w", encoding='utf8') as outfile:
    outfile.write(json_object)