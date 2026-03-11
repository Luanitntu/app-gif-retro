import sys
import os
import time
import traceback

# --- 1. SETUP ---
try:
    import pygame
    from PIL import Image, ImageSequence
except ImportError:
    print("ERROR: pygame and/or PIL not installed")
    sys.exit(1)

from modules.config import *
from modules.helpers import *
from modules.logger import get_logger

# Initialize logger
logger = get_logger()

# ==========================================
# --- GIF PLAYER CLASS ---
# ==========================================
class GifPlayer:
    """Handles GIF animation playback"""
    def __init__(self, filepath):
        self.frames = []
        self.durations = []
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.valid = False
        self.filepath = filepath
        self.load_gif(filepath)

    def load_gif(self, filepath):
        """Load GIF frames and durations"""
        try:
            logger.info(f"Loading GIF: {filepath}")
            info = pygame.display.Info()
            scr_w, scr_h = info.current_w, info.current_h
            pil_img = Image.open(filepath)
            img_w, img_h = pil_img.size
            
            # Calculate scaling to fit screen
            ratio = min(scr_w / img_w, scr_h / img_h)
            new_size = (int(img_w * ratio), int(img_h * ratio))

            frame_count = 0
            for frame in ImageSequence.Iterator(pil_img):
                frame = frame.convert("RGBA")
                frame = frame.resize(new_size, Image.Resampling.LANCZOS)
                mode = frame.mode
                size = frame.size
                data = frame.tobytes()
                py_image = pygame.image.fromstring(data, size, mode)
                self.frames.append(py_image)
                self.durations.append(frame.info.get('duration', 100))
                frame_count += 1
            
            if len(self.frames) > 0:
                self.valid = True
                logger.info(f"Successfully loaded GIF: {len(self.frames)} frames, "
                           f"Size: {new_size}, Original: {img_w}x{img_h}")
            else:
                logger.warning(f"GIF loaded but no frames found: {filepath}")
                self.valid = False
        except Exception as e:
            logger.error(f"GIF Load Error: {filepath} - {str(e)}")
            logger.debug(traceback.format_exc())
            self.valid = False

    def update(self):
        """Update current frame based on duration"""
        if not self.valid:
            return
        
        now = pygame.time.get_ticks()
        if now - self.last_update > self.durations[self.current_frame]:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = now

    def draw(self, surface):
        """Draw current frame centered on surface"""
        if not self.valid:
            return
        
        info = pygame.display.Info()
        scr_w, scr_h = info.current_w, info.current_h
        img = self.frames[self.current_frame]
        rect = img.get_rect(center=(scr_w // 2, scr_h // 2))
        surface.blit(img, rect)

# ==========================================
# --- INPUT HANDLER CLASS ---
# ==========================================
class InputHandler:
    """Handles keyboard and joystick input"""
    def __init__(self):
        self.btn_A = False
        self.btn_B = False
        self.btn_X = False
        self.btn_Y = False
        self.btn_Up = False
        self.btn_Down = False
        self.last_input_time = pygame.time.get_ticks()
        self.last_debug = "Start"

    def update(self, event):
        """Process input event and update button states"""
        self.btn_A = self.btn_B = self.btn_X = self.btn_Y = False
        self.btn_Up = self.btn_Down = False

        if event.type == pygame.KEYDOWN:
            if event.key in KEY_A:
                self.btn_A = True
            elif event.key in KEY_B:
                self.btn_B = True
            elif event.key in KEY_X:
                self.btn_X = True
            elif event.key in KEY_Y:
                self.btn_Y = True
            elif event.key in KEY_UP:
                self.btn_Up = True
            elif event.key in KEY_DOWN:
                self.btn_Down = True

        elif event.type == pygame.JOYBUTTONDOWN:
            joy_id = getattr(event, 'instance_id', event.joy)
            btn_id = event.button
            self.last_debug = f"Joy:{joy_id} Btn:{btn_id}"
            
            if btn_id == BTN_ID_A:
                self.btn_A = True
            elif btn_id == BTN_ID_B:
                self.btn_B = True
            elif btn_id == BTN_ID_X:
                self.btn_X = True
            elif btn_id == BTN_ID_Y:
                self.btn_Y = True
            elif btn_id == BTN_ID_MENU:
                self.btn_A = True  # Use A button for menu shortcut

        elif event.type == pygame.JOYHATMOTION:
            if event.value[1] == 1:
                self.btn_Up = True
            elif event.value[1] == -1:
                self.btn_Down = True

        elif event.type == pygame.JOYAXISMOTION:
            if abs(event.value) > 0.5 and event.axis == 1:
                if event.value < -0.5:
                    self.btn_Up = True
                elif event.value > 0.5:
                    self.btn_Down = True

        self.last_input_time = pygame.time.get_ticks()

    def time_since_input(self):
        """Get milliseconds since last input"""
        return pygame.time.get_ticks() - self.last_input_time

# ==========================================
# --- APPLICATION STATE MANAGER ---
# ==========================================
class AppState:
    """Manages application state and configuration"""
    def __init__(self):
        self.mode = "MENU"
        self.gif_list = []
        self.current_gif_index = 0
        self.current_player = None
        self.manual_mode = True
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.dir_items = []
        self.selected_item = 0
        
        self.bg_surface = None
        self.current_bg_path = None
        self.bg_list = []
        self.selected_bg_index = 0
        
        self.config = load_config()
        self.load_saved_background()

    def load_saved_background(self):
        """Load previously selected background"""
        try:
            if self.config.get("current_background"):
                bg_path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    BACKGROUNDS_DIR,
                    self.config["current_background"]
                )
                logger.info(f"Loading saved background: {self.config['current_background']}")
                self.load_background(bg_path)
        except Exception as e:
            logger.error(f"Error loading saved background: {str(e)}")

    def load_background(self, bg_path):
        """Load background image"""
        try:
            info = pygame.display.Info()
            bg = load_background_image(bg_path, info.current_w, info.current_h)
            if bg:
                self.bg_surface = bg
                self.current_bg_path = bg_path
                self.config["current_background"] = os.path.basename(bg_path)
                save_config(self.config)
                logger.info(f"Background loaded successfully: {os.path.basename(bg_path)}")
            else:
                logger.warning(f"Failed to load background: {bg_path}")
        except Exception as e:
            logger.error(f"Error loading background {bg_path}: {str(e)}")

    def load_gif_list(self, directory):
        """Load GIF files from directory"""
        try:
            self.gif_list = get_gif_files(directory)
            self.current_gif_index = 0
            logger.info(f"Loaded {len(self.gif_list)} GIF files from: {directory}")
        except Exception as e:
            logger.error(f"Error loading GIF list from {directory}: {str(e)}")

    def load_directory_items(self, directory):
        """Load directory contents"""
        try:
            self.dir_items = get_directory_items(directory)
            self.selected_item = 0
            logger.debug(f"Loaded directory: {directory} ({len(self.dir_items)} items)")
        except Exception as e:
            logger.error(f"Error loading directory {directory}: {str(e)}")

    def load_background_list(self):
        """Load available backgrounds"""
        try:
            bg_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), BACKGROUNDS_DIR)
            self.bg_list = get_image_files(bg_dir, ".png")
            self.selected_bg_index = 0
            logger.info(f"Loaded {len(self.bg_list)} background images from: {bg_dir}")
        except Exception as e:
            logger.error(f"Error loading background list: {str(e)}")

# ==========================================
# --- UI RENDERER CLASS ---
# ==========================================
class UIRenderer:
    """Handles all UI drawing"""
    def __init__(self, screen, screen_w, screen_h):
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.font = pygame.font.Font(None, 40)
        self.debug_font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 25)

    def draw_background(self, bg_surface=None):
        """Draw background"""
        if bg_surface:
            self.screen.blit(bg_surface, (0, 0))
        else:
            self.screen.fill(BG_COLOR)

    def draw_menu(self, app_state):
        """Draw menu screen"""
        draw_text_with_shadow(self.screen, self.font, "GIF VIEWER", 
                            self.screen_w, self.screen_h, -80, HIGHLIGHT_COLOR)
        draw_text_with_shadow(self.screen, self.font, "[A] VIEW GIFS", 
                            self.screen_w, self.screen_h, -20)
        draw_text_with_shadow(self.screen, self.font, "[X] BROWSE FILES", 
                            self.screen_w, self.screen_h, 20)
        draw_text_with_shadow(self.screen, self.font, "[MENU] BACKGROUNDS", 
                            self.screen_w, self.screen_h, 60)
        draw_text_with_shadow(self.screen, self.font, "[B] EXIT", 
                            self.screen_w, self.screen_h, 120, ERROR_COLOR)
        
        # Display current background info
        if app_state.current_bg_path:
            bg_name = get_file_name_from_path(app_state.current_bg_path)
            draw_text_at_position(self.screen, self.small_font, f"BG: {bg_name}", 
                                 10, self.screen_h - 30, (150, 150, 150))

    def draw_browser(self, app_state):
        """Draw file browser screen"""
        # Header
        current_path = app_state.current_dir[-40:]
        draw_text_at_position(self.screen, self.debug_font, current_path, 10, 5, (150, 150, 150))
        
        # Items list
        start = max(0, app_state.selected_item - 5)
        end = min(len(app_state.dir_items), start + 10)
        
        for i in range(start, end):
            color = HIGHLIGHT_COLOR if i == app_state.selected_item else TEXT_COLOR
            item_name = app_state.dir_items[i]
            y_pos = 50 + (i - start) * 35
            draw_text_at_position(self.screen, self.font, item_name, 20, y_pos, color)
        
        # Footer
        draw_text_at_position(self.screen, self.debug_font, 
                            "[A] Select  [B] Back", 10, self.screen_h - 30, (150, 150, 150))

    def draw_background_selector(self, app_state):
        """Draw background selection screen"""
        draw_text_with_shadow(self.screen, self.font, "SELECT BACKGROUND", 
                            self.screen_w, self.screen_h, -100, HIGHLIGHT_COLOR)
        
        if not app_state.bg_list:
            draw_text_with_shadow(self.screen, self.font, "NO BACKGROUNDS FOUND", 
                                self.screen_w, self.screen_h, 0, ERROR_COLOR)
            draw_text_with_shadow(self.screen, self.small_font, 
                                "Add .png files to 'backgrounds' folder", 
                                self.screen_w, self.screen_h, 50, TEXT_COLOR)
        else:
            # Show backgrounds list
            start = max(0, app_state.selected_bg_index - 4)
            end = min(len(app_state.bg_list), start + 8)
            
            for i in range(start, end):
                color = HIGHLIGHT_COLOR if i == app_state.selected_bg_index else TEXT_COLOR
                bg_name = get_file_name_from_path(app_state.bg_list[i])
                y_pos = -50 + (i - start) * 35
                draw_text_with_shadow(self.screen, self.debug_font, bg_name, 
                                    self.screen_w, self.screen_h, y_pos, color)
        
        draw_text_with_shadow(self.screen, self.small_font, "[A] Select  [B] Back", 
                            self.screen_w, self.screen_h, 100, (150, 150, 150))

    def draw_viewer(self, app_state, input_handler):
        """Draw GIF viewer screen"""
        if app_state.current_player:
            app_state.current_player.draw(self.screen)
        
        # Show controls if recent input
        if input_handler.time_since_input() < 5000:
            if not app_state.manual_mode:
                help_text = "[A] Next  [Y] Prev  [B] Back"
            else:
                help_text = "[B] Back"
            
            draw_text_at_position(self.screen, self.debug_font, help_text, 
                                10, self.screen_h - 30, TEXT_COLOR, with_shadow=True)
            
            # Debug info
            draw_text_at_position(self.screen, self.debug_font, input_handler.last_debug, 
                                self.screen_w - 180, 10, (0, 255, 255), with_shadow=True)

    def update_screen_dims(self, screen_w, screen_h):
        """Update screen dimensions"""
        self.screen_w = screen_w
        self.screen_h = screen_h

# ==========================================
# --- MAIN APPLICATION ---
# ==========================================
def disable_screensaver():
    """Disable screensaver and power saving"""
    try:
        pygame.display.set_screensaver(False)
    except:
        pass
    
    try:
        os.system('setterm -blank 0 -powerdown 0')
        os.system('setterm -powersave off')
    except:
        pass

def restore_screensaver():
    """Restore screensaver and power saving"""
    try:
        os.system('setterm -blank 10 -powerdown 10')
    except:
        pass

def main():
    """Main application loop"""
    try:
        logger.info("Initializing pygame...")
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.joystick.init()
        logger.info("Pygame initialized successfully")
        
        # Disable screensaver
        logger.info("Disabling screensaver...")
        disable_screensaver()
        
        # Initialize joysticks
        joystick_count = pygame.joystick.get_count()
        logger.info(f"Found {joystick_count} joystick(s)")
        joysticks = []
        for x in range(joystick_count):
            j = pygame.joystick.Joystick(x)
            j.init()
            joysticks.append(j)
            logger.debug(f"Joystick {x} initialized: {j.get_name()}")

        # Setup screen and UI
        logger.info("Setting up display...")
        screen, SCREEN_W, SCREEN_H = get_screen()
        pygame.display.set_caption("GIF Viewer")
        logger.info(f"Display set to: {SCREEN_W}x{SCREEN_H}")
        
        # Ensure directories exist
        logger.info("Creating necessary directories...")
        ensure_directories()
        
        # Initialize components
        clock = pygame.time.Clock()
        input_handler = InputHandler()
        app_state = AppState()
        ui = UIRenderer(screen, SCREEN_W, SCREEN_H)
        logger.info("Application components initialized")
        
        # Setup directories
        default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), DEFAULT_DIR)
        bg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), BACKGROUNDS_DIR)
        logger.info(f"Default GIF path: {default_path}")
        logger.info(f"Backgrounds path: {bg_path}")
        
        logger.info("Application ready - entering main loop")
        
        running = True
        frame_count = 0
        
        while running:
            frame_count += 1
            clock.tick(60)
            
            # Draw background
            if app_state.mode == "MENU" and app_state.bg_surface:
                ui.draw_background(app_state.bg_surface)
            else:
                ui.draw_background()
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logger.info("Quit event received")
                    running = False
                
                if event.type in [pygame.KEYDOWN, pygame.JOYBUTTONDOWN, pygame.JOYHATMOTION, pygame.JOYAXISMOTION]:
                    input_handler.update(event)
                
                # --- STATE MACHINE ---
                if app_state.mode == "MENU":
                    if input_handler.btn_A:
                        logger.info("Menu: View GIFs selected")
                        app_state.load_gif_list(default_path)
                        if app_state.gif_list:
                            app_state.mode = "VIEWER"
                            app_state.current_gif_index = 0
                            app_state.current_player = GifPlayer(app_state.gif_list[0])
                            app_state.manual_mode = False
                            logger.info(f"Entering VIEWER mode with first GIF")
                            pygame.event.clear()
                            pygame.time.wait(500)
                        else:
                            logger.warning(f"No GIFs found in: {default_path}")
                            ui.draw_menu(app_state)
                            draw_text_with_shadow(screen, ui.font, 
                                                f"NO GIFS IN '{DEFAULT_DIR}'", 
                                                SCREEN_W, SCREEN_H, 0, ERROR_COLOR)
                            pygame.display.flip()
                            pygame.time.wait(2000)

                    elif input_handler.btn_X:
                        logger.info("Menu: File browser selected")
                        app_state.mode = "BROWSER"
                        app_state.current_dir = os.path.dirname(os.path.abspath(__file__))
                        app_state.load_directory_items(app_state.current_dir)
                        pygame.event.clear()
                        pygame.time.wait(300)

                    elif input_handler.btn_Y:
                        logger.info("Menu: Background selector selected")
                        app_state.mode = "BG_SELECT"
                        app_state.load_background_list()
                        pygame.event.clear()
                        pygame.time.wait(300)

                    elif input_handler.btn_B:
                        logger.info("Menu: Exit selected")
                        running = False

                elif app_state.mode == "BROWSER":
                    if input_handler.btn_B:
                        logger.info("Browser: Back to menu")
                        app_state.mode = "MENU"
                        pygame.event.clear()
                        pygame.time.wait(300)
                    
                    elif input_handler.btn_Up:
                        app_state.selected_item = max(0, app_state.selected_item - 1)
                    
                    elif input_handler.btn_Down:
                        app_state.selected_item = min(len(app_state.dir_items) - 1, app_state.selected_item + 1)
                    
                    elif input_handler.btn_A:
                        selected_name = app_state.dir_items[app_state.selected_item]
                        full_path = os.path.join(app_state.current_dir, selected_name)
                        
                        if selected_name == "..":
                            app_state.current_dir = os.path.dirname(app_state.current_dir)
                            app_state.load_directory_items(app_state.current_dir)
                            logger.debug(f"Navigated up to: {app_state.current_dir}")
                            pygame.time.wait(200)
                        
                        elif is_directory(full_path):
                            app_state.current_dir = full_path
                            app_state.load_directory_items(app_state.current_dir)
                            logger.debug(f"Entered directory: {full_path}")
                            pygame.time.wait(200)
                        
                        elif selected_name.lower().endswith(".gif"):
                            logger.info(f"Selected GIF: {selected_name}")
                            app_state.gif_list = [full_path]
                            app_state.current_gif_index = 0
                            app_state.current_player = GifPlayer(full_path)
                            app_state.mode = "VIEWER"
                            app_state.manual_mode = True
                            pygame.event.clear()
                            pygame.time.wait(500)

                elif app_state.mode == "BG_SELECT":
                    if input_handler.btn_B:
                        logger.info("Background selector: Back to menu")
                        app_state.mode = "MENU"
                        pygame.event.clear()
                        pygame.time.wait(300)
                    
                    elif input_handler.btn_Up:
                        app_state.selected_bg_index = max(0, app_state.selected_bg_index - 1)
                    
                    elif input_handler.btn_Down:
                        app_state.selected_bg_index = min(len(app_state.bg_list) - 1, app_state.selected_bg_index + 1)
                    
                    elif input_handler.btn_A and app_state.bg_list:
                        selected_bg = app_state.bg_list[app_state.selected_bg_index]
                        logger.info(f"Selected background: {os.path.basename(selected_bg)}")
                        app_state.load_background(selected_bg)
                        app_state.mode = "MENU"
                        pygame.event.clear()
                        pygame.time.wait(500)

                elif app_state.mode == "VIEWER":
                    if input_handler.btn_B:
                        logger.info("Viewer: Back to menu")
                        app_state.mode = "MENU" if not app_state.manual_mode else "BROWSER"
                        app_state.current_player = None
                        pygame.event.clear()
                        pygame.time.wait(500)
                    
                    elif input_handler.btn_A and not app_state.manual_mode:
                        app_state.current_gif_index = (app_state.current_gif_index + 1) % len(app_state.gif_list)
                        logger.debug(f"Next GIF: {os.path.basename(app_state.gif_list[app_state.current_gif_index])}")
                        app_state.current_player = GifPlayer(app_state.gif_list[app_state.current_gif_index])
                        pygame.time.wait(200)
                    
                    elif input_handler.btn_Y and not app_state.manual_mode:
                        app_state.current_gif_index = (app_state.current_gif_index - 1) % len(app_state.gif_list)
                        logger.debug(f"Previous GIF: {os.path.basename(app_state.gif_list[app_state.current_gif_index])}")
                        app_state.current_player = GifPlayer(app_state.gif_list[app_state.current_gif_index])
                        pygame.time.wait(200)

            # --- DRAW UI ---
            if app_state.mode == "MENU":
                ui.draw_menu(app_state)
            elif app_state.mode == "BROWSER":
                ui.draw_browser(app_state)
            elif app_state.mode == "BG_SELECT":
                ui.draw_background_selector(app_state)
            elif app_state.mode == "VIEWER":
                ui.draw_viewer(app_state, input_handler)

            pygame.display.flip()
        
        logger.info(f"Application exiting - Total frames rendered: {frame_count}")
        
    except Exception as e:
        logger.error(f"Fatal error in main loop: {str(e)}")
        logger.debug(traceback.format_exc())
        raise
    finally:
        # Cleanup
        logger.info("Restoring screensaver...")
        restore_screensaver()
        logger.info("Shutting down pygame...")
        pygame.quit()
        logger.info("Application shutdown complete")
        sys.exit()

if __name__ == "__main__":
    main()