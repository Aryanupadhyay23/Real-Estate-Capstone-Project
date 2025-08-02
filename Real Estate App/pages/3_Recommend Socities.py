import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize

# --- Data Loading ---
# It's good practice to cache data loading in Streamlit to improve performance.
@st.cache_data
def load_data():
    """Loads the necessary data files."""
    try:
        # Paths are reverted to their original location as requested.
        loc_df = pickle.load(open('Real Estate App/location_distance.pkl', 'rb'))
        sim1 = pickle.load(open('Real Estate App/cosine_sim1.pkl', 'rb'))
        sim2 = pickle.load(open('Real Estate App/cosine_sim2.pkl','rb'))
        sim3 = pickle.load(open('Real Estate App/cosine_sim3.pkl','rb'))
        return loc_df, sim1, sim2, sim3
    except FileNotFoundError:
        st.error("One or more data files were not found. Please make sure the 'Real Estate App' directory exists and contains 'location_distance.pkl', 'cosine_sim1.pkl', 'cosine_sim2.pkl', and 'cosine_sim3.pkl'.")
        return None, None, None, None

# --- Main App Logic ---
loc_df, sim1, sim2, sim3 = load_data()

# Stop the app if data loading failed.
if loc_df is None:
    st.stop()

# Create a mapping from society name to its index
name_to_idx = {name: i for i, name in enumerate(loc_df.index)}

def blend_sim(sim1, sim2, sim3, w):
    """Blends similarity matrices with given weights and normalizes the result."""
    return normalize(w[0]*sim1 + w[1]*sim2 + w[2]*sim3, axis=1)

# Initialize weights in session state if they don't exist
if 'weights' not in st.session_state:
    st.session_state.weights = np.array([0.2, 0.6, 1.0])

# Calculate the blended similarity matrix
sim_matrix = blend_sim(sim1, sim2, sim3, st.session_state.weights)

st.title("Society Recommender System")

# --- User Inputs ---
center = st.selectbox("Select Your Location", sorted(loc_df.columns))
radius = st.number_input("Radius (in km)", min_value=1.0, max_value=50.0, value=5.0, step=0.5)

# Find nearby societies based on selected location and radius
nearby_societies = loc_df[loc_df[center] < radius * 1000]

if nearby_societies.empty:
    st.warning("No societies found within the selected radius. Try increasing the radius.")
    st.stop()

# Let user select a base society from the filtered list
base = st.selectbox("Select a Society to Find Similar Ones", sorted(nearby_societies.index))

# --- Weight Adjustment (Optional) ---
with st.expander("Adjust Recommendation Weights (Advanced)"):
    st.markdown("Fine-tune how much each factor contributes to the recommendation score.")
    w1 = st.slider("Amenity Importance", 0.0, 2.0, float(st.session_state.weights[0]))
    w2 = st.slider("Property Feature Importance", 0.0, 2.0, float(st.session_state.weights[1]))
    w3 = st.slider("Location Proximity Importance", 0.0, 2.0, float(st.session_state.weights[2]))

    # The button to apply weights is removed to make it more dynamic.
    # The matrix will re-calculate automatically whenever a slider is moved.
    st.session_state.weights = np.array([w1, w2, w3])
    sim_matrix = blend_sim(sim1, sim2, sim3, st.session_state.weights)


# --- Recommendation Function ---
def recommend(base_society, candidate_societies, center_location, top_n=5):
    """
    Recommends societies based on similarity scores and distance.
    Filters out the base_society from the recommendations.
    """
    base_idx = name_to_idx.get(base_society)
    if base_idx is None:
        st.error(f"Could not find the selected society '{base_society}' in the data.")
        return pd.DataFrame()

    results = []
    for candidate in candidate_societies:
        # *** THE FIX IS HERE: Skip the candidate if it's the same as the base society ***
        if candidate == base_society:
            continue

        candidate_idx = name_to_idx.get(candidate)
        if candidate_idx is not None:
            # Calculate similarity score
            similarity = sim_matrix[base_idx, candidate_idx]

            # Get distance in km
            dist_km = round(loc_df.at[candidate, center_location] / 1000, 2)

            # Combine similarity and distance into a final score
            # A higher weight on similarity, but distance still matters.
            score = 0.9 * similarity + 0.1 * (1 / (1 + dist_km))
            results.append((candidate, dist_km, score))

    # Create a DataFrame and sort by the final score
    df = pd.DataFrame(results, columns=["Society", "Distance (km)", "Score"])
    return df.sort_values("Score", ascending=False).head(top_n)[["Society", "Distance (km)"]]

# --- Display Recommendations ---
if st.button("Recommend Similar Societies"):
    recommendations = recommend(base, nearby_societies.index.tolist(), center)
    if not recommendations.empty:
        st.success("Here are your top recommendations:")
        st.dataframe(recommendations.reset_index(drop=True))
    else:
        st.info("No other similar societies found in the selected area.")
