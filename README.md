
# 🏠 Real Estate Capstone Project — Gurgaon Property Insights

Welcome to the **Real Estate Capstone Project**, a comprehensive, AI-powered Streamlit web application focused on the Gurgaon property market. Built on a rich dataset of residential properties, this project helps buyers, investors, and analysts **predict prices**, **explore market analytics**, and **receive personalized society recommendations** — all in one platform.

---

## 📌 Key Modules

### 1️⃣ 🤖 Price Predictor  
Estimate accurate property prices based on various input features such as:  
- Property type (flat/house), Sector, BHK, Bathrooms, Area, Furnishing type, etc.  
- Built with a machine learning regression pipeline.  
- Outputs an estimated price range (in Cr) based on historical data.

> 🔍 Model: Scikit-learn regression model  
> 📦 Input: User form through Streamlit  
> 🎯 Output: Predicted price range with low–high confidence interval

---

### 2️⃣ 📊 Market Analytics Dashboard  
Explore Gurgaon’s real estate trends with interactive visualizations:
- 🗺 **GeoMap:** Price per sqft & built-up area by sector  
- ☁️ **Word Cloud:** Popular amenities  
- 📈 **Scatter & Box Plots:** Area vs Price, Price by BHK  
- 🧱 **Distribution Charts:** Furnishing types, property types, price distribution  
- 🔥 **Heatmaps:** Avg prices by sector and BHK  
- 🏷 **Bar Charts:** Price per sqft rankings by sector

> 📊 Tools: Plotly, Seaborn, Matplotlib, WordCloud  
> 🧮 Data: Cleaned & preprocessed Gurgaon property dataset

---

### 3️⃣ 💡 Smart Society Recommender  
Receive recommendations for similar societies based on:  
- 🔗 Amenities similarity  
- 🏠 Property feature similarity  
- 📍 Location proximity  

With **adjustable sliders**, you control the importance of each factor and get a ranked list of societies within your preferred **radius**.

> 🤖 Algorithm: Cosine similarity + weighted blending  
> ⚙️ Features: Sliders for weight tuning, dynamic filtering, real-time recommendations

---

## 🛠️ Tech Stack

| Component        | Tools/Libraries                                 |
|------------------|--------------------------------------------------|
| UI & App         | Streamlit                                       |
| Data Handling    | Pandas, NumPy                                   |
| ML/Prediction    | Scikit-learn (Regression)                       |
| Visualization    | Plotly, Seaborn, Matplotlib, WordCloud          |
| Recommender      | Cosine Similarity, Normalized Matrix Blending   |
| Geo Visualization| Plotly Mapbox (OpenStreetMap)                   |

---

## 👤 Author

**Aryan Upadhyay**  
📫 [GitHub](https://github.com/Aryanupadhyay23) | [LinkedIn](https://www.linkedin.com/in/aryanupadhyay23)

---

## 🌟 Highlights

- ✅ End-to-end ML-powered real estate application  
- ✅ Real-time visualization & recommendation  
- ✅ Modular, intuitive, and user-friendly  
- ✅ Built specifically for the Gurgaon property market  

---

## 💬 Feedback

If you like this project or found it helpful, consider ⭐ starring the repo or sharing it with others.  
Feel free to raise issues or PRs to contribute!
