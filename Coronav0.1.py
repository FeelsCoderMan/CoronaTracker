from googlesearch import search
import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime
import random
from discord.ext import commands
import pandas as pd
import requests

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('Bot is ready')

#################Poe ascendancy randomizer##############
@client.command()
async def poerand(ctx):
    poe_classes = ['Gladiator', 'Champion', 'Slayer', 'Assassin', 'Saboteur', 'Trickster', 'Juggernaut', 'Berserker',
                   'Chieftain',
                   'Necromancer', 'Occultist', 'Elementalist', 'Deadeye', 'Raider', 'Pathfinder', 'Inquisitor',
                   'Hierophant',
                   'Guardian', 'Ascendant']
    poe_classes_rand = random.choice(poe_classes)
    await ctx.send('Your random class will be {0}'.format(poe_classes_rand))
#########################################################


#############Poe item search ############################
@client.command(aliases=['poeitem'])
async def Poeitem(ctx, *, parameter):
    deneme = Url_searching(parameter)
    await ctx.send(deneme)

def Url_searching(user_ctx):
    Poe_wiki_url = []
    Poe_wiki_address = 'https://pathofexile.gamepedia.com/'
    for j in search('Poe' + user_ctx, tld='com', lang='en', start=0, stop=5):
        Poe_wiki_url.append(j)
    Poe_wiki_separation = [i for i in Poe_wiki_url if Poe_wiki_address in i]  # List includes only Poe wiki urls
    if Poe_wiki_separation == []:
        print('Nothing is found!')
    return Url_open(Poe_wiki_separation[0])


def Url_open(theurl):
    thepage = urllib.request.urlopen(theurl)  # Opening web page
    soup = BeautifulSoup(thepage, "html.parser")  # Opening web page as html
    Poe_wiki_item = soup.find(attrs={"class": "infobox-page-container"})
    Poe_wiki_item_new = "\n".join(Poe_wiki_item.strings)
    Poe_wiki_item_list = []
    for x in Poe_wiki_item_new:
        Poe_wiki_item_list.append(x)
    for elements_of_item in Poe_wiki_item_list:
        if elements_of_item==',':
            Poe_wiki_item_list.remove(',')
    B = ''.join(Poe_wiki_item_list)
    return(B)
####################################################

#################Poe daily uber lab ################
@client.command()
async def uberlab(ctx):
    [image,comment]=Uberlabcondition()
    await ctx.send(image+'\n'+comment)


def Uberlabcondition():
    Uber_lab_address = 'https://www.poelab.com'
    Uber_lab_url = []
    for j in search('Poe Uber Labyrinth Daily Notes' + str(datetime.datetime.now()), tld='com', lang='en', start=0,
                    stop=5):
        Uber_lab_url.append(j)
    Uber_lab_separation = [x for x in Uber_lab_url if Uber_lab_address in x]
    Uber_lab_date_url = Uber_lab_separation[0]
    Uber_lab_page = urllib.request.urlopen(Uber_lab_date_url)
    Uber_soup = BeautifulSoup(Uber_lab_page, 'html.parser')
    Uber_lab_image_link = Uber_soup.findAll(id="notesImg")  # Locating Uber Lab image
    for img in Uber_lab_image_link:
        uber_lab_image = img.get('src')  # image for uber lab
    Uber_lab_comment = Uber_soup.find('div', {"class": "comment-content"})  # It will be used as .text
    return uber_lab_image, Uber_lab_comment.text
###################################################


##########################help#####################
@client.command()
async def elp(ctx):
    await ctx.send("Commands\n-poerand for random ascendancy generator\n-uberlab for daily uber lab info")
    await ctx.send("-poeitem (item name) for getting info about unique item you write\n-w2g for opening w2g link")
###################################################

#####################watch2gether link#############
@client.command()
async def w2g(ctx):
    watch2_url='https://www.watch2gether.com/rooms/jxpqlvgc1xaobutsyr?lang=en?app=1'
    await ctx.send(watch2_url)
###################################################

#######################corona data##########
@client.command()
async def corona(ctx,*,corona_country_parameter):
    counter = 0
    now = datetime.date.today()

    while True:
        now_day = now.day
        now_day = now_day - counter
        year = '{:02d}'.format(now.year)
        month = '{:02d}'.format(now.month)
        day = '{:02d}'.format(now_day)
        time_for_url = '{}-{}-{}'.format(month, day, year)
        url_csv = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + time_for_url + ".csv"
        r = requests.get(url_csv)
        if r.status_code == 404:
            counter += 1
        else:
            break

    df=pd.read_csv(url_csv,error_bad_lines=False)
    editing_corona_country_parameter = corona_country_parameter.title()
    country_row = df.loc[df["Country_Region"] == editing_corona_country_parameter]
    if country_row.empty == True:
        country_row = df.loc[df["Province_State"] == editing_corona_country_parameter]
        if country_row.empty == True:
            await ctx.send("Error! 404 Not Found!")
        else:
            country_info = country_row[["Province_State", "Last_Update", "Confirmed", "Recovered", "Active"]]
    else:
        country_info = country_row[["Country_Region", "Last_Update", "Confirmed", "Recovered", "Active"]]

    #await ctx.send(country_info)
    [r, c] = country_info.shape
    if r == 1:
        await ctx.send(country_info)
    elif r > 1:
        confirmed = country_info["Confirmed"].sum()
        recovered = country_info["Recovered"].sum()
        active = country_info["Active"].sum()
        last_update = country_info.iloc[0]["Last_Update"]
        column_0_name = country_info.columns[0]

        data = ([[editing_corona_country_parameter], [last_update], [confirmed], [recovered], [active]])
        row_name = [column_0_name, "Last_Update", "Confirmed", "Recovered", "Active"]

        new_df = pd.DataFrame(data=data, index=row_name)
        print(new_df.columns)
        await ctx.send(new_df)


#############################################################


######################magic ball#############################
@client.command(aliases=['8ball'])
async def eightball(ctx, *,question,):
    choices = [
        "Definitely",
        "Yes",
        "Probably",
        "Mabye",
        "Probably Not",
        "No",
        "Definitely Not",
        "I don't know",
        "Ask Later",
        "I'm too tired"
    ]
    rand_choice=random.choice(choices)
    await ctx.send("Your question was " + question)
    await ctx.send("Response: " + rand_choice)
#############################################################




