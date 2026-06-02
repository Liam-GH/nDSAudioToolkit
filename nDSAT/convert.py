# CONVERT SWAR FILES TO WAV AUDIO FILES!
# Brought to you by https://croaker.dev
# Check out NSMB+ [New Super Mario Bros DS - reimagined] https://github.com/Liam-GH/NSMBplus

import os

input_folder = os.path.expanduser('~/Desktop/ROM-Sounds')
output_folder = os.path.expanduser('~/Desktop/ROM-WAV')

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.swar'):
        input_path = os.path.join(input_folder, filename)
        name = filename.replace('.swar', '')
        # Loop through up to 50 streams per file
        for i in range(1, 50):
            output_path = os.path.join(output_folder, f'{name}_s{i}.wav')
            result = os.system(f'vgmstream-cli "{input_path}" -s {i} -o "{output_path}"')
            if result != 0:
                # No more streams in this file
                break