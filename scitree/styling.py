from pathlib import Path


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

    # Color coding
    if item.suffix == ".py":
        style = _color_file(style)

    if item.stem.lower().startswith("readme"):
        style = _color_file(style, color=34)

    return style
