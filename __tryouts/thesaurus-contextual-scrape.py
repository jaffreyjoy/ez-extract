from bs4 import BeautifulSoup

import csv
import urllib.request
import time


def scrape(writer, url, word, word_class_name):
    try:
        with urllib.request.urlopen(f'{url}{word}') as f:
            html_doc = f.read().decode()
            soup = BeautifulSoup(html_doc, 'html.parser')
            nodesList = soup.find_all("a", class_ = word_class_name)
            if(nodesList is not None):
                contextualWords = [ node.strong.string for node in nodesList ]
                print(f"contextual: {contextualWords}")
                for contextualWord in contextualWords:
                    print("writing...")
                    writer.writerow({ "word" : word, "contextual": contextualWord })
            else:
                print(f"contextual: ABSENT")
    except:
        print(f"contextual: ABSENT #NOTHINGNESS")

def main():
    fw = open('gre-words-contextual.csv', 'w+', newline='')
    fieldnames = ['word', 'contextual']
    with open('gre-words.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        url = "https://www.thesaurus.com/browse/"
        word_class_name = "e9i53te7"
        writer = csv.DictWriter(fw, fieldnames=fieldnames)
        writer.writeheader()
        reader_length = 4869
        for row in reader:
            percentDone = (reader.line_num - 2) / reader_length
            print(f'{reader.line_num - 1}/{reader_length} | {round(percentDone*100, 4)} % DONE' )
            word = row['word']
            print(f"word: {word}")
            scrape(writer, url, word, word_class_name)
    fw.close()

if __name__ == "__main__":
    main()