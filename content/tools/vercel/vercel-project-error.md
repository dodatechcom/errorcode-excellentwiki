---
title: "[Solution] Vercel Project Not Found Error — Fix Project Configuration"
description: "Fix Vercel project not found errors. Resolve project lookup failures, linking issues, and team permission problems."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
weight: 10
---

A Vercel project not found error occurs when Vercel cannot locate the project you are trying to deploy, link, or manage. This can happen due to linking issues, team membership problems, or incorrect project names.

## What This Error Means

```
Error: Project not found
The specified project does not exist or you do not have access.
```

This means the project ID or name you referenced does not exist in the current Vercel scope, or you lack permission to access it.

## Why It Happens

- The project was deleted from Vercel
- You are not logged in to the correct Vercel account
- The project belongs to a different team
- The `.vercel` directory is corrupted or outdated
- The project name was changed
- You do not have access to the team that owns the project

## How to Fix It

### Check Login Status

```bash
# Check current user
vercel whoami

# Login if needed
vercel login

# Switch teams if needed
vercel switch
```

### Re-link Project

```bash
# Remove old link
rm -rf .vercel

# Re-link the project
vercel link

# Follow prompts to select team and project
```

### List Available Projects

```bash
# List all projects in current team
vercel project ls

# Or via API
curl -X GET "https://api.vercel.com/v9/projects" \
  -H "Authorization: Bearer YOUR_TOKEN" | jq '.projects[].name'
```

### Check Team Membership

```bash
# Check team membership
vercel teams ls

# Request access if needed
# Ask team owner to add you in Dashboard > Team Settings
```

### Verify Project Name

```bash
# If using project name in commands
vercel deploy --name my-project

# The name must match exactly (case-sensitive)
# Check in Dashboard > Project Settings
```

### Fix Corrupted .vercel Directory

```bash
# The .vercel directory stores project linking info
# Delete and re-create it

rm -rf .vercel
vercel link --yes
```

### Set Up CI/CD with Token

```bash
# For CI/CD, use the Vercel Token
# or Vercel GitHub Integration

# In GitHub Actions
- name: Deploy to Vercel
  uses: amondnet/vercel-action@v25
  with:
    vercel-token: ${{ secrets.VERCEL_TOKEN }}
    vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
    vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

## Common Mistakes

- Running `vercel deploy` from a directory not linked to a project
- Having multiple Vercel accounts and being logged into the wrong one
- Not having the correct team selected in multi-team setups
- Forgetting to add team members when collaborating
- Using the wrong project name in CLI commands

## Related Pages

- [Vercel Deploy Error]({{< relref "/tools/vercel/vercel-deploy-error" >}}) — Deployment failed
- [Vercel Domain Error]({{< relref "/tools/vercel/vercel-domain-error" >}}) — Domain configuration failed
