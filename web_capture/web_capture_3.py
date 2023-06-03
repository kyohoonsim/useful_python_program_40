from html2image import Html2Image

html = Html2Image() 
html_src = "<div>Hello World!</div>"
css_src = '''
    div {
        width: 1200px; 
        height: 1200px; 
        background-color: blue; 
        color: white; 
        font-size: 100px;
        text-align: center;
    }
'''
html.screenshot(html_str=html_src, css_str=css_src, save_as="custom.png")