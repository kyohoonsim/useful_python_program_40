from html2image import Html2Image

html = Html2Image() 
html.screenshot(url=["https://www.google.com/", "https://www.naver.com/", "https://www.daum.net/"], 
                save_as=['google.png', 'naver.png', 'daum.png'])