---
title: "[Solution] Python ImportError: ctranslate2 not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: ctranslate2 not found or ModuleNotFoundError: No module named 'ctranslate2'. Install ctranslate2 properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: ctranslate2 not found — ModuleNotFoundError Fix

An `ImportError: ctranslate2 not found` or `ModuleNotFoundError: No module named 'ctranslate2'` means Python cannot locate the ctranslate2 package.

## What This Error Means

ctranslate2 is a C++/Python library for efficient inference of Transformer models. It is not part of the standard library.

## Common Causes

```python
# Cause 1: ctranslate2 not installed
import ctranslate2  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install ctranslate2
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install ctranslate2
python -c "import ctranslate2; print(ctranslate2.__version__)"
```

## Related Errors

- {{< relref "importerror-whisper" >}} — ImportError: whisper
- {{< relref "importerror-whisperx" >}} — ImportError: whisperx
- {{< relref "importerror-faster-whisper" >}} — ImportError: faster_whisper
