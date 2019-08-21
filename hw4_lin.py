import bs4
import urllib2
from watson_developer_cloud import AlchemyLanguageV1


# Part 1
def main_text(url):
    page = urllib2.urlopen(url)
    soup = bs4.BeautifulSoup(page.read(), "html.parser")
    text = soup.find('div', {"class" : "article-text"}).get_text()
    return text



#Part 2
def get_keywords(maintext):
    alchemy_language = AlchemyLanguageV1(api_key='86122f6328bf362fc8060f85713f8f6b21f0831f')
    result = alchemy_language.keywords(text = maintext)
    keywords = result["keywords"]
    return keywords



if __name__ == "__main__":
    url = "https://www.engadget.com/2013/09/16/youtube-tests-chromecast-support-for-embedded-videos/"
    print main_text(url)
    maintext = main_text(url)
    keywords = get_keywords(maintext)
    for i in range(10):
        print "Number " + str(i+1) + " Keyword: "  + keywords[i]["text"]
        print "Relevance: " + keywords[i]["relevance"]
