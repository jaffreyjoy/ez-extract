from bs4 import BeautifulSoup

word_class_name = "abcd"

f = open('test.html')
html_doc = f.read()
soup = BeautifulSoup(html_doc, 'html.parser')
nodesList = soup.find_all("a", class_ = word_class_name)
for node in nodesList:
    print(node.strong.string)
