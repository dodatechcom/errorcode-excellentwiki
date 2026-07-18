---
title: "[Solution] Stripe Too Many Requests to API Error — How to Fix"
description: "Fix Stripe rate limit errors by implementing exponential backoff, caching API responses, batching requests, and respecting Retry-After headers"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Too Many Requests to API Error

This error means your application has exceeded Stripe's API rate limit. Stripe enforces per-key and per-IP rate limits to ensure fair usage and platform stability. When exceeded, requests return HTTP 429.

## Why It Happens

- Sending more than 100 read requests per second per API key
- Sending more than 100 write requests per second per API key
- Multiple server instances sharing the same API key without coordination
- Retry storms where failed requests are retried immediately without backoff
- Polling Stripe APIs in a tight loop without delays
- Batch operations that do not use Stripe's batch endpoints
- Webhook endpoints making synchronous API calls for each event

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "rate_limit",
    "message": "Too many requests hit the API too quickly."
  }
}
```

```
HTTP 429 Too Many Requests
Retry-After: 2
```

```
{
  "error": {
    "type": "api_error",
    "code": "rate_limit",
    "message": "An earlier request is still processing. Please retry after a few seconds."
  }
}
```

## How to Fix It

### 1. Implement Exponential Backoff

```javascript
const stripe = require('stripe')('sk_live_...');

async function stripeRequestWithRetry(fn, maxRetries = 5) {
  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (err.type === 'StripeRateLimitError') {
        const delay = Math.pow(2, attempt) * 1000 + Math.random() * 1000;
        const retryAfter = err.headers?.['retry-after'];
        const waitTime = retryAfter ? parseInt(retryAfter) * 1000 : delay;
        console.log(`Rate limited, retrying in ${waitTime}ms (attempt ${attempt + 1})`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
      } else {
        throw err;
      }
    }
  }
  throw new Error('Max retries exceeded for Stripe API request');
}

// Usage
const customer = await stripeRequestWithRetry(() =>
  stripe.customers.create({ email: 'user@example.com' })
);
```

### 2. Cache API Responses

```javascript
const NodeCache = require('node-cache');
const cache = new NodeCache({ stdTTL: 300 }); // 5-minute cache

async function getCustomer(customerId) {
  const cached = cache.get(`customer:${customerId}`);
  if (cached) return cached;

  const customer = await stripe.customers.retrieve(customerId);
  cache.set(`customer:${customerId}`, customer);
  return customer;
}

// Use cache for read-heavy operations
const customer = await getCustomer('cus_abc123');
```

### 3. Batch Similar Requests

```python
import stripe

# Instead of individual API calls for each customer
# Use auto-pagination to fetch all at once
customers = stripe.Customer.list(
    limit=100,
    email='user@example.com'
)

# Process all results in batches
for customer in customers.auto_paging_iter():
    process_customer(customer)
```

### 4. Spread Requests Over Time

```python
import time
import random

def process_payments(payment_ids):
    for pid in payment_ids:
        stripe.PaymentIntent.retrieve(pid)
        # Add jitter to avoid thundering herd
        time.sleep(0.01 + random.uniform(0, 0.01))
```

### 5. Monitor Rate Limit Usage

```javascript
// Log rate limit headers from every Stripe response
async function stripeWithMonitoring(fn) {
  const result = await fn();

  // The Stripe client includes rate limit info
  // Monitor these metrics in your observability system
  console.log('Stripe API call completed', {
    endpoint: fn.name,
    requestId: result.request_id
  });

  return result;
}
```

## Common Scenarios

- **Webhook handler calls API**: Each incoming webhook triggers multiple API calls to retrieve related objects. Cache frequently accessed objects and batch API calls.
- **Migration script**: Importing 10,000 customers in a loop. Use `stripe.Customer.create` with a delay between calls and implement retry with backoff.
- **Multi-service architecture**: Five services share one API key and collectively exceed the limit. Use separate restricted keys per service.

## Prevent It

- Always implement exponential backoff with jitter for Stripe API retries
- Cache read-only API responses (customers, products, prices) for at least 5 minutes
- Use Stripe's expand parameter to reduce the number of API calls needed per object

## Related Pages

- [Stripe Idempotency Error](/tools/stripe/stripe-idempotency-error)
- [Stripe Webhook Error](/tools/stripe/stripe-webhook-error)
- [Stripe API Key Invalid](/tools/stripe/stripe-api-key-invalid)
