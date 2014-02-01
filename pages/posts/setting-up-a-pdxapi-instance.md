title: "Setting up a PDXAPI instance"
id: 1738
date: 2010-06-03 15:26:40
tags: 
- civicapps
- instructions
- pdxapi
categories: 
- osbridge
- portland

Today I spent a little time setting up a PDXAPI instance of the CivicApps data. There are a few different tools out there for grabbing the data and loading it up, and so I'm documenting the basic steps here for setting up a spatial SQLite using @lokkju's python projects.

<pre>
hg clone https://pyspatialite.googlecode.com/hg/ pyspatialite

cd pyspatialite
mv setup.cfg.OSX setup.cfg
python setup.py build
sudo python setup.py install

cd ..
cd pyod

hg clone https://pyod.googlecode.com/hg/ pyod

# unsatisfied dependency!
sudo easy_install pyyaml

pypython fetcher.py
</pre>

This creates a 1 GB sqlite database called 'test.sqlite'.

Next, I'll be testing out loading this into a CouchDB instance and maybe playing with Max Ogden's initial PostGIS export.
