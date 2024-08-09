import dataclasses

from package.data import data

@dataclasses.dataclass
class Configuration:
    """
    Attributes
    ----------
    company: str
        The name of the company.

    title: str
        The title of commandline (cli) application.
    description: str
        The description of commandline (cli) application.
    copyright: str
        The copyright of commandline (cli) application.
    """

    company: str = data.metadata["company"]
    title: str = data.metadata["title"]
    description: str = data.metadata["description"]
    copyright: str = data.metadata["copyright"]
