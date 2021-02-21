# python-colorconsole

`colorconsole` is well, a colored console module for python, with basic console features. In a nutshell, it performs magic by printing [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code), which can look scary to the untrained eye.

## Required Modules

- [Colorama](https://pypi.org/project/colorama/): A Python module that actualy makes ANSI escape codes work on windows

# Functions

## `print(val="", newline=False, **kwargs)`

Prints an object at the current cursor position, and moves cursor accordingly.

**Parameters**

- `val`: The object to print
- `newline`: Whether to append a newline to the end
- `**kwargs`:
  - `fgColor`: The foreground color. Can be one of `"black"`, `"blue"`, `"cyan"`, `"green"`, `"magenta"`, `"red"`, `"white"`, or `"yellow"`
  - `bgColor`: The background color. Can be one of `"black"`, `"blue"`, `"cyan"`, `"green"`, `"magenta"`, `"red"`, `"white"`, or `"yellow"`
  - `rgbFg`: The forground color, in 3-bit RGB format
  - `rgbBg`: The background color, in 3-bit RGB format

## `input(val="", **kwargs)`

Prints an object at the cursor position, then waits for user input. Also moves cursor accordingly

**Parameters:**
- `val`: The object to print
- `**kwargs`:
  - `fgColor`: The foreground color. Can be one of `"black"`, `"blue"`, `"cyan"`, `"green"`, `"magenta"`, `"red"`, `"white"`, or `"yellow"`
  - `bgColor`: The background color. Can be one of `"black"`, `"blue"`, `"cyan"`, `"green"`, `"magenta"`, `"red"`, `"white"`, or `"yellow"`
  - `rgbFg`: The forground color, in 3-bit RGB format
  - `rgbBg`: The background color, in 3-bit RGB format

## `setCursor(row=0, col=0)`

Sets cursor position.

**Parameters**
- `row`: The row to set the cursor position (row 1 is the top)
- `col`: The column to set the cursor position (column 0 is the leftmost column)

## `clear()`

Clears the output console
