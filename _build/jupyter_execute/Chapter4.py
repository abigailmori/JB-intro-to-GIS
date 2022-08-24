#!/usr/bin/env python
# coding: utf-8

# # Advanced Topics

# ## Additional mapping ideas
# Research question: What does the majority ethnic cluster look like in Los Angeles?
# 
# You can answer this question by using python queries.
# 
# <img src="images/query.png">

# In[1]:


# query the data for where there are more than 80% hispanics
gdf[gdf['Percent Hispanic'] > 80]


# In[ ]:


gdf[gdf['Percent Hispanic'] > 90].plot(figsize=(12,10))


# <div class="alert alert-info">
# 
# Now it's your turn! Create map plots based on other race indicators with varying segments of the population.
# 
# </div>

# In[ ]:





# ## Add a basemap
# 
# Adding a basemap to a geopandas plot can be done using the [contextily library](https://contextily.readthedocs.io/en/latest/intro_guide.html). To do so, you must:
# 
# * reproject your geodataframe to Web Mercator (epsg: 3857)
# * add a basemap, use the following [guidelines](https://github.com/geopandas/contextily/blob/master/notebooks/providers_deepdive.ipynb)

# ### Project to web mercator
# 
# ![projections](https://www.esri.com/arcgis-blog/wp-content/uploads/2022/02/grid2.png)
# 
# In order to conduct spatial analysis, it is recommended to use a projected coordinate system, rather than a geographic coordinate system (which uses angular measurements). Here is an [blog post from ESRI](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/gcs_vs_pcs/) that describes the differences between the two.

# In[ ]:


# reproject to Web Mercator
gdf_web_mercator = gdf.to_crs(epsg=3857)
gdf_web_mercator


# In[ ]:


# use subplots that make it easier to create multiple layered maps
fig, ax = plt.subplots(figsize=(15, 15))

# add the layer with ax=ax in the argument 
gdf_web_mercator[gdf_web_mercator['Percent Hispanic'] > 50].plot(ax=ax, alpha=0.8)

# turn the axis off
ax.axis('off')

# set a title
ax.set_title('Census Tracts with more than 50% Hispanic Population',fontsize=16)

# add a basemap
ctx.add_basemap(ax)

