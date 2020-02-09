# build/cb_2014_us_county_20m.zip:
# 	mkdir -p $(dir $@)
# 	curl -o $@ https://www2.census.gov/geo/tiger/GENZ2014/shp/cb_2014_us_county_20m.zip

all: us.json

clean: rm -rf -- us.json build

.PHONY: all clean

# od means where to download
# $@ is build/gz_2010_us_050_00_20m.zip
# $< is build/gz_2010_us_050_00_20m.shp
# touch $@ means go and unzip that file and use it

build/gz_2010_us_050_00_20m.shp: build/gz_2010_us_050_00_20m.zip
	unzip -od $(dir $@) $<
	touch $@

# Download the shapefile   
build/gz_2010_us_050_00_20m.zip:
	mkdir -p $(dir $@)
	curl -o $@ https://www2.census.gov/geo/tiger/GENZ2010/$(notdir $@)
