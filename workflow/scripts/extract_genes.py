from Bio import SeqIO

input_file = snakemake.input[0]

# Approximate mature protein coordinates on DENV polyprotein (1-based inclusive)
# Capsid 1-100, prM 101-267, E 268-762, NS1 763-1114, NS2A 1115-1344,
# NS2B 1345-1474, NS3 1475-2092, NS4A 2093-2241, 2K 2242-2264,
# NS4B 2265-2516, NS5 2517-3410

poly_coords = {
    "E":   (268, 762),
    "NS1": (763, 1114),
    "NS3": (1475, 2092),
    "NS5": (2517, 3410),
}

results = {k: [] for k in poly_coords}

for record in SeqIO.parse(input_file, "genbank"):
    isolate_name = record.id
    found = {k: False for k in poly_coords}

    for feature in record.features:
        if feature.type not in {"CDS", "mat_peptide"}:
            continue

        product = " ".join(feature.qualifiers.get("product", [])).lower()
        gene = " ".join(feature.qualifiers.get("gene", [])).lower()
        note = " ".join(feature.qualifiers.get("note", [])).lower()
        text = f"{product} {gene} {note}"

        seq = feature.extract(record.seq)

        if ("envelope" in text or "protein e" in text) and not found["E"]:
            results["E"].append((isolate_name, str(seq)))
            found["E"] = True

        elif ("ns1" in text or "nonstructural protein 1" in text) and not found["NS1"]:
            results["NS1"].append((isolate_name, str(seq)))
            found["NS1"] = True

        elif ("ns3" in text or "nonstructural protein 3" in text) and not found["NS3"]:
            results["NS3"].append((isolate_name, str(seq)))
            found["NS3"] = True

        elif ("ns5" in text or "nonstructural protein 5" in text) and not found["NS5"]:
            results["NS5"].append((isolate_name, str(seq)))
            found["NS5"] = True

        elif "polyprotein" in text or gene == "poly":
            aa_len = len(seq) // 3
            for target, (aa_start, aa_end) in poly_coords.items():
                if not found[target] and aa_len >= aa_end:
                    nt_start = (aa_start - 1) * 3
                    nt_end = aa_end * 3
                    sub_seq = seq[nt_start:nt_end]
                    results[target].append((isolate_name, str(sub_seq)))
                    found[target] = True

for gene_name, seqs in results.items():
    with open(f"data/{gene_name}.fasta", "w") as out:
        for name, seq in seqs:
            out.write(f">{name}\n{seq}\n")