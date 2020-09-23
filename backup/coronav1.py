import pandas as pd
import datetime
import requests
def corona(corona_country_parameter):
    counter=0
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
        if r.status_code==404:
            counter+=1
        else:
            break

    df=pd.read_csv(url_csv)
    editing_corona_country_parameter = corona_country_parameter.capitalize()
    country_row = df.loc[df["Country_Region"] == editing_corona_country_parameter]
    country_info = country_row[["Country_Region", "Last_Update", "Confirmed", "Recovered", "Active"]]
    if country_info.empty==True:
        print('Error! 404 not found1')
        input_if_US=input("Is it a state? (Y/N)")
        input_if_US=input_if_US.capitalize()
        if input_if_US=='Y':
            country_row = df.loc[df["Province_State"] == editing_corona_country_parameter]
            country_info = country_row[["Province_State", "Last_Update", "Confirmed", "Recovered", "Active"]]
            if  country_info.empty==True:
                print('Error! 404 not found1')
            else:
                print(country_info)
        elif input_if_US=='N':
            print("Process finished!")
        else:
            print("You have entered wrong letter!")
    else:
        print(country_info)




corona('Alaska')





