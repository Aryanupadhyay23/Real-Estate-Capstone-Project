import streamlit as st

st.set_page_config(
    page_title="Real Estate Capstone Project",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hero / Intro
st.title("🏠 Real Estate Capstone Project")
st.write(
    """
Welcome to the Real Estate Capstone Project — a data-driven Streamlit web application designed to transform the way you explore and understand the Gurugram property market.

This project is built on a comprehensive **Gurgaon real estate dataset**, containing detailed information about property prices, sectors, amenities, furnishing, built-up areas, and other market features.  
The data has been cleaned, preprocessed, and enriched to provide accurate predictions, meaningful analytics, and personalized recommendations.
"""
)

# Why This Project
st.header("💡 Why This Project?")
st.write(
    """
Traditional property searches are often time-consuming, static, and overwhelming.  
Buyers and investors face:
- A lack of interactive tools  
- Opaque pricing models  
- Generic, non-personalized listings  

Our solution removes the guesswork by making the process interactive, transparent, and personalized.  
With powerful analytics and AI-driven insights, you can make smarter, faster, and more confident real estate decisions.
"""
)

st.write("---")

# Solution Overview
st.header("🚀 Our Solution — An Integrated 3-Module Platform")

# 1. Price Prediction
st.subheader("1️⃣ 🤖 AI-Powered Price Prediction Engine")
st.write(
    """
No more rough estimates — get data-backed property valuations.

How it Works:
- Input property details (type, sector, size, BHK, amenities, furnishing, etc.).
- Our machine learning regression model (trained on Gurgaon real estate data) predicts the base price.
- Output includes a confidence range (Low–High price in Cr) for better decision-making.

Benefits:
- Quick, transparent, and reliable pricing.  
- Considers multiple property attributes for accuracy.  
- Eliminates guesswork in negotiations.
"""
)

st.write("---")

# 2. Analytics
st.subheader("2️⃣ 📊 Advanced Analytics Dashboard")
st.write(
    """
Move beyond static charts — explore real-time, interactive market visualizations.

Key Features:
- 🗺 Sector-Level Geomap: Price per sqft & built-up area on an interactive map.
- 💬 Features Word Cloud: Most in-demand amenities.
- 📈 Area vs Price: Compare trends for flats and houses separately.
- 🏠 BHK-Based Insights: Pie charts & box plots for price by BHK count.
- 🏷 Property Type Distribution: Distplots & histograms for houses vs flats.
- 🔥 Heatmaps: Average sector-wise prices by BHK.
- 🛋 Furnishing Trends: Market share of furnishing categories.
- 💰 Price Per Sqft Rankings: Premium & affordable sectors.
"""
)

st.write("---")

# 3. Recommender
st.subheader("3️⃣ 💡 Smart Society Recommender System")
st.write(
    """
Find properties similar to the ones you love — instantly.

Under the Hood:
- Blends amenities similarity, property feature similarity, and location proximity.
- Adjustable sliders let you control importance.
- Distance filter ensures recommendations are within your preferred radius.

What You Get:
- Ranked list of similar societies.
- Distance from your chosen location (in km).
- Fully interactive filtering and ranking.
"""
)

st.write("---")

# Technical Stack
st.subheader("⚙️ Technical Stack")
st.write(
    """
- Frontend: Streamlit (interactive UI, sliders, caching)  
- Data Handling: Pandas, NumPy  
- Visualization: Plotly, Seaborn, Matplotlib, WordCloud  
- Machine Learning: Scikit-learn (Regression + cosine similarity)  
- Geospatial Analysis: Plotly Mapbox (OpenStreetMap)  
- Recommendation Engine: Normalized similarity blending with adjustable weights
"""
)

# Why It Stands Out
st.subheader("📌 Why It Stands Out")
st.write(
    """
- End-to-end solution: prediction, analysis, and recommendations in one place.  
- User-controlled weighting for personalized suggestions.  
- Visual-first approach for quick insights.  
- Designed for real-world decision-making in the Gurugram property market.
"""
)

# Try It Yourself
st.subheader("📢 Try It Yourself")
st.write(
    """
- Predict a Price → Get an accurate, instant valuation.  
- Explore the Market → Dive into the interactive analytics dashboard.  
- Find Similar Societies → Discover homes tailored to your preferences.
"""
)

st.write("---")

# Connect / Footer
st.subheader("Connect")
st.write("GitHub: https://github.com/Aryanupadhyay23")
st.write("LinkedIn: https://www.linkedin.com/in/aryanupadhyay23")
