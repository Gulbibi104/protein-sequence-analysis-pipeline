# Python-Based Protein Sequence Analysis Pipeline

## Project Overview
This project implements a simple bioinformatics pipeline
for analyzing protein sequences in FASTA format using Python
and Biopython.

## Objectives
- Read protein sequences from a FASTA file.
- Validate sequences against the 20 standard amino acids.
- Calculate protein sequence length.
- Estimate molecular weight and theoretical isoelectric point.
- Calculate GRAVY (grand average of hydropathicity).
- Export results to a CSV file.

## Requirements
- Python 3
- Biopython
- Pandas (for displaying results in a notebook)

## How to Run
1. Install Biopython:
   pip install biopython
2. Place your input file at proteins.fasta.
3. Run protein_analysis.py.
4. Inspect protein_analysis_results.csv.

## Input
A FASTA file containing protein amino acid sequences.

## Output
A CSV file containing the sequence identifier, length,
estimated molecular weight, theoretical pI, and GRAVY score.

## Limitations
This pipeline calculates sequence-derived properties only.
It does not predict protein function, immunogenicity, or
experimental solubility. Sequences containing non-standard
amino acid symbols are skipped by the current implementation.

## Testing
The initial demonstration uses illustrative sequences
to test the software workflow. Biological analyses should
use documented protein sequences from traceable sources.
