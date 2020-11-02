# HAS TOOLS - Assignment 10 - Mapping
# Danielle Tadych

# %%
import os
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx


# %%
#  Gauges II USGS stream gauge dataset:
# Download here:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

# Reading it using geopandas
file = os.path.join('../data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Zoom  in and just look at AZ
gages.columns
gages.STATE.unique()
gages_AZ = gages[gages['STATE'] == 'AZ']
gages_AZ.shape


# %%
# adding more datasets
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Example reading in a geodataframe
# Watershed boundaries for the lower Colorado
file = os.path.join('../data', 'NHD_H_Arizona_State_GDB.gdb')
fiona.listlayers(file)
HUC10 = gpd.read_file(file, layer='WBDHU10')
HUC10.head()

# NHD was giving me problems so I'm going to try some other flowline shape
# The Nature Conservatory datsets can be downloaded here:
# http://azconservation.org/downloads/category/gis
file = os.path.join('../data', 'az_hydro_routes.shp')
flowlines = gpd.read_file(file)

# %%
# Add point for stream gauge
# UA:  32.22877495, -110.97688412
# Stream gauge:  34.9455, -111.789167

point_list = np.array([[-111.789167, 34.448333]])

# Make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

# make a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC10.crs)


# To fix this we need to re-project
points_project = point_df.to_crs(gages_AZ.crs)

# %%
# reprojecting streamflow
stream_project = flowlines.to_crs(gages_AZ.crs)
HUC10_project = HUC10.to_crs(gages_AZ.crs)

# Want to add one more layer for groundwater wells
# Groundwater well shape files can be downloaded here from ADWR:
# https://new.azwater.gov/gis
file = os.path.join('../data', 'GWSI_SITES.shp')
wells = gpd.read_file(file)
wells_project = wells.to_crs(gages_AZ.crs)

# %%
# Actual plotting

fig, ax = plt.subplots()
# gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
#               legend=True, markersize=25, cmap='Set2',
#               ax=ax)
stream_project.plot(ax=ax, label="Flowlines", color='blue')
wells_project.plot(ax=ax, label="Groundwater Wells", color='green')
HUC10_project.boundary.plot(ax=ax, color=None,
                            edgecolor='black', linewidth=1,
                            label="HUC 10 Watershed Boundary")
points_project.plot(ax=ax, color='red', marker='*', label="Stream Gauge")
ax.set(title="VERDE RIVER NEAR CAMP VERDE, AZ", ylim=[1.36e6, 1.4e6],
       xlim=[-1.45e6, -1.395e6])
ax.legend()
ctx.add_basemap(ax)

