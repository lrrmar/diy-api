from netCDF4 import Dataset, date2num
import numpy as np
from datetime import datetime, timedelta

# Create NetCDF file
file_path = "temperature_timeseries.nc"
ncfile = Dataset(file_path, 'w', format='NETCDF4_CLASSIC')

# Define dimensions
time_dim = ncfile.createDimension('time', 24)  # 24 hourly steps

# Create time variable
time_var = ncfile.createVariable('time', 'f8', ('time',))
time_var.units = 'hours since 2025-07-03 00:00:00'
time_var.calendar = 'gregorian'
time_var.standard_name = 'time'
time_var.long_name = 'time'

# Generate time data
base_time = datetime(2025, 7, 3, 0, 0, 0)
times = [base_time + timedelta(hours=i) for i in range(24)]
time_var[:] = date2num(times, units=time_var.units, calendar=time_var.calendar)

# Create temperature variable
temp_var = ncfile.createVariable('air_temperature', 'f4', ('time',))
temp_var.units = 'K'
temp_var.standard_name = 'air_temperature'
temp_var.long_name = 'Hourly air temperature'
temp_var.coordinates = 'time'

# Generate synthetic temperature data
np.random.seed(0)
temperature_data = 293 + np.random.normal(0, 2, 24)  # around 20°C
temp_var[:] = temperature_data

# Global attributes
ncfile.title = 'Hourly Air Temperature Time Series'
ncfile.institution = 'OpenAI Climate Lab'
ncfile.source = 'Synthetic data'
ncfile.history = f'Created {datetime.now().isoformat()}'
ncfile.references = 'None'

# Close file
ncfile.close()
print(f"File saved as {file_path}")
