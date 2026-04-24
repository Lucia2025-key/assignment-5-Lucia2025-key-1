from pathlib import Path
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from Bio import Phylo

treefile = Path(sys.argv[1])
outfile = Path(sys.argv[2])
title = sys.argv[3]

outfile.parent.mkdir(parents=True, exist_ok=True)

tree = Phylo.read(str(treefile), "newick")

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(1, 1, 1)

Phylo.draw(tree, axes=ax, do_show=False)
ax.set_title(title)
ax.set_xlabel("Branch length")

plt.tight_layout()
plt.savefig(str(outfile), dpi=300, bbox_inches="tight")
plt.close()