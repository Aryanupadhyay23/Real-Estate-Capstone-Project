import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv(r'C:\Real Estate Capstone Project\Real Estate App\Datasets\data_viz1.csv')

group_df = (
    new_df
    .groupby('sector', dropna=False)
    .mean(numeric_only=True)[
        ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
    ]
)

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

