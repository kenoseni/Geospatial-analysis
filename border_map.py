import folium

m = folium.Map(zoom_start=3)

folium.Choropleth(geo_data='worldBorders.json',
                  line_color='red', line_weight=1).add_to(m)

folium.LayerControl().add_to(m)

m.save('main.html')
