import pickle
import streamlit as st
import requests

# -----------------------------------
# Fetch movie poster using OMDb
# -----------------------------------
def fetch_poster(movie_title):

    api_key = "YOUR_OMDB_API_KEY"

    url = "https://www.omdbapi.com/"

    params = {
        "apikey": api_key,
        "t": movie_title
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        if data.get("Response") == "True":

            poster = data.get("Poster")

            if poster and poster != "N/A":
                return poster

    # If poster is not found
    return "https://via.placeholder.com/300x450?text=No+Poster"


# -----------------------------------
# Recommendation function
# -----------------------------------
def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:

        movie_title = movies.iloc[i[0]].title

        # Fetch poster using movie title
        poster = fetch_poster(movie_title)

        recommended_movie_posters.append(poster)
        recommended_movie_names.append(movie_title)

    return recommended_movie_names, recommended_movie_posters


# -----------------------------------
# Streamlit UI
# -----------------------------------

st.header("Movie Recommender System")

movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button("Show Recommendation"):

    recommended_movie_names, recommended_movie_posters = recommend(
        selected_movie
    )

    # New Streamlit syntax
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])