---
title: "[Solution] Python ImportError: whisperx not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: whisperx not found or ModuleNotFoundError: No module named 'whisperx'. Install whisperx properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: whisperx not found — ModuleNotFoundError Fix

An `ImportError: whisperx not found` or `ModuleNotFoundError: No module named 'whisperx'` means Python cannot locate the whisperx package.

## What This Error Means

whisperx is an improved version of OpenAI's Whisper with word-level timestamps. It is not part of the standard library.

## Common Causes

```python
# Cause 1: whisperx not installed
import whisperx  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install whisperx
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install whisperx
python -c "import whisperx; print('OK')"
```

## Related Errors

- {{< relref "importerror-whisper" >}} — ImportError: whisper
- {{< relref "importerror-faster-whisper" >}} — ImportError: faster_whisper
- {{< relref "importerror-ctranslate2" >}} — ImportError: ctranslate2
