---
title: "[Solution] Go net/http: response body not closed — Resource Leak Fix"
description: "Fix Go response body not closed warning."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# net/http: response body not closed

If you forget to close `resp.Body`, the TCP connection cannot be reused and may leak.

## How to Fix

```go
resp, err := http.Get(url)
if err != nil { log.Fatal(err) }
defer resp.Body.Close()
```

### Fix 1: Always close response body

```go
resp, err := client.Do(req)
if err != nil { return err }
defer resp.Body.Close()

_, err = io.Copy(ioutil.Discard, resp.Body)
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
- [goroutine-leak]({{< relref "/languages/go/goroutine-leak" >}}) — goroutine leak.
