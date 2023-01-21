import streamlit
import pandas

streamlit.header('🥣 Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Fruit List')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
my_fruit_selection = streamlit.multiselect('pick',my_fruit_list.index,['Grapes'])

fruits_to_show = my_fruit_list.loc[my_fruit_selection]
streamlit.dataframe(my_fruit_list)
