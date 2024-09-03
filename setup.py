from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A simple package that contains a set of useful printing options'
LONG_DESCRIPTION = 'This Package uses the ANSI escape sequences to format console printouts as well as animations such as a progress bar for use in the console. Furthermore options to automatically create logfiles of each statement printed.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="PrettyPrint",
    version=VERSION,
    author="Lorenz Kuhn",
    author_email="<lorenz.achim.kuhn@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package', 'console formatting', 'output', 'logging', 'printing'],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)