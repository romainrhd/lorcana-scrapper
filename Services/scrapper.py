import requests
from bs4 import BeautifulSoup
from DTO.card import Card

class Scrapper:
    def __init__(self, extension, nb_pages):
        self.extension = extension
        self.nb_pages = nb_pages

    def scrap(self):
        for page in range(1, self.nb_pages):
            url = f'https://www.lorcards.fr/cards/search?page={page}&sortBy=number&serie={self.extension}&language=FR&rarity=27,28,29,30,31,72'

            response = requests.get(url)

            cards = []

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for card in soup.find_all('div', class_='item p-1 p-md-2'):
                    cards.append(Card(
                        card.find('h3').text.strip(),
                        card.find('img')['data-src']
                    ))
            else:
                print(f"Erreur {response.status_code} lors de la requête.")

        return cards
