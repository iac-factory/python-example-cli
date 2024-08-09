import sys

from package.cli.parser import Parser

def main():
    parser = Parser()

    parser.add_argument("--download-timeout", action="store", dest="download_timeout", metavar="timeout", type=int, help="Download timeout in seconds",default=120)
    parser.add_argument("--request-timeout", action="store", dest="request_timeout", metavar="timeout", type=int, help="Request timeout in seconds", default=60)
    parser.add_argument("--log-level", action="store", dest="log_level", metavar="level", type=str.lower, choices=["debug", "info", "warning", "error", "critical"], help="Log level to use", default="info")

    parser.add_argument("-h", "--help", action="help", help="Display this message")

    arguments = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
