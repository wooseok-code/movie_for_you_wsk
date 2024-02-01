import pandas as pd
from konlpy.tag import Okt
import re


# 1. 리뷰를 보고 비슷한 리뷰가 있는 것끼리 추천
# 2. 영화/감독
# 워딩의 유사도
# 형태소로 바꿔줌
# 영화나 감독에 대한 내용 + stopword 제거 + 한글자 단어 제거

df = pd.read_csv('./crawling_data/reviews_cleaned.csv')
df.info()

df_stopwords = pd.read_csv('./stopwords.csv')
stopwords = list(df_stopwords['stopword'])
stopwords = stopwords +['영화','감독','연출','배우','연기','작품','관객','장면','각본','개봉','장르','구성','모르다']
okt = Okt()
cleaned_sentences = []
# 부사는 학습에 별 도움이안됨
# 조사 영어에 없음 -> josa
# -> 명사 동사 형용사만 남길 것

for review in df.reviews:
    review = re.sub('[^가-힣]',' ',review)
    tokened_review = okt.pos(review,stem=True)
    print(tokened_review)
    df_token = pd.DataFrame(tokened_review, columns=['word','class'])
    df_token = df_token[(df_token['class']=='Noun') |(df_token['class']=='Verb')|(df_token['class']=='Adjective') ]

    words = []

    for word in df_token.word:
        if 1<len(word):
            if word not in stopwords:
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['reviews'] = cleaned_sentences
df.dropna(inplace = True)
df.to_csv('./cleaned_reviews.csv',index=False)
print(df.head())
df.info()

df = pd.read_csv('./cleaned_reviews.csv')
df.dropna(inplace=True)
df.info()
df.to_csv('./cleaned_reviews2.csv',index=False)


