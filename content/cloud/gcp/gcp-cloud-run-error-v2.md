---
title: "[Solution] GCP Cloud Run — container failed to start"
description: "Fix Cloud Run container failed to start. Resolve container startup and runtime errors."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Cloud Run container failed to start error means the container image could not be started or failed during the startup phase. The revision is not receiving traffic and the service is degraded.

## What This Error Means

Cloud Run starts your container and listens on the port specified by the `PORT` environment variable (default 8080). The container must start a process that listens on this port within the startup CPU boost period. If the process crashes, exits, or never binds to the port, Cloud Run marks the revision as failed and routes traffic away from it. Common causes include missing binary, wrong port, OOM during startup, or dependency failures.

## Common Causes

- Application not listening on the correct port (must use `$PORT`)
- Container process crashes on startup
- Insufficient memory allocated to the container
- Missing or broken dependencies in the container image
- Entrypoint or CMD in Dockerfile is incorrect
- Application requires environment variables not configured
- Container exceeds startup CPU or time limits

## How to Fix

### Check Revision Logs

```bash
gcloud run services describe my-service --region us-central1
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=my-service" --limit=50
```

### Verify Container Port

```bash
# Ensure app listens on $PORT
# Cloud Run sets PORT env var (default 8080)
PORT=${PORT:-8080}
```

### Test Container Locally

```bash
docker run -p 8080:8080 gcr.io/my-project/my-image
docker run -e PORT=8080 -p 8080:8080 gcr.io/my-project/my-image
```

### Increase Memory

```bash
gcloud run services update my-service \
  --memory 1Gi \
  --region us-central1
```

### Fix Dockerfile

```dockerfile
FROM gcr.io/distroless/base-debian12

COPY --from=builder /app/server /server
EXPOSE 8080
CMD ["/server"]
```

### Set Startup CPU Boost

```bash
gcloud run services update my-service \
  --cpu-boost \
  --region us-central1
```

### Check Container Startup Time

```bash
# Ensure startup completes within the timeout
# Cloud Run gives ~10 seconds for HTTP health check to respond
gcloud logging read "resource.type=cloud_run_revision AND jsonPayload.status=Failed" --limit=10
```

### Verify Service Account

```bash
gcloud run services describe my-service \
  --region us-central1 \
  --query='spec.template.spec.serviceAccountName'
```

## Related Errors

- [GCP Cloud Functions Error]({{< relref "/cloud/gcp/gcp-cloud-functions-error-v2" >}}) — deployment error
- [AWS ECS Error]({{< relref "/cloud/aws/aws-ecs-error-v2" >}}) — CannotPullContainerError
- [Azure App Service Error]({{< relref "/cloud/azure/azure-app-service-error-v2" >}}) — 503 Service Unavailable
