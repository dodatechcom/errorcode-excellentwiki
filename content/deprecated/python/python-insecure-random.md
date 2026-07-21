---
title: "[Solution] Deprecated Function Migration: random module to secrets for security"
description: "Migrate from deprecated random module to secrets for cryptographically secure random numbers in Python."
deprecated_function: "random.random()"
replacement_function: "secrets.token_hex()"
languages: ["python"]
deprecated_since: "Python 3.6+"
---

# [Solution] Deprecated Function Migration: random module to secrets for security

The `random.random()` has been deprecated in favor of `secrets.token_hex()`.

## Migration Guide

The random module is not cryptographically secure. Use secrets for security-sensitive random values.

## Before (Deprecated)

```python
import random

token = random.randint(0, 1000000)
password = "".join(random.choice("abcdef0123456789") for _ in range(16))
```

## After (Modern)

```python
import secrets

token = secrets.randbelow(1000000)
password = secrets.token_hex(8)
api_key = secrets.token_urlsafe(32)
```

## Key Differences

- Use secrets for tokens, passwords, security
- Use random for simulations and games
- secrets uses OS-provided CSPRNG
