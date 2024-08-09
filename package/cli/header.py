from typing import List

from package.cli import colors

from package.cli.configuration import Configuration

def title() -> str:
    return colors.italic(colors.red(Configuration.company)) + " - " + colors.bold(Configuration.title)

def description() -> str:
    return Configuration.description

def copyright() -> str:
    return colors.gray(Configuration.copyright)

def help() -> str:
    value = "--[H]elp for Usage"

    return colors.yellow(value)

def Header() -> List[str]:
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
