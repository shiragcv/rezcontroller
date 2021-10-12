import os
import yaml

from rezcontroller import package
from rezcontroller import context


# Current directory
__CD = os.path.dirname(__file__)

# Config file
CONFIG_FILE = os.path.join(__CD, 'configs', 'projects.yaml')


def get_requests(name):
    """
    Get all package requests for given project

    Args:
        name (str): Name of the project

    Raises:
        KeyError: When project not defined in config

    Returns:
        list: List of package requests
    """

    with open(CONFIG_FILE) as f:
        projects = yaml.safe_load(f) or {}

    if name not in projects:
        raise KeyError('No project found with name {0}'.format(name))

    return projects.get(name) or []


def get_packages(name):
    """
    Get defined packages of a given project

    Args:
        name (str): Name of the project

    Raises:
        KeyError: When project not found in config

    Returns:
        str: Package
    """

    packages = []
    requests = get_requests(name=name)

    for request in requests:
        packages.append(package.get(request=request))

    return packages


def create_context(name):
    """
    Create a context for given project

    Args:
        name (str): Name of the project

    Returns:
        ResolvedContext: Resolved context object
    """

    return context.create(requests=get_requests(name=name))
