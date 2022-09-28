[![scitree_repocard.png](https://github.com/J535D165/scitree/raw/main/scitree_repocard.png)](github.com/j535d165/scitree)

# Scitree - Like tree, but optimized for science

> In computing, tree is a recursive directory listing command or program that
> produces a depth-indented listing of files. [Wikipedia, 2022](https://en.wikipedia.org/wiki/Tree_(command)).

Scitree is like tree, but different. Instead of sorting content on its name,
scitree sorts and highlights given opiniated scientific principles. In this
way, you can inspect directory listings more easily.

## The zen of scisort

Scitree is based on [scisort](https://github.com/j535d165/scisort), a Python
package to sort file paths based on scientific principles.

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
example_makita/
├── README.md
├── LICENSE.txt
├── data/
│   └── Bos_2018.csv
├── scripts/
│   ├── get_plot.py
│   ├── merge_descriptives.py
│   └── merge_metrics.py
├── output/
│   ├── simulation/
│   │   └── Bos_2018/
│   │       ├── descriptives/
│   │       │   ├── data_stats_Bos_2018.json
│   │       │   ├── wordcloud_Bos_2018.png
│   │       │   ├── wordcloud_irrelevant_Bos_2018.png
│   │       │   └── wordcloud_relevant_Bos_2018.png
│   │       ├── metrics_sim_Bos_2018_0.json
│   │       ├── metrics_sim_Bos_2018_6.json
│   │       ├── metrics_sim_Bos_2018_559.json
│   │       ├── metrics_sim_Bos_2018_1640.json
│   │       ├── metrics_sim_Bos_2018_3154.json
│   │       ├── metrics_sim_Bos_2018_3518.json
│   │       ├── metrics_sim_Bos_2018_3519.json
│   │       ├── metrics_sim_Bos_2018_3721.json
│   │       ├── metrics_sim_Bos_2018_4612.json
│   │       ├── metrics_sim_Bos_2018_4699.json
│   │       ├── metrics_sim_Bos_2018_5673.json
│   │       ├── plot_recall_sim_Bos_2018.png
│   │       └── state_files/
│   │           ├── sim_Bos_2018_0.asreview
│   │           ├── sim_Bos_2018_6.asreview
│   │           ├── sim_Bos_2018_559.asreview
│   │           ├── sim_Bos_2018_1640.asreview
│   │           ├── sim_Bos_2018_3154.asreview
│   │           ├── sim_Bos_2018_3518.asreview
│   │           ├── sim_Bos_2018_3519.asreview
│   │           ├── sim_Bos_2018_3721.asreview
│   │           ├── sim_Bos_2018_4612.asreview
│   │           ├── sim_Bos_2018_4699.asreview
│   │           └── sim_Bos_2018_5673.asreview
│   └── tables/
│       ├── data_descriptives.csv
│       ├── data_descriptives.xlsx
│       ├── data_metrics.csv
│       └── data_metrics.xlsx
└── jobs.sh
```

### Other examples

10.5281/zenodo.4161444


### `scitree` function for Python

The `scitree` function in Python prints the tree.

```sh
from scitree import scitree

scitree(".")
```

<!--
cd example/example_makita
scitree

scitree example/example_makita
 -->


## License

[MIT](/LICENSE)

## Contact

Scitree is developed and maintained by Jonathan de Bruin ([jonathandebruinos@gmail.com](email:jonathandebruinos@gmail.com)).
