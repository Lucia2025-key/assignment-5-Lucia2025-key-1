from pathlib import Path
import dendropy
from dendropy.calculate import treecompare

outdir = Path("results/tree_comparison")
outdir.mkdir(parents=True, exist_ok=True)

tree_paths = {
    "E": "results/trees/individual/E.treefile",
    "NS1": "results/trees/individual/NS1.treefile",
    "NS3": "results/trees/individual/NS3.treefile",
    "coalescent": "results/trees/coalescent/species_tree.treefile",
    "concatenated": "results/trees/concatenated/concatenated.treefile",
}

tns = dendropy.TaxonNamespace()
trees = {}

for name, path in tree_paths.items():
    trees[name] = dendropy.Tree.get(
        path=path,
        schema="newick",
        taxon_namespace=tns,
        preserve_underscores=True,
    )
    trees[name].encode_bipartitions()

names = list(trees.keys())

with open(outdir / "robinson_foulds_distances.txt", "w") as fh:
    fh.write("tree1\ttree2\trf_distance\n")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            rf = treecompare.symmetric_difference(trees[names[i]], trees[names[j]])
            fh.write(f"{names[i]}\t{names[j]}\t{rf}\n")

with open(outdir / "topological_summary.txt", "w") as fh:
    fh.write("Topological comparison summary\n")
    fh.write("Robinson-Foulds distances were calculated among individual gene trees, the coalescent species tree, and the concatenated tree.\n")
    fh.write("Lower RF distance indicates greater topological similarity.\n")

with open(outdir / "concordance_analysis.txt", "w") as fh:
    fh.write("Concordance analysis\n")
    fh.write("Gene trees were compared with the coalescent and concatenated species trees.\n")
    fh.write("Discordance may reflect incomplete lineage sorting, missing data, recombination, or locus-specific evolutionary signal.\n")
