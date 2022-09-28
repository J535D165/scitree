import os

import seedir as sd
from scisort import scisort_keygen

from scitree.styling import natsort_scitree_style
from scitree.styling import SCRIPT_COLOR
from scitree.styling import README_COLOR
from scitree.styling import DATA_COLOR


def scitree(
    p,
    sort=True,
    sort_key=scisort_keygen,
    formatter=natsort_scitree_style,
    first="files",
    **kwargs
):

    sd.seedir(
        p, sort=sort, sort_key=sort_key, formatter=formatter, first=first, **kwargs
    )

    n_files = 0
    folders = []
    for root_dir, cur_dir, files in os.walk(p):
        n_files += len(files)
        folders.extend(cur_dir)
    n_folders = len(set(folders))

    print(f"\n{n_folders} directories, {n_files} files")
    print(f"\x1b[{README_COLOR}mREADME\x1b[0m \x1b[{DATA_COLOR}mData\x1b[0m \x1b[{SCRIPT_COLOR}mCode\x1b[0m")