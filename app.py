import streamlit as st
import pandas as pd
import numpy as np

st.title("간단한 Pandas + Streamlit 데모")

# 1. 데이터프레임 생성
st.subheader("무작위 데이터프레임")
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

st.dataframe(df)

# 2. 간단한 통계
st.subheader("통계 요약")
st.write(df.describe())

# 3. 사용자 입력으로 필터링
st.subheader("A 컬럼 필터링")
min_val = st.slider('A 컬럼 최소값 선택', float(df['A'].min()), float(df['A'].max()), float(df['A'].min()))
filtered_df = df[df['A'] >= min_val]

st.write("필터링된 데이터프레임")
st.dataframe(filtered_df)

# 4. 시각화 (라인 차트)
st.subheader("라인 차트")
st.line_chart(df)