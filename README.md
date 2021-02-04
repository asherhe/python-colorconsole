# python-colorconsole

`colorconsole` is well, a colored console module for python, with basic console features.

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
