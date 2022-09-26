from scitree.styling import natsort_scitree_style
from scisort import scisort_keygen

import seedir as sd


def scitree(p, **kwargs):

    return sd.seedir(p, sort=True, sort_key=scisort_keygen, formatter=natsort_scitree_style, **kwargs)
