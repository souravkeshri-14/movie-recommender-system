🎬 Movie Recommender System

A content-based Movie Recommendation System built using Python, Machine Learning, and Streamlit. The application recommends 5 similar movies based on the movie selected by the user.

🚀 Live Demo : https://movie-recommender-system-4t4wa7jnhhcaedeuz9e8ed.streamlit.app/

👉 Try the Movie Recommender System

📌 Features
🎥 Select a movie from a searchable dropdown
🤖 Get 5 similar movie recommendations
🖼️ Automatically fetch movie posters
⚡ Fast recommendation using a precomputed similarity matrix
🌐 Interactive web interface using Streamlit
☁️ Deployed online with Streamlit Community Cloud

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Requests
Pickle
Wikipedia API – for movie poster retrieval

🧠 How It Works

The system uses a content-based recommendation approach.

Movie information is processed and transformed into numerical features.
Similarity between movies is calculated.
The similarity matrix is saved as similarity.pkl.
When a user selects a movie, the system finds movies with the highest similarity scores.
The top 5 similar movies are displayed along with their posters.

📂 Project Structure

movie-recommender-system
-> app.py
-> movie_list.pkl
-> similarity.pkl
-> movie-recommender-system.ipynb
-> requirements.txt
-> README.md

⚙️ Run Locally

1. Clone the repository git clone https://github.com/souravkeshri-14/movie-recommender-system.git
2. Open the project cd movie-recommender-system
3. Create and activate virtual environment python -m venv .venv
Windows: .venv\Scripts\activate
4. Install dependencies pip install -r requirements.txt
5. Run the application streamlit run app.py

The application will open at:

http://localhost:8501

📊 Dataset

The project uses movie information containing movie titles and related features for generating recommendations.

The trained/precomputed similarity matrix is stored separately as similarity.pkl.

🔮 Future Improvements
Add movie ratings and genres
Improve recommendation accuracy
Add movie descriptions and release information
Add user-based recommendations
Improve UI/UX
Add personalized recommendation history

👨‍💻 Author

Sourav Keshri

GitHub: souravkeshri-14
Project Repository: Movie Recommender System

⭐ If you found this project useful, consider giving it a star!
