---
title: "[Solution] Poetry PyPI Error - Fix HTTPError 403 Forbidden from PyPI"
description: "Fix Poetry HTTPError 403 Forbidden when installing packages from PyPI. Resolve authentication, proxy, and rate limiting issues."
tools: ["poetry"]
error-types: ["pypi-error"]
severities: ["error"]
weight: 5
---

This error means PyPI rejected your request with a 403 Forbidden status. Poetry cannot download the package because access is denied by the PyPI server.

## What This Error Means

When Poetry tries to install or update packages and receives a 403 response from PyPI, installation stops:

```
HTTPError: 403 Forbidden from https://pypi.org/simple/<package>/
```

A 403 is different from 404 (not found). The server recognized your request but actively refused it. This can be triggered by authentication issues, IP blocking, or PyPI access controls.

## Why It Happens

- Your PyPI token is expired or invalid
- You configured a private repository URL that requires authentication
- PyPI rate-limited your IP due to excessive requests from a CI/CD pipeline
- A corporate proxy is modifying requests in a way PyPI rejects
- The package is private and you have not configured credentials
- You are using a legacy API token instead of a scoped token

## How to Fix It

### Verify your PyPI token

```bash
poetry config pypi-token.pypi pypi-XXXX...
poetry install
```

Generate a new token at https://pypi.org/manage/account/token/ if yours is expired.

### Check repository configuration

```bash
poetry source show
```

Ensure the repository URL is correct and requires valid credentials.

### Configure credentials in pyproject.toml

```toml
[[tool.poetry.source]]
name = "private-pypi"
url = "https://pypi.company.com/simple/"
priority = "supplemental"

[tool.poetry.source.auth]
private-pypi = {username = "__token__", password = "pypi-XXXXX"}
```

### Work around IP rate limiting

```bash
# Wait a few minutes, then retry
poetry install

# Or use a different network
poetry config repositories.pypi https://pypi.org/simple/
```

CI systems with shared IPs often trigger rate limits. Distribute installs across time.

### Use a proxy if corporate firewalls interfere

```bash
export HTTPS_PROXY=http://proxy.company.com:8080
poetry install
```

### Clear cache and retry

```bash
poetry cache clear --all pypi
poetry install
```

Stale cached 403 responses can cause repeated failures even after the issue is resolved.

## Common Mistakes

- Hardcoding PyPI tokens in `pyproject.toml` and committing to version control
- Not rotating API tokens periodically
- Using a global PyPI token instead of a project-scoped token
- Assuming 403 means the package does not exist when it means access is denied
- Not configuring proxy settings for corporate network environments

## Related Pages

- [Poetry Auth Error]({{< relref "/tools/poetry/poetry-auth-error" >}}) -- authentication failures
- [Poetry Source Error]({{< relref "/tools/poetry/poetry-source-error" >}}) -- source repository configuration
- [Poetry Dependency Conflict]({{< relref "/tools/poetry/poetry-dependency-conflict" >}}) -- resolver conflicts
