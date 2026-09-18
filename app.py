import os
import pickle
from urllib.parse import quote

import requests
import streamlit as st


# -----------------------------------
# Fetch movie poster from Wikipedia
# -----------------------------------
@st.cache_data
def fetch_poster(movie_title):

    search_url = "https://en.wikipedia.org/w/api.php"

    headers = {
        "User-Agent": "MovieRecommendationSystem/1.0"
    }

    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": movie_title + " film",
        "srlimit": 5
    }

    try:
        response = requests.get(
            search_url,
            params=search_params,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return None

        results = response.json().get("query", {}).get("search", [])

        if not results:
            return None

        page_title = results[0]["title"]

        encoded_title = quote(
            page_title.replace(" ", "_")
        )

        summary_url = (
            "https://en.wikipedia.org/api/rest_v1/page/summary/"
            + encoded_title
        )

        response = requests.get(
            summary_url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            thumbnail = data.get("thumbnail")

            if thumbnail:
                return thumbnail.get("source")

    except Exception:
        pass

    return None


# -----------------------------------
# Load movie list
# -----------------------------------
movies = pickle.load(
    open("movie_list.pkl", "rb")
)


# -----------------------------------
# Download similarity matrix
# from Hugging Face
# -----------------------------------
MODEL_URL = (
    "https://huggingface.co/"
    "souravkeshri14/movie-recommender-model/"
    "resolve/main/similarity.pkl"
)


@st.cache_resource
def load_similarity():

    file_path = "similarity.pkl"

    # Download only if the file doesn't already exist
    if not os.path.exists(file_path):

        with requests.get(
            MODEL_URL,
            stream=True,
            timeout=600
        ) as response:

            response.raise_for_status()

            with open(file_path, "wb") as f:

                for chunk in response.iter_content(
                    chunk_size=1024 * 1024
                ):

                    if chunk:
                        f.write(chunk)

    # Load similarity matrix
    with open(file_path, "rb") as f:
        return pickle.load(f)


similarity = load_similarity()


# -----------------------------------
# Recommendation function
# -----------------------------------
def recommend(movie):

    index = movies[
        movies["title"] == movie
    ].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:

        movie_title = movies.iloc[i[0]]["title"]

        recommended_movie_names.append(
            movie_title
        )

        poster = fetch_poster(movie_title)

        recommended_movie_posters.append(
            poster
        )

    return (
        recommended_movie_names,
        recommended_movie_posters
    )


# -----------------------------------
# Streamlit UI
# -----------------------------------
st.title("🎬 Movie Recommender System")

st.write(
    "Select a movie and get 5 similar movie recommendations."
)


movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button("Show Recommendation"):

    (
        recommended_movie_names,
        recommended_movie_posters
    ) = recommend(selected_movie)

    st.subheader(
        "Recommended Movies"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    columns = [
        col1,
        col2,
        col3,
        col4,
        col5
    ]

    for i in range(5):

        with columns[i]:

            st.write(
                recommended_movie_names[i]
            )

            if recommended_movie_posters[i]:

                st.image(
                    recommended_movie_posters[i],
                    use_container_width=True
                )

            else:

                st.write(
                    "Poster not available"
                )