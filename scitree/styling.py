from pathlib import Path

# colors are blue, green, red, yellow
SCRIPT_COLOR = 31
README_COLOR = 34
DATA_COLOR = 32
FIGURE_COLOR = 33
FOLDER_COLOR = 30

SCRIPT_ICON = '\U0001F4C4'  # 📄
README_ICON = '\U0001F4D6'  # 📖
DATA_ICON = '\U0001F4DC'    # 📜
FIGURE_ICON = '\U0001F4CA'  # 📊
FOLDER_ICON = '\U0001F4C1'  # 📁

CODE_SUFFIXES = [".py", ".R", ".m", ".js", ".sh", ".ipynb", ".cpp", ".h", ".bat"]
DATA_SUFFIXES = [".csv", ".tab", ".xlsx", ".xls", ".json", ".zip", ".dat" ".txt", ".tsv"]
FIGURE_SUFFIXES = [".png", ".jpg", ".jpeg", ".svg", ".pdf", ".eps", ".tiff", ".tif" ".gif" ".bmp"]


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


def _color_folder(style, color=30, inner=True):

    return _color(style=style, ftype="folder", color=color, inner=inner)


def _icon_file(style, icon=SCRIPT_ICON):

    if "filestart" in style:
        style["filestart"] = icon + " " + style["filestart"]
    else:
        style["filestart"] = icon + " "

    return style


def _icon_folder(style, icon=FOLDER_ICON):

    if "folderstart" in style:
        style["folderstart"] = icon + " " + style["folderstart"]
    else:
        style["folderstart"] = icon + " "

    return style


def natsort_scitree_style(item, **kwargs):

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
        if kwargs.get("icons", True):
            style = _icon_file(style, icon=SCRIPT_ICON)

    if item.suffix in DATA_SUFFIXES:
        style = _color_file(style, color=DATA_COLOR)
        if kwargs.get("icons", True):
            style = _icon_file(style, icon=DATA_ICON)

    if item.suffix in FIGURE_SUFFIXES:
        style = _color_file(style, color=FIGURE_COLOR)
        if kwargs.get("icons", True):
            style = _icon_file(style, icon=FIGURE_ICON)

    if item.stem.lower().startswith("readme"):
        style = _color_file(style, color=README_COLOR)
        if kwargs.get("icons", True):
            style = _icon_file(style, icon=README_ICON)

    if item.is_dir():
        if kwargs.get("icons", True):
            style = _icon_folder(style, icon=FOLDER_ICON)

    return style
