# etalumacontrol

## Introduction

This library provides a simplified Python interface for interacting with Etaluma microscopes and motorized stages (600 and 700 series). Essentially, the code provides a simplified wrapper for Etaluma's own C# SDK using [Python.NET](http://pythonnet.github.io/). This package requires Python 3.8 (or higher, but Python.NET currently supports only up to 3.8).

## Current state and limitations

This library was written to facilitate our own use case, but may also be useful to others. If there's a particular feature that you feel is lacking, feel free to submit an issue or PR. Etalumacontrol has only been tested on our LS720, but should work on any 600 and 700 series microscope. 32-bit versions of the LumaUSB and WSC DLL's are included, but have not been tested.

## Installation

You may install etalumacontrol from [PyPI](https://pypi.org/project/etalumacontrol/) by entering the following into a shell prompt, preferably after activating a virtual environment:

```
py -m pip install etalumacontrol
```

## Sample program

Here's a sample program which moves the stage to a specified position, acquires an image, and displays it on the screen.

```python
from etalumacontrol import EtalumaStage, LumaScope

# use the "with" statement to automatically handle resource allocation
with EtalumaStage() as stage, LumaScope() as scope:
    # move stage to center of microscopy slide
    stage.move('x', -62.9)
    stage.move('y', -38)

    # turn on the brightfield led
    scope.set_led(brightness=20)

    # turn up the gain
    scope.gain = 10

    # set shutter speed to 150 ms
    scope.shutter = 150

    # acquire image and show it
    img = scope.get_image()
    img.show()
```

## Documentation

The documentation for this package can be found at [ReadTheDocs](https://etalumacontrol.readthedocs.io/en/latest/).

## License

Etalumacontrol is licensed under a 2-clause BSD license. 

Etalumacontrol contains microscope firmware and DLL files kindly provided by Etaluma, which are not subject to this license. These files may be distributed as part of the etalumacontrol package, but for other uses please contact Etaluma directly.

Etalumacontrol contains code written by [John Kelley](https://github.com/John-K). See its separate license file in the CypressFX directory.
