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
Main WSL command
"""

from . import command_line_args, link_executables, wsl_running

def main():
    command_sys = command_line_args().parse_args()
    if wsl_running():
        if command_sys.link:
            link_executables()
    else:
        print("Run only on WSL")

if __name__ == '__main__':
    main()
