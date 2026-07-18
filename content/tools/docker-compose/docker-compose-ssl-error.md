---
title: "[Solution] Docker Compose SSL Error — Fix SSL Certificate Problem"
description: "Fix Docker Compose SSL errors when TLS certificate verification fails. Resolve expired certificates, self-signed certs, and registry certificate issues."
---

## What This Error Means

Docker Compose SSL errors occur when TLS certificate verification fails during communication between services, with registries, or with external APIs.

A typical error:

```
Error: SSL: CERTIFICATE_VERIFY_FAILED certificate verify failed
```

Or:

```
error: Invalid SSL certificate for registry.example.com
```

## Why It Happens

SSL errors happen when:

- **Certificate is expired**: The SSL certificate has passed its expiration date.
- **Self-signed certificate**: Using a self-signed cert that is not trusted by the container.
- **Hostname mismatch**: The certificate CN or SAN does not match the hostname.
- **Internal CA not trusted**: The container lacks the internal CA certificate bundle.
- **Date/time incorrect**: The container's clock is out of sync with the certificate's validity period.
- **Registry certificate issue**: Docker registry has an invalid or untrusted certificate.

## How to Fix It

**Step 1: Test SSL from inside the container**

```bash
docker compose exec <service> openssl s_client -connect example.com:443
```

**Step 2: Sync container time**

```yaml
services:
  app:
    image: my-app
    volumes:
      - /etc/localtime:/etc/localtime:ro
    environment:
      - TZ=UTC
```

**Step 3: Add custom CA certificates**

```yaml
services:
  app:
    image: my-app
    volumes:
      - ./certs/ca.crt:/usr/local/share/ca-certificates/ca.crt
    command: update-ca-certificates && <your-command>
```

**Step 4: Configure insecure registries**

```yaml
services:
  app:
    image: my-app
    dns:
      - 8.8.8.8
```

For the Docker daemon:

```json
{
  "insecure-registries": ["registry.example.com:5000"]
}
```

**Step 5: Use environment variables to skip SSL verification**

```yaml
services:
  app:
    image: my-app
    environment:
      - NODE_TLS_REJECT_UNAUTHORIZED=0
      - CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

## Common Mistakes

- **Disabling SSL verification permanently with env vars**: Only disable for development; always fix the root CA issue.
- **Not updating the CA certificates bundle**: CA bundles go out of date; run `update-ca-certificates`.
- **Ignoring the container time sync**: A wrong system clock causes SSL certificate validity failures.
- **Using expired certificates in CI/CD**: Rotate certificates before they expire.

## Related Pages

- [Docker Compose Network Error](/tools/docker-compose/docker-compose-network-error/) -- Network issues
- [Docker Compose Build Error](/tools/docker-compose/docker-compose-build-error/) -- Build failures
- [Docker Compose Secrets Error](/tools/docker-compose/docker-compose-secrets-error/) -- Secrets issues
