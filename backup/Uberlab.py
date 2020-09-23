from googlesearch import search
import datetime
import urllib
import urllib.request
from bs4 import BeautifulSoup

def Uberlabcondition():
    Uber_lab_address='https://www.poelab.com'
    Uber_lab_url=[]
    for j in search('Poe Uber Labyrinth Daily Notes'+ str(datetime.datetime.now()),tld='com',lang='en',start=0,stop=5):
        Uber_lab_url.append(j)
    Uber_lab_separation=[x for x in Uber_lab_url if Uber_lab_address in x]
    Uber_lab_date_url=Uber_lab_separation[0]
    Uber_lab_page=urllib.request.urlopen(Uber_lab_date_url)
    Uber_soup=BeautifulSoup(Uber_lab_page,'html.parser')
    Uber_lab_image_link=Uber_soup.findAll(id="notesImg") #Locating Uber Lab image
    for img in Uber_lab_image_link:
        uber_lab_image=img.get('src') #image for uber lab
    #Uber_lab_comment=Uber_soup.findAll('div',{"class":"comment-content"})
    Uber_lab_comment = Uber_soup.find('div', {"class": "comment-content"}) # It will be used as .text
    return uber_lab_image,Uber_lab_comment.text

Uberlabcondition()



















Uberlabcondition()
