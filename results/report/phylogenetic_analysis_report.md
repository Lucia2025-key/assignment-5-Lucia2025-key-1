# Phylogenetic Analysis Report

## Dataset
This analysis used three loci (E, NS1, NS3) across 13 taxa in a Snakemake workflow.

## Alignment Summary
| gene   |   taxa |   alignment_length |   variable_sites |   gap_fraction |
|:-------|-------:|-------------------:|-----------------:|---------------:|
| NS3    |      9 |               1854 |              331 |              0 |

## Phylogenetic Approaches
- **Coalescent approach:** individual gene trees were inferred and combined with ASTRAL.
- **Supermatrix approach:** trimmed alignments were concatenated and analyzed with partitioned IQ-TREE.

## Tree Comparison
| tree1      | tree2        |   rf_distance |
|:-----------|:-------------|--------------:|
| E          | NS1          |            16 |
| E          | NS3          |            10 |
| E          | coalescent   |             0 |
| E          | concatenated |            14 |
| NS1        | NS3          |            14 |
| NS1        | coalescent   |            16 |
| NS1        | concatenated |            14 |
| NS3        | coalescent   |            10 |
| NS3        | concatenated |            16 |
| coalescent | concatenated |            14 |

## Interpretation
The concatenated analysis provides a single partitioned maximum-likelihood estimate from the combined signal of all loci.
The coalescent analysis accounts for possible discordance among gene trees and is often preferred when incomplete lineage sorting is a concern.
Any disagreement between gene trees and species trees may reflect locus-specific evolutionary history, missing data, or limited phylogenetic signal.

## Final Recommendation
Both approaches should be reported. If the gene trees show notable discordance, the coalescent tree is often the more cautious species-level interpretation. If discordance is low and support is strong, the concatenated tree may provide a clearer overall phylogenetic estimate.
