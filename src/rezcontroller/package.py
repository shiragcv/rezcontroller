import os
import yaml


# Current directory
__CD = os.path.dirname(__file__)

# Config file
CONFIG_FILE = os.path.join(__CD, 'configs', 'packages.yaml')


def get(request):
    """
    Get package from given request. Request can be in following formats

    1. einer:alpha
    2. maya-2019.3.1

    Args:
        request (str): Package request

    Raises:
        KeyError: When package not defined in config

    Returns:
        str: Package
    """

    if ':' not in request:
        return request

    name, _, version = request.partition(':')
    version = version or 'release'

    with open(CONFIG_FILE) as f:
        packages = yaml.safe_load(f)

    if name not in packages:
        raise KeyError('No package found with name {0}'.format(name))

    package = packages.get(name, {}).get(version, None)

    if not package:
        return None

    return package
