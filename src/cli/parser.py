from . import constants

import os
import sys
import argparse
import textwrap

from . import header
class Parser(argparse.ArgumentParser):
    def __init__(self, *args, width=80, **kwargs):
        """
        Parameters
        ----------
        args : tuple
        width : int - Postition of 'width' argument: https://www.python.org/dev/peps/pep-3102/
        kwargs : dict
        """
        # At least self.positionals + self.options need to be initialized before calling
        # __init__() of parent class, as argparse.ArgumentParser.__init__() defaults to
        # 'add_help=True', which results in call of add_argument("-h", "--help", ...)
        self.program = {key: kwargs[key] for key in kwargs}

        self.positionals = []
        self.options = []
        self.width = width

        # If the standard-output is interactive, recalculate the terminal's width
        if os.isatty(sys.stdin.fileno()):
            self.width = os.get_terminal_size().columns

        program: str = constants.Title
        usage: str = "Usage"
        description: str = constants.Description

        options = {
            "prog": program,
            "usage": usage,
            "description": description,

            "epilog": "",
            "formatter_class": argparse.RawTextHelpFormatter,
            "exit_on_error": True,
            "add_help": False,
            "argument_default": argparse.SUPPRESS,
            "allow_abbrev": False,
        }

        for k, v in kwargs.items():
            options[k] = v

        super(Parser, self).__init__(*args, **options)

    def add_argument(self, *args, **kwargs):
        super(Parser, self).add_argument(*args, **kwargs)
        argument = {key: kwargs[key] for key in kwargs}

        # Positional: argument with only one name not starting with '-' provided as
        # positional argument to method -or- no name and only a 'dest=' argument
        if (len(args) == 0 or (len(args) == 1 and isinstance(args[0], str) and not args[0].startswith("-"))):
            argument["name"] = args[0] if (len(args) > 0) else argument["dest"]
            self.positionals.append(argument)
            return

        # Option: argument with one or more flags starting with '-' provided as
        # positional arguments to method
        argument["flags"] = [item for item in args]
        self.options.append(argument)

    def format_usage(self):
        return "\n" + "\n".join(header.header())

    def format_help(self):
        output = []
        dewrapper = textwrap.TextWrapper(width=self.width)

        # Add usage message to output
        output.append(self.format_usage())

        # Determine what to display left and right for each argument, determine max
        # string lengths for left and right
        lmaxlen = rmaxlen = 0
        for positional in self.positionals:
            positional["left"] = positional["metavar"] if ("metavar" in positional) else positional["name"]
        for option in self.options:
            if ("action" in option and (option["action"] == "store_true" or option["action"] == "store_false")):
                option["left"] = str.join(", ", option["flags"])
            else:
                option["left"] = str.join(", ", [
                    # "%s %s" % (item, option["metavar"]) if ("metavar" in option) else "%s %s" % (item, option["dest"].upper()) if ("dest" in option) else item for item in option["flags"]])
                    "%s %s" % (item, option["metavar"]) if ("metavar" in option) else "%s %s" % (item, option["dest"]) if ("dest" in option) else item
                    for item in option["flags"]])
        for argument in self.positionals + self.options:
            argument["right"] = ""
            if ("help" in argument and argument["help"] != "" and not str.isspace(argument["help"])):
                argument["right"] += argument["help"]
            else:
                # argument["right"] += "No description available"
                argument["right"] += "No help available"
            if ("choices" in argument and len(argument["choices"]) > 0):
                argument["right"] += " (choices: %s)" % str.join(", ", (
                "'%s'" % item if isinstance(item, str) else "%s" % str(item) for item in argument["choices"]))
            if ("default" in argument and argument["default"] != argparse.SUPPRESS):
                argument["right"] += " (default: %s)" % (
                    "'%s'" % argument["default"] if isinstance(argument["default"], str) else "%s" % str(
                        argument["default"]))
            lmaxlen = max(lmaxlen, len(argument["left"]))
            rmaxlen = max(rmaxlen, len(argument["right"]))

        # Determine width for left and right parts based on maximum string lengths,
        # define output template. Limit width of left part to a maximum of self.width
        # / 2. Use max() to prevent negative values. -4: two leading spaces (indent)
        # + two trailing spaces (spacing between left and right), see template
        lwidth = lmaxlen
        rwidth = max(0, self.width - lwidth - 4)
        if (lwidth > int(self.width / 2) - 4):
            lwidth = max(0, int(self.width / 2) - 4)
            rwidth = int(self.width / 2)
        # outtmp = "  %-" + str(lwidth) + "s  %-" + str(rwidth) + "s"
        outtmp = "  %-" + str(lwidth) + "s  %s"

        # Wrap text for left and right parts, split into separate lines
        lwrapper = textwrap.TextWrapper(width=lwidth)
        rwrapper = textwrap.TextWrapper(width=rwidth)
        for argument in self.positionals + self.options:
            argument["left"] = lwrapper.wrap(argument["left"])
            argument["right"] = rwrapper.wrap(argument["right"])

        # Add positional arguments to output
        if (len(self.positionals) > 0):
            output.append("")
            output.append("Positionals:")
            for positional in self.positionals:
                for i in range(0, max(len(positional["left"]), len(positional["right"]))):
                    left = positional["left"][i] if (i < len(positional["left"])) else ""
                    right = positional["right"][i] if (i < len(positional["right"])) else ""
                    output.append(outtmp % (left, right))

        # Add option arguments to output
        if (len(self.options) > 0):
            output.append("")
            output.append("Options:")
            for option in self.options:
                for i in range(0, max(len(option["left"]), len(option["right"]))):
                    left = option["left"][i] if (i < len(option["left"])) else ""
                    right = option["right"][i] if (i < len(option["right"])) else ""
                    output.append(outtmp % (left, right))

        # Add epilog to output if present
        if ("epilog" in self.program and self.program["epilog"] != "" and not str.isspace(self.program["epilog"])):
            output.append("")
            output.append(dewrapper.fill(self.program["epilog"]))

        # Return output as single string
        return str.join("\n", output)

    # Method redefined as format_usage() does not return a trailing newline like
    # the original does
    def print_usage(self, file=None):
        if (file == None):
            file = sys.stdout
        file.write(self.format_usage() + "\n")
        file.flush()

    # Method redefined as format_help() does not return a trailing newline like
    # the original does
    def print_help(self, file=None):
        if (file == None):
            file = sys.stdout
        file.write(self.format_help() + "\n")
        file.flush()

    def error(self, message):
        sys.stderr.write(self.format_usage() + "\n")
        sys.stderr.write(("Error: %s" % message) + "\n")
        sys.exit(2)
