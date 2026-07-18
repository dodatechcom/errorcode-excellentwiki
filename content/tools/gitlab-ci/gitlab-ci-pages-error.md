---
title: "[Solution] GitLab CI Pages Error"
description: "Fix GitLab CI pages errors. Learn why this happens and how to resolve it quickly."
tools: ["gitlab-ci"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# GitLab CI Pages Error

Pages errors occur when GitLab Pages deployment fails to publish static sites.

## Why This Happens

- Job name not pages
- Public/ missing from artifacts
- Custom domain not configured
- SSL certificate invalid

## Common Error Messages

- `pages_deployment_failed`
- `pages_artifact_error`
- `pages_domain_error`
- `pages_ssl_error`

## How to Fix It

### Solution 1: Use pages job name

The job must be named exactly `pages`:

```yaml
pages:
  stage: deploy
  script:
    - mkdir -p public
    - cp -r dist/* public/
  artifacts:
    paths:
      - public
```

### Solution 2: Configure custom domains

Set up in Settings > Pages > Domains. Add DNS CNAME record pointing to your Pages URL.

### Solution 3: Fix SSL certificates

GitLab Pages provides automatic SSL. Ensure your domain DNS is configured correctly.


## Common Scenarios

- **Stuck in pending:** Job name must be exactly `pages`.
- **Site not accessible:** Verify the public/ directory is in artifacts.

## Prevent It

- Use exact job name
- Include public/ in artifacts
- Configure domains
