#!/usr/bin/python

# The ChartDirector for Python module is assumed to be in "../lib"
import sys, os
sys.path.insert(0, os.path.join(os.path.abspath(sys.path[0]), "..", "lib"))

from pychartdir import *

# The diameter of the wafer
diameter = 20
radius = diameter / 2.0

# The random data array are for a square grid of 20 x 20 cells
r = RanSeries(2)
zData = r.get2DSeries(diameter, diameter, 0, 100)

# We remove cells that are outside the wafer circle by setting them to NoValue
for i in range(0, len(zData)) :
    x = i % diameter + 0.5
    y = (i - x) / diameter + 0.5
    if (x - radius) * (x - radius) + (y - radius) * (y - radius) > radius * radius :
        zData[i] = NoValue

# Create an XYChart object of size 520 x 480 pixels.
c = XYChart(520, 480)

# Add a title the chart with 15pt Arial Bold font
c.addTitle("Wafer Map Demonstration", "Arial Bold", 15)

# Set the plotarea at (50, 40) and of size 400 x 400 pixels. Set the backgound and border to
# transparent. Set both horizontal and vertical grid lines to light grey. (0xdddddd)
p = c.setPlotArea(50, 40, 400, 400, -1, -1, Transparent, 0xdddddd, 0xdddddd)

# Create a discrete heat map with 20 x 20 cells
layer = c.addDiscreteHeatMapLayer(zData, diameter)

# Set the x-axis scale. Use 8pt Arial Bold font. Set axis color to transparent, so only the labels
# visible. Set 0.5 offset to position the labels in between the grid lines.
c.xAxis().setLinearScale(0, diameter, 1)
c.xAxis().setLabelStyle("Arial Bold", 8)
c.xAxis().setColors(Transparent, TextColor)
c.xAxis().setLabelOffset(0.5)

# Set the y-axis scale. Use 8pt Arial Bold font. Set axis color to transparent, so only the labels
# visible. Set 0.5 offset to position the labels in between the grid lines.
c.yAxis().setLinearScale(0, diameter, 1)
c.yAxis().setLabelStyle("Arial Bold", 8)
c.yAxis().setColors(Transparent, TextColor)
c.yAxis().setLabelOffset(0.5)

# Position the color axis 20 pixels to the right of the plot area and of the same height as the plot
# area. Put the labels on the right side of the color axis. Use 8pt Arial Bold font for the labels.
cAxis = layer.setColorAxis(p.getRightX() + 20, p.getTopY(), TopLeft, p.getHeight(), Right)
cAxis.setLabelStyle("Arial Bold", 8)

# Output the chart
c.makeChart("wafermap.png")

