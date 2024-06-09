import streamlit as st
from models.recommendation_model import RecommendationModel

# Initialize the recommendation model
model = RecommendationModel("data/North_America_Restaurants.csv")

# Streamlit app
st.title("Restaurant Recommendation System")

# Display a table of restaurant names with indices
st.subheader("Restaurant List")
st.dataframe(model.df[["name", "city", "state"]])

# Input restaurant index
restaurant_index = st.number_input(
    "Enter restaurant index", min_value=0, max_value=len(model.df) - 1
)

# Number of recommendations
num_recommendations = st.slider(
    "Number of recommendations", min_value=1, max_value=20, value=10
)

# Button to get recommendations
if st.button("Get Recommendations"):
    recommendations = model.get_recommendations(restaurant_index, num_recommendations)
    st.write(f"Recommendations for restaurant index {restaurant_index}:")
    for i, row in recommendations.iterrows():
        st.write(f"**{row['name']}**")
        st.write(f"Cuisines: {row['cuisines']}")
        st.write("---")

# Search functionality (optional)
search_query = st.text_input("Search for a restaurant by name")
if search_query:
    search_results = model.df[model.df["name"].str.contains(search_query, case=False)]
    st.write("Search Results:")
    st.dataframe(search_results[["name", "city", "state", "cuisines"]])
