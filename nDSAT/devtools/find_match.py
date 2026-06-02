# WAV AUDIO FILE FINDER!
# Brought to you by https://croaker.dev

# This was used for my own personal ROM modification project (NSMB+). 
# Check out NSMB+ [New Super Mario Bros DS - reimagined] https://github.com/Liam-GH/NSMBplus

############################ README ########################################
# finds WAV files in a given folder that match a target duration
# useful for finding replacement audio clips of a similar length
# usage: set target to the duration of the clip you want to replace, then run
############################################################################


import os
import wave
import sys

# path to your WAV folder
folder = sys.argv[1]

# target duration in seconds and how close the match needs to be
target = float(sys.argv[2])
tolerance = 0.2

# keyword to filter filenames e.g. 'LUIGI' to only search Luigi clips
keyword = sys.argv[3]

for filename in os.listdir(folder):
    if keyword in filename and filename.endswith('.wav'):
        path = os.path.join(folder, filename)
        with wave.open(path, 'r') as w:
            duration = w.getnframes() / w.getframerate()
            if abs(duration - target) < tolerance:
                print(f"{filename}: {duration:.3f}s")