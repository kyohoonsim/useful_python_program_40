from html2image import Html2Image

html = Html2Image() 
html_src = '''
    <div>
        <div id="top"></div>
        <div id="bottom"></div>
    </div>
'''
css_src = '''
    #top {width: 1000px; height: 300px; background-color: #0058b5;}
    #bottom {width: 1000px; height: 300px; background-color: #f7ce00;}
'''
html.screenshot(html_str=html_src, css_str=css_src, save_as="ukraine.png")