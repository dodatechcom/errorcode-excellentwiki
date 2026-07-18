---
title: "[Solution] Go Buf Error — How to Fix"
description: "Fix Go Buf errors. Handle protobuf linting, breaking change detection, and code generation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Buf Error

Fix Go Buf errors. Handle protobuf linting, breaking change detection, and code generation.

## Why It Happens

- Buf lint rules fail because proto files do not follow style guide
- Breaking change detector flags changes that are intentional
- Buf generate produces wrong output because of configuration errors
- Proto dependencies are not properly resolved

## Common Error Messages

```
buf: lint failure
```
```
buf: breaking change detected
```
```
buf: module not found
```
```
buf: invalid configuration
```

## How to Fix It

### Solution 1: Configure Buf

```yaml
# buf.yaml
version: v2
lint:
  use:
    - STANDARD
breaking:
  use:
    - FILE
modules:
  - path: proto
    name: buf.build/myorg/myapi
```

### Solution 2: Run Buf lint

```bash
buf lint
# Fix specific file
buf lint --error-format=json proto/api/v1/service.proto
```

### Solution 3: Check breaking changes

```bash
buf breaking --against '.git#branch=main'
```

### Solution 4: Generate code with Buf

```yaml
# buf.gen.yaml
version: v2
plugins:
  - remote: buf.build/protocolbuffers/go
    out: gen/go
    opt: paths=source_relative
  - remote: buf.build/grpc/go
    out: gen/go
    opt: paths=source_relative
```

```bash
buf generate
```

## Common Scenarios

- Buf lint fails because proto files do not follow naming conventions
- Breaking change detector flags field renames
- Buf generate produces empty output because of wrong configuration

## Prevent It

- Run buf lint before committing proto changes
- Use buf generate to generate code consistently
- Configure breaking change detection for your branching strategy
