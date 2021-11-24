from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

listicle_item_a = soup.select(".listicle-item a")
listicle_item_a_text = [x.get_text() for x in listicle_item_a]

text_start_with_Read = [x for x in listicle_item_a_text if x.startswith("Read")]
movie_titles_split = [x.split("of ") for x in text_start_with_Read]
movie_titles = []

for x in range(98):

    try:
        movie_title = movie_titles_split[x][1]
    except IndexError:
        continue
    else:
        movie_titles.append(movie_title)

print(movie_titles)