### Goal
Better understand Sars-Cov-2

### Background
- [Genes Breakdown](https://www.biosyn.com/tew/Structure-of-Coronavirus-nCoV-2019-2020.aspx)
- [RNA Strucural Diagrams](https://www.news-medical.net/news/20200702/Structure-of-the-full-SARS-CoV-2-RNA-genome-in-infected-cells.aspx)

### Papers
- [Proximal Origin](https://www.nature.com/articles/s41591-020-0820-9?fbclid=IwAR1Nj6E-XsU_N6IrFN1m9gCT-Q7app0iO2eUpN5x7OSi-l_q6c1LBx8-N24)
- [Computational Analysis of non-ideal binding with ACE2](https://jvi.asm.org/content/94/7/e00127-20)
- [Diagnosis and Treatment Methods](https://www.sciencedirect.com/science/article/pii/S1286457920300253?via%3Dihub)
- [Genetic Diversity](https://www.sciencedirect.com/science/article/pii/S1567134820300915#s0005)

### Insights


### Graphs


### Troubleshooting
- Got the following error when using consurf:

```
The uploaded MSA file, which appears to be in clustalw format, contains non-standard characters: "J". 
To fix the format please replace all non-standard characters with standard characters
(gaps : "-" Amino Acids : "A" , "C" , "D" .. "Y") and resubmit your query.
```


This is because we have a 'J' amino acid in on line 998 in our clustalo.clustal_num multi alignment file

`ATG84853.1          GTPNEKLVTTSTAPDFVAFNVFQGIETAVGHYVHARLKGGJILKFDSGTVSKTSDWKCKV	1788'`

Apparently a 'J' is supposed to indicate either 'I' or 'L'.
We will replace with an 'L' in this case because ABN10847.1 and AVP25405.1 have 'L's in that position
which is the majority.


### Protocols
#### Steps for Quering ViPR
1. Go to the [ViPR Immune Epitope Search](https://www.viprbrc.org/brc/vipr_virusEpitope_search.spg?method=ShowCleanSearch&type=curated&decorator=corona)

2. Use the following values in the corresponding fields 
   1. Species: "Severe acute respiratory syndrome-related coronavirus"
   2. Host: "human"

3. Check the "Positive" checkbox for the following Assay Results:
   1. B-Cell
   2. T-Cell
   3. MHC

Search Result returned 1,394 epitopes.