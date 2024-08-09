import pprint

from . import cli

def main():
    parser = cli.Parser()

    parser.add_argument("--download-timeout", action="store", dest="download_timeout", metavar="value", type=int, help="Download timeout in seconds",default=120)
    parser.add_argument("--request-timeout", action="store", dest="request_timeout", metavar="value", type=int, help="Request timeout in seconds", default=60)
    parser.add_argument("--log-level", action="store", dest="log_level", metavar="value", type=str.lower, choices=["debug", "info", "warning", "error", "critical"], help="Log level to use", default="info")

    parser.add_argument("-h", "--help", action="help", help="Display this message")

    arguments = parser.parse_args()

    pprint.pp(arguments)

if __name__ == "__main__":
    main()
