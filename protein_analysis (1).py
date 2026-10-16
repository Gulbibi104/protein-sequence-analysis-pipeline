import csv
from pathlib import Path
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

INPUT_FILE = Path("proteins.fasta")
OUTPUT_FILE = Path("protein_analysis_results.csv")

VALID_AA = set("ACDEFGHIKLMNPQRSTVWY")


def analyze_proteins():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    results = []

    for record in SeqIO.parse(str(INPUT_FILE), "fasta"):
        sequence = str(record.seq).upper()

        if not sequence:
            print(f"Skipping empty sequence: {record.id}")
            continue

        if not set(sequence).issubset(VALID_AA):
            print(f"Skipping invalid sequence: {record.id}")
            continue

        protein = ProteinAnalysis(sequence)

        results.append({
            "Sequence_ID": record.id,
            "Length_aa": len(sequence),
            "Molecular_Weight_Da": round(
                protein.molecular_weight(), 2
            ),
            "Theoretical_pI": round(
                protein.isoelectric_point(), 2
            ),
            "GRAVY": round(protein.gravy(), 3)
        })

    if not results:
        print("No valid protein sequences found.")
        return

    with OUTPUT_FILE.open("w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=list(results[0].keys())
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"Analysis complete: {len(results)} proteins analyzed.")
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    analyze_proteins()
