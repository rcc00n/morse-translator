# Morse-code command-line exercise

Small historical Python exercise that maps Latin/Cyrillic letters, digits, and selected punctuation using `morse_alpha.txt`. Display name is clarified here; the historical repository URL is unchanged.

Run with Python 3.12: `python main.py`, enter one line, and press Enter. No third-party dependencies or network access are needed. The alphabet is resolved relative to the script so the command also works from another directory.

The original output convention is preserved: symbols concatenate with no letter delimiter, spaces become `/`, and unknown symbols are ignored. This is an encoding exercise, not a round-trip Morse protocol implementation.

Run `python -m unittest discover -s tests -v` for mixed-case, Cyrillic, punctuation, unsupported-symbol, and working-directory regressions.
