from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister brother" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

# # element
# print(soup.title)  # <title>The Dormouse's story</title>
# print(soup.find('title'))  # <title>The Dormouse's story</title>
# # soup.p == soup.body.p
#
# # tag
# print(soup.title.name)  # title
#
# # text
# print(soup.title.string)  # The Dormouse's story
# print(soup.title.get_text())  # The Dormouse's story
#
# # single element
# print(soup.a.get_text())  # Elsie
# print(soup.find('a').get_text())  # Elsie
#
# # multi element
# print(soup.find_all(#'a'))
# print(soup.find_all('a')[0].get_text())  # Elsie
# print(soup.find_all('a')[1].get_text())  # Lacie
#
# # attribute
# print(soup.a['class'])  # ['sister']
# print(soup.a.get('class'))  # ['sister']
# print(soup.a['href'])  # http://example.com/elsie
# print(soup.a.attrs['href'])  # http://example.com/elsie
#
# # find by id
# print(soup.find(id='link1'))  # <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
# print(soup.find('', {'id': 'link1'}))  # <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
#
# # find by class
# print(soup.find_all(class_=True))
hasClassElement = soup.find_all(class_=True)
for s in hasClassElement:
    print(s.get('class'))
# print(soup.find_all('', {'class': 'sister'}))
