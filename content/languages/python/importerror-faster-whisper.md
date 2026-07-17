---
title: "[Solution] Python ImportError: faster_whisper not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: faster_whisper not found or ModuleNotFoundError: No module named 'faster_whisper'. Install faster-whisper properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "faster-whisper", "faster_whisper", "module-not-found", "pip", "speech"]
weight: 5
---

# ImportError: faster_whisper not found — ModuleNotFoundError Fix

An `ImportError: faster_whisper not found` or `ModuleNotFoundError: No module named 'faster_whisper'` means Python cannot locate the faster-whisper package.

## What This Error Means

faster-whisper is a faster implementation of OpenAI's Whisper using CTranslate2. The package is installed as `faster-whisper` but imported as `faster_whisper`.

## Common Causes

```python
# Cause 1: faster-whisper not installed
from faster_whisper import WhisperModel  # ModuleNotFoundError

# Cause 2: Installed wrong package name
pip install faster_whisper  # Wrong! Should be faster-whisper
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install faster-whisper

# NOT: pip install faster_whisper
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install faster-whisper
python -c "from faster_whisper import WhisperModel; print('OK')"
```

## Related Errors

- {{< relref "importerror-whisper" >}} — ImportError: whisper
- {{< relref "importerror-whisperx" >}} — ImportError: whisperx
- {{< relref "importerror-ctranslate2" >}} — ImportError: ctranslate2
