class Card:
    def __init__(self, name, urlImage):
        self.name = name
        self.urlImage = urlImage

    def display(self):
        print(f"Carte Lorcana : {self.name}")
        print(f"URL image : {self.urlImage}")