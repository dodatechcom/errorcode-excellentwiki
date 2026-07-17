---
title: "[Solution] Stripe Rate Limit Error — Fix 429 Too Many Requests"
description: "Fix Stripe 429 rate limit errors. Implement proper retry logic and backoff strategies for Stripe API calls."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 3
---

A Stripe rate limit error occurs when you exceed the allowed number of API requests within a given time window. Stripe enforces per-key rate limits to maintain platform stability and fairness across all users.

## What This Error Means

Stripe returns HTTP 429 when you hit the rate limit. The response includes a `Retry-After` header telling you how many seconds to wait:

```
HTTP/1.1 429 Too Many Requests
Retry-After: 10
```

The error body looks like:

```json
{
  "error": {
    "type": "rate_limit_error",
    "message": "Too Many Requests"
  }
}
```

## Why It Happens

- Sending too many requests in a short time window
- Making concurrent requests without queuing
- Polling for status updates too frequently
- Processing bulk operations without proper batching
- Repeatedly retrying failed requests without backoff
- Running multiple server instances hitting the same key

## How to Fix It

### Implement Exponential Backoff

```javascript
async function stripeRequestWithRetry(fn, maxRetries = 5) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (error.statusCode === 429) {
        const retryAfter = error.headers['retry-after'] || Math.pow(2, attempt);
        console.log(`Rate limited. Retrying in ${retryAfter}s...`);
        await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
      } else {
        throw error;
      }
    }
  }
  throw new Error('Max retries exceeded');
}

// Usage
const balance = await stripeRequestWithRetry(() =>
  stripe.balance.retrieve()
);
```

### Use Stripe SDK Built-in Retries

```javascript
const stripe = require('stripe')('sk_test_your_key', {
  maxNetworkRetries: 3,
  timeout: 10000,
});
```

### Batch Operations with Bulk API

```python
import stripe
import time

# Process customers in batches
customers = stripe.Customer.list(limit=100)
for batch_start in range(0, 1000, 100):
    for customer in customers.auto_paging_iter():
        # Process each customer with proper pacing
        time.sleep(0.1)  # Add small delay between requests
```

### Monitor Rate Limit Headers

```javascript
// Stripe includes rate limit info in response headers
const response = await stripe.customers.list({ limit: 100 });
console.log('Rate Limit Remaining:', response.headers['stripe-ratelimit-remaining']);
```

## Common Mistakes

- Ignoring the `Retry-After` header and retrying immediately
- Using tight loops to poll for payment status
- Not using idempotency keys for retried requests
- Running multiple processes with the same API key
- Not implementing circuit breakers for sustained failures

## Related Pages

- [Stripe Authentication Error]({{< relref "/tools/stripe/stripe-authentication-error" >}}) — No API key provided or invalid key
- [Stripe Idempotency Error]({{< relref "/tools/stripe/stripe-idempotency-error" >}}) — Idempotency key mismatch
