# Configuration module
import os
import pygame
import json

# ==========================================
# --- APPLICATION CONSTANTS ---
# ==========================================
DEFAULT_DIR = "images"
BACKGROUNDS_DIR = "backgrounds"
BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 255, 0)
ERROR_COLOR = (255, 100, 100)
SHADOW_COLOR = (0, 0, 0)
CONFIG_FILE = "app_config.json"

# ==========================================
# --- JOYSTICK BUTTON MAPPING ---
# ==========================================
BTN_ID_A = 3   # Next
BTN_ID_B = 4   # Back
BTN_ID_Y = 5   # Previous
BTN_ID_X = 6   # Browse
BTN_ID_MENU = 7  # Menu/Settings (for background change)

# ==========================================
# --- KEYBOARD SHORTCUTS ---
# ==========================================
KEY_A = [pygame.K_z, pygame.K_RETURN]
KEY_B = [pygame.K_x, pygame.K_ESCAPE]
KEY_X = [pygame.K_a, pygame.K_s]
KEY_Y = [pygame.K_y]
KEY_UP = [pygame.K_UP, pygame.K_w]
KEY_DOWN = [pygame.K_DOWN, pygame.K_s]

# ==========================================
# --- SCREEN & DISPLAY SETTINGS ---
# ==========================================
def get_screen():
    if os.name == 'nt':
        screen_w, screen_h = 640, 480
        flags = 0
    else:
        temp_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        screen_w, screen_h = temp_screen.get_size()
        flags = pygame.FULLSCREEN

    screen = pygame.display.set_mode((screen_w, screen_h), flags)
    return screen, screen_w, screen_h

def ensure_directories():
    """Create necessary directories if they don't exist"""
    base_path = os.path.dirname(os.path.abspath(__file__))
    for dir_name in [DEFAULT_DIR, BACKGROUNDS_DIR]:
        dir_path = os.path.join(base_path, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

# ==========================================
# --- CONFIG FILE MANAGEMENT ---
# ==========================================
def get_config_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG_FILE)

def load_config():
    """Load application configuration from JSON file"""
    try:
        config_path = get_config_path()
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Config load error: {e}")
    return {"current_background": None}

def save_config(config):
    """Save application configuration to JSON file"""
    try:
        config_path = get_config_path()
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        print(f"Config save error: {e}")
