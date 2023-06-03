import streamlit as st
import pandas as pd

st.write("""
# 데이터 시각화
전달 받은 엑셀 파일을 시각화해줍니다.
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df = df.set_index('월')
    st.write(df)
    st.bar_chart(df)