from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='etalumacontrol',
    version='0.1.0',
    description='Library for interacting with Etaluma microscopes and stages',
    author='Jonas Ohlsson',
    author_email='jonas.ohlsson@slu.se',
    url='https://github.com/jonasoh/etalumacontrol',
    license=license,
    packages=find_packages(),
    install_requires=['intelhex>=2.3.0', 'Pillow>=8.3.1', 'pycparser>=2.20', 'pythonnet>=2.5.2', 'pyusb>=1.2.1']
)
