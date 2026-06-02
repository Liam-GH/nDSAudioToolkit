# EXTRACT AUDIO ARCHIVES FROM nDS ROM!
# Brought to you by https://croaker.dev
# Check out NSMB+ [New Super Mario Bros DS - reimagined] https://github.com/Liam-GH/NSMBplus

import ndspy.rom
import ndspy.soundArchive
import os
import sys

# 1. Loads ROM. instead of the path being hardcoded, anyone can run the script with their own ROM path.
rom = ndspy.rom.NintendoDSRom.fromFile(sys.argv[1])

sound_id = rom.filenames.idOf('sound_data.sdat')
sdat_data = rom.files[sound_id]

# 2. Take the raw bytes of the SDAT file pulled out of the ROM, and tell ndspy to read it as a proper SDAT so the sounds inside can be accessed.
sdat = ndspy.soundArchive.SDAT(sdat_data)

# 3. Outputs the sounds into "ROM-Sounds" folder, onto your desktop.
      # [change the os path & path name based on your own preference]
folder = os.path.expanduser('~/Desktop/ROM-Sounds')
os.makedirs(folder, exist_ok=True)

# 4. goes through all the SWAVs in the SDAT and saves each one as a file.
for name, waveArchive in sdat.waveArchives:
   with open(os.path.join(folder, name + '.swar'), 'wb') as f:
        f.write(waveArchive.save()[0])

