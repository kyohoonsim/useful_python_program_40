import streamlit as st
from googletrans import Translator

translator = Translator()

st.write("""
# 번역 모델 v0.1
입력된 텍스트를 영어로 번역합니다.
""")

txt = st.text_area('번역할 텍스트', 
    '''
    안녕하세요. 반갑습니다. 파이썬 공부 재밌게 하고 계신가요?
    ''')

st.write('번역 결과:', translator.translate(txt, dest='en', src='ko').text)