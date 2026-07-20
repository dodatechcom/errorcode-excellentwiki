---
title: "[Solution] Java UnknownHostException — DNS Resolution Fix"
description: "Fix Java UnknownHostException by checking DNS configuration, verifying hostname spelling, ensuring network connectivity, and configuring DNS timeouts."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# UnknownHostException — DNS Resolution Fix

An `UnknownHostException` is thrown when the hostname cannot be resolved to an IP address by the DNS system. This typically indicates a DNS configuration issue, a misspelled hostname, or network connectivity problems.

## Description

The `java.net.UnknownHostException` extends `IOException` and is thrown when `InetAddress.getByName()` or any networking operation that requires DNS resolution fails to find the specified host. The hostname is either misspelled, the DNS server is unreachable, or the hostname does not exist in DNS.

Common message variants:

- `java.net.UnknownHostException: example.com`
- `java.net.UnknownHostException:example.com: Name or service not known`
- `java.net.UnknownHostException: Unable to resolve host`

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.io.IOException
                    └── java.net.UnknownHostException
```

## Common Causes

```java
// Cause 1: Hostname does not exist in DNS
InetAddress address = InetAddress.getByName("nonexistent.example.com");  // UnknownHostException

// Cause 2: Misspelled hostname
InetAddress address = InetAddress.getByName("exmaple.com");  // Typo — UnknownHostException

// Cause 3: DNS server is unreachable
// If /etc/resolv.conf points to a non-existent DNS server
InetAddress address = InetAddress.getByName("google.com");  // UnknownHostException

// Cause 4: Network interface is down
// Machine is not connected to any network
InetAddress address = InetAddress.getByName("example.com");  // UnknownHostException

// Cause 5: Hostname uses local /etc/hosts but entry is missing
InetAddress address = InetAddress.getByName("myapp.local");  // Not in /etc/hosts or DNS
```

## Solutions

### Fix 1: Verify hostname spelling and existence

```java
// Wrong — typo in hostname
URL url = new URL("http://exmaple.com/api");  // UnknownHostException

// Correct — verify hostname exists
String hostname = "example.com";
try {
    InetAddress address = InetAddress.getByName(hostname);
    System.out.println("Resolved to: " + address.getHostAddress());
} catch (UnknownHostException e) {
    System.err.println("Hostname '" + hostname + "' cannot be resolved");
    System.err.println("Check spelling and verify DNS configuration");
}
```

### Fix 2: Configure DNS timeout settings

```java
// Set network address lookup timeout (in milliseconds)
InetAddress address = InetAddress.getByName("example.com");  // Uses system default timeout

// Or set a custom timeout
System.setProperty("sun.net.spi.nameservice.provider.1", "dns,sun");
System.setProperty("sun.net.spi.nameservice.provider.2", "default");

// Java 9+ — set via networkaddress.cache.ttl
Security.setProperty("networkaddress.cache.ttl", "30");

// Use InetAddress with timeout (Java 9+)
InetAddress address = InetAddress.getByName("example.com");
// DNS resolution happens internally with system timeout
```

### Fix 3: Add hostname to /etc/hosts for local resolution

```bash
# Add entry to /etc/hosts
echo "127.0.0.1 myapp.local" | sudo tee -a /etc/hosts
echo "192.168.1.100 dbserver.local" | sudo tee -a /etc/hosts

# Or for Docker/Kubernetes environments
echo "172.17.0.2 mydatabase" | sudo tee -a /etc/hosts
```

### Fix 4: Verify DNS configuration and network connectivity

```bash
# Check current DNS configuration
cat /etc/resolv.conf

# Test DNS resolution
nslookup example.com
dig example.com

# Test network connectivity
ping -c 3 example.com
ping -c 3 8.8.8.8  # Test raw IP connectivity

# Check if DNS server is reachable
nslookup example.com 8.8.8.8  # Use Google's DNS server directly
```

### Fix 5: Cache resolved addresses to avoid repeated DNS lookups

```java
import java.net.InetAddress;
import java.util.concurrent.ConcurrentHashMap;

public class DnsCache {
    private static final ConcurrentHashMap<String, InetAddress> cache = new ConcurrentHashMap<>();

    public static InetAddress resolve(String hostname) throws UnknownHostException {
        return cache.computeIfAbsent(hostname, h -> {
            try {
                return InetAddress.getByName(h);
            } catch (UnknownHostException e) {
                throw new RuntimeException("DNS resolution failed for: " + h, e);
            }
        });
    }
}

// Usage
InetAddress address = DnsCache.resolve("example.com");
Socket socket = new Socket(address, 8080);
```

## Prevention Checklist

- Always verify hostname spelling before deployment.
- Configure reliable DNS servers in `/etc/resolv.conf`.
- Add frequently used internal hostnames to `/etc/hosts`.
- Use DNS caching for frequently resolved hostnames.
- Test DNS resolution as part of deployment health checks.
- Set appropriate DNS timeouts to avoid long hangs on unreachable hosts.

## Related Errors

- [SocketException](../socketexception) — general socket-related errors.
- [ConnectException](../connectexception) — connection refused by remote host.
- [SocketTimeoutException](../sockettimeoutexception) — connection or DNS resolution timed out.
- [NoRouteToHostException](../nortoethostexception) — no route to remote host.
