import argparse
import logging
from setuptools_scm import get_version


from scitree.tree import scitree

def main():

    parser = argparse.ArgumentParser(
        prog="scitree",
        description="Print tree with scientific ordering.",
    )
    parser.add_argument(
        "dir",
        nargs='?',
        default=".",
        help="Directory.",
    )
    parser.add_argument(
        "-a",
        action="store_true",
        help="Directory.",
    )


    # version
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=get_version()),
    )

    args, _ = parser.parse_known_args()

    options = {}

    if not args.a:
        options['exclude_folders'] = [".git"]
        options['regex'] = True

    scitree(args.dir, **options)


if __name__ == "__main__":

    main()
