Usage
=====

Installation
------------

You may install etalumacontrol from `PyPI <https://pypi.org/project/etalumacontrol/>`_ by entering the following into a shell prompt, preferably after activating a virtual environment:

.. code-block:: console

    py -m pip install etalumacontrol


Quickstart
----------

Here's a sample program which moves the stage to a specified position, acquires an image, and displays it on the screen.

.. code-block:: python

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

