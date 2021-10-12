from rez import resolved_context
from rezcontroller import package


def create(requests):
    """
    Create a rez context from given packages

    Args:
        requests (list): List of package requests

    Returns:
        ResolvedContext: Resolved context object
    """

    packages = []

    for request in requests:
        packages.append(package.get(request=request))

    return resolved_context.ResolvedContext(package_requests=packages)
