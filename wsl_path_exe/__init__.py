#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
WSL-path-exe is a "script" that helps you use native software (.exe)
more easily inside WSL, putting everyone in the PATH without ever having
to put .exe at the end. The exe's will behave like a WSL command, so the
autocomplete of some application will work too (e.g Python). Only bash
and zsh are supported.
"""

import platform
import argparse
import os


PATH_FOLDER = os.path.join(os.getenv("HOME"), ".wsl")


def wsl_running():
    """Checks whether WSL is running WSL-path-exe and returns a Boolean."""
    data_platform = platform.platform().lower()

    return True if data_platform.find("linux") != -1 \
                   and data_platform.find("microsoft") else False


def list_paths():
    """
    Scans the native system directories that are in the default PATH
    and returns a list of the executables.
    """
    paths_natives = [p for p in os.getenv("PATH").split(":")
                     if p.startswith("/mnt/c/")]
    executables = []
    for files_exe in paths_natives:
        executables = executables + [os.path.join(files_exe, e)
                                     for e in os.listdir(files_exe)
                                     if e.endswith(".exe")]
    return executables


def link_executables():
    """
    Makes a symbolic link of all executables into WSL in a folder in the
    home directory
    """
    if not os.path.isdir(PATH_FOLDER):
        os.mkdir(PATH_FOLDER)

    for command_wsl in list_paths():
        executable = command_wsl.split("/")[-1]
        command = executable.split(".")[-2]
        path_wsl = os.path.join(PATH_FOLDER, command)
        os.system("ln -sf '{}' '{}'".format(command_wsl, path_wsl))


def command_line_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(prog='wsl-path-exe')
    parser.add_argument("-l", "--link", action="store_true")

    return parser
