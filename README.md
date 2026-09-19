# 🎬 Movie Recommender System

> A content-based movie recommendation web application built using **Python, Machine Learning, Pandas, Scikit-learn, and Streamlit** that recommends 5 similar movies based on the user's selection.

<p align="left">
  <a href="https://github.com/souravkeshri-14/movie-recommender-system">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</p>

## 🚀 Live Demo

**Live App:** https://movie-recommender-system-4t4wa7jnhhcaedeuz9e8ed.streamlit.app/

👉 **Try the Movie Recommender System**

---

## 📌 Features

- 🎥 Select a movie from a **searchable dropdown**
- 🤖 Get **5 similar movie recommendations**
- 🖼️ Automatically fetch **movie posters**
- ⚡ Fast recommendations using a **precomputed similarity matrix**
- 🌐 Interactive web interface built with **Streamlit**
- ☁️ Deployed online using **Streamlit Community Cloud**

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Requests**
- **Pickle**
- **Wikipedia API** – for movie poster retrieval

---

## 🧠 How It Works

The system uses a **content-based recommendation approach**.

1. Movie information is processed and transformed into numerical features.
2. Similarity between movies is calculated using the processed features.
3. The similarity matrix is saved as `similarity.pkl`.
4. When a user selects a movie, the system finds movies with the highest similarity scores.
5. The **top 5 similar movies** are displayed along with their posters.

---

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── movie-recommender-system.ipynb
├── requirements.txt
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Streamlit application used to run the recommender system |
| `movie_list.pkl` | Preprocessed movie list/data used by the application |
| `similarity.pkl` | Precomputed movie similarity matrix |
| `movie-recommender-system.ipynb` | Jupyter Notebook containing data processing and model development |
| `requirements.txt` | Python dependencies required to run the project |
| `README.md` | Project documentation |

---

## ⚙️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/souravkeshri-14/movie-recommender-system.git
```

### 2. Open the Project Directory

```bash
cd movie-recommender-system
```

### 3. Create and Activate a Virtual Environment

Create the environment:

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 📊 Dataset

The project uses movie information containing **movie titles and related features** for generating recommendations.

The trained/precomputed similarity matrix is stored separately as:

```text
similarity.pkl
```

---

## 🔮 Future Improvements

- ⭐ Add movie ratings and genres
- 🎯 Improve recommendation accuracy
- 📝 Add movie descriptions and release information
- 👤 Add user-based recommendations
- 🎨 Improve UI/UX
- 🕒 Add personalized recommendation history

---

## 👨‍💻 Author

**Sourav Keshri**

- GitHub: [souravkeshri-14](https://github.com/souravkeshri-14)
- Project: [Movie Recommender System](https://github.com/souravkeshri-14/movie-recommender-system)

---

## ⭐ Support

If you found this project useful, consider giving the repository a **star ⭐** on GitHub!

<p align="center">
  Made with ❤️ using Python & Streamlit
</p>

