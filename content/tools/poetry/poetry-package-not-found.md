---
title: "[Solution] Poetry Package Not Found — Fix Missing PyPI Package Errors"
description: "Fix Poetry package not found errors when a dependency is unavailable in PyPI or private repos. Configure package sources and authentication correctly."
tools: ["poetry"]
error-types: ["not-found-error"]
severities: ["error"]
weight: 5
---

This error means Poetry searched all configured package sources and could not find a package matching the name and version you requested.

## What This Error Means

Poetry queries PyPI (and any private sources you configured) to resolve dependencies. When a package name is not found on any source, you get:

```
PackageNotFoundError

Package [package-name] not found.
```

Or during resolution:

```
SolverProblemError

No package found matching [package-name]
```

## Why It Happens

- The package name has a typo or uses the wrong casing
- The package was renamed on PyPI and the old name is a redirect that Poetry does not follow
- The package is private and you have not configured the source in `pyproject.toml`
- The package exists but not for your Python version or platform
- You are using a private PyPI server that does not mirror the package

## How to Fix It

### Search PyPI for the Correct Name

```bash
poetry search <partial-name>
```

Or visit `https://pypi.org/search/?q=<partial-name>` in a browser.

### Add a Private Source

```toml
[[tool.poetry.source]]
name = "private"
url = "https://pypi.mycompany.com/simple/"
priority = "supplemental"
```

Then reinstall:

```bash
poetry lock
poetry install
```

### Authenticate to a Private Source

```bash
poetry config pypi-token.private your-api-token
```

Or use environment variables:

```bash
export POETRY_REPOSITORIES_PRIVATE_URL=https://pypi.mycompany.com/simple/
export POETRY_HTTP_BASIC_PRIVATE_USERNAME=user
export POETRY_HTTP_BASIC_PRIVATE_PASSWORD=token
```

### Check for PyPI Name Normalization

PyPI normalizes package names (lowercase, hyphens to underscores). Verify the canonical name:

```bash
pip index versions <package-name>
```

### Use the Git Source for Renamed Packages

If the package moved to a new repo:

```toml
[tool.poetry.dependencies]
new-package-name = {git = "https://github.com/org/new-package.git"}
```

## Common Mistakes

- Not adding the private source to `pyproject.toml` before running `poetry add`
- Using environment variable names with incorrect casing
- Forgetting to run `poetry lock` after adding a new source
- Assuming Poetry checks all sources by default (it may skip non-primary sources)
- Using the wrong PyPI mirror URL format (needs `/simple/` at the end)

## Related Pages

- [Poetry Auth Error]({{< relref "/tools/poetry/poetry-auth-error" >}}) -- authentication failures for private repos
- [Poetry Dependency Conflict]({{< relref "/tools/poetry/poetry-dependency-conflict" >}}) -- resolver conflicts
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- install failures
