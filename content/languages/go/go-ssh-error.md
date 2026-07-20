---
title: "[Solution] golang.org/x/crypto/ssh Handshake Failed Fix"
description: "Fix Go SSH handshake errors. Handle key exchange, authentication, and host verification."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# golang.org/x/crypto/ssh Handshake Failed

The SSH client library fails during the handshake phase when the host key is not verified, authentication method is wrong, the server does not support the requested key exchange algorithm, or the private key format is invalid. The SSH handshake is the first step before any commands can be executed.

## Common Causes

```go
// Cause 1: Host key verification fails
config := &ssh.ClientConfig{
    User: "root",
    Auth: []ssh.AuthMethod{ssh.Password("pass")},
    HostKeyCallback: ssh.InsecureIgnoreHostKey(),
    // known_hosts mismatch — host key changed
}

// Cause 2: Private key not parsed correctly
key, err := os.ReadFile("id_rsa")
signer, err := ssh.ParsePrivateKey(key)
// ssh: cannot decode key: asn1: structure error

// Cause 3: Wrong authentication method
config := &ssh.ClientConfig{
    Auth: []ssh.AuthMethod{ssh.Password("pass")},
}
// Server only accepts publickey authentication

// Cause 4: Key exchange algorithm mismatch
// Client: diffie-hellman-group14-sha256
// Server: only diffie-hellman-group1-sha1

// Cause 5: Server disconnects before auth completes
// Firewall or rate limiter dropping connection
```

## How to Fix

### Fix 1: Configure host key callback properly

```go
import (
    "fmt"
    "os"

    "golang.org/x/crypto/ssh"
    "golang.org/x/crypto/ssh/knownhosts"
)

func sshClient() (*ssh.Client, error) {
    key, err := os.ReadFile(os.Getenv("HOME") + "/.ssh/id_rsa")
    if err != nil {
        return nil, fmt.Errorf("read key: %w", err)
    }

    signer, err := ssh.ParsePrivateKey(key)
    if err != nil {
        return nil, fmt.Errorf("parse key: %w", err)
    }

    hostKeyCallback, err := knownhosts.New(os.Getenv("HOME") + "/.ssh/known_hosts")
    if err != nil {
        return nil, fmt.Errorf("known_hosts: %w", err)
    }

    config := &ssh.ClientConfig{
        User: "deploy",
        Auth: []ssh.AuthMethod{ssh.PublicKeys(signer)},
        HostKeyCallback: hostKeyCallback,
        Timeout: 10 * time.Second,
    }

    return ssh.Dial("tcp", "server:22", config)
}
```

### Fix 2: Support multiple authentication methods

```go
config := &ssh.ClientConfig{
    User: "deploy",
    Auth: []ssh.AuthMethod{
        ssh.PublicKeys(signer),
        ssh.Password(os.Getenv("SSH_PASSWORD")),
    },
    HostKeyCallback: ssh.InsecureIgnoreHostKey(),
}
```

## Examples

```go
package main

import (
    "fmt"
    "log"
    "os"

    "golang.org/x/crypto/ssh"
)

func main() {
    key, err := os.ReadFile(os.Getenv("HOME") + "/.ssh/id_rsa")
    if err != nil {
        log.Fatal(err)
    }

    signer, err := ssh.ParsePrivateKey(key)
    if err != nil {
        log.Fatal(err)
    }

    config := &ssh.ClientConfig{
        User: "root",
        Auth: []ssh.AuthMethod{ssh.PublicKeys(signer)},
        HostKeyCallback: ssh.InsecureIgnoreHostKey(),
    }

    client, err := ssh.Dial("tcp", "localhost:22", config)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    session, err := client.NewSession()
    if err != nil {
        log.Fatal(err)
    }
    defer session.Close()

    out, err := session.CombinedOutput("uname -a")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(out))
}
```

## Related Errors

- [tls-handshake]({{< relref "/languages/go/tls-handshake-error" >}}) — TLS handshake similar to SSH handshake
- [go-x509-error]({{< relref "/languages/go/go-x509-error" >}}) — certificate verification failures
- [net-dial]({{< relref "/languages/go/net-dial" >}}) — TCP connection to SSH port fails
