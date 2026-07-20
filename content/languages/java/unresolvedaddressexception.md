---
title: "[Solution] Java UnresolvedAddressException — Unresolved Socket Address Fix"
description: "Fix Java UnresolvedAddressException by resolving address first, using InetSocketAddress properly, and checking DNS resolution."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnresolvedAddressException — Unresolved Socket Address Fix

An `UnresolvedAddressException` is thrown when a network operation is attempted using a socket address that has not been resolved to an IP address. This occurs when `InetSocketAddress.createUnresolved()` is used or DNS resolution fails.

## Description

`java.nio.channels.UnresolvedAddressException` extends `IllegalArgumentException` and is thrown by `SocketChannel.connect()`, `ServerSocketChannel.bind()`, and `DatagramChannel.connect()` when the provided `SocketAddress` does not contain a resolved IP address.

Common message variants:

- `java.nio.channels.UnresolvedAddressException`
- `Unresolved address`

## Common Causes

```java
// Cause 1: Using unresolved address with SocketChannel
SocketAddress unresolved = InetSocketAddress.createUnresolved("example.com", 80);
SocketChannel channel = SocketChannel.open();
channel.connect(unresolved);  // UnresolvedAddressException

// Cause 2: DNS resolution failure
InetSocketAddress addr = InetSocketAddress.createUnresolved("nonexistent.invalid", 80);
// Or:
InetSocketAddress addr2 = new InetSocketAddress("nonexistent.invalid", 80);
// addr2.isUnresolved() == true — DNS failed

SocketChannel channel = SocketChannel.open();
channel.connect(addr2);  // UnresolvedAddressException

// Cause 3: Network unavailable during DNS resolution
// DNS queries require network — if offline, resolution fails silently

// Cause 4: Using createUnresolved() by mistake
// Developer intended to resolve but used wrong factory method
InetSocketAddress addr = InetSocketAddress.createUnresolved("host", 80);  // Not resolved!

// Cause 5: Null hostname in InetSocketAddress
InetSocketAddress addr = InetSocketAddress.createUnresolved(null, 80);  // Unresolved
```

## Solutions

### Fix 1: Use InetSocketAddress constructor for automatic DNS resolution

```java
// Wrong — unresolved address
SocketAddress addr = InetSocketAddress.createUnresolved("example.com", 80);

// Correct — resolves DNS automatically
InetSocketAddress addr = new InetSocketAddress("example.com", 80);
if (addr.isUnresolved()) {
    throw new IOException("Failed to resolve hostname: example.com");
}

SocketChannel channel = SocketChannel.open();
channel.connect(addr);
```

### Fix 2: Verify resolution before connecting

```java
InetSocketAddress address = new InetSocketAddress(hostname, port);

if (address.isUnresolved()) {
    System.err.println("DNS resolution failed for: " + hostname);
    // Fallback to IP address or throw
    throw new IOException("Cannot resolve: " + hostname);
}

SocketChannel channel = SocketChannel.open();
channel.connect(address);
```

### Fix 3: Resolve address explicitly with InetAddress

```java
import java.net.InetAddress;

try {
    InetAddress[] addresses = InetAddress.getAllByName("example.com");
    for (InetAddress addr : addresses) {
        InetSocketAddress socketAddr = new InetSocketAddress(addr, 80);
        try {
            SocketChannel channel = SocketChannel.open();
            channel.connect(socketAddr);
            System.out.println("Connected to: " + addr);
            break;
        } catch (IOException e) {
            System.out.println("Failed to connect to: " + addr);
        }
    }
} catch (UnknownHostException e) {
    System.err.println("DNS resolution failed: " + e.getMessage());
}
```

### Fix 4: Handle DNS failures with fallback

```java
public static InetSocketAddress resolveAddress(String host, int port)
        throws IOException {
    // Try DNS resolution
    InetSocketAddress addr = new InetSocketAddress(host, port);
    if (!addr.isUnresolved()) {
        return addr;
    }

    // Try parsing as IP literal
    try {
        InetAddress ip = InetAddress.getByName(host);
        return new InetSocketAddress(ip, port);
    } catch (UnknownHostException e) {
        throw new IOException("Cannot resolve host: " + host, e);
    }
}

// Usage
InetSocketAddress addr = resolveAddress("myserver.local", 8080);
channel.connect(addr);
```

### Fix 5: Use custom DNS resolver for advanced resolution

```java
import java.net.spi.InetAddressResolver;
import java.net.spi.InetAddressResolverProvider;

// Or manually resolve with custom logic
public static List<InetAddress> resolveWithFallback(String hostname)
        throws UnknownHostException {
    List<InetAddress> result = new ArrayList<>();

    // Standard DNS
    try {
        InetAddress[] addrs = InetAddress.getAllByName(hostname);
        result.addAll(Arrays.asList(addrs));
    } catch (UnknownHostException e) {
        // DNS failed — try /etc/hosts or other sources
    }

    if (result.isEmpty()) {
        throw new UnknownHostException("No addresses for: " + hostname);
    }

    return result;
}
```

## Prevention Checklist

- Use `new InetSocketAddress(host, port)` instead of `createUnresolved()` for automatic DNS resolution.
- Always check `isUnresolved()` before connecting with the resolved address.
- Handle `UnknownHostException` / `UnresolvedAddressException` with fallback resolution logic.
- Test DNS resolution in all deployment environments.
- Cache resolved addresses to avoid repeated DNS lookups.

## Related Errors

- [UnknownHostException](../unknownhostexception) — DNS lookup failed entirely.
- [ConnectException](../connectexception) — TCP connection refused.
- [SocketTimeoutException](../sockettimeoutexception) — connection timed out.
- [UnsupportedAddressTypeException](../unsupportedaddresstypeexception) — unsupported address type.
