from . import colors
from . import constants

from typing import List

def title() -> str:
    return colors.italic(colors.red(constants.Company)) + " - " + colors.bold(constants.Title)

def description() -> str:
    return constants.Description

def copyright() -> str:
    return colors.gray(constants.Copyright)

def help() -> str:
    value = "--[H]elp for Usage"

    return colors.yellow(value)

def header() -> List[str]:
    lines : List[str] = []

    lines.append(colors.blue("    //\\\\--/") + "  " + colors.purple(" //\\\\--/"))
    lines.append(colors.blue("   ╱╱__\\\\/" + "  " + colors.purple(" //__\\\\/")) + "   " + title())
    lines.append(colors.blue("  ╱╱\\\\--/") + "  " + colors.purple(" //\\\\--/"))
    lines.append(colors.blue(" //__\\\\/") + "  " + colors.purple(" //__\\\\/" ) + "   " + description())
    lines.append(colors.blue(" \\\\--/\\\\") + "  " + colors.purple("//\\\\--/"))
    lines.append(colors.blue("  \\\\/__\\\\") + colors.purple("//\\\\--/") + "   " + copyright())
    lines.append(colors.blue("   \\\\---") + colors.purple("//__\\\\/"))
    lines.append(colors.blue("    \\\\") + " " + colors.purple("//__\\\\/") + "   " + help())
    lines.append(colors.blue("     \\\\") + colors.purple("\\\\--//"))

    return lines
