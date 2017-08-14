"""
@file train.py
@author FlorentF9

Neural Cook

Data scraping
"""

import requests
from lxml import html

N = 1000

url = 'http://www.marmiton.org/recettes/recette-hasard.aspx'

for i in range(N):
    if i % 100 == 0:
        print(str(i)+'/'+str(N))
    page = requests.get(url).content
    tree = html.fromstring(page)
    lines = tree.xpath('//li[@class="recipe-preparation__list__item"]')

    recipe = ''
    for line in lines:
        recipe += line.text_content().strip().replace('\t\t\t', ': ') + ' '

    with open('data/recipes.txt', 'a') as f:
        f.write(recipe + '\n')
