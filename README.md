<p align="center">
  <img alt="Scitree - Like tree, but optimized for science" src="https://github.com/J535D165/scitree/raw/main/scitree_repocard.svg">
</p>

# Scitree - Like `tree`, but optimized for science

![PyPI](https://img.shields.io/pypi/v/scitree) [![DOI](https://zenodo.org/badge/541578065.svg)](https://zenodo.org/badge/latestdoi/541578065)

> In computing, tree is a recursive directory listing command or program that
> produces a depth-indented listing of files. [Wikipedia, 2022](https://en.wikipedia.org/wiki/Tree_(command)).

Scitree is like tree, but different. Instead of sorting content on its name,
scitree sorts and highlights given opiniated scientific principles. In this
way, you can inspect directory listings more easily.

Scitree is based on [scisort](https://github.com/j535d165/scisort), a Python
package to sort file paths based on scientific principles.

## Philosophy

Philosophy of [scisort](https://github.com/j535d165/scisort) and scitree:

- Read the README first, therefore I'm on top
- Before I install or use the content, I open the [LICENSE](https://choosealicense.com/).
- Files first, folders second
- Numbered files are [naturally sorted](https://en.wikipedia.org/wiki/Natural_sort_order)
- I love [intuitive and reproducible project structures](https://doi.org/10.1371/journal.pcbi.1005510)
- Follow the order of execution where possible
- I ignore, what git ignores\*

*\* Only for [`scitree`](https://github.com/J535D165/scitree).*

For more information about the structure, see [scisort/scisort/keygen.py](https://github.com/J535D165/scisort/blob/main/scisort/keygen.py). 

## Installation

Scitree requires Python 3.6 or later.

```sh
pip install scitree
```

## Getting started

### `scitree` command

Scittree command on the command line outputs a tree.
```sh
scitree
```

<!--
cd example/example_makita
scitree

scitree example/example_makita
 -->

```sh
./
├── README.md
├── LICENSE.txt
├── jobs.sh
├── data/
│   └── Bos_2018.csv
├── scripts/
│   ├── get_plot.py
│   ├── merge_descriptives.py
│   └── merge_metrics.py
└── output/
    ├── simulation/
    │   └── Bos_2018/
    │       ├── metrics_sim_Bos_2018_0.json
    │       ├── metrics_sim_Bos_2018_6.json
    │       ├── metrics_sim_Bos_2018_559.json
    │       ├── metrics_sim_Bos_2018_1640.json
    │       ├── metrics_sim_Bos_2018_3154.json
    │       ├── metrics_sim_Bos_2018_3518.json
    │       ├── metrics_sim_Bos_2018_3519.json
    │       ├── metrics_sim_Bos_2018_3721.json
    │       ├── metrics_sim_Bos_2018_4612.json
    │       ├── metrics_sim_Bos_2018_4699.json
    │       ├── metrics_sim_Bos_2018_5673.json
    │       ├── plot_recall_sim_Bos_2018.png
    │       ├── descriptives/
    │       │   ├── wordcloud_Bos_2018.png
    │       │   ├── wordcloud_irrelevant_Bos_2018.png
    │       │   ├── wordcloud_relevant_Bos_2018.png
    │       │   └── data_stats_Bos_2018.json
    │       └── state_files/
    │           ├── sim_Bos_2018_0.asreview
    │           ├── sim_Bos_2018_6.asreview
    │           ├── sim_Bos_2018_559.asreview
    │           ├── sim_Bos_2018_1640.asreview
    │           ├── sim_Bos_2018_3154.asreview
    │           ├── sim_Bos_2018_3518.asreview
    │           ├── sim_Bos_2018_3519.asreview
    │           ├── sim_Bos_2018_3721.asreview
    │           ├── sim_Bos_2018_4612.asreview
    │           ├── sim_Bos_2018_4699.asreview
    │           └── sim_Bos_2018_5673.asreview
    └── tables/
        ├── data_descriptives.csv
        ├── data_descriptives.xlsx
        ├── data_metrics.csv
        └── data_metrics.xlsx

8 directories, 38 files
```


### `scitree` function for Python

The `scitree` function in Python prints the tree for the current folder (`"."`).

```python
from scitree import scitree

scitree()
```


## License

[MIT](/LICENSE)

## Contact

Feel free to reach out with questions, remarks, and suggestions. The
[issue tracker](/issues) is a good starting point. You can also email me at
[jonathandebruinos@gmail.com](mailto:jonathandebruinos@gmail.com).
