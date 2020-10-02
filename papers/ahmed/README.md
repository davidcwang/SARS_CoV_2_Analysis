# Paper
[Preliminary Identification of Potential Vaccine Targets for the COVID-19 Coronavirus (SARS-CoV-2) Based on SARS-CoV Immunological Studies](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7150947)

## Paper Code
[Github Repo](https://github.com/faraz107/2019-nCoV-T-Cell-Vaccine-Candidates)

## Insights
1. Protein Sequence Similarity between Sars-CoV-2, Sars-CoV-1, and Mers
   - Similarity between 30-50% Sars-CoV-2 and Mers
   - Similarity between 80-90% Sars-CoV-2 and Sars-Cov-1

2. Found T-Cell, B-Cell and MHC Cell Epitopes

3. Graphical structure of similar residues between Sars-Cov-1 and Sars-Cov-2

## Notes 
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

#### HLA (Human Leukocyte Antigen) Population Allele Analysis
#### Population Coverage Pickle File
MHC Type (String) --> Country (String) --> HLA Type (String) --> (HLA Allele, Population coverage) (Tuple)
#### Data Format
```json
{
   'I': {
      'China': {
         'HLA-A': [
            ('HLA-A*01:01', 0.1009),
            ('HLA-A*01:02', 0.002),
            ('HLA-A*01:03', 0.0005),
            ...
         ],
         'HLA-B': [
            ...
         ]
         ...
      },
      ...
      'Unites State': {
         ...
      }
      ...
      'World': {
         ...
      }
   },
   ...
   'II': {
      ...
   }
   'Combined': {
      ...
   }
}
```

## What I Learned
1. How to align sequences using MAFFT.
2. Sars-Cov-2 Proteins and similarities.
3. ViPR data format.
4. How Epitopes are discovered and ranked using human population coverage.