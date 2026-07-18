---
title: "[Solution] Python BioPython Sequence Analysis Error — How to Fix"
description: "Fix Python BioPython sequence analysis errors. Resolve FASTA parsing, sequence alignment, and GenBank format errors."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python BioPython Sequence Analysis Error

A `Bio.SeqIO.ParseError` or `Bio.Alphabet.HasAlphabet` occurs when BioPython fails to parse sequence files, encounters invalid nucleotide characters, or when sequence operations are applied to incompatible sequence types.

## Why It Happens

BioPython provides biological sequence analysis tools. Errors arise when FASTA/GenBank files have malformed headers, when sequences contain invalid IUPAC characters, when sequence IDs are duplicated, or when alphabet validation fails on raw sequences.

## Common Error Messages

- `Bio.SeqIO.ParseError: Expected FASTA record at line 1`
- `Bio.Alphabet.HasAlphabet: Sequence has no alphabet`
- `ValueError: sequences must all be the same length`
- `KeyError: Sequence ID not found`

## How to Fix It

### Fix 1: Parse FASTA files correctly

```python
from Bio import SeqIO

# Wrong — assuming file format
# records = list(SeqIO.parse("data.fasta", "genbank"))

# Correct — specify correct format
records = list(SeqIO.parse("sequences.fasta", "fasta"))
print(f"Parsed {len(records)} sequences")

for record in records:
    print(f"ID: {record.id}, Length: {len(record.seq)}")
```

### Fix 2: Handle invalid characters

```python
from Bio.Seq import Seq

# Wrong — sequence with invalid characters
# seq = Seq("ATCGX")  # X is not valid IUPAC

# Correct — validate and clean sequences
def clean_sequence(raw_seq):
    valid_chars = set("ATCGNUWSMKRYBDHVatcgnuwsmkrybdhv")
    cleaned = "".join(c for c in raw_seq if c in valid_chars)
    return Seq(cleaned.upper())

raw = "ATCGNXATCG"
cleaned = clean_sequence(raw)
print(f"Cleaned: {cleaned}")
```

### Fix 3: Align sequences properly

```python
from Bio import Align
from Bio.Seq import Seq

aligner = Align.PairwiseAligner()
aligner.mode = "global"

seq1 = Seq("ACGTACGT")
seq2 = Seq("ACGACGT")

# Wrong — sequences of different lengths
# alignments = aligner.align(seq1, Seq("ACGTA"))

# Correct — align with proper parameters
alignments = aligner.align(seq1, seq2)
best = alignments[0]
print(f"Score: {best.score}")
print(best)
```

### Fix 4: Write sequence files

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Wrong — missing required attributes
# record = SeqRecord(Seq("ATCG"))

# Correct — provide complete record
record = SeqRecord(
    Seq("ATCGATCGATCG"),
    id="seq001",
    name="gene_A",
    description="Example gene sequence",
    annotations={"molecule_type": "DNA"},
)

SeqIO.write(record, "output.fasta", "fasta")
print("Written to output.fasta")
```

## Common Scenarios

- **Wrong format specified** — Trying to parse a GenBank file as FASTA or vice versa.
- **Invalid characters** — Sequences containing characters not in the IUPAC alphabet.
- **Duplicate IDs** — Multiple sequences with the same ID cause issues during alignment.

## Prevent It

- Always specify the correct format (`"fasta"`, `"genbank"`, `"fastq"`) when calling `SeqIO.parse()`.
- Clean sequences by removing non-IUPAC characters before analysis.
- Use unique sequence IDs to avoid conflicts during alignment and comparison.

## Related Errors

- [ParseError](/languages/python/parse-error/) — sequence file format error
- [ValueError](/languages/python/valueerror/) — invalid sequence characters
- [KeyError](/languages/python/keyerror/) — sequence ID not found
