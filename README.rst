WSL-path-exe
============

WSL-path-exe is a "script" that helps you use native software (``.exe``) more easily inside `WSL <https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux>`_
, putting everyone in the PATH without ever having to put .exe at the end. The exe's will behave like a WSL command, so the **autocomplete** of some application will work too (e.g Python). Only **bash** and **zsh** are supported.

Dependencies
~~~~~~~~~~~~

- WSL/Ubuntu
- Python (``apt install python``)
- pip (``apt install python-pip``)

Install and Usage
~~~~~~~~~~~~~~~~~

The entire installation process is done within WSL, not in Powershell or CMD.

``$ pip install wsl-path-exe``

``$ wsl-path-exe -l``

You may want to always leave the executables available in PATH add folder WSL:

``$ echo 'export PATH=$PATH:$HOME/.wsl' >> ~/.bashrc``

or

``$ echo 'export PATH=$PATH:$HOME/.wsl' >> ~/.zshrc``
