from settings import *
import sys
import time
import os

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def type_write(text, color="white", speed=TEXT_SPEED) -> None:
    """
    Prints text with specified color and typing speed.

    Args:
        text (str): The text to be printed.
        color (str, optional): The color of the text. Defaults to "white".
        speed (int, optional): The typing speed. Defaults to TEXT_SPEED from settings.

    Raises:
        ValueError: If an invalid color is provided.
    """
    speed_factor = 10 - (speed / 10)
    if color.startswith("#") and len(color) == 7:
        color_code = f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
    else:
        color_upper = color.upper()
        color_code = getattr(Color, color_upper, None)
        if color_code is None:
            raise ValueError(f"Invalid color: {color}")

    for char in text:
        sys.stdout.write(f"{color_code}{char}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(speed_factor)
    print()

def clear_screen():
    """
    Clears the terminal screen.

    Uses 'cls' on Windows and 'clear' on Unix/Linux systems.
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as e:
        print(f"Error clearing screen: {e}")