from bs4 import BeautifulSoup
import requests as re
from csv import writer

url = "https://www.espn.com/nba/player/gamelog/_/id/3975/stephen-curry"
page = re.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="Table__TR Table__TR--sm Table__even")

with open('currydata.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['DATE', 'OPP', 'RESULT', 'MIN', 'FG', 'FG%', '3PT', '3PT%', 'FT', 'FT%', 'REB', 'BLK', 'STL', 'PF', 'TO', 'PTS']
    thewriter.writerow(header)
    for list in lists:
        data = lists.find('td', class_="Table__TD")
        info = [data]
        thewriter.writerow(info)