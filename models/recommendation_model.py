import pandas as pd
from sklearn.feature_extraction.text import (
    TfidfVectorizer,
)
from sklearn.metrics.pairwise import (
    cosine_similarity,
)
from utils.text_preprocessing import (
    preprocess_text,
)  # Ensure this import is correct


class RecommendationModel:
    def __init__(
        self,
        data_path,
    ):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self.tfidf_matrix = None
        self.cosine_sim = None
        print(self.df["cuisines"].isnull().sum())
        self._prepare_model()

    def _prepare_model(
        self,
    ):
        self.df = self.df.dropna(subset=["cuisines"])
        print(self.df["cuisines"].isnull().sum())
        self.df["processed_cuisines"] = self.df["cuisines"].apply(
            preprocess_text
        )
        vectorizer = TfidfVectorizer()
        self.tfidf_matrix = vectorizer.fit_transform(
            self.df["processed_cuisines"]
        )
        self.cosine_sim = cosine_similarity(
            self.tfidf_matrix,
            self.tfidf_matrix,
        )

    def get_recommendations(
        self,
        index,
        num_recommendations=10,
    ):
        sim_scores = list(enumerate(self.cosine_sim[index]))
        sim_scores = sorted(
            sim_scores,
            key=lambda x: x[1],
            reverse=True,
        )
        sim_scores = sim_scores[1 : num_recommendations + 1]
        restaurant_indices = [i[0] for i in sim_scores]
        return self.df[
            [
                "name",
                "cuisines",
            ]
        ].iloc[restaurant_indices]
