---
title: "[Solution] Grafana API Error Fix"
description: "Fix Grafana API errors in Go. Handle dashboard operations, data source queries, and authentication."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Grafana API Error

The Grafana Go client fails when calling the Grafana HTTP API due to invalid API keys, wrong data source UIDs, malformed JSON dashboard models, or permission issues. The Grafana API requires specific content types and authentication headers.

## Common Causes

```go
// Cause 1: Invalid or expired API key
req.Header.Set("Authorization", "Bearer invalid-key")
// 401: Unauthorized

// Cause 2: Wrong data source UID
// 404: data source not found

// Cause 3: Dashboard JSON missing required fields
dashboard := map[string]interface{}{
    "title": "My Dashboard",
    // missing "panels" key
}

// Cause 4: Folder permission denied
// Dashboard belongs to org 2, API key is for org 1

// Cause 5: Content-Type not set
req.Header.Set("Content-Type", "text/plain") // must be application/json
```

## How to Fix

### Fix 1: Use proper API key authentication

```go
import (
    "bytes"
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
)

func grafanaRequest(method, path string, body interface{}) ([]byte, error) {
    url := os.Getenv("GRAFANA_URL") + path

    var bodyReader io.Reader
    if body != nil {
        data, _ := json.Marshal(body)
        bodyReader = bytes.NewReader(data)
    }

    req, _ := http.NewRequest(method, url, bodyReader)
    req.Header.Set("Authorization", "Bearer "+os.Getenv("GRAFANA_API_KEY"))
    req.Header.Set("Content-Type", "application/json")

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    return io.ReadAll(resp.Body)
}
```

### Fix 2: Create dashboard with complete JSON model

```go
func createDashboard(title string) ([]byte, error) {
    dashboard := map[string]interface{}{
        "dashboard": map[string]interface{}{
            "title": title,
            "panels": []map[string]interface{}{
                {"type": "graph", "title": "Panel 1"},
            },
        },
        "overwrite": true,
    }
    return grafanaRequest("POST", "/api/dashboards/db", dashboard)
}
```

## Examples

```go
package main

import (
    "fmt"
    "io"
    "log"
    "net/http"
    "os"
)

func main() {
    req, _ := http.NewRequest("GET",
        os.Getenv("GRAFANA_URL")+"/api/health", nil)
    req.Header.Set("Authorization", "Bearer "+os.Getenv("GRAFANA_API_KEY"))

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)
    fmt.Println(string(body))
}
```

## Related Errors

- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — API key missing
- [http-status-403]({{< relref "/languages/go/http-status-403" >}}) — insufficient permissions
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — malformed response
