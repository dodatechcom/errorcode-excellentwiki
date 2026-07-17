---
title: "[Solution] Docker SDK: Cannot Connect to Daemon Fix"
description: "Fix Docker SDK connection errors in Go. Handle daemon not running, socket permissions, and TLS configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["docker", "sdk", "daemon", "container", "socket"]
weight: 5
---

# Docker SDK: Cannot Connect to Daemon

This error occurs when the Go Docker SDK cannot connect to the Docker daemon. It covers socket permission issues, daemon not running, and TLS misconfiguration.

## What This Error Means

Common error messages:

- `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
- `Cannot connect to the Docker daemon at tcp://localhost:2375. Is the docker daemon running?`
- `error during connect: Post http://%2F%2F.%2Fpipe%2Fdocker_engine: ...`
- `dial unix /var/run/docker.sock: connect: permission denied`

The Docker SDK communicates with the daemon via a Unix socket or TCP. If the daemon isn't running, the socket is inaccessible, or TLS is misconfigured, the connection fails.

## Common Causes

```go
// Cause 1: Docker daemon not running
cli, err := client.NewClientWithOpts(client.FromEnv)
// Cannot connect to Docker daemon

// Cause 2: Permission denied on socket
// Running as non-root user without docker group

// Cause 3: Wrong DOCKER_HOST
os.Setenv("DOCKER_HOST", "tcp://localhost:2376")
// Daemon on unix socket

// Cause 4: TLS not configured but expected
cli, err := client.NewClientWithOpts(
    client.WithHost("tcp://docker:2376"),
    // Missing TLS config
)

// Cause 5: Docker Desktop not running (macOS/Windows)
```

## How to Fix

### Fix 1: Create client with explicit options

```go
import (
    "github.com/docker/docker/client"
)

cli, err := client.NewClientWithOpts(
    client.WithHost("unix:///var/run/docker.sock"),
    client.WithAPIVersionNegotiation(),
)
if err != nil {
    log.Fatal(err)
}
```

### Fix 2: Check daemon is running

```go
func isDockerRunning(cli *client.Client) bool {
    _, err := cli.Ping(context.Background())
    return err == nil
}

func main() {
    cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
    if err != nil {
        log.Fatal(err)
    }

    if !isDockerRunning(cli) {
        log.Fatal("Docker daemon is not running")
    }
}
```

### Fix 3: Handle permission errors

```go
func main() {
    cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
    if err != nil {
        if strings.Contains(err.Error(), "permission denied") {
            log.Fatal("Add your user to the docker group: sudo usermod -aG docker $USER")
        }
        log.Fatal(err)
    }
}
```

### Fix 4: Configure TLS for remote Docker

```go
import (
    "crypto/tls"
    "crypto/x509"
    "github.com/docker/docker/client"
    "github.com/docker/docker/pkg/tlsconfig"
)

func createTLSClient(certPath string) (*client.Client, error) {
    tlsOpts := &tls.Config{}

    cert, err := tls.LoadX509KeyPair(
        filepath.Join(certPath, "cert.pem"),
        filepath.Join(certPath, "key.pem"),
    )
    if err != nil {
        return nil, err
    }
    tlsOpts.Certificates = []tls.Certificate{cert}

    caCert, err := os.ReadFile(filepath.Join(certPath, "ca.pem"))
    if err != nil {
        return nil, err
    }
    caCertPool := x509.NewCertPool()
    caCertPool.AppendCertsFromPEM(caCert)
    tlsOpts.RootCAs = caCertPool

    return client.NewClientWithOpts(
        client.WithHost("tcp://docker:2376"),
        client.WithTLSClientConfig(tlsOpts),
        client.WithAPIVersionNegotiation(),
    )
}
```

### Fix 5: Use context with timeout for operations

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()

containers, err := cli.ContainerList(ctx, types.ContainerListOptions{})
if err != nil {
    log.Printf("Failed to list containers: %v", err)
}
```

## Examples

```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
Is the docker daemon running?
```

```go
// Fix: fallback to TCP if socket fails
func createDockerClient() (*client.Client, error) {
    cli, err := client.NewClientWithOpts(
        client.WithHost("unix:///var/run/docker.sock"),
        client.WithAPIVersionNegotiation(),
    )
    if err != nil {
        // Try TCP fallback
        cli, err = client.NewClientWithOpts(
            client.WithHost("tcp://localhost:2375"),
            client.WithAPIVersionNegotiation(),
        )
    }
    return cli, err
}
```

## Related Errors

- [go-docker-sdk]({{< relref "/languages/go/go-docker-sdk" >}}) — basic Docker SDK error
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — connection refused
- [permission-denied]({{< relref "/languages/go/permission-denied-2" >}}) — permission denied
