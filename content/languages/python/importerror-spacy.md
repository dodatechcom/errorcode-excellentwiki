---
title: "[Solution] Python ImportError: spacy not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: spacy not found or ModuleNotFoundError: No module named 'spacy'. Install spaCy properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "spacy", "module-not-found", "pip", "nlp"]
weight: 5
---

# ImportError: spacy not found — ModuleNotFoundError Fix

An `ImportError: spacy not found` or `ModuleNotFoundError: No module named 'spacy'` means Python cannot locate the spaCy package.

## What This Error Means

spaCy is a natural language processing library. It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: spacy not installed
import spacy  # ModuleNotFoundError: No module named 'spacy'

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install spacy

# Download a language model
python -m spacy download en_core_web_sm
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install spacy
python -c "import spacy; print(spacy.__version__)"
```

## Related Errors

- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-numpy" >}} — ImportError: numpy
- {{< relref "importerror-torch" >}} — ImportError: torch
