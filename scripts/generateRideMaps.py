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
    <title>Coordinate viewing test page</title>
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

    <style>
    .lime-theme.leaflet-control.elevation .background{background-color:rgba(156,194,34,.2);-webkit-border-radius:5px;-moz-border-radius:5px;-ms-border-radius:5px;-o-border-radius:5px;border-radius:5px}.lime-theme.leaflet-control.elevation .axis line,.lime-theme.leaflet-control.elevation .axis path{fill:none;stroke:#566b13;stroke-width:2}.lime-theme.leaflet-control.elevation .mouse-drag{fill:rgba(99,126,11,.4)}.lime-theme.leaflet-control.elevation .elevation-toggle{cursor:pointer;box-shadow:0 1px 7px rgba(0,0,0,.4);-webkit-border-radius:5px;border-radius:5px;width:36px;height:36px;background-color:#f8f8f9}.lime-theme.leaflet-control.elevation .elevation-toggle-icon{background:url(images/elevation-lime.png) no-repeat center center}.lime-theme.leaflet-control.elevation .area{fill:#9cc222}.lime-theme.leaflet-control.elevation .mouse-focus-line{pointer-events:none;stroke-width:1;stroke:#101404}.lime-theme.leaflet-control.elevation-collapsed .background{display:none}.lime-theme.leaflet-control.elevation-collapsed .elevation-toggle{display:block}.lime-theme.height-focus{stroke:#9cc222;fill:#9cc222}.lime-theme.height-focus.line{pointer-events:none;stroke-width:2}.steelblue-theme.leaflet-control.elevation .background{background-color:rgba(70,130,180,.2);-webkit-border-radius:5px;-moz-border-radius:5px;-ms-border-radius:5px;-o-border-radius:5px;border-radius:5px}.steelblue-theme.leaflet-control.elevation .axis line,.steelblue-theme.leaflet-control.elevation .axis path{fill:none;stroke:#0d1821;stroke-width:2}.steelblue-theme.leaflet-control.elevation .mouse-drag{fill:rgba(23,74,117,.4)}.steelblue-theme.leaflet-control.elevation .elevation-toggle{cursor:pointer;box-shadow:0 1px 7px rgba(0,0,0,.4);-webkit-border-radius:5px;border-radius:5px;width:36px;height:36px;background-color:#f8f8f9}.steelblue-theme.leaflet-control.elevation .elevation-toggle-icon{background:url(images/elevation-steelblue.png) no-repeat center center}.steelblue-theme.leaflet-control.elevation .area{fill:#4682b4}.steelblue-theme.leaflet-control.elevation .mouse-focus-line{pointer-events:none;stroke-width:1;stroke:#0d1821}.steelblue-theme.leaflet-control.elevation-collapsed .background{display:none}.steelblue-theme.leaflet-control.elevation-collapsed .elevation-toggle{display:block}.steelblue-theme.height-focus{stroke:#4682b4;fill:#4682b4}.steelblue-theme.height-focus.line{pointer-events:none;stroke-width:2}.purple-theme.leaflet-control.elevation .background{background-color:rgba(115,44,123,.2);-webkit-border-radius:5px;-moz-border-radius:5px;-ms-border-radius:5px;-o-border-radius:5px;border-radius:5px}.purple-theme.leaflet-control.elevation .axis line,.purple-theme.leaflet-control.elevation .axis path{fill:none;stroke:#2d1130;stroke-width:2}.purple-theme.leaflet-control.elevation .mouse-drag{fill:rgba(74,14,80,.4)}.purple-theme.leaflet-control.elevation .elevation-toggle{cursor:pointer;box-shadow:0 1px 7px rgba(0,0,0,.4);-webkit-border-radius:5px;border-radius:5px;width:36px;height:36px;background-color:#f8f8f9}.purple-theme.leaflet-control.elevation .elevation-toggle-icon{background:url(images/elevation-purple.png) no-repeat center center}.purple-theme.leaflet-control.elevation .area{fill:#732c7b}.purple-theme.leaflet-control.elevation .mouse-focus-line{pointer-events:none;stroke-width:1;stroke:#000}.purple-theme.leaflet-control.elevation-collapsed .background{display:none}.purple-theme.leaflet-control.elevation-collapsed .elevation-toggle{display:block}.purple-theme.height-focus{stroke:#732c7b;fill:#732c7b}.purple-theme.height-focus.line{pointer-events:none;stroke-width:2}
    </style>
    <div id="map"></div>

    <script type="text/javascript">
        var map = new L.Map('map');

        var url = 'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attr ='Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
            service = new L.TileLayer(url, {subdomains:"1234",attribution: attr});

        var bounds = new L.LatLngBounds(new L.LatLng(-44.6, 170), new L.LatLng(-45, 168));

        var geojson = {"name":"NewFeatureType","type":"FeatureCollection"
,"features":[
{"type":"Feature","geometry":{"type":"LineString","coordinates":["""

for filename in filenames:
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
    html_filename = map_dir + 'test.html'
    f = open(html_filename, 'a')
    write_str = write_str + """]},"properties":null}
]}
;
var el = L.control.elevation({width: 600});
        el.addTo(map);
        var gjl = L.geoJson(geojson,{
            onEachFeature: el.addData.bind(el)
        }).addTo(map);

        map.addLayer(service).fitBounds(bounds);

var marker = L.marker(geojson.features[0].geometry.coordinates[0]);
marker.addTo(map);



var coords_i = 1;

var moveMarker = function() {
    if(coords_i == geojson.features[0].geometry.coordinates.length) {
        coords_i = 0;
    }
    var coords = geojson.features[0].geometry.coordinates[coords_i];
    var latlng = new L.LatLng(coords[1], coords[0]);
    marker.setLatLng(latlng);
    coords_i++;
}

var interval = setInterval(moveMarker, 1000);

el.addMarker(marker);
    </script>
</body>
</html>
"""
    f.write(write_str)
    f.close()

# now that we have all the points, its time to properly wrap the data