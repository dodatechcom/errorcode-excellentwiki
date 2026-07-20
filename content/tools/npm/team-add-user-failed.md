---
title: "[Solution] npm team Add User Failed"
description: "Handle npm team add user failures by verifying team exists, checking user npm account, and confirming your admin permissions on the team."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm team Add User Failed

This guide helps you diagnose and resolve npm team Add User Failed errors encountered when running npm commands.

## Common Causes

- Team does not exist in the organization
- User account does not exist on npm
- You lack admin permissions to add members to the team

## How to Fix

### Verify Team Exists

```bash
npm team ls <org>
```

### Check User Account

```bash
npm owner ls <package>
```

### Add User to Team

```bash
npm team add <org>:<team> <username>
```

## Examples

```bash
# Team does not exist
npm team add myorg:devs user1
# Fix: Create team first
npm team create myorg:devs

# User not on npm
npm team add myorg:devs unknown-user
# Fix: Verify user exists on npm
npm profile get unknown-user

```

## Related Errors

- [Create Failed]({{< relref "/tools/npm/team-create-failed" >}}) -- team creation error
- [Remove User Failed]({{< relref "/tools/npm/team-remove-user-failed" >}}) -- remove user error
