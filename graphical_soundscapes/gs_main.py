"""
Graphical soundscape with local maxima
WARNING: THIS SCRIPT IS UNDER CONSTRUCTION

"""
import pandas as pd
import yaml
from maad import sound
from gs_utils import spectrogram_local_max, graphical_soundscape, plot_graph
import matplotlib.pyplot as plt

#%% Load configuration files
# Open the config file and load its contents into a dictionary
with open("../config.yaml", "r") as f:
    config = yaml.safe_load(f)

path_audio = config["input_data"]["path_audio"]
path_metadata = config["preprocessing"]["path_save_metadata_clean"]
target_fs = 48000
nperseg = 256
noverlap = 128
db_range = 80
min_peak_distance = 5
min_peak_amplitude = 30  # CAT001=40

#%%
df = pd.read_csv(path_metadata)

for site, df_site in df.groupby('site'):
    graph = graphical_soundscape(
        df_site.reset_index(drop=True),
        target_fs,
        nperseg,
        noverlap,
        db_range,
        min_peak_distance,
        min_peak_amplitude
    )
    plot_graph(graph)

#%%
s, fs = sound.load(
    "/Volumes/lacie_exfat/Cataruben/audio/CAT002/CAT002_20221231_070000.WAV"
)
fpeaks = spectrogram_local_max(
    s,
    fs,
    nperseg,
    noverlap,
    db_range,
    min_peak_distance,
    min_peak_amplitude,
    display=True,
)
