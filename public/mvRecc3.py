# Python3 code for Movie Recommender pro
# Recommendation based on emotion.
# Import library for web scrapping.
from bs4 import BeautifulSoup as SOUP
import re
import sys
import requests as HTTP
import random

# Main Function for scraping


def main(emotion):
    # IMDb Url for Comedy Drama genre of
    # movie against emotion Sad
    if (emotion == "Sad"):
        urlhere = 'https://www.imdb.com/list/ls052109630/'

    # IMDb Url for Musical genre of
    # movie against emotion Disgust
    elif (emotion == "Disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

    # IMDb Url for Family genre of
    # movie against emotion Anger
    elif (emotion == "Angry"):
        urlhere = 'https://www.imdb.com/list/ls004108030/'

    # IMDb Url for Sport genre of
    # movie against emotion Fear
    elif (emotion == "Fear"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

    # IMDb Url for Thriller genre of
    # movie against emotion Enjoyment
    elif (emotion == "Happy"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

    # IMDb Url for Western genre of
    # movie against emotion Trust
    elif (emotion == "Neutral"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

    # IMDb Url for Film_noir genre of
    # movie against emotion Surprise
    elif (emotion == "Surprise"):
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    # IMDb Url for Top Rated Movies.
    # movie against no emotion entered.
    elif (emotion == ""):
        urlhere = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

    else:
        urlhere = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

    # HTTP request to get the data of
    # the whole page
    response = HTTP.get(urlhere)
    data = response.text

    # Parsing the data using
    # BeautifulSoup
    soup = SOUP(data, "lxml")

    # Extract movie titles from the
    # data using regex
    title = soup.find_all(
        "a", attrs={"href": re.compile(r'\/title\/tt+\d*\/')})
    return title


# Driver Function
if __name__ == '__main__':

    emotion = "happy"

    list = ["Sad","Disgust","Angry","Fear","Happy","Neutral","Surprise"]

    emotion = random.choice(list)

    a = main(emotion)
    l = []
    count = 0

    if (emotion == "Surprise"):

        for i in a:
            # Splitting each line of the
            # IMDb data to scrape movies
            tmp = str(i).split('>;')

            if (len(tmp) == 3):
                l.append(tmp[1][:-3])

            if (count > 102):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')

            if (len(tmp) == 3):
                l.append(tmp[1][:-3])

            if (count > 100):
                break
            count += 1
    print(random.choice(l))
