# ⚡ Quick Reference Card

## 🎮 Controls at a Glance

```
┌─────────────────────────────────────────┐
│           MAIN MENU CONTROLS            │
├─────────────────────────────────────────┤
│ [A] ..................... View GIFs     │
│ [X] ............... Browse Files        │
│ [MENU/Y] ... ✨ Change Background       │
│ [B] ..................... Exit          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│        GIF VIEWER CONTROLS              │
├─────────────────────────────────────────┤
│ [A] ............ Next GIF (auto-mode)   │
│ [Y] ........ Previous GIF (auto-mode)   │
│ [B] .................. Back to Menu     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│     BACKGROUND SELECTOR CONTROLS        │
├─────────────────────────────────────────┤
│ [↑/↓] ........... Navigate Backgrounds  │
│ [A] ............. Select Background     │
│ [B] ................... Cancel          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│       FILE BROWSER CONTROLS             │
├─────────────────────────────────────────┤
│ [↑/↓] ........... Navigate Files        │
│ [A] ... Select Folder / Open GIF        │
│ [B] .................. Back to Menu     │
└─────────────────────────────────────────┘
```

---

## 📂 Quick Setup

### 1️⃣ Add GIF Files
```
GifViewerData/
└── images/
    ├── animation1.gif
    ├── animation2.gif
    └── animation3.gif
```

### 2️⃣ Add Background Images (NEW!)
```
GifViewerData/
└── backgrounds/
    ├── bg1.png
    ├── bg2.png
    └── bg3.png
```

### 3️⃣ Run Application
```bash
cd GifViewerData
python main.py
```

---

## 🎨 Background Feature Usage

```
MENU → [Y Button] → SELECT BACKGROUND → [A to confirm] → AUTO-SAVED
                         ↓
                    Use ↑/↓ to browse
```

- Backgrounds auto-save to `app_config.json`
- PNG images scale automatically
- Only shows on menu (not on GIF viewer)
- Easy to change anytime

---

## ⚙️ Quick Config Tips

### Change Menu Colors
Edit `modules/config.py`:
```python
TEXT_COLOR = (255, 255, 255)      # White
HIGHLIGHT_COLOR = (255, 255, 0)   # Yellow
ERROR_COLOR = (255, 100, 100)     # Red
BG_COLOR = (0, 0, 0)              # Black
```

### Remap Buttons
Edit `modules/config.py`:
```python
BTN_ID_A = 3          # Confirm
BTN_ID_B = 4          # Cancel/Back
BTN_ID_X = 6          # Browse
BTN_ID_Y = 5          # Previous/Backgrounds
```

### Change Key Bindings
Edit `modules/config.py`:
```python
KEY_A = [pygame.K_z, pygame.K_RETURN]
KEY_UP = [pygame.K_UP, pygame.K_w]
```

---

## 📊 File Structure Reference

```
GifViewerData/
├── main.py ..................... Main Application
├── modules/
│   ├── config.py .............. Configuration
│   └── helpers.py ............. Utilities
├── images/ .................... GIF Files
└── backgrounds/ ............... Background Images

Root/
├── SETUP_COMPLETE.md .......... This Guide
├── OPTIMIZATION_NOTES.md ...... Detailed Info
├── CODE_OPTIMIZATION_REPORT.md  Before/After
└── BACKGROUND_SETUP.md ........ Background Guide
```

---

## 🐛 Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Background not showing | Verify PNG in `backgrounds/` folder |
| Can't find background selector | Press [Y] or [MENU Button] on joystick |
| Text hard to read | Use darker background image |
| GIFs not loading | Check `images/` folder has .gif files |
| App crashes on start | Ensure pygame and PIL installed |

---

## 📝 Classes & Methods (Development Reference)

```
GifPlayer
  ├── load_gif(filepath)
  ├── update()
  └── draw(surface)

InputHandler
  ├── update(event)
  └── time_since_input()

AppState
  ├── load_background(bg_path)
  ├── load_gif_list(directory)
  ├── load_directory_items(directory)
  └── load_background_list()

UIRenderer
  ├── draw_background(bg_surface)
  ├── draw_menu(app_state)
  ├── draw_browser(app_state)
  ├── draw_background_selector(app_state)
  └── draw_viewer(app_state, input_handler)
```

---

## 🚀 Pro Tips

1. **Dark backgrounds work best** - Better contrast with white text
2. **Square or wider images** - Screens are typically 16:9
3. **Get images free** - Unsplash.com, Pexels.com, Pixabay.com
4. **Use keyboard** - [Z] for A, [X] for B, [A] for X, [Y] for Y
5. **Customize everything** - Edit `modules/config.py` without breaking code

---

## 📞 Need Help?

- **App won't run?** → Install: `pip install pygame pillow`
- **Can't find backgrounds?** → Create `GifViewerData/backgrounds/` folder
- **Buttons not working?** → Check `modules/config.py` mappings
- **Text not visible?** → Use darker background image
- **Want to modify?** → Edit `modules/config.py` for safe changes

---

Enjoy! 🎉✨
