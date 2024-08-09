import pprint

from . import parser

from . import header

def main():
    """Primary entrypoint."""

    instance = parser.Parser()

    instance.add_argument("--download-timeout", action="store", dest="download_timeout", metavar="value", type=int, help="Download timeout in seconds",default=120)
    instance.add_argument("--request-timeout", action="store", dest="request_timeout", metavar="value", type=int, help="Request timeout in seconds", default=60)
    instance.add_argument("--log-level", action="store", dest="log_level", metavar="value", type=str.lower, choices=["debug", "info", "warning", "error", "critical"], help="Log level to use", default="info")

    instance.add_argument("-h", "--help", action="help", help="Display this message")

    arguments = instance.parse_args()

    pprint.pprint(arguments)


