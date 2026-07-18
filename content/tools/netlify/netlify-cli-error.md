---
title: "[Solution] Netlify CLI Error — Fix CLI Authentication or Deploy Error"
description: "Fix Netlify CLI errors when authentication fails or CLI commands do not execute properly. Re-authenticate, update the CLI, and resolve configuration issues."
tools: ["netlify"]
error-types: ["cli-error"]
severities: ["error"]
weight: 5
---

A Netlify CLI error occurs when the Netlify CLI cannot authenticate, deploy, or execute commands. The CLI is the primary tool for local development and deployment management.

## What This Error Means

The Netlify CLI requires authentication and proper configuration. When it fails:

```
Error: Not authenticated. Run `netlify login` to authenticate.
```

Or:

```
Error: Could not find site "my-site". Run `netlify sites:create` to create a new site.
```

## Why It Happens

- The CLI is not authenticated with Netlify
- The authentication token has expired or was revoked
- The CLI version is outdated and incompatible with the API
- The project is not linked to a Netlify site
- The netlify.toml configuration has errors
- The CLI cannot find the deploy directory
- The API rate limit is exceeded
- The `.netlify/state.json` file is corrupted

## How to Fix It

### Authenticate the CLI

```bash
netlify login
```

### Use a Personal Access Token

```bash
# Generate token at: https://app.netlify.com/user/applications
export NETLIFY_AUTH_TOKEN=your-token-here
netlify deploy
```

### Update the CLI

```bash
npm install -g netlify-cli@latest
```

### Link the Project to a Netlify Site

```bash
netlify link
# Or:
netlify sites:create
```

### Check CLI Version

```bash
netlify version
```

### Clear CLI Cache

```bash
rm -rf .netlify
netlify init
```

### Check netlify.toml

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

### Redeploy after Re-authentication

```bash
netlify logout
netlify login
netlify deploy --prod
```

## Common Mistakes

- Not running `netlify login` before using CLI commands
- Using an expired personal access token without refreshing
- Forgetting to link the local project to a Netlify site
- Running outdated CLI versions with new API changes
- Not checking `netlify status` to verify authentication state

## Related Pages

- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Plugin Error]({{< relref "/tools/netlify/netlify-plugin-error" >}}) -- Plugin issues
