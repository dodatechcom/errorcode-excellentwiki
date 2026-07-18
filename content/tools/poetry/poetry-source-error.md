---
title: "[Solution] Poetry Source Error - Fix Source Repository Not Found"
description: "Fix Poetry source repository not found errors. Configure private repositories, credentials, and source priority for package installation."
tools: ["poetry"]
error-types: ["source-error"]
severities: ["error"]
weight: 5
---

This error means Poetry cannot access or find a configured package source. The repository URL may be wrong, the source may require authentication, or the source name does not match your configuration.

## What This Error Means

When Poetry tries to resolve packages from a configured source and fails, you see:

```
SourceRepositoryNotFoundError: <source-name>
# or
HTTPError: 401 Unauthorized from <url>
# or
InvalidSource: The source <name> is not configured
```

This blocks Poetry from downloading packages from private or custom repositories.

## Why It Happens

- The source URL is incorrect or unreachable
- Authentication credentials are missing or expired
- The source name in `pyproject.toml` does not match what Poetry expects
- The private repository is behind a VPN or firewall
- The source is configured in the wrong priority level
- The repository does not follow the PEP 503 simple repository API format

## How to Fix It

### Check configured sources

```bash
poetry source show
```

This lists all configured sources and their URLs.

### Add or update a source in pyproject.toml

```toml
[[tool.poetry.source]]
name = "private-pypi"
url = "https://pypi.company.com/simple/"
priority = "supplemental"
```

### Configure authentication

```bash
poetry config repositories.private-pypi https://pypi.company.com/simple/
poetry config pypi-token.private-pypi your-token-here
```

Or in `pyproject.toml`:

```toml
[tool.poetry.source.auth]
private-pypi = {username = "__token__", password = "pypi-XXXXX"}
```

### Test the source URL

```bash
curl -I https://pypi.company.com/simple/
```

Verify the URL responds with a 200 status and provides the expected HTML.

### Set the correct priority

```toml
[[tool.poetry.source]]
name = "private-pypi"
url = "https://pypi.company.com/simple/"
priority = "explicit"
```

Use `explicit` if you only want this source used for packages explicitly marked with it.

### Verify the repository serves valid packages

```bash
curl https://pypi.company.com/simple/<package-name>/
```

Ensure the repository actually hosts the packages you need.

## Common Mistakes

- Using the wrong URL format (forgetting `/simple/` at the end)
- Not providing credentials for private repositories
- Mixing source priorities in ways that cause unexpected fallback behavior
- Configuring sources in Poetry config instead of `pyproject.toml` for team projects
- Not testing source connectivity before running `poetry install`

## Related Pages

- [Poetry PyPI Error]({{< relref "/tools/poetry/poetry-pypi-error" >}}) -- PyPI access issues
- [Poetry Auth Error]({{< relref "/tools/poetry/poetry-auth-error" >}}) -- authentication failures
- [Poetry Package Not Found]({{< relref "/tools/poetry/poetry-package-not-found" >}}) -- missing packages
