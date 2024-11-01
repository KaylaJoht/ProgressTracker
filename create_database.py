# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:43:17 2024

@author: kayla

This is my create script for the database
Here I create and populate the database

"""
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session, DeclarativeBase
import Data_Cleaning as dc
import pandas as pd
import numpy as np

engine = create_engine("mysql+pymysql://root:root@localhost/progress_tracker")

connection = engine.connect()

class Base(DeclarativeBase): pass

Base.metadata.reflect(bind=engine)

print("Reflected Tables")
for table_name in Base.metadata.tables:
    print(table_name)

#Defining my data
data = dc.data

#Separating my data into different tables and loading them into the database
#anime table

#media table
media_data = pd.DataFrame()
media_data["media"] = data["Type"].unique()
media_data.to_sql(name="media", con=connection, if_exists="replace", index=False)

#Studio table
studio_data = pd.DataFrame()
studio_data["studio"] = data["Studios"].unique()
studio_data.to_sql(name="studio", con=connection, if_exists="replace", index=False)

#release_year table
year_data = pd.DataFrame()
year_data["release_year"] = data["Year"].unique()
year_data.to_sql(name="release_year", con=connection, if_exists="replace", index=False)

#season table
season_data = pd.DataFrame()
season_data["season"] = data["Season"].unique()
season_data.to_sql(name="season", con=connection, if_exists="replace", index=False)

#rating table
rating_data = pd.DataFrame()
rating_data["rating"] = data["Rating"].unique()
rating_data.to_sql(name="rating", con=connection, if_exists="replace", index=False)

#Origin
origin_data = pd.DataFrame()
origin_data["origin"] = data["Source"].unique()
origin_data.to_sql(name="origin", con=connection, if_exists="replace", index=False)

#Genre
genre_data = pd.DataFrame()
genre_data["genre"] = data["Genres"].unique()
genre_data.to_sql(name="genre", con=connection, if_exists="replace", index=False)

#Users
user_data = pd.read_csv("users.csv")
user_data["email"] = user_data["email"].str.lower()
user_data.to_sql(name="users", con=connection, if_exists="replace", index=False)

#Anime 
anime_data = data[["Name", "English name", "Other name", "Synopsis", "Type", "Episodes", "Duration"]]
media_data["media_id"] = np.arange(1, len(media_data)+1)
media_data = media_data.rename(columns={"media" : "Type"})
anime_data = anime_data.merge(media_data, how="outer")
anime_data = anime_data.drop(["Type"], axis=1)
anime_data = anime_data.rename(columns={"Name" : "title", "English name": "english_title", "Other name": "original_title", "Synopsis":"synopsis", "Episodes":"episodes", "Duration":"duration"})
anime_data.to_sql(name="anime", con=connection, if_exists="replace", index=False)

#Anime list data
anime_list_data = data
anime_list_data = anime_list_data.drop(['anime_id'], axis=1)
anime_list_data = anime_list_data.rename(columns={"Name" : "title", "English name": "english_title", "Other name": "original_title", "Genres":"genre", "Synopsis":"synopsis", "Episodes":"episodes", "Studios":"studio", "Source":"origin", "Duration":"duration", "Rating":"rating","Season":"season","Year":"release_year"})
anime_list_data = anime_list_data.merge(media_data, how="outer")
studio_data["studio_id"] = np.arange(1, len(studio_data)+1)
anime_list_data = anime_list_data.merge(studio_data, how="outer")
year_data["release_year_id"] = np.arange(1, len(year_data)+1)
anime_list_data = anime_list_data.merge(year_data, how="outer")
season_data["season_id"] = np.arange(1, len(season_data)+1)
anime_list_data = anime_list_data.merge(season_data, how="outer")
rating_data["rating_id"] = np.arange(1, len(rating_data)+1)
anime_list_data = anime_list_data.merge(rating_data, how="outer")
origin_data["origin_id"] = np.arange(1, len(origin_data)+1)
anime_list_data = anime_list_data.merge(origin_data, how="outer")
genre_data["genre_id"] = np.arange(1, len(genre_data)+1)
anime_list_data = anime_list_data.merge(genre_data, how="outer")
anime_data["anime_id"] = np.arange(1, len(anime_data)+1)
anime_list_data = anime_list_data.merge(anime_data, how="outer")
anime_list_data = anime_list_data.drop(["Type", "studio", "release_year", "season", "rating", "origin", "genre", "title", "english_title", "original_title", "synopsis", "episodes", "duration"], axis=1)
anime_list_data.to_sql(name="anime_list", con=connection, if_exists="replace", index=False)

#User_list
user_data = pd.read_csv("user_list.csv")
user_data.to_sql(name="user_list", con=connection, if_exists="replace", index=False)

connection.close()
