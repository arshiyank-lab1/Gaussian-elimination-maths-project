# M3 Animation Video — Gaussian Elimination

**Mohammad Arshiyan Ali Imran Ali Khan · E25B070750**

This lesson uses reversible row operations and back-substitution to solve one three-variable system. The worked answer is `(1, 2, 3)`.

| File | Purpose |
|---|---|
| `_Video.mp4` | Silent 1080p recording master, exactly 5:00 |
| `Storyboard.pdf` | Six-scene visual, narration and mathematics plan |
| `Narration_Script.md` | Spoken script with time ranges |
| `Recording_Guide.md` | Recording, syncing and export steps |
| `_Code/` | Runnable source for the video, storyboard and script |

## Rebuild

Use Python 3 with FFmpeg on your PATH and the regular and bold DejaVu Sans fonts installed. Run from the repository root.

```sh
python -m pip install -r _Code/requirements.txt
python _Code/render.py --output _Video.mp4
python _Code/supporting_files.py
```

For a single still preview, run `python _Code/render.py --preview 70 --output preview.png`.

## Credits

The M3 Internal Assessment brief provided the topic and project structure. ChatGPT assisted with scripting, visuals and animation code. The animation diagrams are drawn from the worked equations. The recording master contains no music or voice track.
