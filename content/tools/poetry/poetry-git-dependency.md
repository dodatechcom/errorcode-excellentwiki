---
title: "[Solution] Poetry Git Dependency Error - Fix Git Dependency Resolution Failed"
description: "Fix Poetry git dependency resolution failures. Resolve branch, tag, and commit issues when installing packages from git repositories."
tools: ["poetry"]
error-types: ["git-dependency"]
severities: ["error"]
weight: 5
---

This error means Poetry could not install a package from a git repository. The git clone, checkout, or build process failed during dependency resolution.

## What This Error Means

When you declare a git dependency in `pyproject.toml` and Poetry cannot retrieve or build it, you see:

```
GitError: Failed to install dependencies from git repository
# or
error: pathspec 'branch-name' did not match any files
# or
CloneError: Could not clone https://github.com/...
```

This prevents Poetry from resolving your full dependency tree and blocks installation.

## Why It Happens

- The specified branch, tag, or commit does not exist in the repository
- The repository requires SSH keys that are not configured in your environment
- The git repository URL is incorrect or the repository is private
- The package has a `pyproject.toml` or `setup.py` that Poetry cannot parse
- Git is not installed or the git version is too old
- A submodule is required but not initialized

## How to Fix It

### Verify the branch, tag, or commit exists

```bash
git ls-remote https://github.com/user/repo.git refs/heads/main refs/tags/v1.0
```

Confirm the ref you specified actually exists in the remote repository.

### Use SSH for private repositories

```toml
[tool.poetry.dependencies]
my-package = {git = "git@github.com:user/repo.git", branch = "main"}
```

Ensure your SSH key is added to the agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### Specify a tag or commit explicitly

```toml
[tool.poetry.dependencies]
my-package = {git = "https://github.com/user/repo.git", tag = "v1.2.3"}
```

Using a stable tag avoids issues with branch deletion or renaming.

### Install git submodules

```bash
git submodule update --init --recursive
poetry install
```

Some packages require submodules that must be initialized before building.

### Update git and retry

```bash
git --version
poetry lock
poetry install
```

Outdated git versions may fail with newer repository features.

### Use source code archives as an alternative

```toml
[tool.poetry.dependencies]
my-package = {url = "https://github.com/user/repo/archive/main.zip"}
```

Downloading an archive avoids git authentication issues entirely.

## Common Mistakes

- Forgetting that `branch` is the default and omitting it uses HEAD
- Not adding SSH keys to the agent for private repositories
- Referencing a branch that was deleted or renamed after the lock file was created
- Assuming Poetry handles submodules automatically
- Using HTTPS URLs for private repos when SSH is required

## Related Pages

- [Poetry Dependency Conflict]({{< relref "/tools/poetry/poetry-dependency-conflict" >}}) -- dependency resolution failures
- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file issues
- [Poetry Source Error]({{< relref "/tools/poetry/poetry-source-error" >}}) -- repository source configuration
