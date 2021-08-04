"""
=======================================
Three dimensional plots with sunpy Maps
=======================================

Using sunkit-pyvista, one can interface with the `pyvista` package to
produce interactive 3D plots for sunpy Maps.
"""
from sunpy.data.sample import AIA_193_IMAGE
from sunpy.map import Map

from sunkit_pyvista import SunpyPlotter

###############################################################################
# We will firstly use an AIA 193 image from the sunpy sample data as the base image.
m = Map(AIA_193_IMAGE)

###############################################################################
# 3D plots are done on "plotter" objects, which are similar to matplotlib axes.
# sunkit-pyvista has a built in `SunpyPlotter` class that can be used to plot maps
# and coordinate aware objects.

# Start by creating a plotter
plotter = SunpyPlotter()

# Plot the map
plotter.plot_map(m)
# Add an arrow to show the solar rotation axis
plotter.plot_solar_axis()
plotter.show()