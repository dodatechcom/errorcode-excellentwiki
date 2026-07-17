---
title: "GCP Cloud Run: Container Failed to Start"
description: "Cloud Run: Container failed to start — Fix Google Cloud Run startup and deployment errors."
error-types: ["api-error"]
severities: ["error"]
weight: 5
---

The `Container failed to start` error occurs when a Cloud Run service cannot start the user container. This happens during deployment or when Cloud Run attempts to scale up a revision. The container process exits before becoming ready.

## Common Causes

- Container process exits immediately (crash or missing entrypoint)
- Wrong port configuration — Cloud Run expects the container to listen on the port specified by the `PORT` environment variable (8080 by default)
- Container image does not exist or is not accessible
- Resource limits exceeded (OOM killed)

## How to Fix

Check the container logs:

```bash
gcloud logging read "resource.type=cloud_run_revision \
  AND resource.labels.service_name=my-service" \
  --limit=50 --format="json(textPayload,timestamp)"
```

Verify the container runs locally:

```bash
docker run -p 8080:8080 gcr.io/my-project/my-image
```

Check the container configuration:

```bash
gcloud run services describe my-service \
  --region=us-central1 \
  --format="value(spec.template.spec.containers[0].{Ports:ports, Resources:resources, Command:command})"
```

Update the service with correct settings:

```bash
gcloud run deploy my-service \
  --image=gcr.io/my-project/my-image \
  --port=8080 \
  --memory=512Mi \
  --region=us-central1
```

Use the `PORT` environment variable in your application:

```python
import os
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
```

## Examples

- Container exits with code 1 because the application cannot find a required config file
- Container is OOM killed because the default 256Mi memory limit is too low
- Container listens on port 3000 but Cloud Run forwards traffic to port 8080

## Related Errors

- [GCP GKE Error]({{< relref "/cloud/gcp/gke-error" >}}) — GKE cluster issues.
- [GCP Quota Exceeded]({{< relref "/cloud/gcp/quota-exceeded2" >}}) — quota limits.
- [AWS Lambda Error]({{< relref "/cloud/aws/lambda-error" >}}) — AWS Lambda equivalent.
