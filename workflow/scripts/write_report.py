
from pathlib import Path
import pandas as pd

outdir = Path("results/report")
outdir.mkdir(parents=True, exist_ok=True)

stats = pd.read_csv("results/alignment_stats/summary_report.txt", sep="\t")
rf = pd.read_csv("results/tree_comparison/robinson_foulds_distances.txt", sep="\t")

report = outdir / "phylogenetic_analysis_report.md"

with open(report, "w") as fh:
    fh.write("# Phylogenetic Analysis Report\n\n")
    fh.write("## Dataset\n")
    fh.write("This analysis used three loci (E, NS1, NS3) across 13 taxa in a Snakemake workflow.\n\n")

    fh.write("## Alignment Summary\n")
    fh.write(stats.to_markdown(index=False))
    fh.write("\n\n")

    fh.write("## Phylogenetic Approaches\n")
    fh.write("- **Coalescent approach:** individual gene trees were inferred and combined with ASTRAL.\n")
    fh.write("- **Supermatrix approach:** trimmed alignments were concatenated and analyzed with partitioned IQ-TREE.\n\n")

    fh.write("## Tree Comparison\n")
    fh.write(rf.to_markdown(index=False))
    fh.write("\n\n")

    fh.write("## Interpretation\n")
    fh.write("The concatenated analysis provides a single partitioned maximum-likelihood estimate from the combined signal of all loci.\n")
    fh.write("The coalescent analysis accounts for possible discordance among gene trees and is often preferred when incomplete lineage sorting is a concern.\n")
    fh.write("Any disagreement between gene trees and species trees may reflect locus-specific evolutionary history, missing data, or limited phylogenetic signal.\n\n")

    fh.write("## Final Recommendation\n")
    fh.write("Both approaches should be reported. If the gene trees show notable discordance, the coalescent tree is often the more cautious species-level interpretation. If discordance is low and support is strong, the concatenated tree may provide a clearer overall phylogenetic estimate.\n")
