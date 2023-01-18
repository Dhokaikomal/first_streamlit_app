import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥝omega 3 & blueberry oatmeal')
streamlit.text('🍒kale,spinach & rocket smoothoie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#streamlit.dataframe(my_fruit_list)
# choose fruit name as index
my_fruit_list = my_fruit_list.set_index('Fruit')



# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# choose few fruit to set an example 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]      # it will gives only avocado and strawberries data
streamlit.dataframe(fruits_to_show)


# api with streamlit
# new session to display fruity_vise_API response
#streamlit.header("Fruityvice Fruit Advice!")

import requests
#fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruity_vise_response.json())      # write data on screen 

# normalized version using pandas
#fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
# create a data frame
#streamlit.dataframe(fruityvice_normalized)


streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
# create a data frame
streamlit.dataframe(fruityvice_normalized)



# 18/1/2023
# created new file requirements.txt
import snowflake.connector
