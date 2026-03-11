# Helper functions module
import os
import pygame
from modules.config import TEXT_COLOR, HIGHLIGHT_COLOR, SHADOW_COLOR

try:
    from modules.logger import get_logger
    logger = get_logger()
except:
    logger = None

def log(level, message):
    """Utility function to safely log messages"""
    if logger:
        getattr(logger, level, logger.info)(message)

def get_gif_files(directory):
    """Get all GIF files from directory"""
    gifs = []
    try:
        for f in os.listdir(directory):
            if f.lower().endswith(".gif") and os.path.isfile(os.path.join(directory, f)):
                gifs.append(os.path.join(directory, f))
        log('debug', f"Found {len(gifs)} GIF files in {directory}")
    except Exception as e:
        log('error', f"Error reading gif files from {directory}: {str(e)}")
    return sorted(gifs)

def get_image_files(directory, extension=".png"):
    """Get all image files with specified extension from directory"""
    images = []
    try:
        if not os.path.exists(directory):
            log('debug', f"Image directory does not exist: {directory}")
            return images
        
        for f in os.listdir(directory):
            if f.lower().endswith(extension) and os.path.isfile(os.path.join(directory, f)):
                images.append(os.path.join(directory, f))
        log('debug', f"Found {len(images)} {extension} files in {directory}")
    except Exception as e:
        log('error', f"Error reading image files from {directory}: {str(e)}")
    return sorted(images)

def get_directory_items(directory):
    """Get all items in directory (folders and files)"""
    try:
        if not os.path.exists(directory):
            log('warning', f"Directory does not exist: {directory}")
            return [".."]
        
        items = sorted([d for d in os.listdir(directory) if not d.startswith('.')])
        items.insert(0, "..")
        return items
    except Exception as e:
        log('error', f"Error reading directory {directory}: {str(e)}")
        return [".."]

def draw_text_center(screen, font, text, screen_w, screen_h, y_offset=0, color=TEXT_COLOR):
    """Draw text centered on screen"""
    text_surf = font.render(text, True, color)
    rect = text_surf.get_rect(center=(screen_w // 2, screen_h // 2 + y_offset))
    screen.blit(text_surf, rect)

def draw_text_with_shadow(screen, font, text, screen_w, screen_h, y_offset=0, color=TEXT_COLOR, shadow_offset=2):
    """Draw text with shadow effect for better visibility"""
    # Draw shadow
    shadow_surf = font.render(text, True, SHADOW_COLOR)
    shadow_rect = shadow_surf.get_rect(center=(screen_w // 2 + shadow_offset, screen_h // 2 + y_offset + shadow_offset))
    screen.blit(shadow_surf, shadow_rect)
    
    # Draw main text
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(screen_w // 2, screen_h // 2 + y_offset))
    screen.blit(text_surf, text_rect)

def draw_text_at_position(screen, font, text, x, y, color=TEXT_COLOR, with_shadow=False):
    """Draw text at specific position with optional shadow"""
    if with_shadow:
        shadow_surf = font.render(text, True, SHADOW_COLOR)
        screen.blit(shadow_surf, (x + 2, y + 2))
    
    text_surf = font.render(text, True, color)
    screen.blit(text_surf, (x, y))

def load_background_image(image_path, screen_w, screen_h):
    """Load and scale background image to screen dimensions"""
    try:
        if not os.path.exists(image_path):
            log('warning', f"Background image not found: {image_path}")
            return None
        
        bg_img = pygame.image.load(image_path).convert()
        # Scale to fit screen
        bg_surface = pygame.transform.scale(bg_img, (screen_w, screen_h))
        log('debug', f"Background loaded successfully: {os.path.basename(image_path)}")
        return bg_surface
    except Exception as e:
        log('error', f"Error loading background {image_path}: {str(e)}")
        return None

def get_file_name_from_path(path):
    """Extract filename from path"""
    return os.path.basename(path)

def is_directory(path):
    """Check if path is a directory"""
    return os.path.isdir(path)

def get_parent_directory(path):
    """Get parent directory of given path"""
    return os.path.dirname(path)