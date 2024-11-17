## install packages
import streamlit as st
import pandas as pd 

#import geopandas as gpd 
st.title("My new Streamlit app")

##load dolphin database
try:
    dolphin_df = pd.read_csv(r"/workspaces/859-Final-Project/tblDolphin.csv", encoding="ISO-8859-1")
    st.write(dolphin_df.head())
except UnicodeDecodeError:
    st.error("There was an error reading the file due to encoding issues.")
except FileNotFoundError:
    st.error("The file was not found at the specified path.")

## Set up dictionaries of meanings - idk if i actually need to do this

## Take in user input of which dolphin  
search_dolphin = "4445a" # hard coding for now will figure out the input later

## Search dataframe of observations for all sightings of that dolphin  


## Create new dataframe of the dates of those sightings  

## Print basic dolphin information  

## Print out table of dates of observations 

