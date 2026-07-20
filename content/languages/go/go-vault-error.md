---
title: "[Solution] Vault Permission Denied Fix"
description: "Fix HashiCorp Vault permission denied errors. Handle secret access, token renewal, and policy configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vault Permission Denied

The HashiCorp Vault Go client (`github.com/hashicorp/vault/api`) returns permission denied when the client token lacks required policy capabilities, the token has expired, the secret engine path is wrong, or the namespace is not specified in Vault Enterprise. Vault enforces least-privilege by default.

## Common Causes

```go
// Cause 1: Token lacks required policy capabilities
client, _ := api.NewClient(&api.Config{Address: "https://vault:8200"})
client.SetToken("s.old-token")
secret, err := client.Logical().Read("secret/data/myapp")
// permission denied

// Cause 2: Token expired — no renewal
// vault: permission denied (token is expired or invalid)

// Cause 3: Wrong secret engine mount path
client.Logical().Read("secret/myapp")      // KV v1
client.Logical().Read("secret/data/myapp") // KV v2 — different mount

// Cause 4: Namespace not set in Vault Enterprise
// Missing: client.SetNamespace("admin")

// Cause 5: AppRole login failed — wrong credentials
auth := client.Logical().Write("auth/approle/login", map[string]interface{}{
    "role_id":     "wrong-role-id",
    "secret_id":   "wrong-secret-id",
})
// permission denied: invalid credentials
```

## How to Fix

### Fix 1: Use AppRole authentication with token renewal

```go
import (
    "fmt"
    "log"
    "os"
    "time"

    "github.com/hashicorp/vault/api"
)

func vaultClient() (*api.Client, error) {
    config := &api.Config{Address: os.Getenv("VAULT_ADDR")}
    client, err := api.NewClient(config)
    if err != nil {
        return nil, err
    }

    secret, err := client.Logical().Write("auth/approle/login", map[string]interface{}{
        "role_id":   os.Getenv("VAULT_ROLE_ID"),
        "secret_id": os.Getenv("VAULT_SECRET_ID"),
    })
    if err != nil {
        return nil, fmt.Errorf("approle login: %w", err)
    }

    client.SetToken(secret.Auth.ClientToken)

    go func() {
        for {
            time.Sleep(secret.Auth.LeaseDuration * 2 / 3 * time.Second)
            _, err := client.Auth().Token().RenewSelf(0)
            if err != nil {
                log.Printf("token renewal failed: %v", err)
            }
        }
    }()

    return client, nil
}
```

### Fix 2: Use correct KV v2 paths

```go
func readSecretV2(client *api.Client, mount, path string) (map[string]interface{}, error) {
    secret, err := client.Logical().Read(fmt.Sprintf("%s/data/%s", mount, path))
    if err != nil {
        return nil, err
    }
    data, ok := secret.Data["data"].(map[string]interface{})
    if !ok {
        return nil, fmt.Errorf("unexpected secret format")
    }
    return data, nil
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"
    "os"

    "github.com/hashicorp/vault/api"
)

func main() {
    config := &api.Config{Address: os.Getenv("VAULT_ADDR")}
    client, err := api.NewClient(config)
    if err != nil {
        log.Fatal(err)
    }
    client.SetToken(os.Getenv("VAULT_TOKEN"))

    secret, err := client.Logical().Read("secret/data/myapp/config")
    if err != nil {
        log.Fatal(err)
    }
    if secret == nil {
        log.Fatal("secret not found")
    }

    data := secret.Data["data"].(map[string]interface{})
    fmt.Println("db_password:", data["db_password"])
}
```

## Related Errors

- [go-oauth-error]({{< relref "/languages/go/go-oauth-error" >}}) — OAuth token expiry similar to Vault token expiry
- [go-jwt-error]({{< relref "/languages/go/go-jwt-error" >}}) — JWT token validation failures
- [grpc-unauthenticated]({{< relref "/languages/go/grpc-unauthenticated" >}}) — gRPC auth interceptor rejects request
