---
title: "GCP Quota Exceeded"
description: "QuotaExceeded - Quota exceeded for the given resource"
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
tags: ["gcp", "quota", "limit", "resources", "compute"]
weight: 5
---

The `QuotaExceeded` error occurs when a Google Cloud project exceeds its allocated quota for a specific resource (e.g., CPUs, IPs, or API requests per minute).

## Common Causes

- The project has reached the default quota for the resource type
- A burst of activity consumed the remaining quota
- Free tier limits have been exceeded
- The quota was recently reduced by Google Cloud

## How to Fix

Check current quotas:

```bash
gcloud compute project-info describe --project=my-project
```

List per-resource quotas:

```bash
gcloud compute regions describe us-central1 --project=my-project
```

Request a quota increase via the console or:

```bash
gcloud beta services quotas list --service=compute.googleapis.com
```

## Examples

- Attempting to allocate a 100th external IP address when the project limit is 100
- Creating more GPU instances than the region quota allows
- Exceeding the daily API request limit for a Cloud Functions trigger

## Related Errors

- [GCP Permission Denied]({{< relref "/cloud/gcp/permission-denied" >}})
- [AWS EC2 Instance Limit Exceeded]({{< relref "/cloud/aws/ec2-instance-limit" >}})
- [Azure Resource Not Found]({{< relref "/cloud/azure/resource-not-found" >}})
