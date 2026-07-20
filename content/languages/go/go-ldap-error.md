---
title: "[Solution] go-ldap Bind Failed Fix"
description: "Fix Go LDAP bind errors. Handle authentication, connection security, and directory queries."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# go-ldap Bind Failed

The `go-ldap` client fails to bind (authenticate) to the LDAP server when the bind DN is wrong, the password is incorrect, the base DN does not exist, or the LDAP server requires StartTLS before binding. LDAP bind is the authentication step before any directory operations.

## Common Causes

```go
// Cause 1: Wrong bind DN format
conn, _ := ldap.Dial("tcp", "ldap.example.com:389")
err := conn.Bind("cn=admin,dc=example,dc=com", "password")
// invalid credentials (49)

// Cause 2: Anonymous bind not allowed
conn.Bind("", "") // anonymous bind
// Inappropriate authentication (48)

// Cause 3: StartTLS required but not called
conn, _ := ldap.Dial("tcp", "ldap.example.com:389")
conn.Bind("cn=admin,dc=example,dc=com", "password")
// Server requires TLS before bind

// Cause 4: Base DN does not exist
searchReq := ldap.NewSearchRequest("dc=wrong,dc=example,dc=com", ...)
// no such object (32)

// Cause 5: Connection timeout on slow LDAP server
conn, _ := ldap.Dial("tcp", "ldap.example.com:389")
// connection timeout
```

## How to Fix

### Fix 1: Use proper bind DN and TLS

```go
import (
    "crypto/tls"
    "fmt"

    "github.com/go-ldap/ldap/v3"
)

func ldapConnect(host, bindDN, password string) (*ldap.Conn, error) {
    conn, err := ldap.DialTLS("tcp", host+":636", &tls.Config{
        InsecureSkipVerify: false,
    })
    if err != nil {
        return nil, fmt.Errorf("ldap dial: %w", err)
    }

    err = conn.Bind(bindDN, password)
    if err != nil {
        return nil, fmt.Errorf("ldap bind: %w", err)
    }

    return conn, nil
}
```

### Fix 2: Search with proper base DN and filters

```go
func searchUsers(conn *ldap.Conn, baseDN string) ([]string, error) {
    searchReq := ldap.NewSearchRequest(
        baseDN,
        ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false,
        "(objectClass=person)",
        []string{"cn", "email"},
        nil,
    )

    result, err := conn.Search(searchReq)
    if err != nil {
        return nil, err
    }

    var users []string
    for _, entry := range result.Entries {
        users = append(users, entry.GetAttributeValue("cn"))
    }
    return users, nil
}
```

### Fix 3: Handle LDAP error codes

```go
func handleLDAPError(err error) error {
    if ldapErr, ok := err.(*ldap.Error); ok {
        switch ldapErr.ResultCode {
        case 49:
            return fmt.Errorf("invalid credentials")
        case 32:
            return fmt.Errorf("no such object")
        case 48:
            return fmt.Errorf("inappropriate authentication")
        default:
            return fmt.Errorf("LDAP error %d: %s", ldapErr.ResultCode, ldapErr.Error())
        }
    }
    return err
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"

    "github.com/go-ldap/ldap/v3"
)

func main() {
    conn, err := ldap.Dial("tcp", "localhost:389")
    if err != nil {
        log.Fatal(err)
    }
    defer conn.Close()

    err = conn.Bind("cn=admin,dc=example,dc=com", "admin123")
    if err != nil {
        log.Fatal(err)
    }

    searchReq := ldap.NewSearchRequest(
        "dc=example,dc=com",
        ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false,
        "(objectClass=person)",
        []string{"cn", "mail"},
        nil,
    )

    result, err := conn.Search(searchReq)
    if err != nil {
        log.Fatal(err)
    }

    for _, entry := range result.Entries {
        fmt.Printf("CN: %s, Email: %s\n",
            entry.GetAttributeValue("cn"),
            entry.GetAttributeValue("mail"))
    }
}
```

## Related Errors

- [go-oauth-error]({{< relref "/languages/go/go-oauth-error" >}}) — OAuth authentication similar flow
- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — authentication failure responses
- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS required before LDAP bind
