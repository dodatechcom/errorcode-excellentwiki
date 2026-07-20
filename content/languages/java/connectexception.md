---
title: "[Solution] Java ConnectException — Connection Refused Fix"
description: "Fix Java ConnectException by verifying server is running, checking port number, reviewing firewall rules, and using proper connection timeouts."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ConnectException — Connection Refused Fix

A `ConnectException` is thrown when a connection to a remote host is refused. This occurs when the target server is not listening on the specified port, the server is not running, or a firewall is blocking the connection.

## Description

The `java.net.ConnectException` extends `SocketException` and indicates that the TCP connection attempt was actively refused by the remote host. The OS returns a RST packet when no process is listening on the target port, causing this exception.

Common message variants:

- `java.net.ConnectException: Connection refused`
- `java.net.ConnectException: Connection refused: connect`
- `java.net.ConnectException: Connection timed out` (when firewall silently drops)

Class hierarchy:

```
java.lang.Object
  └── java.lang.Throwable
        └── java.lang.Exception
              └── java.io.IOException
                    └── java.net.SocketException
                          └── java.net.ConnectException
```

## Common Causes

```java
// Cause 1: Server not running on target port
Socket socket = new Socket("localhost", 8080);  // ConnectException: Connection refused

// Cause 2: Server bound to different port
Socket socket = new Socket("localhost", 8080);  // Server is actually on 9090

// Cause 3: Server bound to different interface (e.g., 127.0.0.1 only)
Socket socket = new Socket("192.168.1.100", 8080);  // Server only listens on localhost

// Cause 4: Firewall dropping connection attempts
Socket socket = new Socket("10.0.0.50", 3306);  // Firewall blocks port 3306

// Cause 5: Server backlog queue is full
ServerSocket ss = new ServerSocket(8080, 1);  // Backlog of 1
// Multiple simultaneous connections exceed the backlog
```

## Solutions

### Fix 1: Verify server is running on the correct port

```java
// Check if server process is listening on the expected port
// Use command: netstat -tlnp | grep 8080

// In code — try connecting with a timeout
try {
    Socket socket = new Socket();
    socket.connect(new InetSocketAddress("localhost", 8080), 3000);
    System.out.println("Server is running on port 8080");
    socket.close();
} catch (ConnectException e) {
    System.err.println("Server is not running on port 8080");
    System.err.println("Start the server or check the configured port");
}
```

### Fix 2: Use configurable host and port

```java
// Hardcoded values are a common source of ConnectException
// Wrong
Socket socket = new Socket("localhost", 8080);

// Correct — use configuration
String host = config.getProperty("server.host", "localhost");
int port = Integer.parseInt(config.getProperty("server.port", "8080"));

Socket socket = new Socket();
socket.connect(new InetSocketAddress(host, port), 5000);
```

### Fix 3: Handle firewall and network issues

```java
// Check if the target is reachable before connecting
InetAddress address = InetAddress.getByName("example.com");
if (!address.isReachable(5000)) {
    System.err.println("Host is not reachable — check firewall and routing rules");
    return;
}

// If firewall is blocking, try different ports or ask admin to open the port
// Common firewall fixes:
// - iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
// - ufw allow 8080/tcp
```

### Fix 4: Implement retry logic with exponential backoff

```java
public Socket connectWithRetry(String host, int port, int maxRetries) throws IOException {
    int retryDelay = 1000;  // Start with 1 second

    for (int attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            Socket socket = new Socket();
            socket.connect(new InetSocketAddress(host, port), 3000);
            return socket;
        } catch (ConnectException e) {
            if (attempt == maxRetries) {
                throw new IOException("Failed to connect after " + maxRetries + " attempts", e);
            }
            System.err.println("Attempt " + attempt + "/" + maxRetries + " failed: " + e.getMessage());
            Thread.sleep(retryDelay);
            retryDelay = Math.min(retryDelay * 2, 30000);  // Cap at 30 seconds
        }
    }
    throw new IOException("Failed to connect");
}
```

## Prevention Checklist

- Always use connection timeouts with `socket.connect(address, timeout)`.
- Verify the server is running and listening on the expected port before connecting.
- Use configurable host/port values instead of hardcoding.
- Implement retry logic for transient connection failures.
- Check firewall rules if connections to remote hosts consistently fail.

## Related Errors

- [SocketException](../socketexception) — parent class for socket-related errors.
- [SocketTimeoutException](../sockettimeoutexception) — connection timed out.
- [UnknownHostException](../unknownhostexception) — hostname cannot be resolved.
- [NoRouteToHostException](../nortoethostexception) — no route to remote host.
