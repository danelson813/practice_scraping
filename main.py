# practice_scraping/main.py
from helpers.selenium_template import get_soup
from helpers.sqlite3_helper import to_sqlite
import pandas as pd
import sqlite3


conn = sqlite3.connect('movies', )
base = "https.imdb.com"
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

soup = get_soup(url)

movies = soup.select('li.ipc-metadata-list-summary-item')

results = []
for movie in movies:
    try:
        rating = movie.select('span.kLaxqf')[2].text
    except IndexError:
        rating = 'unrated'
    result = {
        'title': movie.select_one('h3.ipc-title__text').text,
        'year': movie.select('span.kLaxqf')[0].text,
        'running_time': movie.select('span.kLaxqf')[1].text,
        'rating' : rating,
        'voteCount': movie.select_one('span.ipc-rating-star--voteCount').text[1:],
        'link': base+movie.select_one('a.ipc-lockup-overlay.ipc-focusable')['href'],
    }
    results.append(result)

df = pd.DataFrame(results)

df.to_csv('data/results.csv', index=False, sep='|')
to_sqlite(df)