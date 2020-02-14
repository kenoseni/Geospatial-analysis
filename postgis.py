import psycopg2, shapely, shapely.speedups

from osgeo import ogr

connection = psycopg2.connect(database='geospatial_db', user='olusola', password='Iimpeccable1@')

cursor = connection.cursor()

# create table to hold hold data for world borders
cursor.execute('DROP TABLE IF EXISTS borders')

command = """CREATE TABLE borders(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    iso_code VARCHAR NOT NULL,
    outline GEOGRAPHY
)""" # a spatial geography field called outline is created here

cursor.execute(command)

# cusor.execute("CREATE TABLE borders(" + 
#               "id SERIAL PRIMARY KEY," + 
#               "name VARCHAR NOT NULL," + 
#               "iso_code VARCHAR NOT NULL," + 
#               "outline GEOGRAPHY)") # a spatial geography field called outline is created here

#  Because we're using a geography field, we
# can use this field to store spatial data that uses unprojected lat/long coordinates

# This statement creates a spatial index on the outline. In PostGIS, we use the
# GIST index type to define a spatial index
cursor.execute("CREATE INDEX border_index ON borders " + 
              "USING GIST(outline)")

connection.commit()

shapefile = ogr.Open("TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp")
layer = shapefile.GetLayer(0)

print('********************', shapely.__version__)
print('>>>>>>>>>>>>>>>>>', shapely.speedups.available)

for i in range(layer.GetFeatureCount()):
    feature = layer.GetFeature(i)
    # provides the properties of each feature
    # print('>>>>>>>>>>>>>>>>>>>', feature.items())
    name = feature.GetField("NAME")
    iso_code = feature.GetField("ISO3")
    geometry = feature.GetGeometryRef()

    wkt = geometry.ExportToWkt()
    
    """
    Because psycopg2 doesn't know about geometry data values, we have to convert the
    geometry into a WKT-format string and then use the ST_GeogFromText() function
    to convert that string back into a PostGIS geography object.
    """
    
    cursor.execute("INSERT INTO borders(name, iso_code, outline) " + 
                  "VALUES (%s, %s, ST_GeogFromText(%s))",
                  (name, iso_code, wkt))

connection.commit()
