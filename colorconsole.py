# Init colorama
from colorama import init
init()

class ColorConsole():
    def print(self, text, **kwargs):
        '''
        Prints a string at the current cursor position\n
        **kwargs:\n
        \t- fore: Text foreground in 3-bit RGB format (green is \"010\", for example)\n
        \t- back: Text background in 3-bit RGB format
        '''
        fore = 7
        back = 0
        for key in kwargs:
            val = kwargs[key]
            if key == "fore":
                fore = int(val[0]) + int(val[1])*2 + int(val[2])*4
            elif key == "back":
                back = int(val[0]) + int(val[1])*2 + int(val[2])*4

        print("\033[1;3%d;4%dm%s" % (fore, back, text), end="")

    def printAt(self, text, row, col, **kwargs):
        '''
        Prints a string at a specified position\n
        **kwargs:\n
        \t- fore: Text foreground in 3-bit RGB format (green is \"010\", for example)\n
        \t- back: Text background in 3-bit RGB format
        '''
        self.moveCursor(row, col)
        self.print(text, **kwargs)

    def moveCursor(self, row, col):
        '''
        Moves the cursor to a certain position.\n
        '''
        print("\033[%d;%dH" % (row, col), end="")

    def clear(self):
        '''
        Clears the output console
        '''
        print("\033[H\033[J")

if __name__ == "__main__":
    console = ColorConsole()
    console.print("Hello,", fore="010")
    console.printAt("World!", 2, 2, fore="011")