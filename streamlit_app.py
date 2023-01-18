# all import statement
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.title('My parents new healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥝omega 3 & blueberry oatmeal')
streamlit.text('🍒kale,spinach & rocket smoothoie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


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


#fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruity_vise_response.json())      # write data on screen 

# normalized version using pandas
#fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
# create a data frame
#streamlit.dataframe(fruityvice_normalized)





 


fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())  
        # create a data frame
streamlit.dataframe(fruityvice_normalized)

      


#streamlit.write('The user entered ', fruit_choice)









# 18/1/2023
# created new file requirements.txt



#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)



# dont run  anything while we are in troubleshoot
# streamlit.stop()
# my_cur.execute("insert into fruit_load_list values('from streamlit')")



# new function to access 
def get_fruity_vice_data(this_fruit_choice):
  fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
  return fruityvice_normalized 

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice')
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 #streamlit.write('thanks for adding',fruit_choice)
 if not fruit_choice:
  streamlit.error('please select one fruit ')
 else:
  back_from_func=get_fruity_vice_data(fruit_choice)
  streamlit.dataframe(back_from_func)
 
except URLError as e:
  streamlit.error()



  
  
# added button
 
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
#button
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
  
#allow end user to add fruit to list
def insert_row_snowflake(new_fruit):  
 with my_cnx.cursor() as my_cur:    
  my_cur.execute("insert into fruit_load_list values('jackfruit')")    
  return "Thanks for adding" + new_fruit
add_my_fruit=streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):  
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
 back_from_function=insert_row_snowflake(add_my_fruit)  
 streamlit.text(back_from_function)















