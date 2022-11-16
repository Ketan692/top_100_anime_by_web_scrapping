from bs4 import BeautifulSoup
import requests, csv

headers = {'Accept-Language': 'en-US,en;q=0.5'}
URL = "https://www.imdb.com/list/ls058654847/"

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

column_name = ["sr no.", "name", "genre", "year"]

anime_names = soup.select("h3.lister-item-header a")
anime_genre = soup.select("span.genre")
anime_year = soup.select("span.lister-item-year")

top_anime = []

for i in range(len(anime_names)):
    name = anime_names[i].text
    genre = " ".join(anime_genre[i].text.replace("\n", "").split())
    year = anime_year[i].text

    result = i+1, name, genre, year
    top_anime.append(list(result))

with open("top_anime_today.csv", 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(column_name)

    # writing the data rows
    csvwriter.writerows(top_anime)









