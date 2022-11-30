# -------- Setup
import win32api, win32con, win32gui, win32ui, pyautogui, os, time, pygame, keyboard, ast, random, PIL, threading, sys, concurrent.futures, psutil, pywintypes, pygetwindow, pyscreeze, PIL, pynput.keyboard, pynput.mouse

pygame.font.init()
keyboard_presser = pynput.keyboard.Controller()

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

os.system('cls')

# -------- Constant Variables

# Screen info
WIDTH, HEIGHT = pyautogui.size()

# Transparent color
TRANSPARENT = (255, 0, 128)

# Colors
class Colors:
    DARK_RED = (139, 0, 0)
    DARK_GREY = (240, 240, 240)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

# Text
TITLE_NAME = 'Valorant UI'

# Utilities
CATEGORY_NAMES = ["     Sounds     ", "    Gameplay    ", "       Fun       "]
LINE_ONE = ["Kills", "Onetap only", "Gun inspect"]
LINE_TWO = ["Ace", "Instalock", "Sage effect"]
LINE_THREE = ["Outro", "Autoloadout", "Gun buy spammer"]

IMAGES = {'images/ace.png':(904, 177, 111, 74), 'images/victory.png':(594, 471, 731, 132), 'images/defeat.png':(632, 475, 665, 127), 'images/spectate.png':(133, 850, 19, 26)}

# -------- Variables

# Only create window on main code
if __name__ == "__main__":
    # Screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    clock = pygame.time.Clock()

    # UI title
    font = pygame.font.Font("fonts\LEMONMILK.otf", 80)
    TITLE = font.render(TITLE_NAME, True, Colors.BLACK, Colors.WHITE).convert_alpha()
    pygame.transform.threshold(TITLE, TITLE, Colors.WHITE, (250, 250, 250), None, 1, None, True)

    # Create layered window
    HWND = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(HWND, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(HWND, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED) #| win32con.WS_EX_TRANSPARENT)

    # Set window transparency color
    win32gui.SetLayeredWindowAttributes(HWND, win32api.RGB(*TRANSPARENT), 0, win32con.LWA_COLORKEY)

    # Set always on top
    win32gui.SetWindowPos(HWND, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)

# Subtitles
categorys = []
for category in CATEGORY_NAMES:
    font = pygame.font.Font("fonts\LEMONMILK.otf", 30)
    categorys.append(font.render(category, True, Colors.BLACK, Colors.WHITE))

# Line one text
line_one = []
for text in LINE_ONE:
    font = pygame.font.Font("fonts\LEMONMILK.otf", 22)
    line_one.append(font.render(text, True, Colors.BLACK, Colors.WHITE))

# Line two text
line_two = []
for text in LINE_TWO:
    font = pygame.font.Font("fonts\LEMONMILK.otf", 22)
    line_two.append(font.render(text, True, Colors.BLACK, Colors.WHITE))

# Line three text
line_three = []
for text in LINE_THREE:
    font = pygame.font.Font("fonts\LEMONMILK.otf", 22)
    line_three.append(font.render(text, True, Colors.BLACK, Colors.WHITE))

# -------- Functions

# Exit pygame then program
def quit():
    pygame.quit()
    sys.exit()

def open_settings():
    if not "notepad.exe" in [p.name() for p in psutil.process_iter()]:
        os.startfile("settings.txt", 'open')

def set_forground():
    try:
        win32gui.SetForegroundWindow(HWND)
    except pywintypes.error:
        pass

# -------- Utilitys functions

def ace(device, volume_multi):
    pygame.mixer.init(devicename = device) # Initialize it with the correct device
    pygame.mixer.music.load("audio/The Verkkars.mp3") # Load the mp3
    pygame.mixer.music.set_volume(1.5 * volume_multi)
    pygame.mixer.music.play() # Play it

    pyautogui.keyDown('t')
    running = True
    while pygame.mixer.music.get_busy() and running:
        pyautogui.keyDown('t')
        time.sleep(0.1)
        if keyboard.is_pressed("*"):
            running = False
            pygame.mixer.music.stop()
    pyautogui.keyUp('t')

def outro(device, volume_multi):
    pygame.mixer.init(devicename = device) # Initialize it with the correct device
    pygame.mixer.music.load("audio/Outro.mp3") # Load the mp3
    pygame.mixer.music.set_volume(0.6 * volume_multi)
    pygame.mixer.music.play() # Play it

    pyautogui.keyDown('t')
    running = True
    while pygame.mixer.music.get_busy() and running:
        pyautogui.keyDown('t')
        time.sleep(0.1)
        if keyboard.is_pressed("*"):
            running = False
            pygame.mixer.music.stop()
    pyautogui.keyUp('t')

def kill(device, play_index, volume_multi):
    pygame.mixer.init(devicename = device) # Initialize it with the correct device
    pygame.mixer.music.load(f"audio/Enemy/enemy ({play_index}).mp3") # Load the mp3
    pygame.mixer.music.set_volume(2.5 * volume_multi)
    pygame.mixer.music.play() # Play it

    pyautogui.keyDown('t')
    running = True
    while pygame.mixer.music.get_busy() and running:
        pyautogui.keyDown('t')
        time.sleep(0.1)
        if keyboard.is_pressed("*"):
            running = False
    pygame.mixer.music.stop()
    pyautogui.keyUp('t')

def get_images(image, box):        
    return pyautogui.locateOnScreen(image, confidence=0.8, region=box)

def get_kills(box):
    pic = PIL.ImageGrab.grab(bbox = box)

    for i in range(22):
        image = pyscreeze.locate(f'images/kills/kill{i}.png', pic, confidence=0.7)
        if image:
            return True

# -------- Utilitys

def print_button(ThreadRunner, name):
    while name in ThreadRunner.get_names():
        print("text")

class Sounds:
    kill = False
    outro = False
    ace = False
    volume_multi = 1

    @classmethod
    def toggle(cls, ThreadRunner, name, sound, volume_multi):
        cls.volume_multi = volume_multi

        running = cls.kill or cls.outro or cls.ace

        setattr(Sounds, sound, not getattr(Sounds, sound))

        if not running:
            cls.playsounds()
    
    @classmethod
    def playsounds(cls):
        last_tick = {'kill': 0, 'ace': 0, 'end': 0}
        devices = ["CABLE Input (VB-Audio Virtual Cable)", None]

        with concurrent.futures.ProcessPoolExecutor() as executor:
            while (cls.kill or cls.outro or cls.ace):
                this_tick = {'kill': False, 'ace': False, 'end': False}
                located_images = {'kill': False, 'images/spectate.png': False, 'images/ace.png': False, 'images/victory.png':False, 'images/defeat.png':False}
                
                workers = 0
                if cls.ace:
                    workers += 1
                if cls.kill:
                    workers += 2
                if cls.outro:
                    workers += 2
                
                if workers > 3:
                    workers = 3
                if workers < 0:
                    workers = 1

                with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor_mini:
                    if cls.ace:
                        located_images['images/ace.png'] = executor_mini.submit(get_images, 'images/ace.png', (904, 177, 111, 74))
                    if cls.kill:
                        located_images["kill"] = executor_mini.submit(get_kills, (890, 790, 1010, 910))
                        located_images['images/spectate.png'] = executor_mini.submit(get_images, 'images/spectate.png', (133, 850, 19, 26))
                    if cls.outro:
                        located_images['images/victory.png'] = executor_mini.submit(get_images, 'images/victory.png', (594, 471, 731, 132))
                        located_images['images/defeat.png'] = executor_mini.submit(get_images, 'images/defeat.png', (632, 475, 665, 127))
                
                if located_images['kill']:
                    if located_images['kill'].result():
                        spectating = False
                        if located_images['images/spectate.png'].result():
                            spectating = True
                        if not spectating and not last_tick['kill']:
                            kill_index = random.randint(1, 41)
                            results = []
                            for dev in devices:
                                results.append(executor.submit(kill, dev, kill_index, cls.volume_multi))
                        this_tick['kill'] = True

                if not this_tick['kill']:
                    if last_tick['kill'] > 0:
                        last_tick['kill'] -= 1
                else:
                    last_tick['kill'] = 2
                
                if located_images['images/ace.png']:
                    if located_images['images/ace.png'].result():
                        if not last_tick['ace']:
                            results = []
                            for dev in devices:
                                results.append(executor.submit(ace, dev, cls.volume_multi))
                        this_tick['ace'] = True

                if not this_tick['ace']:
                    if last_tick['ace'] > 0:
                        last_tick['ace'] -= 1
                else:
                    last_tick['ace'] = 20
                
                victory_result = None
                defeat_result = None
                if located_images['images/victory.png']:
                    victory_result = located_images['images/victory.png'].result()
                if located_images['images/defeat.png']:
                    defeat_result = located_images['images/defeat.png'].result()

                if victory_result or defeat_result:        
                    if not last_tick['end']:
                        results = []
                        for dev in devices:
                            results.append(executor.submit(outro, dev, cls.volume_multi))
                    this_tick['end'] = True
                if not this_tick['end']:
                    if last_tick['end'] > 0:
                        last_tick['end'] -= 1
                else:
                    last_tick['end'] = 30
                

def onetap_only(ThreadRunner, name):
    chat_open = False
    enter_pressed = False

    while name in ThreadRunner.get_names():
        if keyboard.is_pressed("enter") or keyboard.is_pressed("esc"):
            if not enter_pressed:
                chat_open = not chat_open
            
            enter_pressed = True
        else:
            enter_pressed = False
        
        if chat_open:
            continue

        # If left mouse clicked
        if win32api.GetKeyState(0x01) < 0:
            time.sleep(0.1)
            keyboard_presser.tap('3')
            keyboard_presser.tap('2')
            keyboard_presser.tap('1')
        
        time.sleep(0.02)

def gun_inspect(ThreadRunner, name, cps):
    chat_open = False
    enter_pressed = False
    clicking = True

    while name in ThreadRunner.get_names():
        if keyboard.is_pressed("enter") or keyboard.is_pressed("esc"):
            if not enter_pressed:
                chat_open = not chat_open
            
            enter_pressed = True
        else:
            enter_pressed = False
        
        if chat_open:
            continue
        
        if clicking and not win32api.GetKeyState(0x02) < 0:
            keyboard_presser.tap("y")
        
        time.sleep(1/cps)

# -------- Classes

class ThreadRunner:
    threads = {}

    @classmethod
    def add_thread(cls, name, function, *function_args):
        thread = threading.Thread(target=function, args=(ThreadRunner, name, *function_args))
        thread.daemon = True
        cls.threads[name] = thread
        cls.threads[name].start()
    
    @classmethod
    def end_thread(cls, name):
        if name in cls.threads.keys():
            del cls.threads[name]
    
    @classmethod
    def get_names(cls):
        return list(cls.threads.keys())


class Button:
    def __init__(self, image, pos, function, scale = 1, hover_function = None, *function_args):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.pos = pos
        self.function = function
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.hover_function = hover_function
        self.function_args = function_args

        self.last_click_tick = False
    
    def update(self, mouse_down, mouse_pos):

        if self.rect.collidepoint(mouse_pos) and mouse_down and not self.last_click_tick:
            self.last_click_tick = True
            pygame.mixer.music.load("audio/click.wav") # Load the mp3
            pygame.mixer.music.set_volume(1.5)
            pygame.mixer.music.play() # Play it
            self.function(*self.function_args)

        if not self.rect.collidepoint(mouse_pos) or not mouse_down:
            self.last_click_tick = False

        if self.hover_function and self.rect.collidepoint(mouse_pos):
            self.hover_function()

    def display(self, screen):
        screen.blit(self.image, self.pos)
    
    def invert(self):
        pixels = pygame.surfarray.pixels2d(self.image)
        pixels ^= 2 ** 32 - 1
        del pixels


class Utility(Button):
    def __init__(self, image, pos, function, name, scale = 1, hover_function = None, *function_args):
        self.image = image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.pos = pos
        self.function = function
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.hover_function = hover_function
        self.function_args = function_args

        self.last_click_tick = False
        self.enabled = False

    def toggle(self, disable_still_runs, *extra_args):
        self.enabled = not self.enabled
        self.invert()
        if self.enabled or disable_still_runs:
            ThreadRunner.add_thread(self.name, self.function, *self.function_args, *extra_args)
        else:
            ThreadRunner.end_thread(self.name)

    def update(self, mouse_down, mouse_pos, disable_still_runs, *extra_args):
        if self.rect.collidepoint(mouse_pos) and mouse_down and not self.last_click_tick:
            self.last_click_tick = True
            pygame.mixer.music.load("audio/click.wav") # Load the mp3
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play() # Play it
            self.toggle(disable_still_runs, *extra_args)

        if not self.rect.collidepoint(mouse_pos) or not mouse_down:
            self.last_click_tick = False

        if self.hover_function and self.rect.collidepoint(mouse_pos):
            self.hover_function()
            
# Buttons
settings_button = Button(pygame.image.load("images\settings.png"), (20, 20), open_settings, 0.2, set_forground)
exit_button = Button(pygame.image.load("images\exit.png"), (WIDTH - 94, 20), exit, 0.2, set_forground)

# Utilities
LINE_ONE_FUNCTIONS = [Sounds.toggle, onetap_only, gun_inspect]
LINE_TWO_FUNCTIONS = [Sounds.toggle, print_button, print_button]
LINE_THREE_FUNCTIONS = [Sounds.toggle, print_button, print_button]

line_one_images = [Utility(image, (400 + 475 * i, 265), LINE_ONE_FUNCTIONS[i], LINE_ONE[i], 1, set_forground) for i, image in enumerate(line_one)]
line_two_images = [Utility(image, (400 + 475 * i, 300), LINE_TWO_FUNCTIONS[i], LINE_TWO[i], 1, set_forground) for i, image in enumerate(line_two)]
line_three_images = [Utility(image, (400 + 475 * i, 335), LINE_THREE_FUNCTIONS[i], LINE_THREE[i], 1, set_forground) for i, image in enumerate(line_three)]

# -------- Main

def main():
    # UI settings
    settings = {}
    with open("settings.txt", 'r') as f:
        settings_data = f.readlines()
        
        for setting in settings_data:
            setting = setting.strip("\n")
            setting = setting.split(":", 1)
            
            setting = [x.strip() for x in setting]
            
            settings[setting[0]] = ast.literal_eval(setting[1])
    
    stamp = os.stat('settings.txt').st_mtime

    last_tick_pressed = False
    rendering = True
    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit")
                quit()
        
        # Keyboard events
        if keyboard.is_pressed(settings["QuitKeys"]):
            print("Quit")
            quit()

        if keyboard.is_pressed(settings["OpenKeys"]):
            if not last_tick_pressed:
                rendering = not rendering

                if rendering:
                    set_forground()
                    win32api.SetCursorPos((round(WIDTH / 2), round(HEIGHT / 2)))
                else:
                    screen.fill(TRANSPARENT)
                    pygame.display.update()
                    try:
                        win = pygetwindow.getWindowsWithTitle('VALORANT')[0] 
                        win.activate()
                    except pygetwindow.PyGetWindowException:
                        pass
            
            last_tick_pressed = True
        else:
            last_tick_pressed = False
        
        # UI settings
        check_stamp = os.stat('settings.txt').st_mtime
        if check_stamp != stamp:
            stamp = check_stamp

            settings = {}
            with open("settings.txt", 'r') as f:
                settings_data = f.readlines()
                
                for setting in settings_data:
                    setting = setting.strip("\n")
                    setting = setting.split(":", 1)
                    
                    setting = [x.strip() for x in setting]
                    
                    settings[setting[0]] = ast.literal_eval(setting[1])

        # Get info
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]
        
        # Update
        if rendering:
            settings_button.update(mouse_down, mouse_pos)
            exit_button.update(mouse_down, mouse_pos)

            for text in line_one_images:
                if text.name == "Gun inspect":
                    text.update(mouse_down, mouse_pos, False, settings["InspectGunCPS"])
                elif text.name == "Kills":
                    text.update(mouse_down, mouse_pos, True, 'kill', settings["Volume"])
                text.update(mouse_down, mouse_pos, False)
            
            for text in line_two_images:
                if text.name == "Ace":
                    text.update(mouse_down, mouse_pos, True, 'ace', settings["Volume"])
                text.update(mouse_down, mouse_pos, False)
            
            for text in line_three_images:
                if text.name == "Outro":
                    text.update(mouse_down, mouse_pos, True, 'outro', settings["Volume"])
                text.update(mouse_down, mouse_pos, False)

        # Render
        if rendering:
            screen.fill(TRANSPARENT)

            pygame.draw.rect(screen, Colors.RED, pygame.Rect(0, 110, WIDTH, 5))
            
            screen.blit(TITLE, (200, 0))

            for i, category in enumerate(categorys):
                screen.blit(category, (400 + 475 * i, 220))
            
            for text in line_one_images:
                text.display(screen)
            for text in line_two_images:
                text.display(screen)
            for text in line_three_images:
                text.display(screen)

            settings_button.display(screen)
            exit_button.display(screen)
        
            pygame.display.update()

        clock.tick(int(settings["RefreshRate"]))
    quit()

# -------- Start

if __name__ == "__main__":
    main()