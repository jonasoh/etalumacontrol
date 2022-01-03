Welcome to etalumacontrol's documentation!
==========================================

This library provides a simplified Python interface for interacting with Etaluma microscopes and motorized stages (600 and 700 series). Essentially, the code provides a simplified wrapper for Etaluma's own C# SDK using `Python.NET <http://pythonnet.github.io/>`_. This package requires Python 3.8 (or higher, but Python.NET currently supports only up to 3.8).

.. note::

   This library was written to facilitate our own use case, but may also be useful to others. If there's a particular feature that you feel is lacking, feel free to submit an issue or PR on `GitHub <https://github.com/jonasoh/etalumacontrol>`_. Etalumacontrol has only been tested on our LS720, but should work on any 600 and 700 series microscope. 32-bit versions of the LumaUSB and WSC DLL's are included, but have not been tested.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Contents
--------

.. toctree::

   usage

License
-------

Etalumacontrol is licensed under a 2-clause BSD license.

Etalumacontrol contains microscope firmware and DLL files kindly provided by Etaluma, which are not subject to this license. These files may be distributed as part of the etalumacontrol package, but for other uses please contact Etaluma directly.

Etalumacontrol contains code written by `John Kelley <https://github.com/John-K>`_. See its separate license file in the CypressFX directory.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
