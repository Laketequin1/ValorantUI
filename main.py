import win32api, win32con, win32gui, win32ui, pyautogui, os, time, pygame, keyboard, ast, random, PIL, threading, sys, concurrent.futures

os.system('cls')

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = pyautogui.size()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()

image = None

# Settings
settings = {}
with open("settings.txt", 'r') as f:
    settings_data = f.readlines()
    
    for setting in settings_data:
        setting = setting.strip("\n")
        setting = setting.split(":", 1)
        
        setting = [x.strip() for x in setting]
        
        settings[setting[0]] = ast.literal_eval(setting[1])

# Transparent color
TRANSPARENT = (255, 0, 128)

# Colors
DARK_RED = (139, 0, 0)
DARK_GREY = (240, 240, 240)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Text
TITLE_NAME = 'To name UI title'

font = pygame.font.Font("fonts\LEMONMILK.otf", 80)
TITLE = font.render(TITLE_NAME, True, BLACK, WHITE).convert_alpha()
pygame.transform.threshold(TITLE, TITLE, WHITE, (250, 250, 250), None, 1, None, True)

# Create layered window
HWND = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(HWND, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(HWND, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)

# Set window transparency color
win32gui.SetLayeredWindowAttributes(HWND, win32api.RGB(*TRANSPARENT), 0, win32con.LWA_COLORKEY)

# Set always on tip
win32gui.SetWindowPos(HWND, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)

def quit():
    pygame.quit()
    sys.exit()

def take_screenshot():
    hwnd = win32gui.FindWindow(None, "Touch Grass")
    if not hwnd:
        print("Game not open")
        quit()
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, WIDTH, HEIGHT)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (WIDTH, HEIGHT), dcObj, (0, 0), win32con.SRCCOPY)
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    
    # Free Resources
    try:
        dcObj.DeleteDC()
    except Exception:
        print("Game closed")
        quit()
    
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    return bmpstr, bmpinfo

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit")
                quit()
        
        if keyboard.is_pressed(settings["QuitKeys"]):
            print("Quit")
            quit()

        screen.fill(TRANSPARENT)
        
        pygame.draw.rect(screen, DARK_RED, pygame.Rect(0, HEIGHT - 20, WIDTH, HEIGHT))
        
        screen.blit(TITLE, (150, 20))
        
        pygame.display.update()
        
        clock.tick(settings["RefreshRate"])
        
        print(clock.get_fps())
    quit()

if __name__ == "__main__":
    main()