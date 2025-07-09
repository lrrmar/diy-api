from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from pydantic import BaseModel

import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ds = xr.open_dataset('temperature_timeseries.nc')

@app.get('/')
def root():
  return 'hello'

@app.get('/timeRange')
def timeRange():
    t = ds.coords['time'].values
    response = {
        'min': str(t.min()),
        'max': str(t.max())
    }
    return response

@app.get('/times')
def times(unix: bool = False):
    times = ds.coords['time'].values
    response = [str(t) for t in times]
    return response

@app.get('/dataRange')
def timeRange():
    d = ds.variables['air_temperature']
    print(d.attrs)
    response = {
        'min': d.values.min(),
        'max': d.values.max(),
        'units': d.attrs['units']
    }
    return response

class PlotParams(BaseModel):
  colour: str

def makePlot(colour):
  plt.figure()
  plt.plot(ds.coords['time'], ds.variables['air_temperature'], color=colour)
  plt.xlabel('time')
  plt.ylabel('Air Temperature [K]')
  ax = plt.gca()
  ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
  plt.grid()
  plt.savefig('temp.png')
  plt.close()

@app.get('/rangePlot')
def rangePlot(colour: str):
  makePlot(colour)
  return FileResponse('temp.png', media_type="image/png")

@app.post('/rangePlot')
def rangePlot(params: PlotParams):
  colour = params.colour
  makePlot(colour)
  return FileResponse('temp.png', media_type="image/png")
