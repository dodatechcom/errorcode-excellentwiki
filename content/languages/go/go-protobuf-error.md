---
title: "[Solution] protobuf Marshal Error Fix"
description: "Fix Go protobuf marshal errors. Handle required fields, type mismatches, and encoding issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# protobuf Marshal Error

Protocol Buffers marshaling fails in Go when message fields have wrong types, required fields are missing in proto3 (which does not have required, but oneof or wrapper types may fail), the message is nil, or the generated code is out of sync with the `.proto` file. Protobuf encoding is compact but strict about schema compliance.

## Common Causes

```go
// Cause 1: Nil message pointer
msg := (*pb.User)(nil)
data, err := proto.Marshal(msg)
// panic: runtime error: invalid memory address

// Cause 2: Field type mismatch
msg := &pb.User{Name: 123} // Name is string, got int
data, err := proto.Marshal(msg)

// Cause 3: Generated code out of sync with proto file
// Proto file changed but go_out not re-generated
msg := &pb.User{Email: "a@b.com"}
// unknown field "email" — generated code does not have this field

// Cause 4: Oneof field not set
msg := &pb.Event{} // no payload set
// proto.Marshal works, but downstream may fail on empty oneof

// Cause 5: Large message exceeds gRPC max message size
data, err := proto.Marshal(largeMsg)
// grpc: received message larger than max (4194304 vs. 2097152)
```

## How to Fix

### Fix 1: Validate messages before marshaling

```go
import (
    "fmt"

    "google.golang.org/protobuf/proto"
)

func safeMarshal(msg proto.Message) ([]byte, error) {
    if msg == nil {
        return nil, fmt.Errorf("cannot marshal nil message")
    }

    if err := proto.Validate(msg); err != nil {
        return nil, fmt.Errorf("validation failed: %w", err)
    }

    data, err := proto.Marshal(msg)
    if err != nil {
        return nil, fmt.Errorf("marshal failed: %w", err)
    }
    return data, nil
}
```

### Fix 2: Regenerate protobuf code after proto changes

```bash
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    myproto.proto
```

### Fix 3: Increase gRPC max message size

```go
import "google.golang.org/grpc"

server := grpc.NewServer(
    grpc.MaxRecvMsgSize(16 * 1024 * 1024), // 16MB
    grpc.MaxSendMsgSize(16 * 1024 * 1024),
)
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "google.golang.org/protobuf/proto"
    pb "your-project/proto"
)

func main() {
    msg := &pb.User{
        Name:  "Alice",
        Email: "alice@example.com",
        Age:   30,
    }

    data, err := proto.Marshal(msg)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Marshaled %d bytes\n", len(data))

    // Unmarshal
    decoded := &pb.User{}
    if err := proto.Unmarshal(data, decoded); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Decoded: %+v\n", decoded)
}
```

## Related Errors

- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON marshaling has similar nil/type issues
- [encoding-binary]({{< relref "/languages/go/go-binary-error" >}}) — binary encoding with endianness issues
- [go-grpc-gateway-error]({{< relref "/languages/go/go-grpc-gateway-error" >}}) — gRPC-gateway transcode fails on protobuf messages
