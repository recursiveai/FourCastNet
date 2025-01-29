import xarray as xr
import argparse
import os
from utils.YParams import YParams

def get_era5_data(params):
    """Load the ERA5 data from zarr file, subselect variables and time range, save as nc file.
    """
    
    era5_zarr = xr.open_zarr(params.era5_source)
    all_vars = params.era5_vars
    era5_data = era5_zarr.sel(time=params.time_sel, level=params.pressure_level)[all_vars]
    era5_data = era5_data.compute()
    era5_data.to_netcdf("data/era5_data.nc")
    return
    

def main(params):
    # load the data
    get_era5_data(params)
    # format for inference
    # save as h5
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--yaml_config", default='./config/AFNO.yaml', type=str)
    args = parser.parse_args()
    params = YParams(os.path.abspath(args.yaml_config), 'full_field')
    main(params)