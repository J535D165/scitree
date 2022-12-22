from pathlib import Path

import gitignorefile
from scisort import scisort_keygen
import seedir as sd

from scitree.styling import DATA_COLOR
from scitree.styling import README_COLOR
from scitree.styling import SCRIPT_COLOR
from scitree.styling import FIGURE_COLOR
from scitree.styling import SERIAL_COLOR
from scitree.styling import DATA_ICON
from scitree.styling import README_ICON
from scitree.styling import SCRIPT_ICON
from scitree.styling import FIGURE_ICON
from scitree.styling import SERIAL_ICON

from scitree.styling import natsort_scitree_style


def _file_count(d, n_files=0, n_folders=0, mask=None, exclude_folders=[]):

    for f in Path(d).iterdir():

        if mask is None or not mask(str(f)):
            if f.is_file():
                n_files += 1
            else:
                if str(f) not in exclude_folders:
                    n_folders += 1
                    n_files, n_folders = _file_count(
                        f,
                        n_files,
                        n_folders,
                        mask=mask,
                        exclude_folders=exclude_folders,
                    )

    return n_files, n_folders


def scitree(
    p=".",
    sort=True,
    sort_key=scisort_keygen(),
    formatter=natsort_scitree_style,
    gitignore=True,
    first="files",
    exclude_folders=[".git"],
    icons=True,
    **kwargs
):

    if gitignore and Path(p, ".gitignore").exists():
        gi_matcher = gitignorefile.parse(Path(p, ".gitignore"))

        def gi_mask(x):
            return not gi_matcher(x)

    else:
        gi_mask = None

    sd.seedir(
        str(p),
        sort=sort,
        sort_key=sort_key,
        formatter=formatter,
        first=first,
        mask=gi_mask,
        exclude_folders=exclude_folders,
        **kwargs
    )

    n_files, n_folders = _file_count(
        p,
        n_files=0,
        n_folders=0,
        mask=gi_mask,
        exclude_folders=exclude_folders,
    )

    print(f"\n{n_folders} directories, {n_files} files")
    print(f"{README_ICON}\x1b[{README_COLOR}mREADME {DATA_ICON}\x1b[0m \x1b[{DATA_COLOR}mData\x1b[0m {SCRIPT_ICON}\x1b[{SCRIPT_COLOR}mCode\x1b[0m {FIGURE_ICON}\x1b[{FIGURE_COLOR}mFigures\x1b[0m {FOLDER_ICON}Folder {SERIAL_ICON}\x1b[{SERIAL_COLOR}mSerial Data ")  # noqa
