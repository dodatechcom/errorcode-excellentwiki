---
title: "[Solution] Go EOF Error Fix"
description: "Fix Go EOF error when reading from files, streams, or network connections. Handle end-of-file properly with io.EOF checks."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["eof", "io", "read", "stream", "end-of-file"]
weight: 5
---

# EOF — End of File Fix

An EOF (End of File) error occurs when a read operation reaches the end of the data source. In Go, `io.EOF` is returned by `Read()` to indicate no more data is available.

## Description

`io.EOF` is not a true error — it's a signal that the read operation completed successfully but there's no more data. Many Go APIs return `io.EOF` on the final `Read()` call. Failing to handle `io.EOF` properly causes programs to treat a normal end-of-data condition as an error.

Common scenarios:

- **Reading until EOF** — `bufio.Scanner` or `io.Read` loop.
- **File read complete** — reaching the end of a file.
- **Network stream end** — TCP connection closed by peer.
- **JSON decoder** — `decoder.More()` returns false.
- **Unexpected EOF** — truncated input (this IS an error).

## Common Causes

```go
// Cause 1: Treating io.EOF as error
buf := make([]byte, 1024)
n, err := file.Read(buf)
if err != nil {
    log.Fatal(err) // io.EOF is treated as fatal
}

// Cause 2: Not looping on io.Read
data, err := io.ReadAll(file)
// If file is a network stream, io.ReadAll may hang

// Cause 3: Not checking io.EOF in scanner loop
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    fmt.Println(scanner.Text())
}
if err := scanner.Err(); err != nil {
    log.Fatal(err) // This includes io.EOF as an error
}

// Cause 4: Unexpected EOF from truncated data
data := []byte(`{"name": "Ali`)
var m map[string]string
json.Unmarshal(data, &m) // unexpected EOF
```

## How to Fix

### Fix 1: Check for io.EOF specifically

```go
// Wrong
n, err := file.Read(buf)
if err != nil {
    log.Fatal(err)
}

// Correct
n, err := file.Read(buf)
if err != nil {
    if err == io.EOF {
        break // Normal end of file
    }
    log.Fatal(err)
}
```

### Fix 2: Use io.ReadFull for exact reads

```go
// Wrong — may read fewer bytes than expected
buf := make([]byte, 1024)
n, _ := file.Read(buf)

// Correct — read exactly 1024 bytes
buf := make([]byte, 1024)
_, err := io.ReadFull(file, buf)
if err != nil {
    if err == io.ErrUnexpectedEOF {
        fmt.Println("not enough data")
    } else if err == io.EOF {
        fmt.Println("file is empty")
    }
}
```

### Fix 3: Handle EOF in scanner correctly

```go
// Wrong — scanner.Err() returns io.EOF at end
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    process(scanner.Text())
}
if err := scanner.Err(); err != nil {
    log.Fatal(err)
}

// Correct — io.EOF is not a real error for scanners
scanner := bufio.NewScanner(file)
for scanner.Scan() {
    process(scanner.Text())
}
if err := scanner.Err(); err != nil {
    log.Fatal(err) // This is correct — scanner.Err() doesn't return io.EOF
}
```

### Fix 4: Use io.ReadAtLeast for minimum reads

```go
// Correct — read at least 1 byte, up to buffer size
buf := make([]byte, 1024)
n, err := io.ReadAtLeast(file, buf, 1)
if err != nil {
    if err == io.EOF {
        fmt.Println("no data available")
    } else if err == io.ErrUnexpectedEOF {
        fmt.Printf("only got %d bytes\n", n)
    }
}
```

### Fix 5: Handle unexpected EOF separately

```go
// Wrong — treats all EOF the same
data, err := io.ReadAll(file)
if err != nil {
    log.Fatal(err)
}

// Correct — distinguish between expected and unexpected EOF
decoder := json.NewDecoder(file)
var result interface{}
err := decoder.Decode(&result)
if err != nil {
    if err == io.EOF {
        fmt.Println("no data in input")
    } else if err == io.ErrUnexpectedEOF {
        fmt.Println("truncated input")
    } else {
        log.Fatal(err)
    }
}
```

## Examples

```go
// This triggers: EOF (treated as error)
package main

import (
    "fmt"
    "io"
    "strings"
)

func main() {
    reader := strings.NewReader("hello")
    buf := make([]byte, 10)
    n, err := reader.Read(buf)
    fmt.Println(string(buf[:n])) // "hello"
    fmt.Println(err)             // EOF

    n, err = reader.Read(buf)
    fmt.Println(n) // 0
    fmt.Println(err) // EOF
}
```

## Related Errors

- [io-pipe-broken]({{< relref "/languages/go/io-pipe-broken" >}}) — broken pipe during write.
- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file doesn't exist.
- [json-unmarshal]({{< relref "/languages/go/json-unmarshal" >}}) — invalid JSON input (unexpected EOF).
