---
title: "GCP Firebase: Project Not Found / Quota Exceeded"
description: "Firebase: Project not found / quota exceeded — Fix Firebase project and quota errors."
cloud: ["gcp"]
error-types: ["api-error"]
severities: ["error"]
tags: ["gcp", "firebase", "project", "not-found", "quota", "authentication", "api-key"]
weight: 5
---

Firebase errors include `project not found` (the Firebase project does not exist or is inaccessible) and `quota exceeded` (the project has exceeded Firebase or GCP API limits). These are among the most common Firebase SDK and CLI errors.

## Common Causes

- `Project not found`: wrong project ID in `firebase.json` or app configuration
- `Project not found`: the Firebase project was deleted or the API key is invalid
- `Quota exceeded`: too many Firestore reads/writes or Auth operations per day
- `Quota exceeded`: Firebase free tier limits reached (Spark plan)
- The app is registered to a different Firebase project

## How to Fix

Check the Firebase project configuration:

```bash
# List Firebase projects
firebase projects:list

# Check the active project
firebase use
```

Set the correct project:

```bash
firebase use my-project-id
```

Check quota usage:

```bash
# Check Firestore usage
firebase firestore:usage --project my-project-id

# Check Auth usage
gcloud billing budgets list --project=my-project-id
```

Upgrade from the free tier:

```bash
gcloud billing accounts list
gcloud billing projects link my-project-id --billing-account=012345-6789AB-CDEF01
```

Verify the app is registered to the correct project:

```bash
# For Android
google-services.json → project_id field

# For iOS
GoogleService-Info.plist → PROJECT_ID field

# For web
firebaseConfig.js → projectId field
```

## Examples

- `Firebase: project-not-found` because `firebase.json` has `my-project` but the actual project is `my-project-abc123`
- Firestore reads per day exceed the 50,000 free tier limit — upgrade to Blaze plan
- Firebase Auth daily SMS quota exceeded — enable billing or use email/password auth

## Related Errors

- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied10" >}}) — general permission errors.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — GCP quota limits.
- [AWS Throttling]({{< relref "/cloud/aws/throttling" >}}) — API throttling.
