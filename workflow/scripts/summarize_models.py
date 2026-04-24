from pathlib import Path

input_files = snakemake.input
output_file = snakemake.output[0]

with open(output_file, "w") as out:
    out.write("Gene\tBest_Model\n")
    for f in input_files:
        gene = Path(f).name.replace(".model.iqtree", "")
        best_model = "NOT_FOUND"

        with open(f) as fh:
            for line in fh:
                if "Best-fit model according to" in line or "Best-fit model:" in line:
                    parts = line.strip().split(":")
                    if len(parts) > 1:
                        best_model = parts[-1].strip()
                        break

        out.write(f"{gene}\t{best_model}\n")
