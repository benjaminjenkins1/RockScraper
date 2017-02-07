from lxml import html
import requests

page = requests.get('http://www.rockefeller100.org/items/show/4638')
tree = html.fromstring(page.content)

print(tree)

tags = tree.xpath('//div[@id="item-metadata"]/dl/dd/a[@reg="tag"]/text()')

print('tags: ',tags)

input("Press Enter to continue...")