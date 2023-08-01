#from bs4 import BeautifulSoup
#import requests

#url='https://xeno-canto.org/'
#response = requests.get(url)

#get title
#soup=BeautifulSoup(response.content,'html.parser')
#title=soup.find('title')
#print(title)

import requests
from bs4 import BeautifulSoup

def extract_bird_songs():
    url = 'http://xeno-canto.org'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        bird_songs = soup.find_all('div', class_='jp-type-single')

        for song in bird_songs:
            print(song.text)
    else:
        print(f"Failed to fetch the website. Status code: {response.status_code}")

if __name__ == "__main__":
    extract_bird_songs()

          

 



