"""
NVIDIA Auto Installer for Fedora Linux
Copyright (C) 2019-2021 Akashdeep Dhar

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


from click import echo, style

PASS = style("[ \u2713 ]", fg="green", bold=True)
FAIL = style("[ \u2717 ]", fg="red", bold=True)
WARN = style("[ ! ]", fg="yellow", bold=True)
HEAD = style("[ \u2605 ]", fg="magenta", bold=True)
STDS = "     "


def success(message):
    echo(PASS + " " + message)


def failure(message):
    echo(FAIL + " " + message)


def warning(message):
    echo(WARN + " " + message)


def section(message):
    echo(HEAD + " " + style(message, fg="magenta", bold=True))


def general(message):
    echo(STDS + " " + message)
