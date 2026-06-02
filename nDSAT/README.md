# nDSAT

---

## extract.py

Extracts all audio archives from a DS ROM into an `output` folder.

```bash
python3 extract.py your_rom.nds
```

---

## convert.py

Converts all SWAR files in the `output` folder to WAV.

```bash
python3 convert.py
```

---

# devtools

Utility scripts for use alongside nDSAT.

---

## find_match.py

Searches a folder of WAV files for clips matching a target duration. Useful for finding replacement audio when ROM hacking.

```bash
python3 find_match.py ~/path/to/WAV-folder 0.660 KEYWORD
```

- `WAV-folder` — path to your folder of converted WAV files
- `0.660` — target duration in seconds
- `KEYWORD` — filename filter e.g. `LUIGI`