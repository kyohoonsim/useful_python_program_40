from googletrans import Translator

simpago = Translator()

trans_src = "저는 지금 파이썬 코딩에 관한 책을 쓰고 있습니다."
trans_dest = simpago.translate(trans_src, dest='en', src='ko')

print(f"원문: {trans_src}")
print(f"번역: {trans_dest.text}")