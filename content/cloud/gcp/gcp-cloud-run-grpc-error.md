---
title: "[Solution] GCP Cloud Run gRPC Error"
description: "Fix Cloud Run gRPC errors. Resolve gRPC connection, protocol, and load balancing issues when using gRPC with Google Cloud Run."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Run gRPC Error

The Cloud Run gRPC error occurs when gRPC services deployed on Cloud Run fail to establish connections or communicate with clients.

## Common Causes

- gRPC server does not listen on the correct PORT environment variable
- Cloud Run ingress settings block gRPC traffic
- HTTP/2 end-to-end is not enabled for the service
- gRPC health check is not configured
- Load balancer does not support gRPC protocol

## How to Fix

### 1. Enable HTTP/2 end-to-end
```bash
gcloud run deploy SERVICE_NAME \
  --image=gcr.io/PROJECT_ID/IMAGE \
  --use-http2 \
  --region=REGION
```

### 2. Configure gRPC server to use PORT
```go
port := os.Getenv("PORT")
if port == "" {
    port = "8080"
}
lis, err := net.Listen("tcp", ":"+port)
```

### 3. Add ingress settings
```bash
gcloud run deploy SERVICE_NAME \
  --ingress=internal-and-cloud-load-balancing \
  --region=REGION
```

### 4. Check gRPC health check
```bash
gcloud run services describe SERVICE_NAME \
  --region=REGION \
  --format="yaml(spec.template.spec.containers[0].livenessProbe)"
```

## Examples

### Go gRPC server for Cloud Run
```go
func main() {
    port := os.Getenv("PORT")
    lis, _ := net.Listen("tcp", ":"+port)
    s := grpc.NewServer()
    pb.RegisterMyServiceServer(s, &server{})
    go func() {
        if err := s.Serve(lis); err != nil {
            log.Fatalf("failed to serve: %v", err)
        }
    }()
    healthpb.RegisterHealthServer(s, health.NewServer())
}
```

### Test gRPC connectivity
```bash
grpcurl -plaintext SERVICE_URL:443 grpc.health.v1.Health/Check
```

## Related Errors

- [GCP Cloud Run Error]({{< relref "/cloud/gcp/gcp-cloud-run-error" >}})
- [GCP Cloud Run Service]({{< relref "/cloud/gcp/gcp-cloud-run-service" >}})
