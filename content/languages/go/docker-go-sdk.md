---
title: "[Solution] Docker SDK Connection Error Fix"
description: "Fix Go Docker SDK connection errors. Handle Docker daemon connectivity, TLS configuration, and socket issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Docker SDK Connection Error

The Docker Go SDK (`github.com/docker/docker/client`) fails to connect to the Docker daemon when the socket path is wrong, the daemon is not running, TLS is misconfigured, or the API version is incompatible. The SDK communicates over a Unix socket or TCP, and both paths require proper configuration.

## Common Causes

```go
// Cause 1: Docker daemon not running or wrong socket path
cli, err := client.NewClientWithOpts(client.FromEnv)
// Cannot connect to the Docker daemon at unix:///var/run/docker.sock

// Cause 2: API version mismatch
cli, err := client.NewClientWithOpts(
    client.WithVersion("1.40"),
    client.WithHost("unix:///var/run/docker.sock"),
)
// Error response from daemon: client version too old

// Cause 3: TLS certificate path wrong
cli, err := client.NewClientWithOpts(
    client.WithHost("https://docker.example.com:2376"),
    client.WithTLSClientConfig(ca, cert, key),
)
// tls: failed to verify certificate

// Cause 4: DOCKER_HOST env var not set
// SDK defaults to unix:///var/run/docker.sock
// Remote Docker daemon needs explicit host

// Cause 5: Permission denied on socket
// User not in docker group
// Got permission denied while trying to connect to Docker daemon socket
```

## How to Fix

### Fix 1: Create client with environment-based configuration

```go
import (
    "context"
    "fmt"
    "log"

    "github.com/docker/docker/client"
)

func dockerClient() (*client.Client, error) {
    cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
    if err != nil {
        return nil, fmt.Errorf("create docker client: %w", err)
    }

    // Test connection
    ping, err := cli.Ping(context.Background())
    if err != nil {
        return nil, fmt.Errorf("docker ping: %w", err)
    }
    fmt.Printf("Docker version: %s\n", ping.APIVersion)
    return cli, nil
}
```

### Fix 2: Connect to remote Docker daemon with TLS

```go
import (
    "crypto/tls"
    "crypto/x509"
    "io/ioutil"

    "github.com/docker/docker/client"
)

func remoteDockerClient() (*client.Client, error) {
    cert, _ := tls.LoadX509KeyPair("client-cert.pem", "client-key.pem")
    caCert, _ := ioutil.ReadFile("ca.pem")
    caPool := x509.NewCertPool()
    caPool.AppendCertsFromPEM(caCert)

    tlsConfig := &tls.Config{
        Certificates: []tls.Certificate{cert},
        RootCAs:      caPool,
    }

    return client.NewClientWithOpts(
        client.WithHost("https://docker.example.com:2376"),
        client.WithTLSClientConfig(caPool),
        client.WithAPIVersionNegotiation(),
    )
}
```

### Fix 3: List containers to verify connectivity

```go
func listContainers(cli *client.Client) {
    containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{})
    if err != nil {
        log.Fatal(err)
    }
    for _, c := range containers {
        fmt.Printf("Container: %s (%s)\n", c.ID[:12], c.Image)
    }
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/docker/docker/api/types/container"
    "github.com/docker/docker/client"
)

func main() {
    cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
    if err != nil {
        log.Fatal(err)
    }
    defer cli.Close()

    ctx := context.Background()

    resp, err := cli.ContainerCreate(ctx, &container.Config{
        Image: "alpine",
        Cmd:   []string{"echo", "hello from docker"},
    }, nil, nil, nil, "")
    if err != nil {
        log.Fatal(err)
    }

    if err := cli.ContainerStart(ctx, resp.ID, container.StartOptions{}); err != nil {
        log.Fatal(err)
    }

    fmt.Println("Container started:", resp.ID[:12])
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to Docker daemon port fails
- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS handshake with Docker daemon
- [permission-denied]({{< relref "/languages/go/http-status-403" >}}) — user not in docker group
