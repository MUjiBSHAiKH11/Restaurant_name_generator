import streamlit as st
import name_generator as ng
st.title("Restaurant Name Generator")

cuisine=st.sidebar.selectbox("Pick a cuisine", ("indian","italian","arabic","chinese","mexican"))



if cuisine:
    response = ng.generate_rst_food_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items=response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)