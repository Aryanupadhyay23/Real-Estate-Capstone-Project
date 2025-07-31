import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Viz Demo")

with open(r'C:\Real Estate Capstone Project\Real Estate App\df.pkl','rb') as file:
    df = pickle.load(file)

with open(r'C:\Real Estate Capstone Project\Real Estate App\pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your input values')

property_type = st.selectbox('Property Type', ['flat','house'])

sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathrooms = float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Number of Balcony',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0 , 1.0]))
store_room = float(st.selectbox('Store Room',[0.0 , 1.0]))

furnishing_type = st.selectbox('Furnishing_type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury_category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor_category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [[property_type,sector,bedrooms,bathrooms,balcony,property_age,built_up_area,
             servant_room,store_room,furnishing_type,luxury_category,floor_category
             ]]
    columns = ['property_type','sector','bedRoom','bathroom','balcony','agePossession','built_up_area',
             'servant room','store room','furnishing_type','luxury_category','floor_category'
             ]

    one_df = pd.DataFrame(data,columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))
    low = base_price - 0.22
    high = base_price + 0.22

    st.success(f"💰 Estimated Price: Between {low[0]:.2f} Cr and {high[0]:.2f} Cr")

