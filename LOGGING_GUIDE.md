# 📋 Logging System Guide

## Overview

The GIF Viewer application now includes a comprehensive logging system that collects all events, errors, and debug information to help with troubleshooting and monitoring.

---

## 📂 Log Files Location

All logs are stored in the `GifViewerData/logs/` directory:

```
GifViewerData/
└── logs/
    ├── app.log           # All application logs
    ├── error.log         # Error logs only
    ├── app.log.1         # Rotated archive (if needed)
    ├── app.log.2
    ├── error.log.1
    └── error.log.2
```

### Automatic Log Rotation
- **Log files rotate automatically** when they reach 5MB
- **Keep last 5 versions** of each log file
- **Old logs are archived** with numbered suffixes

---

## 🔍 Log Files Explained

### `app.log` - Main Application Log
Contains **all** application events:
- ✅ Application startup/shutdown
- ✅ GIF loading and information
- ✅ Background image selection
- ✅ User actions (menu selections, navigation)
- ✅ Directory scanning
- ✅ Configuration changes
- ✅ Errors and warnings
- ✅ Debug information

**Example:**
```
2024-03-11 14:23:45 - GifViewer - INFO - ============================================================
2024-03-11 14:23:45 - GifViewer - INFO - GIF Viewer Started - 2024-03-11 14:23:45
2024-03-11 14:23:45 - GifViewer - INFO - ============================================================
2024-03-11 14:23:45 - GifViewer - INFO - Initializing pygame...
2024-03-11 14:23:45 - GifViewer - INFO - Pygame initialized successfully
2024-03-11 14:23:46 - GifViewer - INFO - Display set to: 1920x1080
2024-03-11 14:23:47 - GifViewer - INFO - Application ready - entering main loop
2024-03-11 14:23:50 - GifViewer - INFO - Menu: View GIFs selected
2024-03-11 14:23:50 - GifViewer - INFO - Loaded 5 GIF files from: D:\GifViewerData\images
2024-03-11 14:23:51 - GifViewer - INFO - Loading GIF: D:\GifViewerData\images\animation1.gif
2024-03-11 14:23:51 - GifViewer - INFO - Successfully loaded GIF: 12 frames, Size: (1536, 864), Original: 2560x1440
```

### `error.log` - Errors and Warnings Only
Contains **only error and warning level** messages:
- ❌ Application errors
- ⚠️ Warnings (missing files, etc.)
- 🐛 Exception stack traces

**Useful for:**
- Quick troubleshooting
- Identifying problems
- Debugging failures

---

## 📊 Log Levels

The application uses standard logging levels:

| Level | Severity | Color | Example |
|-------|----------|-------|---------|
| **DEBUG** | Low | Gray | `Loading directory items...` |
| **INFO** | Normal | Blue | `Menu: View GIFs selected` |
| **WARNING** | Medium | Yellow | `No GIFs found in directory` |
| **ERROR** | High | Red | `GIF Load Error: Invalid file` |
| **CRITICAL** | Severe | Red Bold | `Fatal error: Cannot initialize Pygame` |

---

## 🔧 How Logging Works

### Initialization
1. Logger is created on application startup
2. Directory structure is verified
3. Rotating file handlers are set up
4. Startup message is logged

### During Operation
1. Every user action is logged
2. File operations are tracked
3. Errors are captured with full details
4. Debug information available for development

### Cleanup
1. Final summary logged on exit
2. Total frames rendered recorded
3. All resources properly closed

---

## 📝 What Gets Logged

### Application Lifecycle
```
✓ Application started
✓ Components initialized
✓ Display configured
✓ Directories created
✓ User actions
✓ Application exited
```

### File Operations
```
✓ GIF files found and loaded
✓ Backgrounds discovered
✓ Directory navigated
✓ File selection changes
✓ Load errors and details
```

### User Interactions
```
✓ Menu selections
✓ Button presses
✓ Mode changes
✓ Navigation events
✓ Background changes
```

### System Information
```
✓ Display resolution
✓ Joystick count and names
✓ File counts
✓ Frame count
✓ Timing information
```

---

## 🔎 Reading Log Files

### Using Command Line (Windows PowerShell)
```powershell
# View last 50 lines of app log
Get-Content "GifViewerData\logs\app.log" -Tail 50

# View errors only
Get-Content "GifViewerData\logs\error.log"

# Search for specific text
Select-String "ERROR" "GifViewerData\logs\app.log"

# Follow log in real-time
Get-Content "GifViewerData\logs\app.log" -Wait
```

### Using Text Editor
1. Open `GifViewerData/logs/app.log` with any text editor
2. Scroll to the end for latest events
3. Use Find (Ctrl+F) to search for keywords

### Using PowerShell
```powershell
# Find all loading errors
Get-Content "GifViewerData\logs\app.log" | Select-String "Load Error"

# Show errors from last hour
Get-Content "GifViewerData\logs\app.log" | Select-String "$(Get-Date -Format 'HH:')"
```

---

## 🐛 Troubleshooting with Logs

### Problem: App won't start
**Check app.log for:**
- `Pygame initialized successfully` → Pygame works
- `Display set to:` → Display configuration
- `Fatal error` → Critical issue

### Problem: GIFs not loading
**Check app.log for:**
- `Loaded X GIF files from:` → File scanning
- `GIF Load Error:` → What failed
- Check error.log for full error details

### Problem: Background not showing
**Check app.log for:**
- `Loaded X background images` → Backgrounds found
- `Background loaded successfully` → Success
- `error loading background` → Failure details

### Problem: Buttons not working
**Check app.log for:**
- `Found X joystick(s)` → Joystick detected
- `Joystick X initialized:` → Which joysticks
- Look for button press logs when testing

---

## 📈 Log File Structure

### Log Line Format
```
TIMESTAMP - LOGGER_NAME - LEVEL - MESSAGE
```

Example:
```
2024-03-11 14:23:50 - GifViewer - INFO - Menu: View GIFs selected
```

### Components:
- **TIMESTAMP**: Date and time with seconds
- **LOGGER_NAME**: Always "GifViewer"
- **LEVEL**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **MESSAGE**: Description of what happened

---

## 💾 Disk Space Management

### Automatic Cleanup
- Logs rotate at 5MB per file
- Last 5 versions kept for each log file
- **Maximum disk usage**: ~50MB for logs

### Manual Cleanup
```powershell
# Remove old logs
Remove-Item "GifViewerData\logs\*.log.*"

# Keep only current logs
Remove-Item "GifViewerData\logs\error.log.*"
```

---

## 🔐 Privacy & Security

### What's NOT Logged
- User keystrokes/sensitive input
- System passwords
- File contents (only filenames)
- Network information

### What IS Logged
- Application events
- File paths
- Error messages
- User selections

---

## 📊 Example Log Analysis

### Typical Startup Sequence
```
INFO - GIF Viewer Started
INFO - Initializing pygame...
INFO - Pygame initialized successfully
INFO - Disabling screensaver...
INFO - Found 1 joystick(s)
INFO - Display set to: 1920x1080
INFO - Application ready - entering main loop
```

### Typical User Session
```
INFO - Menu: View GIFs selected
INFO - Loaded 5 GIF files from: D:\GifViewerData\images
INFO - Entering VIEWER mode with first GIF
INFO - Loading GIF: animation1.gif
INFO - Successfully loaded GIF: 12 frames
DEBUG - Next GIF: animation2.gif
INFO - Selected background: nature.png
INFO - Background loaded successfully
```

### Typical Shutdown
```
INFO - Menu: Exit selected
INFO - Application exiting - Total frames rendered: 45230
INFO - Restoring screensaver...
INFO - Shutting down pygame...
INFO - Application shutdown complete
```

---

## 🚀 Development Tips

### Enable Debug Output
Debug logs are automatically included. Check `app.log` for DEBUG level messages:
```
grep "DEBUG" GifViewerData/logs/app.log
```

### Common Debug Information
- Frame by frame navigation details
- Directory scanning results
- File loading specifics
- Component initialization

### Add Custom Logging (Code)
```python
from modules.logger import get_logger
logger = get_logger()

# Log custom events
logger.info("Custom event occurred")
logger.warning("Something suspicious happened")
logger.error("Something went wrong")
logger.debug("Development information")
```

---

## 📞 When to Check Logs

✅ **Always check logs when:**
- Application doesn't behave as expected
- Files aren't loading
- Features seem broken
- Before reporting issues
- For performance analysis
- During development/testing

✅ **Look for specific patterns:**
- ERROR messages for failures
- Timing information for performance
- File counts for verification
- Mode changes for flow analysis

---

Logging makes debugging and monitoring easy! 📋✨
