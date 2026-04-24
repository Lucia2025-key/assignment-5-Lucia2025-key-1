
from pathlib import Path
from Bio import AlignIO
import csv

GENES = ["E", "NS1", "NS3"]
outdir = Path("results/alignment_stats")
outdir.mkdir(parents=True, exist_ok=True)

summary_rows = []

for gene in GENES:
    aln_path = Path(f"results/alignments/trimmed/{gene}.trimmed.fasta")
    aln = AlignIO.read(aln_path, "fasta")

    n_taxa = len(aln)
    aln_len = aln.get_alignment_length()

    variable_sites = 0
    gap_chars = set("-?Nn")
    total_cells = n_taxa * aln_len
    gap_count = 0

    for i in range(aln_len):
        col = [record.seq[i] for record in aln]
        nongap = [str(x).upper() for x in col if str(x) not in gap_chars]
        gap_count += sum(1 for x in col if str(x) in gap_chars)
        if len(set(nongap)) > 1:
            variable_sites += 1

    gap_fraction = gap_count / total_cells if total_cells else 0.0

    txt = outdir / f"{gene}_stats.txt"
    with open(txt, "w") as fh:
        fh.write(f"Gene: {gene}\n")
        fh.write(f"Taxa: {n_taxa}\n")
        fh.write(f"Alignment_length: {aln_len}\n")
        fh.write(f"Variable_sites: {variable_sites}\n")
        fh.write(f"Gap_fraction: {gap_fraction:.4f}\n")

summary_rows.append({
        "gene": gene,
        "taxa": n_taxa,
        "alignment_length": aln_len,
        "variable_sites": variable_sites,
        "gap_fraction": round(gap_fraction, 4),
    })

summary_file = outdir / "summary_report.txt"
with open(summary_file, "w", newline="") as fh:
    writer = csv.DictWriter(
        fh,
        fieldnames=["gene", "taxa", "alignment_length", "variable_sites", "gap_fraction"],
        delimiter="\t",
    )
    writer.writeheader()
    writer.writerows(summary_rows)
