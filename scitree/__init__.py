try:
    from scitree._version import __version__
    from scitree._version import __version_tuple__
except ImportError:
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)

from scitree.tree import scitree

__all__ = ["scitree"]
