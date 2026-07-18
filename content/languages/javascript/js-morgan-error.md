---
title: "Solved JavaScript Morgan Error — How to Fix"
date: 2026-03-20T14:50:10+00:00
description: "Learn how to resolve JavaScript Morgan HTTP logger middleware configuration and output errors."
categories: ["javascript"]
keywords: ["morgan error", "morgan logger", "http logging", "express logger", "morgan middleware"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

Morgan errors occur when the HTTP request logger middleware encounters invalid format strings, stream issues, or configuration conflicts. Morgan's pre-defined formats may not match your logging requirements.

Common causes include:
- Invalid format string in Morgan configuration
- Stream not writable or closed
- Missing request/response properties in custom formats
- Logging conflicts with other middleware
- Token functions returning undefined

## Common Error Messages

```
Error: invalid format: undefined
```

```
Error: write after end
```

```
TypeError: Cannot read property 'status' of undefined
```

## How to Fix It

### 1. Configure Morgan Formats

Set up Morgan with appropriate logging formats.

```javascript
import morgan from "morgan";
import fs from "fs";

// Pre-defined formats
// combined - Standard Apache combined log output
// common - Standard Apache common log output
// dev - Concise output colored by response status
// short - Short default response time
// tiny - Minimal output

// Basic usage
app.use(morgan("dev"));

// To file
const accessLogStream = fs.createWriteStream(
  path.join(__dirname, "access.log"),
  { flags: "a" }
);

app.use(morgan("combined", { stream: accessLogStream }));

// Skip certain requests
app.use(morgan("combined", {
  skip: (req, res) => res.statusCode < 400
}));

// Custom format
morgan.token("id", (req) => req.id);
morgan.token("user", (req) => req.user?.id || "anonymous");

app.use(morgan(":id :user :method :url :status :response-time ms"));
```

### 2. Implement Custom Tokens

Create custom logging tokens.

```javascript
import morgan from "morgan";

// Custom tokens
morgan.token("content-length", (req, res) => {
  return res.get("Content-Length") || "-";
});

morgan.token("remote-addr", (req) => {
  return req.ip || req.connection.remoteAddress;
});

morgan.token("timestamp", () => {
  return new Date().toISOString();
});

morgan.token("request-body", (req) => {
  return JSON.stringify(req.body).substring(0, 200);
});

// Custom format with tokens
const customFormat = ":timestamp :remote-addr :method :url :status :response-time ms";

app.use(morgan(customFormat));

// Conditional logging
app.use(morgan(customFormat, {
  skip: (req, res) => {
    return req.url.includes("/health") || req.url.includes("/metrics");
  }
}));
```

### 3. Handle Stream Errors

Properly manage log streams.

```javascript
import morgan from "morgan";
import fs from "fs";

// Create stream with error handling
function createLogStream(filename) {
  const stream = fs.createWriteStream(filename, { flags: "a" });
  
  stream.on("error", (err) => {
    console.error("Log stream error:", err);
  });
  
  return stream;
}

// Use stream
const logStream = createLogStream("access.log");
app.use(morgan("combined", { stream: logStream }));

// Multiple streams
app.use(morgan("combined", {
  stream: createLogStream("combined.log")
}));

app.use(morgan("dev", {
  stream: process.stdout
}));

// Rotation (using winston or pino for production)
import winston from "winston";

const winstonStream = {
  write: (message) => {
    winston.info(message.trim());
  }
};

app.use(morgan("combined", { stream: winstonStream }));
```

## Common Scenarios

### Scenario 1: Environment-Based Logging

Configure different logging for dev/prod:

```javascript
import morgan from "morgan";

// Development
if (process.env.NODE_ENV === "development") {
  app.use(morgan("dev"));
} else {
  // Production - combined format
  app.use(morgan("combined", {
    skip: (req, res) => res.statusCode < 400
  }));
}

// Custom skip for health checks
app.use(morgan("combined", {
  skip: (req, res) => {
    return req.url === "/health" || req.url === "/ready";
  }
}));
```

### Scenario 2: Structured JSON Logging

Output logs as JSON:

```javascript
import morgan from "morgan";

const jsonFormat = (tokens, req, res) => {
  return JSON.stringify({
    timestamp: new Date().toISOString(),
    method: tokens.method(req, res),
    url: tokens.url(req, res),
    status: tokens.status(req, res),
    contentLength: tokens.res(req, res, "content-length"),
    responseTime: tokens["response-time"](req, res),
    userAgent: tokens["user-agent"](req, res),
    remoteAddr: tokens["remote-addr"](req, res)
  });
};

app.use(morgan(jsonFormat));
```

## Prevent It

- Use `"combined"` format for production logging to files
- Skip health check endpoints to reduce log noise
- Use custom tokens to add request context like user ID
- Create log streams with error handlers for production
- Use structured JSON format for log aggregation services