<div align="center">

![nDSAT Logo](ndslogo.png)

# nDS Audio Toolkit (nDSAT)

A Nintendo DS ROM audio file extracting & converting tool.


</div>

---

## About
nDS Audio Toolkit enables you to listen to all sounds within any DS ROM of your choosing. Initially created to supplement my own nDS modification project, NSMB+. 

---

## Tools Built

| Script | Purpose |
|--------|---------|
| `extract.py` | Extracts all audio archives from any DS ROM |
| `convert.py` | Batch converts SWAR archives to WAV for listening |

---

## How to Use

1. Install dependencies: `pip3 install ndspy`
2. Place your DS ROM in the same folder as the scripts
3. Extract all audio archives from the ROM:
```bash
   python3 extract.py your_rom.nds
```
   This creates an `output` folder containing all SWAR files.

4. Convert all SWAR files to WAV for listening:
```bash
   python3 convert.py
```
   This creates a `WAV` folder with every individual sound as a separate WAV file.

## Requirements
- Python 3
- `ndspy`
- `vgmstream-cli` — install via `brew install vgmstream` on Mac, or download from [vgmstream.org](https://vgmstream.org) on Windows

---

## Planned Updates
- [ ] N/A 
---

<div align="center">

*Firmware, software, and published games under the Nintendo company are all Original intellectual property of Nintendo. All rights reserved. No game files are included or distributed.*

</div>
