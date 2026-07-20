---
title: "[Solution] go-elasticsearch Connection Refused Fix"
description: "Fix Elasticsearch Go client connection errors. Handle cluster connectivity, sniffing, and health checks."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# go-elasticsearch Connection Refused

The `olivere/elastic` or official `go-elasticsearch` client fails to connect to Elasticsearch due to wrong URLs, version mismatch, authentication failure, or cluster health issues. Elasticsearch requires specific headers and content types for all API calls.

## Common Causes

```go
// Cause 1: Wrong URL or Elasticsearch not running
es, err := elasticsearch.NewClient(elasticsearch.Config{
    Addresses: []string{"http://localhost:9200"},
})
// Get "http://localhost:9200": dial tcp 127.0.0.1:9200: connect: connection refused

// Cause 2: Version mismatch between client and server
es, _ := elasticsearch.NewClient(elasticsearch.Config{
    Addresses: []string{"http://localhost:9200"},
    // Client expects ES 8.x but server is 7.x
})

// Cause 3: X-Pack security enabled but credentials not provided
es, _ := elasticsearch.NewClient(elasticsearch.Config{
    Addresses: []string{"http://localhost:9200"},
    // missing Username/Password
})

// Cause 4: Index does not exist
res, _ := es.Search(es.Search.WithIndex("nonexistent"))
// resource_not_found_exception

// Cause 5: Wrong content type for bulk operations
req := bulkRequest body using wrong format
// Content-Type header [application/x-www-form-urlencoded] is not supported
```

## How to Fix

### Fix 1: Configure client with proper connection settings

```go
import (
    "fmt"
    "log"

    "github.com/elastic/go-elasticsearch/v8"
)

func esClient() (*elasticsearch.Client, error) {
    cfg := elasticsearch.Config{
        Addresses: []string{
            "http://localhost:9200",
        },
        Username: "elastic",
        Password: os.Getenv("ELASTIC_PASSWORD"),
        // Or use API key
        // APIKey: os.Getenv("ES_API_KEY"),
    }

    es, err := elasticsearch.NewClient(cfg)
    if err != nil {
        return nil, fmt.Errorf("create ES client: %w", err)
    }

    // Verify connection
    res, err := es.Info()
    if err != nil {
        return nil, fmt.Errorf("ES info: %w", err)
    }
    defer res.Body.Close()
    return es, nil
}
```

### Fix 2: Create index with proper mappings

```go
func createIndex(es *elasticsearch.Client, index string) error {
    mapping := `{
        "mappings": {
            "properties": {
                "title":   { "type": "text" },
                "content": { "type": "text" },
                "created": { "type": "date" }
            }
        }
    }`

    res, err := es.Indices.Create(index,
        es.Indices.Create.WithBody(strings.NewReader(mapping)),
    )
    if err != nil {
        return err
    }
    defer res.Body.Close()
    return nil
}
```

## Examples

```go
package main

import (
    "context"
    "fmt"
    "log"
    "strings"

    "github.com/elastic/go-elasticsearch/v8"
)

func main() {
    es, err := elasticsearch.NewClient(elasticsearch.Config{
        Addresses: []string{"http://localhost:9200"},
    })
    if err != nil {
        log.Fatal(err)
    }

    doc := `{"title":"Hello Elasticsearch","content":"This is a test document"}`

    res, err := es.Index("my-index",
        strings.NewReader(doc),
        es.Index.WithDocumentID("1"),
        es.Index.WithRefresh("true"),
    )
    if err != nil {
        log.Fatal(err)
    }
    defer res.Body.Close()
    fmt.Println("Indexed:", res.Status())
}
```

## Related Errors

- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to Elasticsearch port fails
- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — Elasticsearch authentication required
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — malformed ES response body
