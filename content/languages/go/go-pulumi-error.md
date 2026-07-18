---
title: "[Solution] Go Pulumi Error — How to Fix"
description: "Fix Go Pulumi errors. Handle program configuration, resource creation, and state management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Pulumi Error

Fix Go Pulumi errors. Handle program configuration, resource creation, and state management.

## Why It Happens

- Pulumi program fails to run because of missing project configuration
- Resource creation fails because of wrong property names
- State backend is not configured causing deployment failures
- Pulumi stack output is not properly exported

## Common Error Messages

```
pulumi: project not found
```
```
pulumi: invalid resource properties
```
```
pulumi: state backend not configured
```
```
pulumi: stack output not found
```

## How to Fix It

### Solution 1: Configure Pulumi project

```yaml
# Pulumi.yaml
name: myproject
type: go
runtime: go
```

### Solution 2: Create resources

```go
import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi-aws/sdk/v5/go/aws/s3"
)
func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
            Bucket: pulumi.String("my-unique-bucket"),
        })
        if err != nil { return err }
        ctx.Export("bucketName", bucket.ID())
        return nil
    })
}
```

### Solution 3: Deploy

```bash
pulumi login s3://my-state-bucket
pulumi stack init dev
pulumi up
```

### Solution 4: Manage state

```bash
pulumi state pull > state.json
pulumi state push state.json
pulumi stack export > stack.json
```

## Common Scenarios

- Pulumi program fails because of missing Go module dependencies
- Resource creation fails because of wrong AWS property names
- State is stored locally instead of in S3

## Prevent It

- Run pulumi up after go mod tidy
- Use Pulumi documentation for correct resource property names
- Configure state backend in Pulumi.yaml or via environment variables
