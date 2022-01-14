from scryfall_wrapper.card import Card
from scryfall_wrapper.utils import write_timestamped_file

def main():
    imoti = Card("Imoti, Celebrant of Bounty")
    write_timestamped_file("data/", imoti.image(), ftype=".jpg")

main()