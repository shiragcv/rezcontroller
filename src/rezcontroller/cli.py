import sys
import argparse

from rezcontroller import project
from rezcontroller import package
from rezcontroller import context


# Project related functions ---------------------------------------------------


def enter_project(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-n',
        '--name',
        type=str,
        required=True,
        help='Project name'
    )

    args = parser.parse_args(argv)

    if (not args.name) or (not isinstance(args.name, str)):
        return 1

    try:
        ctx = project.create_context(name=args.name)
        ctx.execute_shell()

    except Exception as e:
        sys.stderr.write(str(e))

        return 1

    return 0


def view_project(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-n',
        '--name',
        type=str,
        required=True,
        help='Project name'
    )

    args = parser.parse_args(argv)

    if (not args.name) or (not isinstance(args.name, str)):
        return 1

    try:
        ctx = project.create_context(name=args.name)
        ctx.print_info()
        ctx.print_tools()

    except Exception as e:
        sys.stderr.write(str(e))

        return 1

    return 0


# Package related functions ---------------------------------------------------


def view_package(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-r',
        '--request',
        type=str,
        required=True,
        help='Package request'
    )

    args = parser.parse_args(argv)

    if (not args.request) or (not isinstance(args.request, str)):
        return 1

    try:
        sys.stdout.write(
            package.get(request=args.request) or 'No package found'
        )

    except Exception as e:
        sys.stderr.write(str(e))

        return 1

    return 0


# Context related functions ---------------------------------------------------


def view_context(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-r',
        '--requests',
        nargs='+',
        help='Packages'
    )

    args = parser.parse_args(argv)

    try:
        ctx = context.create(requests=args.requests)
        ctx.print_info()
        ctx.print_tools()

    except Exception as e:
        sys.stderr.write(str(e))

        return 1

    return 0


def create_context(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-r',
        '--requests',
        nargs='+',
        help='Packages'
    )

    args = parser.parse_args(argv)

    try:
        ctx = context.create(requests=args.requests)
        ctx.execute_shell()

    except Exception as e:
        sys.stderr.write(str(e))

        return 1

    return 0
