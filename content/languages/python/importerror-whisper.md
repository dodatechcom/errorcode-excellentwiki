---
title: "[Solution] Python ImportError: whisper not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: whisper not found or ModuleNotFoundError: No module named 'whisper'. Install openai-whisper properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ImportError: whisper not found — ModuleNotFoundError Fix

An `ImportError: whisper not found` or `ModuleNotFoundError: No module named 'whisper'` means Python cannot locate the whisper package.

## What This Error Means

whisper is OpenAI's speech recognition model. The package is installed as `openai-whisper` but imported as `whisper`.

## Common Causes

```python
# Cause 1: whisper not installed
import whisper  # ModuleNotFoundError: No module named 'whisper'

# Cause 2: Installed wrong package name
pip install whisper  # Wrong! Should be openai-whisper
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install openai-whisper

# NOT: pip install whisper
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install openai-whisper
python -c "import whisper; print(whisper.__version__)"
```

## Related Errors

- {{< relref "importerror-whisperx" >}} — ImportError: whisperx
- {{< relref "importerror-faster-whisper" >}} — ImportError: faster_whisper
- {{< relref "importerror-ctranslate2" >}} — ImportError: ctranslate2
