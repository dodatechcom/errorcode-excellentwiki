---
title: "[Solution] Python ImportError: ollama not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: ollama not found or ModuleNotFoundError: No module named 'ollama'. Install ollama properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "ollama", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: ollama not found — ModuleNotFoundError Fix

An `ImportError: ollama not found` or `ModuleNotFoundError: No module named 'ollama'` means Python cannot locate the ollama package.

## What This Error Means

ollama is a Python client for Ollama (local LLM runner). It is not part of the standard library and must be installed separately.

## Common Causes

```python
# Cause 1: ollama not installed
import ollama  # ModuleNotFoundError: No module named 'ollama'

# Cause 2: Ollama server not running locally
```

## How to Fix

### Fix 1: Install with pip

```bash
pip install ollama
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install ollama
python -c "import ollama; print('OK')"
```

### Fix 3: Ensure Ollama server is running

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start server
ollama serve

# Pull a model
ollama pull llama2
```

## Related Errors

- {{< relref "importerror-openai" >}} — ImportError: openai
- {{< relref "importerror-llama-cpp" >}} — ImportError: llama_cpp
- {{< relref "importerror-vllm" >}} — ImportError: vllm
