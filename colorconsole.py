'''
Implements basic colored-terminal I/O features
'''

# Import neccessary libraries
from colorama import init, Fore, Back, Style
import ctypes

# Initialize console
init()

# The 3-bit RGB codes corresponding to a color
COLOR_CODE = {
    "black"  : "000",
    "red"    : "100",
    "green"  : "010",
    "yellow" : "110",
    "blue"   : "001",
    "magenta": "101",
    "cyan"   : "011",
    "white"  : "111",
}

class ColorConsole:
    '''
    A console capable of printing text
    '''
    def __init__(self, title="ColorConsole Window"):
        '''
        Creates a new colored console

        Parameters:
        - `title`: The title of the console window
        '''
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    def print(self, val="", newline=False, **kwargs):
        '''
        Prints an object at cursor position, moves cursor accordingly.

        Parameters:
        - `val`: The object to print
        - `newline`: Whether a newline should be printed or not.
        - `**kwargs`:
            - `fgColor`: The color of the foreground. Must be one of:
                - `\"black\"`
                - `\"blue\"`
                - `\"cyan\"`
                - `\"green\"`
                - `\"magenta\"`
                - `\"red\"`
                - `\"white\"`
                - `\"yellow\"`
            - `bgColor`: The color of the background. Must be one of:
                - `\"black\"`
                - `\"blue\"`
                - `\"cyan\"`
                - `\"green\"`
                - `\"magenta\"`
                - `\"red\"`
                - `\"white\"`
                - `\"yellow\"`
            - `rgbBg`: A three-bit RGB value representing the background. Should be formatted `\"[Red][Green][Blue]\"`
            - `rgbFg`: A three-bit RGB value representing the foreground. Should be formatted `\"[Red][Green][Blue]\"`

        If both the RGB *and* the color name for the fore/background, the RGB value will be used.
        '''
        # Set the foreground color
        fg = "1001"
        if "rgbFg" in kwargs:
            fg = kwargs["rgbFg"]
        elif "fgColor" in kwargs:
            fg = COLOR_CODE[kwargs["fgColor"].lower()]

        # Set the background color
        bg = "1001"
        if "rgbBg" in kwargs:
            bg = kwargs["rgbBg"]
        elif "bgColor" in kwargs:
            bg = COLOR_CODE[kwargs["bgColor"].lower()]

        # Create color escape codes
        col = "\x1b[3%dm\x1b[4%dm" % (int(fg[::-1], 2), int(bg[::-1], 2))

        # Replace newlines with non-color newlines
        val = col + str(val).replace("\n", "\x1b[39m\x1b[49m\n" + col)
        print(val, end="")

        # Insert newline if trailing newline requested
        if newline:
            print()

    def input(self, val="", **kwargs):
        '''
        Prints an object at cursor position, then asks for user input. moves cursor accordingly.

        Parameters:
        - `val`: The object to print
        - `**kwargs`:
            - `fgColor`: The color of the foreground. Must be one of:
                - `\"black\"`
                - `\"blue\"`
                - `\"cyan\"`
                - `\"green\"`
                - `\"magenta\"`
                - `\"red\"`
                - `\"white\"`
                - `\"yellow\"`
            - `bgColor`: The color of the background. Must be one of:
                - `\"black\"`
                - `\"blue\"`
                - `\"cyan\"`
                - `\"green\"`
                - `\"magenta\"`
                - `\"red\"`
                - `\"white\"`
                - `\"yellow\"`
            - `rgbBg`: A three-bit RGB value representing the background. Should be formatted `\"[Red][Green][Blue]\"`
            - `rgbFg`: A three-bit RGB value representing the foreground. Should be formatted `\"[Red][Green][Blue]\"`

        If both the RGB *and* the color name for the fore/background, the RGB value will be used.
        '''
        self.print(val, **kwargs)
        self.print()
        userInput = input()
        return userInput

    def setCursor(self, row=0, col=0):
        '''
        Sets cursor position.

        Parameters:
        - `row`: The row to set the cursor position (row 1 is the top)
        - `col`: The column to set the cursor position (column 0 is the leftmost column)
        '''
        print("\x1b[%d;%dH" % (row, col), end="")

    def clear(self):
        '''
        Clears the output console
        '''
        print("\033[H\033[J", end="")

if __name__ == "__main__":
    c = ColorConsole()
    c.print("R", rgbBg="100")
    c.print("A", rgbBg="110")
    c.print("I", rgbBg="010")
    c.print("N", rgbBg="011")
    c.print("B", rgbBg="001")
    c.print("O", rgbBg="101")
    c.print("W", rgbBg="100", newline=True)
    if c.input("Did you see any color?\n")[0].lower() == "y":
        c.print("You're all ")
        c.print("good to go!", fgColor="green")
        c.setCursor(5, 1)
        c.print("Press ")
        c.print("Enter", rgbFg="000", bgColor="white")
        c.input(" to continue...")
        c.clear()
        c.print("a")
        for i in range(1, 10):
            c.setCursor(i, i)
            c.print("(%d, %d)" % (i, i))
        c.print("\nTesting cursor positioning...", True, fgColor="cyan")
        c.print("Did cursor positioning work?", fgColor="yellow")
        c.print(" (In other words, the text above should be starting at the ")
        c.print("coordinates", fgColor="magenta")
        if c.input(" shown)\t")[0].lower() == "y":
            c.print("Awesome! It all works so far!", True, fgColor="Green")
        else:
            c.print("Then it looks like you're having some problems. Try installing Colorama, or reinstalling it if you have it.")
    else:
        c.print("Then it looks like you're having some problems. Try installing Colorama, or reinstalling it if you have it.")
