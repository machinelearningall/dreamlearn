2/5/24 challenge 
create a pygame simulation that turns into a visual 

STEP ONE  extract eog data from .edf file

import numpy as np
import mne
from mne.io import read_raw_edf
import pandas as pd  # Import pandas for CSV handling

# Load EDF file
edf_file = 'SC4001E0-PSG.edf'
raw = read_raw_edf(edf_file, preload=True)

# Pick the horizontal EOG channel
eog_data, times = raw.copy().pick_channels(['EOG horizontal']).get_data(return_times=True)

# Save EOG data to CSV
eog_df = pd.DataFrame(data={'Time': times, 'EOG Horizontal': eog_data[0, :]})
eog_df.to_csv('eogdata.csv', index=False)

print("Horizontal EOG data saved to 'eogdata.csv'")

OUTPUT

Time,EOG Horizontal
0.0,1.650866910866916e-05
0.01,1.601587301587307e-05
0.02,9.609523809523861e-06
0.03,1.7247863247863773e-06
0.04,7.63833943833949e-06
0.05,2.710378510378563e-06
0.06,2.463980463980988e-07
0.07,-7.391941391940868e-07

