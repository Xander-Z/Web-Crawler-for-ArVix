from bs4 import BeautifulSoup
import re


class DataBean():
    def __init__(self, html):

        html = html.read().decode()
        soup = BeautifulSoup(html, 'lxml')
        paper = soup.find_all('dd')
        pdf = soup.find_all('dt')

        self.title = []
        self.comments = []
        self.authors = []
        self.subjects = []
        self.abstract = []
        self.arVix_index = []
        self.pdf = []

        for item in paper:
            title = authors = comments = abstract = subjects = ''
            for index, subitem in enumerate(item.contents[1]):
                text = subitem.text
                if text != '\n':
                    if 'Title:' in text:
                        title = re.search('Title: (.*)', re.sub('\n', '', text)).group(1)
                    elif 'Authors:' in text:
                        authors = re.search('Authors:(.*)', re.sub('\n', '', text)).group(1).split(', ')
                    elif 'Subjects:' in text:
                        subjects = re.search('Subjects: (.*)', re.sub('\n', '', text)).group(1).split('; ')
                    elif 'Comments:' in text:
                        comments = re.search('Comments: (.*)', re.sub('\n', '', text)).group(1)
                    else:
                        abstract = re.sub('\n', ' ', text)

            self.title.append(title)
            self.authors.append(authors)
            self.subjects.append(subjects)
            self.comments.append(comments)
            self.abstract.append(abstract)

        for item in pdf:
            index = item.contents[2].contents[0].text
            self.arVix_index.append(index)
            self.pdf.append('https://arxiv.org/pdf/' + index.split(':')[1] + '/')
