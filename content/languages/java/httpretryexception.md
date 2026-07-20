---
title: "[Solution] Java HttpRetryException — HTTP Manual Retry Fix"
description: "Fix Java HttpRetryException by implementing retry logic, checking response codes, handling redirects, and using HttpClient with retry handler."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# HttpRetryException — HTTP Manual Retry Fix

An `HttpRetryException` is thrown when an HTTP request needs to be retried manually. This occurs with `HttpURLConnection` when the server responds with a status code that requires client intervention, such as a redirect or authentication challenge.

## Description

`java.net.HttpRetryException` extends `IOException` and is thrown by `HttpURLConnection` when:

- A redirect (3xx) is received but auto-redirect is disabled
- An authentication challenge (407 Proxy Required) is received
- The response code indicates a retryable condition

Common message variants:

- `java.net.HttpRetryException: cannot retry due to server authentication`
- `java.net.HttpRetryException: Redirected but streaming is enabled`
- `java.net.HttpRetryException: Server returned HTTP response code: 302`

## Common Causes

```java
// Cause 1: Redirect received with streaming enabled
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setInstanceFollowRedirects(false);  // Disable auto-redirect
InputStream is = conn.getInputStream();  // HttpRetryException on 3xx

// Cause 2: Proxy authentication required (407)
HttpURLConnection conn = (HttpURLConnection) proxyUrl.openConnection();
InputStream is = conn.getInputStream();  // HttpRetryException for 407

// Cause 3: POST redirect without confirmation
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("POST");
conn.setDoOutput(true);
conn.getOutputStream().write(body);
int code = conn.getResponseCode();  // 302 redirect
InputStream is = conn.getInputStream();  // HttpRetryException

// Cause 4: Auto-redirect disabled for sensitive requests
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setInstanceFollowRedirects(false);
conn.setFollowRedirects(false);
// Must manually handle all 3xx responses

// Cause 5: Chunked transfer encoding with redirect
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setChunkedStreamingMode(1024);
conn.setInstanceFollowRedirects(false);
// Streaming mode prevents automatic redirect handling
```

## Solutions

### Fix 1: Enable automatic redirects

```java
// Wrong — manual redirect handling causes HttpRetryException
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setInstanceFollowRedirects(false);

// Correct — let HttpURLConnection handle redirects
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setInstanceFollowRedirects(true);  // default is true

// Or set globally
HttpURLConnection.setFollowRedirects(true);
```

### Fix 2: Handle redirects manually when auto-redirect is disabled

```java
public static String fetchWithRedirects(URL url, int maxRedirects) throws IOException {
    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.setInstanceFollowRedirects(false);

    int code = conn.getResponseCode();
    int redirects = 0;

    while ((code == 301 || code == 302 || code == 307 || code == 308)
            && redirects < maxRedirects) {
        String location = conn.getHeaderField("Location");
        conn.disconnect();

        url = new URL(location);
        conn = (HttpURLConnection) url.openConnection();
        conn.setInstanceFollowRedirects(false);
        code = conn.getResponseCode();
        redirects++;
    }

    if (code != 200) {
        throw new IOException("HTTP error code: " + code);
    }

    try (BufferedReader reader = new BufferedReader(
            new InputStreamReader(conn.getInputStream()))) {
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        return sb.toString();
    }
}
```

### Fix 3: Use HttpClient with built-in retry handler (Java 11+)

```java
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newBuilder()
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.com/api"))
    .GET()
    .build();

HttpResponse<String> response = client.send(request,
    HttpResponse.BodyHandlers.ofString());

// For retries, implement custom logic
public static <T> HttpResponse<T> sendWithRetry(HttpClient client,
        HttpRequest request, HttpResponse.BodyHandler<T> handler,
        int maxRetries) throws IOException, InterruptedException {
    IOException lastException = null;
    for (int i = 0; i <= maxRetries; i++) {
        try {
            HttpResponse<T> response = client.send(request, handler);
            if (response.statusCode() < 500) return response;
            lastException = new IOException("Server error: " + response.statusCode());
        } catch (IOException e) {
            lastException = e;
        }
        if (i < maxRetries) Thread.sleep(1000L * (i + 1));
    }
    throw lastException;
}
```

### Fix 4: Handle proxy authentication properly

```java
HttpURLConnection conn = (HttpURLConnection) url.openConnection(proxy);

// Set proxy auth
String auth = Base64.getEncoder().encodeToString(
    (proxyUser + ":" + proxyPass).getBytes());
conn.setRequestProperty("Proxy-Authorization", "Basic " + auth);

// Handle 407 manually if needed
int code = conn.getResponseCode();
if (code == 407) {
    String proxyAuth = conn.getHeaderField("Proxy-Authenticate");
    // Re-authenticate and retry
}
```

### Fix 5: Use non-chunked streaming for redirect-compatible POST

```java
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("POST");
conn.setDoOutput(true);
conn.setInstanceFollowRedirects(true);
conn.setFixedLengthStreamingMode(body.length);  // Use fixed length, not chunked

try (OutputStream os = conn.getOutputStream()) {
    os.write(body);
}

int code = conn.getResponseCode();  // Redirects handled automatically
```

## Prevention Checklist

- Enable `setInstanceFollowRedirects(true)` unless you specifically need manual redirect handling.
- Use `java.net.http.HttpClient` (Java 11+) for modern HTTP with built-in redirect support.
- Implement exponential backoff retry logic for 5xx server errors.
- Handle proxy authentication before making requests.
- Use fixed-length streaming instead of chunked mode when redirects are possible.

## Related Errors

- [IOException](../ioexception) — parent class for all I/O failures.
- [SocketTimeoutException](../sockettimeoutexception) — request timed out.
- [MalformedURLException](../malformedurlexception) — invalid URL format.
