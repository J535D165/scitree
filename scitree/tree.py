import seedir as sd
from scisort import scisort_keygen

from scitree.styling import natsort_scitree_style


def scitree(
    p,
    sort=True,
    sort_key=scisort_keygen,
    formatter=natsort_scitree_style,
    first="files",
    **kwargs
):

    return sd.seedir(
        p, sort=sort, sort_key=sort_key, formatter=formatter, first=first, **kwargs
    )
