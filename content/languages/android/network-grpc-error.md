---
title: "gRPC Connection Error"
description: "Fix Android gRPC connection and streaming errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
gRPC calls fail with connection timeout or status errors

## Common Causes

- Channel not properly configured
- Deadline not set on calls
- Streaming not properly managed
- TLS not configured for secure channel

## Fixes

- Create ManagedChannel with proper authority
- Set deadline on each call or channel
- Use client streaming or server streaming correctly
- Configure TLS with certificates

## Code Example

```kotlin
val channel = ManagedChannelBuilder.forAddress("api.example.com", 443)
    .useTransportSecurity()
    .keepAliveTime(30, TimeUnit.SECONDS)
    .build()

val stub = MyServiceGrpc.newStub(channel)
    .withDeadlineAfter(10, TimeUnit.SECONDS)

// Unary call:
stub.myMethod(request, object : StreamObserver<Response> {
    override fun onNext(value: Response) { /* handle response */ }
    override fun onError(t: Throwable) { /* handle error */ }
    override fun onCompleted() { /* done */ }
})
```

# gRPC uses HTTP/2 under the hood
# Set deadline to prevent hung calls
# Use keepAlive for connection health
