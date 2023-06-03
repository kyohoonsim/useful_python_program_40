import pandas as pd

df = pd.read_excel('./회원리스트.xlsx')
print(df, "\n")

df_lucky = df[df['이벤트 당첨 여부']=='O']
print(df_lucky, "\n")

for idx, row in df_lucky.iterrows():
    print(f"{row['이름']}님의 이메일 {row['이메일주소']}으로 당첨 이메일 전송!")