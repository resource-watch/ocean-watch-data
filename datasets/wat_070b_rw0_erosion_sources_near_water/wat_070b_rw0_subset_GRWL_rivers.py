# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# wat_070b_rw0_subset_GRWL_rivers.py
# Created on: 2021-10-29 14:11:25.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
GRWL_projected = "GRWL_projected"
GRWL_projected__2_ = GRWL_projected
ne_10m_coastline_shp = "C:\\Users\\RThoms.Local\\Downloads\\ne_10m_coastline\\ne_10m_coastline.shp"
GRWL_projected__4_ = GRWL_projected__2_
HydroRiv_5km_Buffer = "C:\\Users\\RThoms.Local\\OneDrive - World Resources Institute\\Documents\\ArcGIS\\Sediment Pressure\\Sediment Pressure.gdb\\HydroRiv_5km_Buffer"
GRWL_selection_coast_and_rivers = "C:\\Users\\RThoms.Local\\OneDrive - World Resources Institute\\Documents\\ArcGIS\\Sediment Pressure\\Sediment Pressure.gdb\\GRWL_selection_coast_and_rivers"

# Process: Select Layer By Location
arcpy.SelectLayerByLocation_management(GRWL_projected, "WITHIN_A_DISTANCE_GEODESIC", ne_10m_coastline_shp, "5 Kilometers", "NEW_SELECTION", "NOT_INVERT")

# Process: Select Layer By Location (2)
arcpy.SelectLayerByLocation_management(GRWL_projected__2_, "HAVE_THEIR_CENTER_IN", HydroRiv_5km_Buffer, "3 Kilometers", "ADD_TO_SELECTION", "NOT_INVERT")

# Process: Copy Features
arcpy.CopyFeatures_management(GRWL_projected__4_, GRWL_selection_coast_and_rivers, "", "0", "0", "0")

