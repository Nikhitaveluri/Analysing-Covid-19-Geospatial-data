from datetime import datetime 
import pandas as pd
import numpy as np
import geopandas as gpd
import contextily as ctxdflfölfd
import matplotlib.pyplot as plt

#Reading the data:
#url = 'https://proxy.hxlstandard.org/data/e2bb4b/download/jrc-covid-19-regions-hxl.csv'
dtypes = {
    'Date': object,
    'iso3': object,
    'CountryName': object,
    'Region': object,
    'lat': float,
    'lon': float,
    'CumulativePositive': float,
    'CumulativeDeceased': float,
    'CumulativeRecovered': float,
    'CurrentlyPositive': float,
    'Hospitalized': float,
    'IntensiveCare': float,
    'EUcountry': np.bool,
    'EUCPMcountry': np.bool,
    'NUTS': object,
    }

df = pd.read_csv("jrc-covid-19-regions-hxl.csv", skiprows=range(1, 2), dtype=dtypes)
