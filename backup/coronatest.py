import requests
import datetime
import pandas as pd
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
    editing_corona_country_parameter = corona_country_parameter.title()
    country_row = df.loc[df["Country_Region"] == editing_corona_country_parameter]
    country_row2 = df.loc[df["Province_State"] == editing_corona_country_parameter]
    if country_row.empty==True:
        country_row = df.loc[df["Province_State"] == editing_corona_country_parameter]
        if country_row.empty==True:
            print("Error! 404 Not Found!")
        else:
            country_info=country_row[["Province_State", "Last_Update", "Confirmed", "Recovered", "Active"]]
    else:
        country_info = country_row[["Country_Region", "Last_Update", "Confirmed", "Recovered", "Active"]]

    [r,c]=country_info.shape
    if r==1:
        print(country_info)
    elif r>1:
        confirmed=country_info["Confirmed"].sum()
        recovered=country_info["Recovered"].sum()
        active=country_info["Active"].sum()
        last_update=country_info.iloc[0]["Last_Update"]
        column_0_name=country_info.columns[0]        #getting column 0 name


        data=([[editing_corona_country_parameter],[last_update],[confirmed],[recovered],[active]])
        row_name=[column_0_name,"Last_Update","Confirmed","Recovered","Active"]

        new_df=pd.DataFrame(data=data,index=row_name)

        print(new_df)





corona('alabama')
#corona('turkey')














