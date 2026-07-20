---
title: "[Solution] Consul Agent Unreachable Fix"
description: "Fix Consul agent unreachable errors. Handle service discovery, health checks, and cluster connectivity."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Consul Agent Unreachable

The HashiCorp Consul agent in Go fails to connect due to wrong address, datacenter mismatch, ACL token issues, or the agent not running. Consul uses both HTTP and gossip protocols, so connectivity issues can come from either layer.

## Common Causes

```go
// Cause 1: Wrong Consul address
config := api.DefaultConfig()
config.Address = "wrong-host:8500"
client, _ := api.NewClient(config)
// Put "http://wrong-host:8500/v1/agent/self": dial tcp: lookup wrong-host

// Cause 2: Datacenter mismatch
config.Datacenter = "dc2" // agent is in dc1
// rpc error: permission denied

// Cause 3: ACL token missing or expired
config.Token = "invalid-token"
// Permission denied: Request missing internal token

// Cause 4: Consul agent not running
// Connection refused to port 8500

// Cause 5: TLS not configured but agent requires it
// tls: first record does not look like a TLS handshake
```

## How to Fix

### Fix 1: Configure Consul client properly

```go
import (
    "fmt"
    "log"
    "os"

    "github.com/hashicorp/consul/api"
)

func consulClient() (*api.Client, error) {
    config := api.DefaultConfig()
    config.Address = os.Getenv("CONSUL_HTTP_ADDR") // e.g., "consul:8500"
    config.Token = os.Getenv("CONSUL_HTTP_TOKEN")

    client, err := api.NewClient(config)
    if err != nil {
        return nil, fmt.Errorf("create consul client: %w", err)
    }

    // Verify connectivity
    agent := client.Agent()
    self, err := agent.Self()
    if err != nil {
        return nil, fmt.Errorf("consul self: %w", err)
    }
    fmt.Printf("Consul datacenter: %s\n", self.Config.Datacenter)
    return client, nil
}
```

### Fix 2: Register services with health checks

```go
func registerService(client *api.Client, name, address string, port int) error {
    registration := &api.AgentServiceRegistration{
        ID:      fmt.Sprintf("%s-%d", name, port),
        Name:    name,
        Address: address,
        Port:    port,
        Check: &api.AgentServiceCheck{
            HTTP:                           fmt.Sprintf("http://%s:%d/health", address, port),
            Interval:                       "10s",
            Timeout:                        "3s",
            DeregisterCriticalServiceAfter: "30s",
        },
    }
    return client.Agent().ServiceRegister(registration)
}
```

### Fix 3: Query services with health filter

```go
func healthyServices(client *api.Client, service string) ([]*api.ServiceEntry, error) {
    entries, _, err := client.Health().Service(service, "", true, nil)
    if err != nil {
        return nil, err
    }
    return entries, nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "github.com/hashicorp/consul/api"
)

func main() {
    config := api.DefaultConfig()
    client, err := api.NewClient(config)
    if err != nil {
        log.Fatal(err)
    }

    // Register a service
    reg := &api.AgentServiceRegistration{
        ID:      "web-1",
        Name:    "web",
        Port:    8080,
        Address: "127.0.0.1",
    }
    if err := client.Agent().ServiceRegister(reg); err != nil {
        log.Fatal(err)
    }

    // List services
    services, err := client.Agent().Services()
    if err != nil {
        log.Fatal(err)
    }
    for id, svc := range services {
        fmt.Printf("Service: %s -> %s:%d\n", id, svc.Address, svc.Port)
    }
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to Consul port fails
- [grpc-unavailable]({{< relref "/languages/go/grpc-unavailable" >}}) — Consul RPC layer unavailable
- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault depends on Consul for HA
