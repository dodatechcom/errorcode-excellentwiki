---
title: "[Solution] Poetry Export Error - Fix poetry export to requirements.txt Failed"
description: "Fix Poetry export failures when generating requirements.txt files. Resolve format issues, dependency conflicts, and export command errors."
tools: ["poetry"]
error-types: ["export-error"]
severities: ["error"]
weight: 5
---

This error means `poetry export` failed to generate a requirements file from your lock file. The export process encountered incompatible dependencies, missing lock data, or unsupported options.

## What This Error Means

When you run `poetry export -f requirements.txt` and the command fails, you see:

```
ExportError: Unable to export lock file
# or
ValueError: ...
# or PoetryException: ...
```

The export command reads `poetry.lock` and converts it into a pip-compatible format. Failures indicate the lock file is incomplete, corrupted, or contains dependency types that cannot be exported.

## Why It Happens

- `poetry.lock` does not exist or is out of sync with `pyproject.toml`
- The lock file contains git or path dependencies that export cannot represent
- The export plugin is not installed (required in Poetry 1.2+)
- You specified a format that does not support all dependency types
- Optional dependencies or extras are not included in the export
- The lock file was generated with a different Poetry version

## How to Fix It

### Install the export plugin

```bash
poetry self add poetry-plugin-export
```

The export functionality is a plugin since Poetry 1.2 and must be installed separately.

### Regenerate the lock file

```bash
poetry lock
poetry export -f requirements.txt -o requirements.txt
```

A fresh lock file resolves inconsistencies.

### Export only non-git dependencies

```bash
poetry export -f requirements.txt --without-hashes
```

The `--without-hashes` flag can work around some export incompatibilities.

### Export with all extras

```bash
poetry export -f requirements.txt --extras "all" --all-groups
```

This includes optional dependencies that might be missing from the default export.

### Handle git dependencies manually

```bash
poetry export -f requirements.txt > requirements.txt
echo "git+https://github.com/user/repo.git@main#egg=git-dep" >> requirements.txt
```

Append git dependencies that export cannot represent.

### Check export plugin version

```bash
poetry show poetry-plugin-export
```

Ensure you are running the latest version of the plugin.

## Common Mistakes

- Forgetting to install the export plugin after upgrading Poetry
- Not regenerating `poetry.lock` after modifying dependencies
- Assuming export handles all dependency types including git and path
- Running export without `--without-hashes` when hashes cause compatibility issues
- Not testing the exported requirements file with `pip install -r requirements.txt`

## Related Pages

- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file problems
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- installation failures
- [Poetry Git Dependency]({{< relref "/tools/poetry/poetry-git-dependency" >}}) -- git dependency issues
