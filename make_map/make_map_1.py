import folium

jecheon_map = folium.Map(location=[37.14315, 128.2016], zoom_start=14)
jecheon_map.save('jecheon_map.html')