from googlesearch import search
import urllib
import urllib.request
from bs4 import BeautifulSoup
def Url_searching(user_ctx):
    Poe_wiki_url=[]
    Poe_wiki_address='https://pathofexile.gamepedia.com/'
    for j in search('Poe'+ user_ctx,tld='com',lang='en',start=0,stop=5):
        Poe_wiki_url.append(j)
    Poe_wiki_separation=[i for i in Poe_wiki_url if Poe_wiki_address in i] #List includes only Poe wiki urls
    if Poe_wiki_separation==[]:
        print('Nothing is found!')
    Url_open(Poe_wiki_separation[0])

def Url_open(theurl):
    thepage=urllib.request.urlopen(theurl) #Opening web page
    soup=BeautifulSoup(thepage,"html.parser")  #Opening web page as html
    Poe_wiki_item=soup.find(attrs={"class":"item-box -unique"})
    Poe_wiki_item_newline="\n".join(Poe_wiki_item.strings)
    Poe_wiki_item_list=[]
    for x in Poe_wiki_item_newline:
        Poe_wiki_item_list.append(x)
    B=''.join(Poe_wiki_item_list)
    print(B)

Url_searching('Belly of The Beast')











