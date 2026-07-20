---
title: "[Solution] SAML Assertion Error Fix"
description: "Fix Go SAML assertion errors. Handle XML signature validation, certificate issues, and redirect binding."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# SAML Assertion Error

The SAML library fails when the assertion signature is invalid, the identity provider (IdP) certificate is not trusted, the ACS URL is wrong, or the clock skew between SP and IdP causes validation failure. SAML assertions are XML documents with XML digital signatures.

## Common Causes

```go
// Cause 1: IdP certificate not loaded
sp, _ := samlsp.New(samlsp.Options{
    IDPMetadataURL: nil,
    // IDPMetadata not set — cannot verify assertion signature
})

// Cause 2: Assertion clock skew
// IdP sent assertion with NotBefore: 2024-01-01T00:00:00Z
// SP clock is 5 minutes behind — assertion appears not yet valid

// Cause 3: ACS URL mismatch
// SP configured: https://sp.example.com/saml/acs
// IdP configured: https://sp.example.com/acs
// SAML Response destination does not match

// Cause 4: Audience restriction fails
// Assertion Audience: https://sp.example.com
// SP Entity ID: https://myapp.example.com

// Cause 5: InResponseTo mismatch
// IdP sends assertion with InResponseTo="request-id"
// SP has no matching pending request
```

## How to Fix

### Fix 1: Configure SAML SP properly

```go
import (
    "crypto/tls"
    "net/http"

    "github.com/crewjam/saml/samlsp"
)

func setupSAML() (*samlsp.Middleware, error) {
    keyPair, _ := tls.LoadX509KeyPair("sp.crt", "sp.key")

    opts := samlsp.Options{
        EntityID:    "https://myapp.example.com",
        URL:         "https://myapp.example.com/saml",
        Key:         keyPair.PrivateKey,
        Certificate: keyPair.Certificate,
        IDPMetadataURL: &url.URL{
            Scheme: "https",
            Host:   "idp.example.com",
            Path:   "/metadata",
        },
        AllowIDPInitiated: true,
    }

    return samlsp.New(opts)
}
```

### Fix 2: Handle clock skew

```go
opts := samlsp.Options{
    // Allow 5 minutes clock skew
    Clock:         samlsp.Clock{Time: time.Now()},
    // Set NotBeforeSkew on SP
}

sp, _ := samlsp.New(opts)
// Add to middleware
http.Handle("/saml/", sp)
```

### Fix 3: Validate assertion attributes

```go
func handleAssertion(w http.ResponseWriter, r *http.Request) {
    assertion := samlsp.AssertionFromContext(r.Context())
    if assertion == nil {
        http.Error(w, "no assertion", http.StatusUnauthorized)
        return
    }

    for _, attrStatement := range assertion.AttributeStatement {
        for _, attr := range attrStatement.Attributes {
            fmt.Printf("Attribute: %s = %s\n", attr.Name, attr.Values[0].Value)
        }
    }
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"
    "net/http"
    "os"

    "github.com/crewjam/saml/samlsp"
)

func main() {
    keyPair, _ := tls.LoadX509KeyPair("sp.crt", "sp.key")

    opts := samlsp.Options{
        EntityID:    os.Getenv("SAML_ENTITY_ID"),
        URL:         os.Getenv("SAML_ACS_URL"),
        Key:         keyPair.PrivateKey,
        Certificate: keyPair.Certificate,
    }

    sp, err := samlsp.New(opts)
    if err != nil {
        log.Fatal(err)
    }

    http.Handle("/saml/", sp)
    http.HandleFunc("/hello", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "Hello, SAML user!")
    })

    log.Fatal(http.ListenAndServeTLS(":443", "sp.crt", "sp.key", nil))
}
```

## Related Errors

- [go-x509-error]({{< relref "/languages/go/go-x509-error" >}}) — X.509 certificate verification in SAML
- [xml-unmarshal]({{< relref "/languages/go/go-xml-error" >}}) — SAML assertion XML parsing
- [go-oauth-error]({{< relref "/languages/go/go-oauth-error" >}}) — OAuth/SAML SSO alternatives
