from typing import Union

from fastapi import FastAPI, HTTPException
import pandas as pd


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movie/{movie_cd}")
def movie_meta(movie_cd: str):
    df = pd.read_parquet('/home/kim1/code/ffapi/data')

    # df 에서 mmovieCd == movie_cd row 를 조회
    # 조회된 데이터를 .to_dict() 로 만들어
    result = df[df['movieCd'] == movie_cd]
    if meta_df.empty:
        raise HTTPException(status_code=404, detail="영화를 찾을 수 없습니다")

    #return {"movie_cd": movie_cd,"df_count": len(df), "result" : result}
    return meta_df.iloc[0].to_dict()

@app.get("/sample")
def sample_data():
    df = pd.read_parquet('/home/kim1/code/ffapi/data')
    sample_df = df.sample(n=5)
    r = sample_df.to_dict(orient='records')
    return r
