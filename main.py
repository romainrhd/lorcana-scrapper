import argparse
from Services.scrapper import Scrapper
def main():
  parser = argparse.ArgumentParser(
    description='Lorcana scrapper is a tool to list all the cards from a given extension of Lorcana'
  )

  parser.add_argument('--extension', type=str, help='The id of the extension of lorcards.fr')
  parser.add_argument('--nb-pages', type=int, help='The number of pages to scrap')

  args = parser.parse_args()

  print(args.extension)
  print(args.nb_pages)

  scrapper = Scrapper(args.extension, args.nb_pages)
  cards = scrapper.scrap()

  print(cards)

  # TODO: send to database via API
  for card in cards:
      card.display()

if __name__ == '__main__':
  main()