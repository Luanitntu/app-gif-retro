# 🎬 GIF Viewer

A feature-rich GIF viewer application built with Python, Pygame, and PIL. Display, navigate, and manage GIF animations and background images with full logging and configuration support.

![Version](https://img.shields.io/badge/version-2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.7+-blue)

## ✨ Features

### Core Features
- 🎬 **GIF Playback** - Smooth animation playback with frame timing
- 📂 **File Browser** - Navigate and select GIF files from any directory
- 🎨 **Custom Backgrounds** - Select and persist background images for menu screen
- ⌨️ **Dual Input** - Joystick and keyboard support with customizable button mapping
- 📋 **Comprehensive Logging** - Detailed event tracking and error reporting
- ⚙️ **Configuration Management** - JSON-based persistent settings

### Advanced Features
- 🔄 **Rotating Logs** - Automatic log rotation with archive management
- 🎮 **Auto/Manual Modes** - Automatic GIF cycling or manual navigation
- 🌙 **Screensaver Control** - Disable/restore screensaver during operation
- 📊 **Performance Tracking** - Monitor frame count and application statistics
- 🔍 **Log Viewer Utility** - Interactive tool to analyze logs
- 🏗️ **Modular Architecture** - Clean, maintainable, object-oriented design

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/GifViewer.git
cd GifViewer
```

2. **Install dependencies**
```bash
pip install pygame pillow
```

3. **Run the application**
```bash
cd GifViewerData
python main.py
```

## 📖 Usage

### Menu Controls

#### Joystick Controls
| Button | Action |
|--------|--------|
| **[A]** | View GIFs from default folder |
| **[X]** | Browse files |
| **[Y/MENU]** | Select background image |
| **[B]** | Exit application |

#### Keyboard Controls
| Key | Action |
|-----|--------|
| **[Z/Enter]** | Confirm (A button) |
| **[X/Esc]** | Cancel/Back (B button) |
| **[↑/W]** | Navigate up |
| **[↓/S]** | Navigate down |
| **[Y]** | Backgrounds (Y button) |

### GIF Viewer
- **[A]** - Next GIF (auto-mode only)
- **[Y]** - Previous GIF (auto-mode only)
- **[B]** - Return to menu
- Auto-hide controls after 5 seconds of inactivity

### File Browser
- **[↑/↓]** - Navigate files and folders
- **[A]** - Select folder or open GIF file
- **[B]** - Return to menu

### Background Selector (NEW!)
- **[↑/↓]** - Navigate available backgrounds
- **[A]** - Select and save background
- **[B]** - Cancel

## 📂 Project Structure

```
GifViewer/
├── README.md                        # This file
├── SETUP_COMPLETE.md               # Setup and optimization guide
├── OPTIMIZATION_NOTES.md           # Code optimization details
├── CODE_OPTIMIZATION_REPORT.md     # Before/after comparison
├── BACKGROUND_SETUP.md             # Background feature guide
├── LOGGING_GUIDE.md                # Comprehensive logging guide
├── LOGGING_IMPLEMENTATION.md       # Logging technical details
├── LOGGING_QUICK_REFERENCE.md      # Quick logging reference
├── QUICK_REFERENCE.md              # Controls and tips
├── GifViewerData/
│   ├── main.py                     # Main application
│   ├── app_config.json             # Auto-created config
│   ├── images/                     # GIF files (put .gif files here)
│   ├── backgrounds/                # Background images (.png)
│   ├── logs/                       # Application logs (auto-created)
│   │   ├── app.log                 # Main log
│   │   └── error.log               # Error log
│   └── modules/
│       ├── __init__.py
│       ├── config.py               # Configuration constants
│       ├── helpers.py              # Utility functions
│       └── logger.py               # Logging system
├── GifViewer.sh                    # Unix/Linux launcher
├── MUOS_READER.md                  # MUOS documentation
└── log_viewer.py                   # Log management utility
```

## ⚙️ Configuration

### Application Settings (modules/config.py)

**Color Customization**
```python
BG_COLOR = (0, 0, 0)              # Background fill color
TEXT_COLOR = (255, 255, 255)      # Text color
HIGHLIGHT_COLOR = (255, 255, 0)   # Highlight color
ERROR_COLOR = (255, 100, 100)     # Error message color
```

**Button Mapping (Joystick)**
```python
BTN_ID_A = 3      # Confirm
BTN_ID_B = 4      # Cancel/Back
BTN_ID_X = 6      # Browse
BTN_ID_Y = 5      # Previous/Backgrounds
BTN_ID_MENU = 7   # Menu/Settings
```

**Keyboard Shortcuts**
```python
KEY_A = [pygame.K_z, pygame.K_RETURN]
KEY_B = [pygame.K_x, pygame.K_ESCAPE]
KEY_UP = [pygame.K_UP, pygame.K_w]
KEY_DOWN = [pygame.K_DOWN, pygame.K_s]
```

### Persistent Configuration (app_config.json)

Auto-created on first run:
```json
{
  "current_background": "my_background.png"
}
```

## 📋 Logging System

### Log Files
- **app.log** - All application events (DEBUG level and above)
- **error.log** - Errors and warnings only
- Automatic rotation at 5MB with 5-version history

### View Logs

**Interactive log viewer**
```bash
python log_viewer.py
```

**Command-line usage**
```bash
python log_viewer.py view 50       # View last 50 lines
python log_viewer.py errors        # View errors only
python log_viewer.py session       # View last session
python log_viewer.py search "GIF"  # Search keyword
python log_viewer.py stats         # Show statistics
```

### Log Contents
- Application startup/shutdown
- GIF and background loading
- User actions and navigation
- Error messages and warnings
- Performance metrics (frame count)
- Detailed debug information

## 🎨 Background Images

### Adding Backgrounds

1. **Create backgrounds folder** (auto-created on first run)
   ```
   GifViewerData/backgrounds/
   ```

2. **Add PNG images**
   - Copy PNG files to `backgrounds/` folder
   - Any size (will be auto-scaled)
   - Recommended: Dark or subtle patterns for text readability

3. **Select from menu**
   - Press **[MENU/Y Button]** on joystick
   - Navigate with **[↑/↓]**
   - Press **[A]** to select
   - Automatically saved and loads next time

### Good Practices
✅ Dark backgrounds (better text contrast)  
✅ Subtle patterns (text readability)  
✅ Wide aspect ratio (for widescreen displays)  

❌ Very bright images  
❌ Complex detailed backgrounds  
❌ Very small resolution  

## 🏗️ Architecture

### Class Structure

**GifPlayer**
- Handles GIF animation playback
- Frame management and timing
- Render-to-surface functionality

**InputHandler**
- Unified input processing
- Keyboard and joystick support
- Input timing tracking

**AppState**
- Centralized application state
- Background and GIF management
- Configuration persistence

**UIRenderer**
- All UI drawing logic
- Menu, browser, and viewer screens
- Background selector

### Design Patterns
- **Singleton**: LoggerSetup for global logger access
- **State Machine**: Menu, Viewer, Browser, BG_Select modes
- **Modular**: Separated concerns (config, helpers, logger)

## 🔧 Development

### Code Quality
- Object-oriented design
- Comprehensive error handling
- Full docstring coverage
- Modular, testable components
- ~40% code duplication reduction from original

### Adding Features

**Add new logging**
```python
from modules.logger import get_logger
logger = get_logger()
logger.info("Your message here")
```

**Add new configuration constants**
```python
# In modules/config.py
NEW_SETTING = "value"
```

**Create utility function**
```python
# In modules/helpers.py
def new_function():
    """Function description"""
    return result
```

### Building & Testing

```bash
# Check syntax
python -m py_compile GifViewerData/main.py

# Run with debug output
python GifViewerData/main.py

# Check logs
python log_viewer.py view 100
```

## 🐛 Troubleshooting

### GIFs not loading
1. Check `GifViewerData/images/` folder
2. Verify files have `.gif` extension
3. Check logs: `python log_viewer.py errors`

### Buttons not responding
1. Verify joystick is connected
2. Check logs for "joystick" messages
3. Review button mapping in `modules/config.py`

### Background not showing
1. Ensure PNG files in `GifViewerData/backgrounds/`
2. Check logs for "Background loaded"
3. Try different image format

### Application crashes
1. Check `GifViewerData/logs/error.log`
2. Review full traceback in logs
3. Verify dependencies installed: `pip install pygame pillow`

### Performance issues
1. Check frame count in final log line
2. Monitor system resources
3. Reduce background image resolution

See **LOGGING_QUICK_REFERENCE.md** for quick troubleshooting commands.

## 📚 Documentation

- **README.md** - This file, project overview and quick start
- **SETUP_COMPLETE.md** - Complete setup and optimization guide
- **OPTIMIZATION_NOTES.md** - Code optimization and architecture details
- **BACKGROUND_SETUP.md** - Detailed background feature guide
- **LOGGING_GUIDE.md** - Comprehensive logging system guide
- **QUICK_REFERENCE.md** - Controls and configuration reference
- **LOGGING_QUICK_REFERENCE.md** - Quick logging commands

## 💻 System Requirements

### Minimum
- Python 3.7+
- 512MB RAM
- Display: 640x480 or higher
- Pygame-compatible OS (Windows, Linux, macOS)

### Recommended
- Python 3.9+
- 2GB+ RAM
- Full HD display (1920x1080)
- Modern joystick controller

### Supported Platforms
- ✅ Windows (7+)
- ✅ Linux
- ✅ macOS
- ✅ MUOS (handheld gaming OS)

## 📦 Dependencies

```
pygame>=2.0.0
pillow>=8.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

Or individually:
```bash
pip install pygame pillow
```

## 🎮 Tested Joysticks

- Xbox 360 Controller
- Xbox One Controller
- Generic USB Joysticks
- MUOS handheld controllers
- Keyboard (for testing)

## 📊 Performance

- **Rendering**: 60 FPS
- **Memory**: ~50-150MB (depends on GIF complexity)
- **Log Disk Usage**: ~50MB maximum (auto-managed)
- **Startup Time**: <5 seconds (typically)

## 🔐 Privacy & Security

- ✅ No internet connection required
- ✅ All data stored locally
- ✅ No telemetry or tracking
- ✅ No personal data collection
- ✅ Open source (code auditable)

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Update logs when adding features
- Test thoroughly before submitting
- Update documentation

## 🐛 Reporting Issues

Found a bug? Please create an issue with:
1. Clear description of the problem
2. Steps to reproduce
3. Expected vs actual behavior
4. Relevant log excerpts
5. System information

## 🚀 Future Enhancements

- [ ] image filters and effects
- [ ] Support for JPG, BMP, WebP formats
- [ ] Background preview in selector
- [ ] Custom color theme management
- [ ] Slideshow mode
- [ ] Zoom and pan controls
- [ ] Settings UI menu
- [ ] Plugin system
- [ ] Network file support
- [ ] Thumbnail previews

## 📞 Support

For help or questions:
- Check the documentation files
- Review logs with `python log_viewer.py`
- Search existing GitHub issues
- Create a new issue with details

## 🙏 Acknowledgments

- **Pygame**: Game development library
- **PIL/Pillow**: Image processing
- **Python**: Programming language
- Community contributors and testers

## 📈 Version History

### v2.0 (Current)
- Complete code refactoring and optimization
- Object-oriented architecture
- Background image selection system
- Comprehensive logging system
- Configuration management
- Log viewer utility
- Extensive documentation

### v1.0
- Initial release
- Basic GIF viewing
- File browser
- Joystick and keyboard support

## 🎯 Project Stats

- **Lines of Code**: ~700 (main.py) + ~200 (modules)
- **Classes**: 5 (GifPlayer, InputHandler, AppState, UIRenderer, LoggerSetup)
- **Functions**: 30+ utility functions
- **Documentation**: 8 comprehensive guides
- **Test Coverage**: Manual testing on multiple platforms

---

## Quick Command Reference

```bash
# Run application
cd GifViewerData && python main.py

# View logs
python log_viewer.py

# Search logs (Windows PowerShell)
Select-String "ERROR" GifViewerData\logs\app.log

# Check dependencies
pip list | grep pygame

# Install requirements
pip install -r requirements.txt

# Check Python version
python --version
```

---

**Made with ❤️ for GIF enthusiasts**

*Last Updated: March 11, 2026*  
*Latest Version: 2.0*
