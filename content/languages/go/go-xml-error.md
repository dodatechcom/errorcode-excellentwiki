---
title: "[Solution] encoding/xml Unmarshal Error Fix"
description: "Fix Go XML unmarshal errors. Handle malformed XML, missing fields, and type conversion issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# encoding/xml Unmarshal Error

The `encoding/xml` package fails to unmarshal XML when element names don't match struct tags, attributes are missing, XML namespaces are wrong, or the XML structure has unexpected nesting. XML unmarshaling in Go is strict about tag names and case sensitivity.

## Common Causes

```go
// Cause 1: XML element name does not match struct tag
type User struct {
    Name string `xml:"name"`
}
// <Name>Alice</Name> — wants <name>, not <Name>
// encoding: cannot unmarshal <Name> into Go struct field

// Cause 2: Attribute not declared in struct
type User struct {
    Name string `xml:"name"`
}
// <user id="1"><name>Alice</name></user>
// id is ignored — not declared in struct

// Cause 3: Namespace mismatch
// <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
// <Envelope xmlns="http://www.w3.org/2005/Atom"> — different namespace

// Cause 4: XML has mixed content (text + elements)
// <p>Hello <b>world</b></p>
// Go XML decoder does not handle mixed content well

// Cause 5: CDATA sections not handled
// <data><![CDATA[raw content]]></data>
// may lose CDATA wrapper
```

## How to Fix

### Fix 1: Use correct XML struct tags

```go
import (
    "encoding/xml"
    "fmt"
    "strings"
)

type User struct {
    XMLName xml.Name `xml:"user"`
    Name    string   `xml:"name"`
    Email   string   `xml:"email"`
    Age     int      `xml:"age"`
    Admin   bool     `xml:"admin,attr"` // attribute
}

func parseUser(xmlData string) (*User, error) {
    var u User
    if err := xml.Unmarshal([]byte(xmlData), &u); err != nil {
        return nil, fmt.Errorf("unmarshal xml: %w", err)
    }
    return &u, nil
}
```

### Fix 2: Handle XML with decoder for streaming

```go
func decodeXML(r io.Reader) ([]User, error) {
    decoder := xml.NewDecoder(r)
    var users []User

    for {
        var u User
        if err := decoder.DecodeElement(&u, nil); err == io.EOF {
            break
        } else if err != nil {
            return nil, err
        }
        users = append(users, u)
    }
    return users, nil
}
```

### Fix 3: Handle namespaces with xml.Name

```go
type SoapEnvelope struct {
    XMLName xml.Name `xml:"http://schemas.xmlsoap.org/soap/envelope/ Envelope"`
    Body    SoapBody `xml:"http://schemas.xmlsoap.org/soap/envelope/ Body"`
}

type SoapBody struct {
    Response string `xml:"GetUserResponse"`
}
```

## Examples

```go
package main

import (
    "encoding/xml"
    "fmt"
    "log"
)

type User struct {
    XMLName xml.Name `xml:"user"`
    Name    string   `xml:"name"`
    Email   string   `xml:"email"`
    Active  bool     `xml:"active"`
}

func main() {
    xmlData := `
<user>
    <name>Alice</name>
    <email>alice@example.com</email>
    <active>true</active>
</user>`

    var u User
    if err := xml.Unmarshal([]byte(xmlData), &u); err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Name: %s, Email: %s, Active: %v\n", u.Name, u.Email, u.Active)

    // Marshal back
    output, _ := xml.MarshalIndent(u, "", "  ")
    fmt.Println(string(output))
}
```

## Related Errors

- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — JSON unmarshal has similar tag-matching issues
- [go-yaml-error]({{< relref "/languages/go/go-yaml-error" >}}) — YAML parsing errors
- [encoding-binary]({{< relref "/languages/go/go-binary-error" >}}) — binary encoding issues
