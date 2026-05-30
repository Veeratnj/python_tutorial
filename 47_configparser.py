"""
ConfigParser

Example and comments for ConfigParser.
"""

# ConfigParser
from configparser import ConfigParser
config = ConfigParser()
config["DEFAULT"] = {"Server": "localhost"}
print(config["DEFAULT"]["Server"])
