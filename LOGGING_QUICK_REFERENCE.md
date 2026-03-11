# 📋 Logging Quick Reference

## 📂 Log Files Location
```
GifViewerData/logs/
├── app.log       ← All events
├── error.log     ← Errors only
└── (archives)
```

## 🚀 Quick Start

### View Logs
```bash
# Interactive menu
python log_viewer.py

# View app log (last 50 lines)
python log_viewer.py view 50

# View errors only
python log_viewer.py errors

# View last session
python log_viewer.py session

# Search for text
python log_viewer.py search "GIF"

# Show statistics
python log_viewer.py stats

# Clean old logs
python log_viewer.py clean
```

## 📊 What Gets Logged

| Event | Level | Example |
|-------|-------|---------|
| App starts | INFO | `Application started` |
| Pygame init | INFO | `Pygame initialized successfully` |
| Display setup | INFO | `Display set to: 1920x1080` |
| Joysticks | INFO | `Found 2 joystick(s)` |
| GIFs loaded | INFO | `Loaded 5 GIF files` |
| GIF playing | INFO | `Loading GIF: animation.gif` |
| Backgrounds | INFO | `Selected background: nature.png` |
| Menu actions | INFO | `Menu: View GIFs selected` |
| Errors | ERROR | `GIF Load Error: invalid file` |
| Warnings | WARNING | `No GIFs found in directory` |
| Details | DEBUG | `Next GIF: animation2.gif` |

## 🔍 Find Specific Info

### Check if GIFs loaded
```powershell
Select-String "Loaded.*GIF" GifViewerData\logs\app.log
```

### Find errors
```powershell
Select-String "ERROR" GifViewerData\logs\error.log
```

### Check last startup
```powershell
Get-Content GifViewerData\logs\app.log -Tail 20
```

### Search by keyword
```powershell
Select-String "background" GifViewerData\logs\app.log
```

## ⚡ Common Issues

| Problem | Check For |
|---------|-----------|
| App won't start | `ERROR` in app.log |
| GIFs not loading | `Loaded 0 GIF files` in app.log |
| Background not showing | `Background loaded successfully` |
| Buttons don't work | `Found X joystick` in app.log |
| App crashes | `ERROR` or `CRITICAL` in error.log |

## 💾 Log Rotation
- Files auto-rotate at **5MB**
- Keeps last **5 versions**
- Max disk usage: ~**50MB**

## 📝 Log Format
```
2024-03-11 14:23:45 - GifViewer - INFO - Message here
TIMESTAMP          - NAME      - LEVEL - CONTENT
```

## 🎯 Debug Tips

1. **Check startup**: First 20 lines of app.log
2. **Find errors**: Search error.log for `ERROR`
3. **Track actions**: Search for user actions (Menu, Viewer, etc.)
4. **Performance**: Count total frames in final line
5. **File issues**: Search for file operations

## 🧹 Keep Logs Clean
```bash
# Remove old rotated logs (keep current)
python log_viewer.py clean

# Or manually
Remove-Item GifViewerData\logs\*.log.*
```

## 📞 When to Check Logs
- ✅ Something doesn't work
- ✅ Need to understand what happened
- ✅ Before reporting issues
- ✅ Performance troubleshooting
- ✅ Development/testing

---

**Pro Tip**: Check logs first before troubleshooting! Most problems are visible in the logs. 📋✨
