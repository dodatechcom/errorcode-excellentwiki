---
title: "[Solution] Python ImportError: text-generation-inference not found — ModuleNotFoundError Fix"
description: "Fix Python ImportError: text-generation-inference not found. Install TGI properly."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["importerror", "tgi", "text-generation-inference", "module-not-found", "pip", "llm"]
weight: 5
---

# ImportError: text-generation-inference not found — ModuleNotFoundError Fix

This error occurs when trying to use Hugging Face Text Generation Inference (TGI) but it is not installed or configured.

## What This Error Means

TGI is a Rust-based inference server. It is typically deployed as a Docker container rather than installed as a Python package.

## Common Causes

```python
# Cause 1: TGI client not installed
# Cause 2: TGI server not running
# Cause 3: Using wrong client library
```

## How to Fix

### Fix 1: Run TGI as Docker container

```bash
docker run --gpus all --shm-size 1g \
  -p 8080:80 \
  -v /data:/data \
  ghcr.io/huggingface/text-generation-inference:latest \
  --model-id bigscience/bloom
```

### Fix 2: Use the client library

```bash
pip install text-generation
```

### Fix 3: Use with requests

```python
import requests

response = requests.post(
    "http://localhost:8080/generate",
    json={"inputs": "Hello, world!"}
)
print(response.json())
```

## Related Errors

- {{< relref "importerror-vllm" >}} — ImportError: vllm
- {{< relref "importerror-transformers" >}} — ImportError: transformers
- {{< relref "importerror-ollama" >}} — ImportError: ollama
