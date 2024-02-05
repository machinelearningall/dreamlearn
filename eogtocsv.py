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
