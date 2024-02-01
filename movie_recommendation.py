import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from scipy.io import mmread

from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle
from konlpy.tag import Okt
from gensim.models import Word2Vec

nMovie = 10

def getRecommendation(cosine_sim):
    simScore = list(enumerate(cosine_sim[-1]))
    simScore = sorted(simScore,key=lambda x:x[1],reverse=True)
    simScore = simScore[:11]
    movieIdx=[i[0]for i in simScore]
    recmovieList = df_reviews.iloc[movieIdx,0]
    return recmovieList[1:11]

df_reviews = pd.read_csv('./cleaned_one_review.csv')
Tfidf_matrix=mmread('./models/Tfidf_movie_review.mtx').tocsr()
with open('./models/tfidf.pickle','rb') as f:
    Tfidf = pickle.load(f)

print('타겟영화:' ,df_reviews.iloc[nMovie,0])

cosine_sim = linear_kernel(Tfidf_matrix[nMovie],Tfidf_matrix)

# print(cosine_sim)
reccommendation = getRecommendation(cosine_sim)
print(reccommendation)