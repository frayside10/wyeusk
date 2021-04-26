"""Main module."""
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.fishingpassport.co.uk/salmon-catches').read()

soup = bs.BeautifulSoup(sauce, 'html.parser')
