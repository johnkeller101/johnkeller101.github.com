# -*- coding: utf-8 -*-

import os
import glob

# reading the gpx data requires gpxpy, if you don't have it you will need to install it using pip

import gpxpy
import gpxpy.gpx

# necessary for encoding the javascript part of the html file

import json

#!/usr/bin/env python

# This script will generate a corresponding HTML map file for each .gpx file in the gpx directory
# if the map file already exists, it will not re-generate the file
# written by John Keller for john.coffee
# feel free to use this on your own projects

# based on the code found here: http://dutkowski.me/index.php/2016/12/26/leaflet-elevation-plugin-with-dynamic-markers/

gpx_dir = 'gpx/'
map_dir = 'maps/'

filenames = glob.glob(gpx_dir + '*gpx')

if len(filenames) == 0:
    print("No GPX files found.")

write_str = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
     <style>
       html, body, #map {
          height:100%;
          width:100%;
          padding:0px;
          margin:0px;
       }
    </style>
    <script src="/assets/js/d3.v3.min.js" charset="utf-8"></script>
    <script type="text/javascript" src="/assets/js/leaflet.js"></script>
    <link rel="stylesheet" href="/assets/built/leaflet.css" />
    <!--[if lte IE 8]><link rel="stylesheet" href="https://cdn.leafletjs.com/leaflet-0.7.2/leaflet.ie.css" /><![endif]-->

    <script type="text/javascript" src="/assets/js/leaflet.js"></script>
    <script type="text/javascript" src="/assets/js/L.Control.Elevation.js"></script>
</head>
<body>
    <div id="map"></div>

    <script type="text/javascript">
        var map = new L.Map('map');

        var url = 'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attr ='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
            service = new L.TileLayer(url, {subdomains:"1234",attribution: attr});

        var bounds = new L.LatLngBounds(new L.LatLng(39.6, -105), new L.LatLng(40.6, -105.5));

        var geojson = {"name":"NewFeatureType","type":"FeatureCollection"
,"features":[
{"type":"Feature","geometry":{"type":"LineString","coordinates":["""

for filename in filenames:
    # check if the file already exists
    name = filename.replace(gpx_dir,'').replace('.gpx','')
    filenames2 = glob.glob(map_dir + '*html')

    file_htm = map_dir + name + ".html"
    if file_htm in filenames2:
        # delete the old file
        print("Deleting old  ",name)
        os.remove(file_htm)

    print("Generating map file for ",name)

    # now to iterate through each of the files
    gps_data = []
    try:
        gpx_file = open(filename, "r")
        gpx = gpxpy.parse(gpx_file)
    except IOError:
        print("Couldn't open the input GPX file. Ensure it's in the 'data' dir.")
        raise()
    # now to formulate the data part of the html file to generate
    cutoff = 6
    count = 0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if count == cutoff:
                    write_str = write_str + '[' + str(point.longitude) + ',' + str(point.latitude) + ','+str(point.elevation)+'],'
                    count = 0
                # gps_data.append([point.latitude, point.longitude, point.elevation])
                count = count + 1
    write_str = write_str[:-1] #remove comma
    html_filename = map_dir + name + '.html'
    f = open(html_filename, 'a')
    write_str = write_str + """]},"properties":null}
]}
;
        var el = L.control.elevation({width: 600,imperial:true});
        el.addTo(map);
        var gjl = L.geoJson(geojson,{
            onEachFeature: el.addData.bind(el)
        }).addTo(map);

        map.addLayer(service).fitBounds(bounds);
    </script>
</body>
</html>
"""
    f.write(write_str)
    f.close()

# now that we have all the points, its time to properly wrap the data