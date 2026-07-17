---
title: "[Solution] Java ServletException / IllegalStateException Fix"
description: "Fix Java ServletException and IllegalStateException in servlet applications. Handle request lifecycle violations, async context errors, and state management issues."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ServletException / IllegalStateException

A `ServletException` is thrown when a servlet encounters an error during request processing, while `IllegalStateException` signals that a method has been invoked at an invalid point in the request lifecycle. Both are common in Java web applications using Servlet API or Spring MVC.

## Description

**ServletException** wraps errors that occur inside a servlet's `service()`, `doGet()`, or `doPost()` methods. **IllegalStateException** indicates that the servlet response has already been committed (headers sent) and further modifications are illegal.

Common variants:

- `javax.servlet.ServletException: ...`
- `java.lang.IllegalStateException: Cannot forward after response has been committed`
- `java.lang.IllegalStateException: getOutputStream() has already been called for this response`
- `java.lang.IllegalStateException: Response already set`

## Common Causes

```java
// Cause 1: Forwarding after response is committed
response.getWriter().write("Hello");
response.getRequestDispatcher("/other").forward(request, response);  // IllegalStateException

// Cause 2: Calling getOutputStream() after getWriter() (or vice versa)
PrintWriter out = response.getWriter();
ServletOutputStream stream = response.getOutputStream();  // IllegalStateException

// Cause 3: Async context timeout
@WebServlet(asyncSupported = true)
public class MyServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
        AsyncContext ctx = req.startAsync();
        ctx.start(() -> {
            Thread.sleep(60000);  // Takes too long, async times out
            ctx.complete();  // IllegalStateException: already timed out
        });
    }
}

// Cause 4: Request dispatched to wrong context
RequestDispatcher dispatcher = request.getRequestDispatcher("/other-app/page");
dispatcher.forward(request, response);  // May throw ServletException
```

## How to Fix

### Fix 1: Don't forward after writing to response

```java
// Wrong
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.getWriter().write("Partial");
    req.getRequestDispatcher("/template").forward(req, resp);  // IllegalStateException
}

// Correct — use forward FIRST, or use include
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    req.getRequestDispatcher("/template").forward(req, resp);
    // Or use include to combine responses
    req.getRequestDispatcher("/header").include(req, resp);
    req.getRequestDispatcher("/content").include(req, resp);
}
```

### Fix 2: Don't mix getWriter() and getOutputStream()

```java
// Wrong
PrintWriter out = response.getWriter();
ServletOutputStream stream = response.getOutputStream();  // IllegalStateException

// Correct — choose one and stick with it
// For text content:
PrintWriter out = response.getWriter();
out.write("Hello");

// For binary content:
ServletOutputStream stream = response.getOutputStream();
stream.write(bytes);
```

### Fix 3: Handle async context properly

```java
@WebServlet(urlPatterns = "/async", asyncSupported = true)
public class AsyncServlet extends HttpServlet {
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
        AsyncContext ctx = req.startAsync();
        ctx.setTimeout(30000);  // Set appropriate timeout

        ctx.start(() -> {
            try {
                // Do async work
                String result = processRequest();
                ctx.getResponse().getWriter().write(result);
            } catch (Exception e) {
                ctx.getResponse().getWriter().write("Error: " + e.getMessage());
            } finally {
                ctx.complete();  // Always complete the context
            }
        });
    }
}
```

### Fix 4: Check response state before modifying

```java
// Wrong — assumes response is not committed
response.setStatus(200);
response.getWriter().write("Data");
// ... later
response.setStatus(404);  // IllegalStateException if response committed

// Correct — check before modifying
if (!response.isCommitted()) {
    response.setStatus(404);
} else {
    log.warn("Response already committed, cannot change status");
}
```

### Fix 5: Use Spring's exception handling

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ServletException.class)
    public ResponseEntity<String> handleServletException(ServletException e) {
        return ResponseEntity.status(500).body("Servlet error: " + e.getMessage());
    }

    @ExceptionHandler(IllegalStateException.class)
    public ResponseEntity<String> handleIllegalState(IllegalStateException e) {
        return ResponseEntity.status(409).body("State conflict: " + e.getMessage());
    }
}
```

## Examples

This error commonly occurs when:

- A filter modifies the response and then a servlet tries to forward
- Using both JSP include and servlet forward in the same request
- Async servlet times out while still processing
- REST controller tries to redirect after already writing JSON body

## Related Errors

- [NullPointerException](nullpointerexception) — accessing null request/response objects
- [IOException](ioexception) — I/O errors during response writing
- [IllegalStateException](illegal-argument) — general invalid state violations
