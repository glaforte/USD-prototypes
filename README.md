# USD-prototypes

The purpose of this repository is to advance my knowledge of the USD API through small and quick prototypes.
This repository is testing exclusively on Windows 10, since that's my home development/gaming workstation.

## How to run

1. Setup Python 2.7.16
2. Setup the MSVS 2017 C++ build tools.
2. Setup the USD SDK on Windows 10.
3. Start your favorite prototype script.

### Python 2.7.16

Please note that Python 2.x is marked obsolete. You will need to go into the older download folder, or use this link: https://www.python.org/downloads/release/python-2717/
* Make sure to toggle adding Python to the PATH environment variable.

From a command-line:
* pip install PySide
* pip install pyopengl
* pip install jinja2

### MSVS 2017 C++ build tools.

My first thought was to install the latest version of Visual Studio. Unfortunately, the USD SDK has Boost 1.65 as a dependency and its build tool refuses to work with the newest build tools in Visual Studio 2019 Community Edition. In order to use Pixar's build script for the USD SDK, you must download Visual Studio 2017 Community Edition.

* Sign up for a Microsoft account.
* Sign up for the Microsoft free Dev Essentials program.
* In the Visual Studio Subscriptions, you should now have access to the Downloads tab.
* Filter for Visual Studio 2017 (version 15.0).
* Download Visual Studio Community 2017 (version 15.0).
* Start the installer.
* Install the packages: Visual C++ core desktop features, VC++ 2017 v141 toolset (x86,x64)

Optionally:
* Download Visual Studio Code while you are on Microsoft's website!

### Build the USD SDK on Windows

You can download the source code for the USD SDK for Pixar's GitHub account: https://github.com/PixarAnimationStudios/USD. It includes a script that will build the USD SDK. I've found that script to be quite trust-worthy, but to requires quite a few prerequisite installed. vfxpro99 keeps a decent list of prerequisites in his usd-build-club repository: https://github.com/vfxpro99/usd-build-club/wiki/USD-on-Windows

Pre-requistes:
* Install the latest Git.
* Install the latest CMake.
* Install the latest NASM.
* Install the latest 7-zip.
* Make sure that CMake, NASM and 7-zip are added to your PATH environment variable.

To build the USD SDK:
* Start the VC++2017 command-line from your start-menu: "\x64 Native Tools Command Prompt for VS 2017"
* cd C:\dev
* git clone https://github.com/PixarAnimationStudios/USD.git
* USD\build_scripts\build_usd.py C:\dev\build-output

The build took an hour, on my somewhat powerful workstation.
Once the build completes, it should instruct you to add two folders to the PATH environment variable and one folder to the PYTHONPATH environment variable.

