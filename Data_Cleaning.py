# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:38:05 2024

@author: kayla

This file processes the data
I drop columns I don't want and create new columns
I drop entries I don't need, standardize the values

Further reasoning for my decisions can be found in my progress document

"""

import pandas as pd
import numpy as np

#Getting the list of anime
#Source: https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?
data = pd.read_csv("anime-dataset-2023.csv")

#Dropping irrelevent columns
data = data.drop(["Score", "Status", "Producers", "Licensors", "Rank", "Popularity", "Favorites", "Scored By", "Members", "Image URL"], axis = 1)


#Analyzing all Uknonwns. 
print(data["Name"].value_counts())

#If English name is unknown, we set it equal to Name
print(data["English name"].value_counts())
data["English name"].loc[data["English name"] == "UNKNOWN"] = data["Name"]

#Analyzing unknown kanji names and setting them to Name
print(data["Other name"].value_counts())
data["Other name"].loc[data["Other name"] == "UNKNOWN"] = data["Name"]

#After analyzing unknown data
print(data["Genres"].value_counts())
#dropping all entries with an unknown genre
data = data.loc[data['Genres'] != "UNKNOWN"]

#Leaving Synopsis with the Not Available segment
print(data["Synopsis"].value_counts())

#After doing some research before dowloading the data, I discovered that music videos
#Were part of anime watches. So I am dropping those
print(data["Type"].value_counts())
type_Data = data[["Type", "Duration"]]
data = data.loc[data['Type'] != "Music"]

#Analyzing unknown types. Anime is typically TV shows, so I am going to replace unknown with TV 
unknown_data = data[data["Type"] == "UNKNOWN"]
data['Type'].loc[data['Type'] == "UNKNOWN"] = "TV"

#Analyzing Unknown Episode Count
print(data["Episodes"].value_counts())
unknown_data = data[data["Episodes"] == "UNKNOWN"]
#Because unknown episode count is affiliated with Currently Airing/Already Aired anime, I am going to drop it. The list is from 2023, so those anime would have already aired, but that would require me to do extra work.
data = data.loc[data['Episodes'] != "UNKNOWN"]


#Dropping all anime with an unknown "Aired date"
print(data["Aired"].value_counts())
data = data.loc[data['Aired'] != "Not available"]

#I want to separate premiered into season and year. However, it is mostly empty.
#So I am to take aired data and extrapolate the season and year from that.
#First step is to take the start date from the Aired column

data["Aired"] = data['Aired'].str.split(' to ').str[0]

#Then I am going to change the "Aired and Premiered column to two column that approximates the season and year. December - February Will be Winter, March - May Spring. June-August Summer, and September-Novemebr Fall. 

air_data = data[["Aired", "Premiered"]]

air_data["Aired"] = data["Aired"].str.strip()
air_data["Aired"] = pd.to_datetime(air_data["Aired"], format = "mixed")
air_data["Aired"] = air_data["Aired"].dt.date
air_data["Aired"] = pd.to_datetime(air_data["Aired"])
air_data["Season"] = None
air_data["Year"] = None

air_data["Season"] = air_data["Aired"].dt.month
#air_data["Season"] = pd.to_numeric(air_data["Season"])
air_data["Year"] = air_data["Aired"].dt.year
air_data["Year"] = pd.to_numeric(air_data["Year"])

months = air_data["Season"]

months = months.replace(1, "Winter")
months = months.replace(2, "Winter")
months = months.replace(3, "Spring")
months = months.replace(4, "Spring")
months = months.replace(5, "Spring")
months = months.replace(6, "Summer")
months = months.replace(7, "Summer")
months = months.replace(8, "Summer")
months = months.replace(9, "Fall")
months = months.replace(10, "Fall")
months = months.replace(11, "Fall")
months = months.replace(12, "Winter")

air_data["Season"] = months

data = data.drop(["Aired", "Premiered"], axis = 1)
data["Season"] = air_data["Season"]
data["Year"] = air_data["Year"]


#Analyzing studios
print(data["Studios"].value_counts())
#For anime with multiple studios, I'm just going to use the first one
data["Studios"] = data['Studios'].str.split(',').str[0]
#Upon closer inspection, it seems that most Studios who are unknown are simply misreported. Due to the scope, I am just going to drop those shows
data = data.loc[data['Studios'] != "UNKNOWN"]

#Analyzing Source
print(data["Source"].value_counts())
unknown_data = data[data["Source"] == "Unknown"]
#Most anime is original, and a lot of unknown anime are sequels, or I will list them as original to be safe
data['Source'].loc[data['Source'] == "Unknown"] = "Original"

#Analyzing Duration
print(data["Duration"].unique())
unique = data["Duration"].unique()
#Upon closer inspection, there are shows with a duration of a few seconds. I will remove those as well, as most are commercials
data["Duration"] = data['Duration'].str.split(" per ").str[0]
data["time"] = None
data["time"] = data['Duration'].str.split(" ").str[1]
data = data.loc[data["time"] != "sec"]
data = data.drop("time", axis=1)
#Dropping shows with an unknown duration
data = data.loc[data['Duration'] != "Unknown"]

#Analyzing Rating
print(data["Rating"].value_counts())
unknown_data = data[data["Rating"] == "UNKNOWN"]
#Due to the nature of rating, I am going to drop all series with an unknown rating
data = data.loc[data['Rating'] != "UNKNOWN"]
#Replacing all values with only the rating
data["Rating"] = data['Rating'].str.split(' ').str[0]
#To keep my list appropriate, I'm going to drop all values that have an Rx rating
#R is used for gore and language, while R+ is used for mild mudity. Rx is adult content
data = data.loc[data['Rating'] != "Rx"]

#Updating ID to reflect the actual amount of values
anime_id = np.arange(0,len(data))
data.index = anime_id


#For no reason at all, I'm choosing the second genre listed to be the definitive genre
for i in range (0,len(data)):
    spl = data["Genres"].iloc[i].split(", ")
    size = len(spl)
    
    if(size > 1): 
        data["Genres"].iloc[i] = spl[1]
        if(spl[1] == "Award Winning" and size > 2):
            data["Genres"].iloc[i] = spl[2]
        else:
            data["Genres"].iloc[i] = spl[0]
    else:
        data["Genres"].iloc[i] = spl[0]
