---
title: "[Solution] Netlify CMS Error — Fix CMS Authentication Failed"
description: "Fix Netlify CMS authentication errors when the content management system cannot connect to Git. Resolve OAuth configuration, token issues, and API access problems."
tools: ["netlify"]
error-types: ["cms-error"]
severities: ["error"]
weight: 5
---

A Netlify CMS authentication error occurs when the CMS cannot authenticate with the Git provider. The CMS UI shows a login error or fails to load content collections.

## What This Error Means

Netlify CMS (Decap CMS) connects to GitHub, GitLab, or Bitbucket to manage content. When authentication fails:

```
Error: Authentication failed
Failed to get token from https://api.netlify.com/auth
```

## Why It Happens

- The OAuth app is not configured correctly in the Git provider
- The Netlify OAuth integration is not properly set up
- The user has not logged in or the session expired
- The Git provider API rate limits are exceeded
- The repository permissions do not include content storage
- The config.yml has incorrect backend settings
- The site is not connected to the correct Git repository

## How to Fix It

### Check CMS Configuration

```yaml
# admin/config.yml
backend:
  name: git-gateway
  branch: main
  # Or for GitHub:
  # name: github
  # repo: owner/repo
  # branch: main
```

### Set Up Netlify OAuth

Go to Netlify Dashboard > Site > Settings > Access > OAuth and verify the OAuth provider is configured.

### Check Git Provider OAuth App

```bash
# GitHub: Settings > Developer settings > OAuth Apps
# Ensure the callback URL is https://api.netlify.com/auth
```

### Re-authenticate CMS

Navigate to `/admin/index.html` and log in again.

### Check Git Gateway

```bash
# Verify Git Gateway is enabled
# Netlify Dashboard > Site > Settings > Identity > Git Gateway
```

### Clear Browser Cache

Clear browser cookies and local storage for the CMS domain, then reload.

### Verify Repository Permissions

Ensure the OAuth token has access to the correct repository.

## Common Mistakes

- Using GitHub OAuth when the site is connected via Git Gateway
- Not configuring the Netlify Identity service alongside the CMS
- Forgetting to enable Git Gateway in the Netlify dashboard
- Pointing config.yml to a repository that does not exist
- Using an expired OAuth token without regenerating it

## Related Pages

- [Netlify Identity Error]({{< relref "/tools/netlify/netlify-identity-error" >}}) -- Identity issues
- [Netlify Build Error]({{< relref "/tools/netlify/netlify-build-error" >}}) -- Build failures
- [Netlify Deploy Error]({{< relref "/tools/netlify/netlify-deploy-error" >}}) -- Deploy failures
