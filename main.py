import requests
from bs4 import BeautifulSoup
import nltk 
import textstat
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('punkt')
medium_urls=[
    'https://medium.com/@emorphis.technologies/what-is-cloud-computing-everything-you-need-to-know-439b99e69625', #cloud computing
    'https://medium.com/@sadafsaleem5815/neural-networks-in-10mins-simply-explained-9ec2ad9ea815',
    'https://medium.com/@smithd4466/the-future-of-education-embracing-online-learning-40e7f5fc4fd7',
    'https://medium.com/@israelchris2024/personal-development-through-lifelong-learning-8c998f80541b#:~:text=Section%201%3A%20Understanding%20Lifelong%20Learning,to%20individual%20development%20and%20enrichment.',
    'https://medium.com/@hwhelpera/strategies-for-teachers-to-incorporate-ai-tutors-into-their-teaching-methods-36b9c2669858',
    'https://medium.com/@gzm.err/the-evolution-of-music-genre-preferences-across-generations-sociological-and-psychological-factors-a9002c789c8f',#music
    'https://medium.com/@ashish006734/adaptive-storytelling-how-web-series-tailor-content-for-different-platforms-cadb82709a9d',#film
    'https://medium.com/@syedsharjeelshah11/crispr-gene-editing-a-breakthrough-in-biotechnology-a2f91b0f3158',
    'https://medium.com/@justmeeee/the-impact-of-social-media-on-society-transforming-communication-and-shaping-daily-lives-558682646a17#:~:text=Social%20media%20has%20become%20an,aspects%20of%20our%20daily%20lives.',#social
    'https://medium.com/@atharv.s.16.10/the-role-of-social-media-in-modern-society-535f7cdee5a6',#social media
    'https://medium.com/@yagnesh.pandya/ai-powered-creativity-how-is-artificial-intelligence-transforming-the-arts-and-content-creation-c2bf40b1188a#:~:text=Conclusion%3A%20A%20Symphony%20of%20Innovation,catalyst%20for%20innovation%20and%20exploration.',#ai
    
]
nerdy_urls=[
    # 'https://www.almabetter.com/bytes/articles/cryptography-and-network-security',#cryptography and network security
    'https://www.nerdwallet.com/article/investing/investing-101',#Investing Basics
    'https://www.nerdwallet.com/article/investing/cryptocurrency',
    # 'https://www.vulture.com/article/best-movies-2024-film.html'

]

forbes_urls=[
    'https://www.forbes.com/sites/joemckendrick/2024/04/19/artificial-intelligence-2024-smarter-but-more-expensive/',
    'https://www.forbes.com/councils/theyec/2022/11/08/introduction-to-machine-learning-for-marketing/',
    'https://www.forbes.com/sites/jamesellsmoor/2019/07/23/77-of-people-want-to-learn-how-to-live-more-sustainably/',#lifestyle
    'https://www.forbes.com/sites/neloliviawaga/2022/12/31/23-sustainable-habits-to-adapt-in-2023/',#lifestyle
    'https://www.forbes.com/sites/fionatapp/2020/06/04/how-to-travel-and-live-sustainably-after-lockdown/',
    'https://www.forbes.com/councils/forbesbusinesscouncil/2022/08/01/understanding-the-value-of-art-at-work/',#art
    'https://www.forbes.com/councils/forbesbusinesscouncil/2022/12/09/what-will-the-future-of-contemporary-art-look-like/',
    'https://www.forbes.com/sites/forbescommunicationscouncil/2017/06/05/the-science-of-happiness-and-the-creative-brain/',
    'https://www.forbes.com/councils/forbesfinancecouncil/2024/09/03/unlocking-success-the-power-of-data-driven-decision-making/#:~:text=By%20tapping%20into%20the%20power,the%20forthcoming%20data%2Dcentric%20era.',#decision making
    'https://www.forbes.com/sites/eriklarson/2022/01/12/since-data-scientists-dont-do-business-decisions---businesses-need-decision-scientists/',

]


def name_of_author(author):
    name=author.text.strip()
    return name
def publish_date_of_article(publish_date):
    date_=publish_date.text.strip()
    return date_
def content_of_article(content):
    content_=content.text.strip()
    return content_
def word_length_of_content(content):
    words_token=word_tokenize(content)
    count_of_words=len(words_token)
    return count_of_words
def sentence_length_of_content(content):
    sentence_token=sent_tokenize(content)
    count_of_sentence=len(sentence_token)
    return sentence_token
def avg_word_length_of_content(content):
    words_token=word_tokenize(content)
    avg_len=sum(len(word) for word in words_token)/len(words_token)
    return avg_len
    
def readability_Score_of_the_arcticle(content):
    readability_Score=textstat.flesch_reading_ease(content)
    return readability_Score
def repetitve_task(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    return soup

def title_of_article():
    list_of_title=[]
    for url in urls:
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        list_of_title.append(soup.title.string)
    print(len(list_of_title))



def get_data_from_article():
        

    def medium_publisher_method(medium_url):
        count=0
        for medium_url in medium_urls:
            article=repetitve_task(medium_url)
            author=article.find('a',attrs={'class':"af ag ah ai aj ak al am an ao ap aq ar il"})
            author_name=name_of_author(author)
            publish_date=article.find('span',attrs={'data-testid':"storyPublishDate"})
            date=publish_date_of_article(publish_date)
            content_article=article.find('article')
            content=content_of_article(content_article)
            print(author_name,date,content)
            print()
            count+=1
            # print(count)
            
    # article=medium_publisher_method('https://medium.com/@bogatinov.leonardo/the-future-of-programming-trends-and-predictions-for-the-next-decade-d088761f44de#:~:text=Conclusion%3A,ever%2Dchanging%20world%20of%20programming.')
    # first_article=medium_publisher_method('https://medium.com/@emorphis.technologies/what-is-cloud-computing-everything-you-need-to-know-439b99e69625')
    # third_article=medium_publisher_method('https://medium.com/@sadafsaleem5815/neural-networks-in-10mins-simply-explained-9ec2ad9ea815')
    
    def nerd_wallet_method():
        for nerd_url in nerdy_urls:
            article=repetitve_task(nerd_url)
            authors=article.find_all("a",attrs={'class':"_28z5Fp WnBKuV _2JIHTU vLzrnO _3mJuQ4"})
            list_of_authors=[]
            for auth in authors:
                list_of_authors.append(auth.text.strip())
            publish_date=article.find("span",attrs={'class':"gIxhiX _21EZtY TS4Kq- _3_uGsM _28z5Fp _2G3s3O"})
            date=publish_date_of_article(publish_date)
            content_article=article.find('div',attrs={'class':"_2_Pyfm _1gun6R"})
            content=content_of_article(content_article)
            print(list_of_authors,date,content)
    # sixth_article=nerd_wallet_method('https://www.nerdwallet.com/article/investing/investing-101')
    # seventh_article=nerd_wallet_method('https://www.nerdwallet.com/article/investing/cryptocurrency')

    def forbes_method():
        count=0
        for forbes_url in forbes_urls:
            article=repetitve_task(forbes_url)
            author_article=article.find('a',attrs={'data-ga-track':"contrib block byline"})
            author=name_of_author(author_article)
            publish_date=article.find('time')
            date=publish_date_of_article(publish_date)
            content_article=article.find('div',attrs={'class':"body-container"})
            content=content_of_article(content_article)
            word_length=word_length_of_content(content)
            sentence_length=sentence_length_of_content(content)
            avg_word_length=avg_word_length_of_content(content)
            readability_score=readability_Score_of_the_arcticle(content)
            print(author,date,content,word_length,sentence_length,avg_word_length,readability_score)
            print()
            count+=1
            print(count)
    # fouth_article=forbes_method('https://www.forbes.com/councils/theyec/2022/11/08/introduction-to-machine-learning-for-marketing/')

    def fivth_article(fivth_article_url):
        article=repetitve_task(fivth_article_url)
        author_article=article.find('p',attrs={'class':"font-satoshi-medium text-[14px] font-semibold leading-5"})
        author=name_of_author(author_article)
        publish_date=article.find('span',attrs={'class':"text-[14px] leading-5"})
        date=publish_date_of_article(publish_date)
        content_article=article.find('section',attrs={'class':"md:col-span-12 lg:col-span-8 lg:col-start-5"})
        content=content_of_article(content_article)
        print(author,date,content)
    def twenty_first(twenty_article_url):
        article=repetitve_task(twenty_article_url)
        author_article=article.find('span',attrs={'class':'primary-bylines with-bio'})
        author=name_of_author(author_article)
        publish_date=article.find('span',attrs={'class':'article-date'})
        date=publish_date_of_article(publish_date)
        content_article=article.find('div',attrs={'class':'article-content inline'})
        content=content_of_article(content_article)
        print(author,date,content)
    # medium_publisher_method()
    # forbes_method()
    # nerd_wallet_method()
    fivth_article('https://www.almabetter.com/bytes/articles/cryptography-and-network-security')
    twenty_first('https://www.vulture.com/article/best-movies-2024-film.html')
        




    



    

    
get_data_from_article()

