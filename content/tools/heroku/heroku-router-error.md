---
title: "[Solution] Heroku Router Timeout (H12 Error) — How to Fix"
description: "Fix Heroku H12 request timeout errors by optimizing slow endpoints, enabling request queuing, using background jobs, tuning timeouts, and scaling dynos for traffic spikes."
tools: ["heroku"]
error-types: ["router-error"]
severities: ["error"]
weight: 5
comments: true
---

A Heroku H12 router timeout error occurs when a web request takes longer than 30 seconds to respond. Heroku's HTTP router terminates the connection and returns a 503 error to the client.

## What This Error Means

The Heroku router is the front-end proxy that routes HTTP requests to your dynos. It enforces a 30-second timeout for all requests. If your application does not send a response within 30 seconds, the router returns a 503 Service Unavailable H12 error. This timeout is a platform limit and cannot be increased.

H12 errors indicate that your application is taking too long to process requests. This is typically caused by slow database queries, external API calls, or CPU-intensive operations. Requests that block for more than 30 seconds are terminated, and the client receives an error.

## Why It Happens

- Slow database queries that take more than 30 seconds
- External API calls that hang or respond slowly
- Large file uploads or downloads that exceed the timeout
- CPU-intensive operations (image processing, report generation) running in the request cycle
- Dyno is overloaded and requests queue up waiting for a worker
- Memory swapping causes requests to slow down significantly
- Inefficient code with N+1 queries or O(n²) algorithms
- Database connection pool exhaustion causes requests to wait for connections

## Common Error Messages

```
at=error code=H12 desc="Request timeout" method=GET path="/reports/generate"
# or
at=error code=H12 desc="Request timeout" method=POST path="/api/upload"
# or
at=error code=H25 desc="HTTP Restriction" — triggered when too many H12 errors occur
# or
service=30000ms status=503 bytes=0 — the request took exactly 30 seconds
```

## How to Fix It

### 1. Identify Slow Endpoints

```bash
# View H12 errors in logs
heroku logs -a my-app --tail | grep "code=H12"

# Use Heroku Logging Addon for structured logs
heroku addons:create logdna -a my-app

# Query recent H12 errors
heroku logs -a my-app -n 1000 | grep "H12" | awk '{print $7}' | sort | uniq -c | sort -rn
```

### 2. Move Slow Operations to Background Jobs

```python
# Instead of generating a report in the request cycle:
def generate_report_sync(request):
    data = process_large_dataset()  # Takes 20-40 seconds
    return render_report(data)      # Returns H12 error!

# Use a background job instead:
from rq import Queue
from redis import Redis

def generate_report_async(request):
    job = queue.enqueue('tasks.generate_report', request.user.id)
    return {"job_id": job.id, "status": "processing"}

# The client polls for the result:
def get_report_result(request, job_id):
    job = queue.fetch_job(job_id)
    if job.is_finished:
        return job.result
    return {"status": "still processing"}
```

### 3. Optimize Slow Database Queries

```python
# Add database indexes
# Instead of a full table scan:
# CREATE INDEX CONCURRENTLY idx_orders_user_date ON orders (user_id, created_at);

# Use select_related/prefetch_related in Django
# Instead of:
orders = Order.objects.filter(user=user)  # N+1 queries
# Use:
orders = Order.objects.filter(user=user).select_related('product')

# Add pagination for large result sets
# Instead of:
products = Product.objects.all()  # Could return millions
# Use:
products = Product.objects.all()[:100]  # Limit results
```

### 4. Set Up Request Queuing

```bash
# Add more web dynos to handle concurrent requests
heroku ps:scale web=5 -a my-app

# Use a larger dyno type for better throughput
heroku ps:type web=standard-2x -a my-app
```

### 5. Implement Timeouts in External API Calls

```python
import requests

# Always set timeouts on external API calls
try:
    response = requests.get(
        'https://api.example.com/data',
        timeout=5  # Raise exception after 5 seconds
    )
except requests.Timeout:
    # Return a reasonable default or error
    return {"error": "External service timed out"}, 504
```

### 6. Use Streaming Responses

```python
# For large responses, use streaming instead of buffering

# Flask example
from flask import Response
import time

def stream_large_dataset():
    for row in get_large_dataset():  # Generator
        yield format_row(row)
        time.sleep(0.01)  # Yield to event loop

@app.route('/export')
def export():
    return Response(
        stream_large_dataset(),
        mimetype='text/csv'
    )
```

```javascript
// Node.js example
app.get('/stream', (req, res) => {
  res.writeHead(200, {
    'Content-Type': 'text/plain',
    'Transfer-Encoding': 'chunked'
  });
  
  for (const chunk of largeDataset()) {
    res.write(chunk);
  }
  res.end();
});
```

### 7. Enable HTTP/2 for Multiplexing

```bash
# HTTP/2 allows multiple concurrent requests on one connection
# Enable on Heroku:
heroku features:enable http2 -a my-app

# Verify:
heroku features -a my-app | grep http2
```

### 8. Use CDN for Static Assets

```bash
# Set up a CDN to serve static assets
heroku config:set CDN_URL=https://assets.example.com -a my-app

# Add caching headers for static assets
# Nginx/Apache config: add Cache-Control: public, max-age=31536000
```

## Common Scenarios

### Report Generation in Request Cycle

A reporting endpoint aggregates millions of database records to generate a PDF. This takes 45 seconds on average. Every request triggers an H12 timeout. The fix is to move report generation to a background job (Sidekiq, RQ, etc.) and have the client poll for the result.

### Slow External API Integration

A checkout endpoint calls a third-party payment gateway that occasionally takes 35 seconds to respond. Hero's 30-second timeout kills the request. Add a 10-second timeout on the external call and return a friendly error if the payment gateway is slow.

### Unoptimized Database Query

An e-commerce dashboard loads all orders for the last year without pagination or proper indexing. The query takes 25 seconds. Add indexes on `created_at` and `user_id`, paginate results, and use `select_related` for joins.

## Prevent It

- Monitor H12 error rates with Heroku Metrics or a logging addon
- Set up alerts when H12 errors exceed a threshold (e.g., 1% of requests)
- Move all long-running operations to background jobs
- Set timeouts on all external API calls
- Use pagination on all list endpoints
- Add database indexes for frequently queried columns
- Load test your application to identify slow endpoints before deployment
- Use APM tools (New Relic, Scout, AppSignal) to trace slow requests
- Keep web dyno CPU utilization below 70% with proper scaling

## Related Pages

- [Heroku Dyno Error](/tools/heroku/heroku-dyno-error)
- [Heroku SSL Error](/tools/heroku/heroku-ssl-error)
- [Heroku Rate Limit Error](/tools/heroku/heroku-rate-limit-error)
