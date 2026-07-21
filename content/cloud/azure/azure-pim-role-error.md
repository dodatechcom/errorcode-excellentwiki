---
title: "[Solution] Azure PIM Role Activation Error"
description: "Fix Azure Privileged Identity Management role activation failures for just-in-time access."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

PIM role activation errors prevent users from requesting time-limited elevated access. This blocks emergency access to critical resources.

## Common Causes

- User does not have an eligible role assignment in PIM
- MFA was not completed during the activation request
- Activation request exceeded the maximum allowed duration
- Approval workflow is enabled and the approver has not responded

## How to Fix

### Check PIM eligible assignments

```bash
az rest --method GET \
  --uri "https://graph.microsoft.com/v1.0/privilegedAccess/aadRoles/roleAssignments?$filter=assignmentState eq 'Eligible'"
```

### Request role activation

```bash
az rest --method POST \
  --uri "https://graph.microsoft.com/v1.0/privilegedAccess/aadRoles/roleAssignmentScheduleRequests" \
  --body '{
    "action": "selfActivate",
    "principalId": "userId",
    "roleDefinitionId": "roleId",
    "directoryScopeId": "/",
    "justification": "Need access for production deployment",
    "scheduleInfo": {
      "startDateTime": "2026-01-01T10:00:00Z",
      "expiration": {
        "type": "AfterDuration",
        "duration": "PT4H"
      }
    }
  }'
```

### Check pending approvals

```bash
az rest --method GET \
  --uri "https://graph.microsoft.com/v1.0/privilegedAccess/aadRoles/roleAssignmentScheduleRequests?$filter=requestType eq 'AdminUpdate' and status eq 'Pending'"
```

## Examples

- Activation request is rejected because the user has not completed MFA registration
- PIM approval is pending for 48 hours because the designated approver is unavailable
- Role activation fails with `PrerequisiteValidationFailed` because the user is not in the eligible list

## Related Errors

- [Azure PIM Activation]({{< relref "/cloud/azure/azure-pim-activation" >}}) -- PIM activation issues.
- [Azure RBAC Error]({{< relref "/cloud/azure/azure-rbac-error" >}}) -- RBAC issues.
