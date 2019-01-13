#!/usr/bin/python3.5
import sys, re
from html.parser import HTMLParser

class LinksExtractor(HTMLParser):
    links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    global href
                    href = attr[1]

    def handle_endtag(self, tag):
        if tag == 'a':
            self.links.append("[{0}]({1})".format(content, href))

    def handle_data(self, data):
        global content
        content = data

if __name__ == "__main__":
    HTML_file = open(sys.argv[1])
    HTML_file_content = HTML_file.read()
    
    links_extractor = LinksExtractor()
    links_extractor.feed(HTML_file_content)
    
    links = re.findall(r'<a[^>]+>[^<]+</a>', HTML_file_content)
    
    for index in range(len(links)):
        HTML_file_content = HTML_file_content.replace(links[index], links_extractor.links[index])
    
    print(HTML_file_content)
