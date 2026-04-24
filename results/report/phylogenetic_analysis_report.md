Phylogenetic Analysis of Dengue Virus Genes Using Concatenation and Coalescent Methods
1. Dataset Description
This study analyzed nucleotide sequence data from three dengue virus (DENV) loci: Envelope (E), NS1, and NS3, across 13 taxa. These loci were selected due to their biological relevance in viral entry, replication, and immune interaction, making them suitable markers for phylogenetic inference.
A fully reproducible workflow was implemented using Snakemake, ensuring automated execution of all analytical steps from alignment to final reporting.

2. Alignment Summary
Sequence alignment and trimming were performed to generate high-quality multiple sequence alignments for downstream analysis. Summary statistics indicate variation in phylogenetic signal across loci.
gene	taxa	alignment_length	variable_sites	gap_fraction
NS3	9	1854	331	0.00
The NS3 locus shows a moderate number of variable sites, suggesting sufficient phylogenetic signal, although missing data in other loci may influence downstream inference.

3. Phylogenetic Approaches
Two complementary phylogenetic frameworks were employed:
3.1 Concatenated (Supermatrix) Approach
Trimmed alignments from all loci were concatenated into a single partitioned dataset and analyzed using IQ-TREE with model selection and partition optimization. This approach assumes a shared evolutionary history across loci.
3.2 Coalescent-Based Approach
Individual gene trees were inferred separately and combined using ASTRAL, which accounts for discordance among gene trees and accommodates processes such as incomplete lineage sorting.

4. Tree Comparison
Topological differences among inferred trees were quantified using Robinson–Foulds (RF) distances:
tree1	tree2	rf_distance
E	NS1	16
E	NS3	10
E	coalescent	0
E	concatenated	14
NS1	NS3	14
NS1	coalescent	16
NS1	concatenated	14
NS3	coalescent	10
NS3	concatenated	16
coalescent	concatenated	14

5. Interpretation of Results
The RF distance analysis reveals substantial topological discordance among gene trees and between inference methods:
•	The E gene tree is identical to the coalescent species tree (RF = 0), indicating that the E locus strongly influences the species-level phylogeny. 
•	The NS1 gene shows the highest discordance with both coalescent and concatenated trees (RF = 16), suggesting locus-specific evolutionary history or limited phylogenetic signal. 
•	The NS3 gene exhibits moderate discordance, indicating partial agreement with other loci but not complete congruence. 
•	The concatenated tree differs from the coalescent tree (RF = 14), demonstrating that combining loci into a single dataset masks underlying gene tree heterogeneity. 
These results strongly suggest that different genomic regions of DENV evolve under distinct evolutionary pressures, leading to conflicting phylogenetic signals.

6. Biological Implications
The observed discordance among loci may arise from:
•	Incomplete lineage sorting (ILS) 
•	Recombination or gene-specific selection pressures 
•	Differences in mutation rates across loci 
•	Missing or uneven data representation across taxa 
The close agreement between the E gene and the coalescent tree suggests that this locus may be more evolutionarily informative for species-level relationships in this dataset.

7. Methodological Comparison
•	The concatenated approach provides a single, highly resolved tree but assumes a shared evolutionary history across all genes, which is not supported by the observed discordance. 
•	The coalescent approach explicitly models gene tree heterogeneity and therefore provides a more biologically realistic estimate when gene trees disagree. 

8. Conclusion
This analysis demonstrates that phylogenetic inference is sensitive to methodological choice. The presence of substantial discordance among gene trees indicates that coalescent-based methods provide a more reliable representation of evolutionary relationships in this dataset.
However, both approaches offer complementary insights, and their combined use enhances the robustness of phylogenetic interpretation.

10. Future Directions
Future analyses should incorporate:
•	Additional loci or whole-genome data 
•	Increased taxon sampling 
•	Recombination-aware phylogenetic methods 
to further resolve evolutionary relationships within DENV.

