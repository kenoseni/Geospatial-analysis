import folium

m = folium.Map(
    tiles='https://api.mapbox.com/v4/mapbox.mapbox-streets-v8/12/1171/1566.mvt?style=mapbox://styles/mapbox/streets-v11@00&access_token=pk.eyJ1Ijoia2Vub3NlbmkiLCJhIjoiY2s2a2tlZDJmMDR1bzNvbHNuZm9yaWU1cyJ9.h3y1GdgaNvwVMJFvQtgdEg',
    attr='Mapbox attribution',
    zoom_start=0,
)

# folium.GeoJson(
#     'lagos-local-government-administrative-boundaries/local-government-administrative-boundaries.geojson',
#     name='geojson'
# ).add_to(m)



# m = folium.Map(zoom_start=25, tiles='Mapbox', API_key='pk.eyJ1Ijoia2Vub3NlbmkiLCJhIjoiY2s2a2tlZDJmMDR1bzNvbHNuZm9yaWU1cyJ9.h3y1GdgaNvwVMJFvQtgdEg')

folium.Choropleth(geo_data='lagos-local-government-administrative-boundaries/local-government-administrative-boundaries.geojson',
                  line_color='green',
                  fill_color='white',
                  name='choropleth',
                  key_on='feature.id',
                  line_weight=3).add_to(m)

folium.LayerControl(position='bottomleft').add_to(m)

folium.Icon().add_to(m)

m.save('lagos.html')
