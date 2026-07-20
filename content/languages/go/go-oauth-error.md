---
title: "[Solution] golang.org/x/oauth2 Token Expired Fix"
description: "Fix Go OAuth2 token expired errors. Handle token refresh, credential management, and scope validation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# golang.org/x/oauth2 Token Expired

The OAuth2 token from `golang.org/x/oauth2` has expired, was never refreshed, or the refresh token is invalid. Without automatic token refresh, all requests fail with 401 after the initial access token expires.

## Common Causes

```go
// Cause 1: Not checking token expiry
token := &oauth2.Token{AccessToken: "old-token"}
client := oauth2.NewClient(ctx, oauth2.StaticTokenSource(token))
// 401 Unauthorized

// Cause 2: Refresh token not used
conf := &oauth2.Config{...}
// refresh token may have expired or been revoked

// Cause 3: Token source not set up for auto-refresh
ts := oauth2.StaticTokenSource(token) // no refresh

// Cause 4: Clock skew
// local clock ahead of provider's clock

// Cause 5: Redirect URI mismatch
conf.RedirectURL = "http://localhost:8080/callback"
// provider configured with https://localhost:8080/callback
```

## How to Fix

### Fix 1: Use TokenSource for automatic refresh

```go
import (
    "context"
    "golang.org/x/oauth2"
)

func oauthClient(ctx context.Context) *http.Client {
    conf := &oauth2.Config{
        ClientID:     os.Getenv("OAUTH_CLIENT_ID"),
        ClientSecret: os.Getenv("OAUTH_CLIENT_SECRET"),
        Endpoint: oauth2.Endpoint{
            TokenURL: "https://provider.com/token",
        },
        Scopes: []string{"read", "write"},
    }

    token, _ := conf.Exchange(ctx, authCode)
    ts := conf.TokenSource(ctx, token) // handles refresh
    return oauth2.NewClient(ctx, ts)
}
```

### Fix 2: Use client credentials for server-to-server

```go
conf := &clientcredentials.Config{
    ClientID:     os.Getenv("CLIENT_ID"),
    ClientSecret: os.Getenv("CLIENT_SECRET"),
    TokenURL:     "https://provider.com/token",
    Scopes:       []string{"read"},
}
client := conf.Client(ctx)
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "golang.org/x/oauth2"
    "golang.org/x/oauth2/google"
)

func main() {
    conf := &oauth2.Config{
        ClientID:     os.Getenv("GOOGLE_CLIENT_ID"),
        ClientSecret: os.Getenv("GOOGLE_CLIENT_SECRET"),
        Endpoint:     google.Endpoint,
        Scopes:       []string{"https://www.googleapis.com/auth/userinfo.email"},
        RedirectURL:  "http://localhost:8080/callback",
    }

    authCode := os.Getenv("AUTH_CODE")
    token, err := conf.Exchange(context.Background(), authCode)
    if err != nil {
        log.Fatal(err)
    }

    client := conf.Client(context.Background(), token)
    resp, err := client.Get("https://www.googleapis.com/oauth2/v2/userinfo")
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)
    fmt.Println(string(body))
}
```

## Related Errors

- [go-jwt-error]({{< relref "/languages/go/go-jwt-error" >}}) — JWT token expired
- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — API returns unauthorized
- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault token renewal
