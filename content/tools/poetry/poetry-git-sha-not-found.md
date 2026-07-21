---
title: "[Solution] Poetry Git SHA Not Found -- Fix Git Reference Resolution"
description: "Fix Poetry git SHA not found errors when a git dependency references a commit that does not exist. Verify the commit hash and repository state."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry tried to check out a specific git commit hash but could not find it in the repository. The reference is invalid or the repository is shallow.

## Common Causes

- The commit hash is truncated or incorrect
- The repository was fetched with --depth 1 (shallow clone)
- The commit was force-pushed away
- The branch containing the commit was deleted

## How to Fix

### 1. Verify the Commit Exists

```bash
git ls-remote https://github.com/user/repo.git | grep abc1234
```

### 2. Fetch Full History

```bash
poetry config installer.parallel false
```

### 3. Use Branch Instead of SHA

```toml
[tool.poetry.dependencies]
mylib = {git = "https://github.com/user/repo.git", branch = "main"}
```

### 4. Use a Tag Instead

```toml
[tool.poetry.dependencies]
mylib = {git = "https://github.com/user/repo.git", tag = "v1.0.0"}
```

## Examples

```bash
$ poetry install
GitError: revision abc1234 not found in repository

$ git ls-remote https://github.com/user/repo.git | grep abc12
abc1234def5678...  refs/heads/main

# Use the correct full SHA:
[tool.poetry.dependencies]
mylib = {git = "https://github.com/user/repo.git", rev = "abc1234def56789012345678901234567890abcd"}
```
