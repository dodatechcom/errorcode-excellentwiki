---
title: "[Solution] Grafana Team Error"
description: "Fix Grafana team errors. Learn why this happens and how to resolve it quickly."
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Grafana Team Error

Grafana team errors occur when team management, permissions, or syncing fails.

## Why This Happens

- Team not found
- Member not added
- Permission denied
- LDAP sync failed

## Common Error Messages

- `team_not_found_error`
- `team_member_error`
- `team_permission_error`
- `team_sync_error`

## How to Fix It

### Solution 1: Check teams

List teams:

```bash
curl -H "Authorization: Bearer $API_KEY" http://grafana:3000/api/teams/search
```

### Solution 2: Add members

Add team members:

```bash
curl -X POST http://grafana:3000/api/teams/1/members -d '{"userId":2}'
```

### Solution 3: Fix LDAP sync

Check LDAP team sync configuration.


## Common Scenarios

- **Team not found:** Check the team ID or name.
- **Permission denied:** Verify team admin permissions.

## Prevent It

- Use teams for access control
- Sync with LDAP
- Monitor team activity
