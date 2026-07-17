---
title: "[Solution] Poetry Auth Error — Fix 401 Unauthorized Private Repository Access"
description: "Fix Poetry 401 Unauthorized errors when accessing private PyPI repositories. Configure API tokens, HTTP basic auth, and environment variables correctly."
tools: ["poetry"]
error-types: ["auth-error"]
severities: ["error"]
weight: 5
---

This error means Poetry received a 401 Unauthorized response from a package source. The credentials you provided (or did not provide) are missing, expired, or incorrect.

## What This Error Means

When Poetry tries to download a package from a private source, it sends authentication headers. If the server rejects them, Poetry raises:

```
HTTPError

401 Unauthorized
```

Or:

```
AuthorizationError

Your credentials are incorrect or expired for source "private"
```

This blocks both dependency resolution and package installation.

## Why It Happens

- The API token or password is expired or revoked
- You configured the source URL but never set credentials
- The token has insufficient permissions (read-only vs. read-write)
- Environment variables for credentials are not exported or have wrong names
- The private registry requires a different authentication method (e.g., OIDC, certificate)

## How to Fix It

### Configure Credentials via Poetry Config

```bash
poetry config pypi-token.private your-api-token
```

The token name matches the source name you defined in `pyproject.toml`.

### Use HTTP Basic Auth

```toml
[[tool.poetry.source]]
name = "private"
url = "https://pypi.mycompany.com/simple/"
```

```bash
poetry config http-basic.private username password
```

### Use Environment Variables

```bash
export POETRY_REPOSITORIES_PRIVATE_URL=https://pypi.mycompany.com/simple/
export POETRY_HTTP_BASIC_PRIVATE_USERNAME=deploy-token
export POETRY_HTTP_BASIC_PRIVATE_PASSWORD=gp1234567890abcdef
```

### Verify Your Token Is Valid

Test with curl directly:

```bash
curl -u "token:your-token" https://pypi.mycompany.com/simple/<package-name>/
```

If this also returns 401, regenerate the token on your registry's dashboard.

### Check for Trailing Whitespace in Config

```bash
poetry config --list
```

Look at `http-basic.private` or `pypi-token.private` and make sure there are no extra spaces.

### Use `--no-interaction` in CI with Proper Env Setup

```bash
# In your CI pipeline
export POETRY_HTTP_BASIC_PRIVATE_USERNAME=$REGISTRY_USER
export POETRY_HTTP_BASIC_PRIVATE_PASSWORD=$REGISTRY_TOKEN
poetry install --no-interaction
```

## Common Mistakes

- Setting the token via `poetry config` but forgetting the source name (e.g., `private` vs. `pypi-private`)
- Using a PyPI token with a private registry that does not accept PyPI-style tokens
- Exporting environment variables in a subshell instead of the current shell
- Leaving credentials in `.bashrc` after rotating tokens

## Related Pages

- [Poetry Package Not Found]({{< relref "/tools/poetry/poetry-package-not-found" >}}) -- missing packages
- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file issues
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- install failures
