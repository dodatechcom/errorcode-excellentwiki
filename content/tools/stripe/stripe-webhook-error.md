---
title: "[Solution] Stripe Webhook Signature Verification Failed Error — How to Fix"
description: "Fix Stripe webhook signature verification errors by using the correct secret, handling raw body correctly, and validating timestamp and payload integrity"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Webhook Signature Verification Failed Error

This error means your webhook endpoint could not verify the signature of the incoming event from Stripe. Stripe signs every webhook with a secret key, and your endpoint must validate this signature to confirm the event is authentic.

## Why It Happens

- The `STRIPE_WEBHOOK_SECRET` environment variable is incorrect or missing
- The webhook endpoint is parsing the request body as JSON before signature verification
- The webhook secret was rotated and the old secret is still in use
- The request body was modified by middleware (e.g., body-parser)
- The webhook is receiving events from a different Stripe endpoint than expected
- The signature header is missing or malformed
- Clock skew causes the timestamp verification to fail

## Common Error Messages

```
No signatures found matching the expected signature
```

```
Webhook signature verification failed
```

```
timestamp_tolerance exceeded
```

```
Error: No signatures found matching the expected signature for payload
```

## How to Fix It

### 1. Use Raw Body for Signature Verification

```javascript
// Express.js — CRITICAL: use raw body for Stripe
const express = require('express');
const stripe = require('stripe')('sk_live_...');

const app = express();

// Use raw body for the webhook endpoint only
app.post('/webhook',
  express.raw({ type: 'application/json' }),
  (req, res) => {
    const sig = req.headers['stripe-signature'];
    let event;

    try {
      event = stripe.webhooks.constructEvent(
        req.body,  // Must be raw Buffer, NOT parsed JSON
        sig,
        process.env.STRIPE_WEBHOOK_SECRET
      );
    } catch (err) {
      console.error('Webhook signature verification failed:', err.message);
      return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    handleEvent(event);
    res.json({ received: true });
  }
);
```

### 2. Verify the Correct Webhook Secret

```bash
# Check your webhook secret in Stripe Dashboard
# Go to Developers > Webhooks > Select endpoint > Signing secret

# The secret starts with whsec_...
echo $STRIPE_WEBHOOK_SECRET

# For test mode: whsec_test_...
# For live mode: whsec_...
```

### 3. Handle Timestamp Tolerance

```python
import stripe
from django.conf import settings

def verify_webhook(payload, sig_header):
    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET,
            tolerance=300  # Allow 5 minutes of clock skew
        )
        return event
    except stripe.error.SignatureVerificationError as e:
        print(f"Invalid signature: {e}")
        return None
    except ValueError as e:
        print(f"Invalid payload: {e}")
        return None
```

### 4. Test with Stripe CLI

```bash
# Install Stripe CLI
stripe listen --forward-to localhost:4242/webhook

# This gives you a webhook signing secret for testing
# Use it as STRIPE_WEBHOOK_SECRET

# In another terminal, trigger a test event
stripe trigger payment_intent.succeeded
```

### 5. Debug Webhook Signature

```javascript
// Log the signature header for debugging
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const sig = req.headers['stripe-signature'];
  console.log('Stripe-Signature:', sig);
  console.log('Body type:', typeof req.body);
  console.log('Body is Buffer:', Buffer.isBuffer(req.body));

  // Verify
  try {
    const event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );
    console.log('Event verified:', event.type);
  } catch (err) {
    console.error('Verification failed:', err.message);
  }

  res.json({ received: true });
});
```

## Common Scenarios

- **Body parser mismatch**: The global body parser middleware parses the body as JSON before the webhook handler. Use `express.raw()` specifically for the webhook route.
- **Secret rotation**: You regenerated the webhook secret in Stripe but did not update the server. Both old and new secrets must be supported during the transition.
- **Proxy modifying the body**: A reverse proxy or CDN modifies headers or the body. Configure the proxy to pass the raw body through unchanged.

## Prevent It

- Always use `express.raw()` (Node.js) or equivalent raw body parser for webhook endpoints
- Store webhook secrets in environment variables, never hardcoded in source
- Use the Stripe CLI to test webhooks locally before deploying to production

## Related Pages

- [Stripe Rate Limit Error](/tools/stripe/stripe-rate-limit-error)
- [Stripe Idempotency Error](/tools/stripe/stripe-idempotency-error)
- [Stripe Charge Disputed](/tools/stripe/stripe-charge-disputed)
