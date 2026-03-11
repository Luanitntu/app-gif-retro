# 🎨 Background Image Setup Guide

## Quick Start

### Step 1: Create Backgrounds Folder
If not auto-created, manually create:
```
GifViewerData/backgrounds/
```

### Step 2: Add Background Images
1. Find or create PNG images (any size is fine)
2. Copy them to `GifViewerData/backgrounds/` folder
3. Supported format: PNG (recommended), also works with JPG/BMP

### Step 3: Select Your Background
1. Launch the application
2. From main menu, press **[MENU Button]** on joystick
   - Or press **[Y]** if using keyboard (gtk)
3. Use **[UP/DOWN arrows]** to browse available backgrounds
4. Press **[A]** to select
5. Background is automatically saved and will load next time!

## Example Directory Structure
```
GifViewerData/
├── backgrounds/
│   ├── space.png
│   ├── forest.png
│   ├── retro_80s.png
│   └── solid_color.png
├── images/
│   ├── animation1.gif
│   └── animation2.gif
└── main.py
```

## Tips & Tricks

### 💡 Good Background Images:
- Solid colors or subtle patterns work best (text needs to be readable)
- Dark backgrounds (better contrast for white text)
- Aspect ratio: wider is better (screens are wide)
- Size: 1280x720 or larger (will be auto-scaled)

### 🎯 What NOT to use:
- Very bright backgrounds (text will be hard to read)
- Complex detailed images (UI text needs contrast)
- Very small images (will be pixelated when scaled)

### 🔧 Quick Tips:
- Background only shows on MENU screen
- GIF viewer shows full-screen GIF (no background overlay)
- Last selected background is remembered automatically
- Empty backgrounds folder? Just copy some PNG files there!

## File Format Details

**app_config.json** (auto-created, don't edit manually):
```json
{
  "current_background": "my_background.png"
}
```

This file saves your last selected background so it auto-loads next time!

## Troubleshooting

### Background not showing?
- Check that PNG file is in `backgrounds/` folder
- Make sure file extension is `.png`
- Try a different image file

### Can't find background selector?
- Make sure to press **[MENU Button]** on joystick
- Or press **[Y]** key on keyboard

### Text not readable on background?
- Choose a darker background
- Or select "No background" (if available)
- Try solid colors instead of patterns

## Creating Custom Backgrounds

### Option 1: Use Online Resources
- Unsplash.com (free backgrounds)
- Pexels.com (free high-quality images)
- Download as PNG, place in `backgrounds/` folder

### Option 2: Create with Image Editor
- Use Photoshop, GIMP, or Paint.net
- Save as PNG format
- Keep text areas dark for readability

### Option 3: Simple Approach
- Take a screenshot of something nice
- Crop/resize to screen dimensions
- Save as PNG in `backgrounds/` folder

Enjoy! 🎉
