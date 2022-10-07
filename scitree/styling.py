from pathlib import Path

SCRIPT_COLOR = 31
README_COLOR = 34
DATA_COLOR = 32

CODE_SUFFIXES = [".py", ".R", ".m", ".js", ".sh", ".ipynb", ".cpp", ".h"]

DATA_SUFFIXES = [".csv", ".tab", ".xlsx", ".xls", ".json", ".zip", ".dat"]


def _color(style, ftype, color=31, inner=True):

    if inner:
        if f"{ftype}start" in style:
            style[f"{ftype}start"] = style[f"{ftype}start"] + f"\x1b[{color}m"
        else:
            style[f"{ftype}start"] = f"\x1b[{color}m"

        if f"{ftype}end" in style:
            style[f"{ftype}end"] = "\x1b[0m" + style[f"{ftype}end"]
        else:
            style[f"{ftype}end"] = "\x1b[0m"

    else:
        if f"{ftype}start" in style:
            style[f"{ftype}start"] = f"\x1b[{color}m" + style[f"{ftype}start"]
        else:
            style[f"{ftype}start"] = f"\x1b[{color}m"

        if f"{ftype}end" in style:
            style[f"{ftype}end"] = style[f"{ftype}end"] + "\x1b[0m"
        else:
            style[f"{ftype}end"] = "\x1b[0m"

    return style


def _color_file(style, color=31, inner=True):

    return _color(style=style, ftype="file", color=color, inner=inner)


def _color_folder(style, color=31, inner=True):

    return _color(style=style, ftype="folder", color=color, inner=inner)


def natsort_scitree_style(item):

    # convert to Path
    item = Path(item)

    style = {
        "split": "├── ",
        "extend": "│   ",
        "space": "    ",
        "final": "└── ",
        "folderend": "/",
    }

    if item.suffix in CODE_SUFFIXES:
        style = _color_file(style, color=SCRIPT_COLOR)

    if item.suffix in DATA_SUFFIXES:
        style = _color_file(style, color=DATA_COLOR)

    if item.stem.lower().startswith("readme"):
        style = _color_file(style, color=README_COLOR)

    return style
