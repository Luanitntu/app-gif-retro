# GIF Viewer - Code Optimization & New Features

## 🎯 Improvements Made

### 1. **Code Organization & Modularity**
   - **Separated concerns** into multiple classes:
     - `GifPlayer`: Handles GIF animation
     - `InputHandler`: Manages keyboard/joystick input
     - `AppState`: Tracks application state
     - `UIRenderer`: Handles all UI rendering
   
   - **Modularized configuration** (config.py):
     - Centralized all constants and settings
     - Added configuration file support (app_config.json)
     - Easy to modify button mappings and colors

   - **Enhanced helpers.py**:
     - Reusable utility functions
     - Image/GIF loading helpers
     - Text rendering functions
     - Path manipulation utilities

### 2. **Code Quality Improvements**
   - ✅ Removed code duplication
   - ✅ Better error handling
   - ✅ Added comprehensive comments
   - ✅ Consistent naming conventions
   - ✅ Reduced magic numbers (moved to config)
   - ✅ Improved function organization

### 3. **Performance Optimizations**
   - Frame-limited rendering loop (60 FPS)
   - Efficient screen update management
   - Better memory handling in GifPlayer
   - Optimized image scaling

### 4. **New Feature: Background Image Management**
   - 🎨 **Select custom background images** from the menu
   - 🎨 **Persistent background selection** (saved to config file)
   - 🎨 **Background browser** to browse available backgrounds
   - 🎨 **Auto-load** last selected background on startup

## 📋 Controls

### Menu Screen
- **[A]** - View GIFs from default folder
- **[X]** - Browse for GIF files
- **[MENU Button]** - Change background image (NEW!)
- **[B]** - Exit application

### GIF Viewer
- **[A]** - Next GIF (auto-mode only)
- **[Y]** - Previous GIF (auto-mode only)
- **[B]** - Return to menu

### Background Selector (NEW!)
- **[↑/↓]** - Navigate through available backgrounds
- **[A]** - Select background
- **[B]** - Cancel

### File Browser
- **[↑/↓]** - Navigate items
- **[A]** - Select folder/file
- **[B]** - Return to menu

## 📂 Directory Structure

```
GifViewerData/
├── main.py                 # Main application
├── images/                 # Place GIF files here
├── backgrounds/            # Place background images here (NEW!)
├── modules/
│   ├── __init__.py
│   ├── config.py          # Configuration & constants
│   └── helpers.py         # Utility functions
└── app_config.json        # Saved configuration (auto-created)
```

## 🖼️ How to Use Background Feature

1. **Create backgrounds folder** (or it will auto-create):
   ```
   GifViewerData/backgrounds/
   ```

2. **Add background images** (PNG format):
   - Copy your PNG images to `GifViewerData/backgrounds/`
   - Images can be any size (will be scaled to screen)

3. **Select background from menu**:
   - Press **[MENU Button]** on joystick (or [Y] on keyboard)
   - Navigate with **[↑/↓]**
   - Press **[A]** to select
   - Background is saved and will load automatically next time

## ⚙️ Configuration

Edit `modules/config.py` to customize:

```python
# Colors
BG_COLOR = (0, 0, 0)           # Background fill color
TEXT_COLOR = (255, 255, 255)   # Text color
HIGHLIGHT_COLOR = (255, 255, 0) # Highlight color
ERROR_COLOR = (255, 100, 100)  # Error message color

# Button mappings (Joystick)
BTN_ID_A = 3
BTN_ID_B = 4
BTN_ID_Y = 5
BTN_ID_X = 6
BTN_ID_MENU = 7  # Background selection button

# Keyboard shortcuts
KEY_A = [pygame.K_z, pygame.K_RETURN]
KEY_UP = [pygame.K_UP, pygame.K_w]
KEY_DOWN = [pygame.K_DOWN, pygame.K_s]
```

## 📝 Configuration File (app_config.json)

Automatically created and contains:
```json
{
  "current_background": "my_background.png"
}
```

## 🔧 Technical Details

### Classes
- **GifPlayer**: Efficient frame management and timing
- **InputHandler**: Unified input processing
- **AppState**: Single source of truth for app state
- **UIRenderer**: Clean separation of UI logic

### State Machine
- `MENU`: Main menu screen
- `VIEWER`: GIF display
- `BROWSER`: File browser
- `BG_SELECT`: Background selector (NEW!)

## 🚀 Future Enhancement Ideas

- Add image filters/effects
- Support for additional image formats (JPG, BMP)
- Background preview in selector
- Custom color themes saving
- Slideshow mode for GIFs
- Zoom controls for GIFs

## 📝 Notes

- The application disables screensaver during operation
- All file operations are wrapped with error handling
- Resolution detection works on Windows and Linux
- Supports both keyboard and joystick input
