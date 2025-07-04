import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from .models import Movie

def get_recommendations(movie_id, top_n=5, min_shared_genres=2):
    movies = Movie.objects.all().values("id", "title", "genres")
    movies_df = pd.DataFrame(movies)

    if not movies_df[movies_df["id"] == movie_id].empty:
        selected_movie = movies_df[movies_df["id"] == movie_id].iloc[0]
    else:
        return []

    movies_df = movies_df.drop_duplicates(subset="title", keep="first").reset_index(drop=True)

    if not movies_df[movies_df["id"] == movie_id].empty:
        movie_idx = movies_df[movies_df["id"] == movie_id].index[0]
    else:
        return []

    mlb = MultiLabelBinarizer()
    genres_encoded = mlb.fit_transform(
        movies_df["genres"].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
    )
    genre_df = pd.DataFrame(genres_encoded, columns=mlb.classes_)

    similarity_matrix = cosine_similarity(genre_df)
    sim_scores = [(i, score) for i, score in enumerate(similarity_matrix[movie_idx]) if i != movie_idx]

    if not any(score > 0 for _, score in sim_scores):
        return []

    # Compter les genres partagés pour chaque film
    selected_genres = set(
        json.loads(selected_movie["genres"]) if isinstance(selected_movie["genres"], str) else selected_movie["genres"]
    )
    shared_genres = []
    for i, score in sim_scores:
        if score > 0:
            movie_genres = set(
                json.loads(movies_df.iloc[i]["genres"]) if isinstance(movies_df.iloc[i]["genres"], str) else movies_df.iloc[i]["genres"]
            )
            num_shared = len(selected_genres.intersection(movie_genres))
            shared_genres.append((i, score, num_shared))

    # Filtrer les films avec au moins min_shared_genres genres communs
    filtered_scores = [(i, score) for i, score, num_shared in shared_genres if num_shared >= min_shared_genres]

    if not filtered_scores:
        return []

    # Trouver la similarité maximale parmi les films filtrés
    max_similarity = max(score for _, score in filtered_scores)
    max_sim_indices = [i for i, score in filtered_scores if score == max_similarity]
    max_sim_indices = max_sim_indices[:top_n]

    return movies_df.iloc[max_sim_indices][["id", "title", "genres"]].to_dict("records")