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
feature_text = pickle.load(open(r'C:\Real Estate Capstone Project\Real Estate App\Datasets\feature_text.pkl','rb'))


group_df = (new_df.groupby('sector', dropna=False).mean(numeric_only=True)[
        ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']])

st.header('Sectors Geomap')

fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    text=group_df.index,
    hover_data=["price", "price_per_sqft", "built_up_area", "latitude", "longitude"],
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10
)

fig.update_layout(
    mapbox_style="open-street-map",
    width=1200,
    height=600,
    margin=dict(l=0, r=0, t=40, b=0)
)
st.plotly_chart(fig,use_container_width=True)


st.header('Features Wordcloud')

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='black',
                      stopwords = set(['s']),
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize = (8, 8), facecolor = None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

# Streamlit header
st.header("BHK Analysis Dashboard")

# Dropdown to select sector
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'Overall')
selected_sector = st.selectbox('Select Sector', sector_options)

new_df['bedRoom'] = pd.to_numeric(new_df['bedRoom'], errors='coerce')
new_df = new_df.dropna(subset=['bedRoom'])
new_df['bedRoom'] = new_df['bedRoom'].astype(int)

# Filter dataset based on selected sector
if selected_sector == 'Overall':
    df_filtered = new_df
    sector_title = "All Sectors"
else:
    df_filtered = new_df[new_df['sector'] == selected_sector]
    sector_title = f" {selected_sector}"

# Sort by bedRoom
df_filtered = df_filtered.sort_values('bedRoom')

# ---------- PIE CHART ----------
fig_pie = px.pie(
    df_filtered,
    names='bedRoom',
    hole=0.45,
    color_discrete_sequence=px.colors.sequential.Viridis_r,
    title=f"Bedroom Distribution – {sector_title}"
)

fig_pie.update_layout(
    template="plotly_dark",
    title=dict(text=f"Bedroom Distribution – {sector_title}", x=0.5, xanchor="center", font=dict(size=20)),
    legend_title_text="",
    legend=dict(
        orientation="v",
        yanchor="middle",
        y=0.5,
        xanchor="left",
        x=1.05,
        font=dict(size=12),
        bgcolor="rgba(0,0,0,0)"
    ),
    margin=dict(t=60, b=20, l=20, r=100)
)

fig_pie.update_traces(
    textposition="outside",
    textinfo="percent+label",
    hovertemplate="<b>%{label}</b><br>%{percent:.1%}<extra></extra>",
    marker=dict(line=dict(color="#1e1e1e", width=2))
)

st.plotly_chart(fig_pie, use_container_width=True)

# ---------- BOX PLOT ----------
st.subheader("Side-by-Side Price Comparison by BHK")

fig_box = px.box(
    df_filtered,
    x='bedRoom',
    y='price',
    color='bedRoom',
    color_discrete_sequence=px.colors.sequential.Viridis_r,
    title=f"Price Distribution by BHK – {sector_title}"
)

fig_box.update_layout(
    template="plotly_dark",
    title=dict(x=0.5, xanchor="center", font=dict(size=18)),
    legend_title_text=""
)

st.plotly_chart(fig_box, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)

st.header("Price Distribution by Property Type")

fig_kde = px.histogram(
    new_df,
    x="price",
    color="property_type",
    marginal="rug",
    opacity=0.6,
    histnorm='density',
    nbins=100,
    barmode='overlay',
    title="KDE Plot of Price Distribution"
)

fig_kde.update_layout(template="plotly_dark", xaxis_title="Price", yaxis_title="Density")
st.plotly_chart(fig_kde, use_container_width=True)


st.header("Heatmap: Avg Price by Sector and BHK")

heatmap_data = new_df.groupby(['sector', 'bedRoom'])['price'].mean().reset_index()
fig_heatmap = px.density_heatmap(
    heatmap_data,
    x='bedRoom',
    y='sector',
    z='price',
    color_continuous_scale='Viridis',
    title="Average Price (INR) by Sector and BHK"
)

fig_heatmap.update_layout(template="plotly_dark", xaxis_title="BHK", yaxis_title="Sector")
st.plotly_chart(fig_heatmap, use_container_width=True)

st.header("Furnishing Type Distribution")

fig_furnishing = px.pie(
    new_df,
    names='furnishing_type',
    hole=0.4,
    title="Share of Furnishing Types",
    color_discrete_sequence=px.colors.sequential.RdBu
)

fig_furnishing.update_layout(template="plotly_dark", title=dict(x=0.5))
st.plotly_chart(fig_furnishing, use_container_width=True)

st.header("Price per Sqft by Sector")

avg_price_sqft = new_df.groupby("sector")["price_per_sqft"].mean().reset_index().sort_values(by="price_per_sqft", ascending=False)

fig_sqft = px.bar(
    avg_price_sqft,
    x="price_per_sqft",
    y="sector",
    orientation="h",
    title="Average Price per Sqft by Sector",
    color="price_per_sqft",
    color_continuous_scale="sunset"
)

fig_sqft.update_layout(template="plotly_dark")
st.plotly_chart(fig_sqft, use_container_width=True)

