import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('\N{Bowl with Spoon} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{Green Salad} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{Chicken} Hard-Boiled Free-Range Egg')
streamlit.text('\N{Avocado} \N{Bread} Avocado Toast')


streamlit.header('\N{Banana}\N{Strawberry} Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
