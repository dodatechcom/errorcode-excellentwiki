---
title: "[Solution] Go Go-Zero RPC Error — How to Fix"
description: "Fix Go Go-Zero gRPC service errors. Handle proto definition, RPC handler, and service deployment."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Go-Zero RPC Error

Fix Go Go-Zero gRPC service errors. Handle proto definition, RPC handler, and service deployment.

## Why It Happens

- Proto definition has errors causing gRPC code generation failures
- RPC service is not properly registered with the gRPC server
- Client cannot connect because of wrong endpoint configuration

## Common Error Messages

```
go-zero: proto generation failed
```
```
go-zero: rpc service not found
```
```
go-zero: client connection refused
```
```
go-zero: invalid proto syntax
```

## How to Fix It

### Solution 1: Define proto service

```protobuf
syntax = "proto3";
package product;
option go_package = "product";

service ProductService {
  rpc GetProduct (GetProductRequest) returns (GetProductResponse);
  rpc ListProducts (ListProductsRequest) returns (ListProductsResponse);
}

message GetProductRequest {
  int64 id = 1;
}
message GetProductResponse {
  int64 id = 1;
  string name = 2;
}
```

### Solution 2: Implement RPC handler

```go
type ProductRpc struct {
    pb.UnimplementedProductServiceServer
}
func (s *ProductRpc) GetProduct(ctx context.Context, req *pb.GetProductRequest) (*pb.GetProductResponse, error) {
    return &pb.GetProductResponse{Id: req.Id, Name: "Widget"}, nil
}
```

### Solution 3: Configure and run RPC service

```yaml
Name: product-rpc
ListenOn: 0.0.0.0:8081
Etcd:
  Hosts:
    - etcd:2379
  Key: product.rpc
```

### Solution 4: Generate RPC code

```bash
goctl rpc go -proto product.proto -go_out ./product-rpc
goctl rpc template -type product -go_out ./product-rpc
```

## Common Scenarios

- Proto definition syntax error causes code generation to fail
- RPC handler is not registered with the gRPC server
- Client cannot connect because etcd is not running

## Prevent It

- Validate proto files before generating code
- Register RPC handlers in the server initialization
- Ensure etcd is running and accessible for service discovery
