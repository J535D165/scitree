from scitree import scitree_keygen

tree = ["data", "README.md", "scripts", "installation.R", "requirements.txt", "tests"]

tree_expected = [
    "README.md",
    "installation.R",
    "requirements.txt",
    "data",
    "scripts",
    "tests",
]


def test_keygen():

    assert sorted(tree, key=scitree_keygen()) == tree_expected