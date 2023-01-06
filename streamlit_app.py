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
#choose the Fruit name column as index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#displays the selected fruits
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
