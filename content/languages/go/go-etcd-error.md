---
title: "[Solution] etcd Connection Timeout Fix"
description: "Fix etcd connection timeout errors. Handle cluster connectivity, leader election, and watch operations."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# etcd Connection Timeout

The `go.etcd.io/etcd/client/v3` package fails to connect to the etcd cluster due to wrong endpoints, network issues, TLS misconfiguration, or cluster health problems. etcd uses gRPC internally, so connection errors surface as gRPC status codes or context deadline exceeded.

## Common Causes

```go
// Cause 1: Wrong endpoint or etcd not running
cli, err := clientv3.New(clientv3.Config{
    Endpoints:   []string{"localhost:2379"},
    DialTimeout: 5 * time.Second,
})
// context deadline exceeded

// Cause 2: TLS required but not configured
cli, err := clientv3.New(clientv3.Config{
    Endpoints: []string{"etcd1:2379"},
    // missing TLS config — server requires mTLS
})

// Cause 3: Authentication enabled but credentials missing
cli, err := clientv3.New(clientv3.Config{
    Endpoints: []string{"etcd1:2379"},
    Username:  "",
    Password:  "",
})
// auth: user name is empty

// Cause 4: Cluster not healthy — no leader elected
// etcd cluster with 3 nodes, only 1 alive
// cannot健康check

// Cause 5: KeepAlive channel not consumed — connection leaks
ch, _ := cli.KeepAlive(ctx, leaseID)
// not reading from ch causes buffer overflow
```

## How to Fix

### Fix 1: Configure client with proper timeouts and TLS

```go
import (
    "context"
    "crypto/tls"
    "crypto/x509"
    "fmt"
    "io/ioutil"
    "time"

    clientv3 "go.etcd.io/etcd/client/v3"
)

func newEtcdClient() (*clientv3.Client, error) {
    cert, _ := tls.LoadX509KeyPair("client.crt", "client.key")
    caCert, _ := ioutil.ReadFile("ca.crt")
    caPool := x509.NewCertPool()
    caPool.AppendCertsFromPEM(caCert)

    cli, err := clientv3.New(clientv3.Config{
        Endpoints:   []string{"etcd1:2379", "etcd2:2379", "etcd3:2379"},
        DialTimeout: 5 * time.Second,
        TLS: &tls.Config{
            Certificates: []tls.Certificate{cert},
            RootCAs:      caPool,
        },
    })
    if err != nil {
        return nil, fmt.Errorf("etcd connect: %w", err)
    }
    return cli, nil
}
```

### Fix 2: Handle lease keepalive properly

```go
func keepAlive(ctx context.Context, cli *clientv3.Client, leaseID clientv3.LeaseID) {
    ch, err := cli.KeepAlive(ctx, leaseID)
    if err != nil {
        log.Printf("keepalive error: %v", err)
        return
    }

    for {
        select {
        case <-ctx.Done():
            return
        case resp, ok := <-ch:
            if !ok {
                log.Println("keepalive channel closed")
                return
            }
            if resp != nil {
                // keepalive acknowledged
            }
        }
    }
}
```

### Fix 3: Use endpoints from discovery or environment

```go
import "os"

func getEndpoints() []string {
    endpoints := os.Getenv("ETCD_ENDPOINTS")
    if endpoints == "" {
        return []string{"http://127.0.0.1:2379"}
    }
    return strings.Split(endpoints, ",")
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"
    "time"

    clientv3 "go.etcd.io/etcd/client/v3"
)

func main() {
    cli, err := clientv3.New(clientv3.Config{
        Endpoints:   []string{"localhost:2379"},
        DialTimeout: 5 * time.Second,
    })
    if err != nil {
        log.Fatal(err)
    }
    defer cli.Close()

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()

    _, err = cli.Put(ctx, "greeting", "hello etcd")
    if err != nil {
        log.Fatal(err)
    }

    resp, err := cli.Get(ctx, "greeting")
    if err != nil {
        log.Fatal(err)
    }
    for _, kv := range resp.Kvs {
        fmt.Printf("%s = %s\n", kv.Key, kv.Value)
    }
}
```

## Related Errors

- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — gRPC transport layer failure
- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — dial timeout exceeded
- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS negotiation with etcd fails
