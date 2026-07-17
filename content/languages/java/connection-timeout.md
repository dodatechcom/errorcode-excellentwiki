---
title: "[Solution] Java ConnectException: Connection Timed Out Fix"
description: "Fix Java ConnectException: Connection timed out. Increase timeouts, check network connectivity, verify host/port, and handle connection failures gracefully."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ConnectException: Connection Timed Out

A `java.net.ConnectException: Connection timed out` is thrown when a TCP connection attempt to a remote host does not complete within the configured timeout period. The OS tried to establish a TCP connection but the server didn't respond in time, the host was unreachable, or a firewall silently dropped the packets.

## Description

Unlike `Connection refused` (which means the server actively rejected the connection), `Connection timed out` means no response was received at all. This typically indicates a network-level issue.

Common variants:

- `java.net.ConnectException: Connection timed out`
- `java.net.ConnectException: connect timed out`
- `java.net.SocketTimeoutException: connect timed out`
- `org.apache.http.conn.ConnectTimeoutException: Connect to ... timed out`

## Common Causes

```java
// Cause 1: Server is not running or wrong port
Socket socket = new Socket();
socket.connect(new InetSocketAddress("localhost", 9999), 5000);  // timeout

// Cause 2: Firewall blocking the connection
URL url = new URL("https://api.example.com/data");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setConnectTimeout(5000);
conn.connect();  // ConnectException if firewall blocks

// Cause 3: DNS resolution is slow or failing
// DNS resolves but the host doesn't respond
URL url = new URL("https://slow-server.example.com");
url.openConnection().getInputStream();  // may timeout

// Cause 4: Server behind load balancer is down
// Load balancer IP resolves but all backends are down
```

## How to Fix

### Fix 1: Set appropriate timeouts

```java
// Wrong — no timeout, blocks forever
URL url = new URL("https://api.example.com/data");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
InputStream is = conn.getInputStream();

// Correct — set both connect and read timeouts
URL url = new URL("https://api.example.com/data");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setConnectTimeout(5000);   // 5 seconds to establish connection
conn.setReadTimeout(30000);     // 30 seconds to read response
InputStream is = conn.getInputStream();
```

### Fix 2: Verify network connectivity

```bash
# Check if the host is reachable
ping api.example.com

# Check if the port is open
telnet api.example.com 443

# Or use nc (netcat)
nc -zv api.example.com 443

# Check DNS resolution
nslookup api.example.com
```

### Fix 3: Use Apache HttpClient with timeout configuration

```java
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

RequestConfig config = RequestConfig.custom()
    .setConnectTimeout(5000)
    .setSocketTimeout(30000)
    .setConnectionRequestTimeout(5000)
    .build();

CloseableHttpClient client = HttpClients.custom()
    .setDefaultRequestConfig(config)
    .build();

HttpGet request = new HttpGet("https://api.example.com/data");
try (CloseableHttpResponse response = client.execute(request)) {
    // handle response
}
```

### Fix 4: Implement retry with backoff

```java
public <T> T executeWithRetry(Callable<T> operation, int maxRetries) {
    for (int attempt = 1; attempt <= maxRetries; attempt++) {
        try {
            return operation.call();
        } catch (ConnectException e) {
            if (attempt == maxRetries) throw new RuntimeException("Max retries exceeded", e);
            long delay = (long) Math.min(1000 * Math.pow(2, attempt), 30000);
            Thread.sleep(delay);
        }
    }
    throw new RuntimeException("Max retries exceeded");
}
```

### Fix 5: Use CompletableFuture with timeout

```java
import java.util.concurrent.*;

ExecutorService executor = Executors.newSingleThreadExecutor();
CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
    URL url = new URL("https://api.example.com/data");
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setConnectTimeout(5000);
    conn.setReadTimeout(10000);
    return new String(conn.getInputStream().readAllBytes());
}, executor);

try {
    String result = future.get(15, TimeUnit.SECONDS);
} catch (TimeoutException e) {
    future.cancel(true);
    throw new ConnectException("Request timed out after 15 seconds");
}
```

## Examples

This error commonly occurs when:

- The target server is behind a firewall that silently drops packets
- Connecting to a wrong port where no service is listening
- DNS resolves to an IP but the server at that IP is down
- Network switch or router is malfunctioning

## Related Errors

- [Connection refused](#) — server actively rejects the connection (port not listening)
- [SocketTimeoutException](#) — read timeout after connection is established
- [UnknownHostException](#) — DNS resolution failure
