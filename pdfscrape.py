from PyPDF2 import PdfFileReader as pdfr

import re
import csv


def split(splitLines):
    '''
    CONVERT

    `\nAbscission n. The act of cutting off, as in a surgical operation.\n'`

    TO

    {
        word: "Abscission"
        pos: "noun"
        meaning: "The act of cutting off, as in a surgical operation."
    }
    '''
    posMap = {
        "n." : "noun",
        "v." : "verb",
        "adv." : "adverb",
        "adj.": "adjective"
    }
    for splitLine in splitLines:
        posList = ["n", "v" , "adj", "adv"]
        regexStr = "(" + ("|").join([ f"\\s{pos}[.]\\s" for pos in posList]) + ")"
        # print("regexStr")
        # print(regexStr)
        [word, pos, meaning] = re.split(regexStr, splitLine)
        print({
            "word" : word,
            "pos" : posMap[pos.strip()],
            "meaning": meaning
        })
        # exit()
        return {
            "word" : word,
            "pos" : posMap[pos.strip()],
            "meaning": meaning
        }


def main():
    # init reader object
    grePdfReader = pdfr(open("gre-words.pdf", "rb"))

    # get no of pages
    numPages = grePdfReader.getNumPages()

    print("numPages")
    print(numPages)

    with open('gre-words.csv', 'w+', newline='') as csvfile:
        fieldnames = ['word', 'pos', 'meaning']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        # iterate through pages to extract text
        for pageNo in range(numPages):
            pageText = grePdfReader.getPage(pageNo).extractText()
            splitLines = [ line.strip() for line in re.split(r"\d+",pageText)[2:-1] ]
            # print(splitLines)
            splitData = split(splitLines)
            writer.writerow(splitData)

if __name__ == "__main__":
    main()