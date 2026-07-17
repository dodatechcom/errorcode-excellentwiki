---
title: "[Solution] Stripe Webhook Error — Signature Verification Failed"
description: "Fix Stripe webhook signature verification errors. Resolve webhook authentication failures and event handling issues."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 8
---

A Stripe webhook error occurs when your server cannot verify that an incoming webhook event actually came from Stripe. Stripe signs every webhook with a unique signature so you can confirm the event is legitimate.

## What This Error Means

When webhook signature verification fails, your endpoint returns an error and Stripe marks the event as failed:

```
Webhook signature verification failed
```

This means the `Stripe-Signature` header on the incoming request does not match the expected signature computed from the raw request body and your webhook signing secret.

## Why It Happens

- The webhook signing secret is wrong or not set
- The request body has been modified (e.g., by middleware parsing JSON)
- You are reading the request as text instead of raw bytes
- The signing secret was rotated and not updated in your code
- A proxy or load balancer is modifying the request body
- You are testing with a tool that does not preserve the raw body

## How to Fix It

### Node.js / Express

```javascript
const express = require('express');
const stripe = require('stripe')('sk_test_your_key');

const app = express();

// CRITICAL: Use raw body for webhook route
app.post(
  '/webhook',
  express.raw({ type: 'application/json' }),
  (req, res) => {
    const sig = req.headers['stripe-signature'];
    const endpointSecret = process.env.STRIPE_WEBHOOK_SECRET;

    let event;
    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        sig,
        endpointSecret
      );
    } catch (err) {
      console.error('Webhook signature verification failed:', err.message);
      return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Handle the event
    switch (event.type) {
      case 'payment_intent.succeeded':
        console.log('Payment succeeded:', event.data.object.id);
        break;
      case 'payment_intent.payment_failed':
        console.log('Payment failed:', event.data.object.id);
        break;
    }

    res.json({ received: true });
  }
);
```

### Python / Flask

```python
import stripe
from flask import Flask, request

app = Flask(__name__)
endpoint_secret = os.environ['STRIPE_WEBHOOK_SECRET']

@app.route('/webhook', methods=['POST'])
def webhook():
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            request.data,  # raw bytes, not request.json
            sig_header,
            endpoint_secret
        )
    except stripe.error.SignatureVerificationError as e:
        return 'Invalid signature', 400

    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        print(f"Payment {payment_intent['id']} succeeded")

    return 'OK', 200
```

### Retrieve Your Webhook Secret

```bash
# From Stripe CLI
stripe listen --forward-to localhost:4242/webhook
# Outputs: whsec_...

# Or from Dashboard
# Developers > Webhooks > Select endpoint > Signing secret
```

### Test Webhook Locally

```bash
# Install Stripe CLI
stripe login

# Forward events to your local server
stripe listen --forward-to localhost:4242/webhook

# Trigger a test event
stripe trigger payment_intent.succeeded
```

## Common Mistakes

- Using `express.json()` middleware before the webhook route
- Reading `req.body` as parsed JSON instead of raw buffer
- Not including the full webhook secret including the `whsec_` prefix
- Mixing up test and production webhook secrets
- Not returning a 2xx response quickly (Stripe expects a response within 20 seconds)

## Related Pages

- [Stripe Authentication Error]({{< relref "/tools/stripe/stripe-authentication-error" >}}) — No API key provided or invalid key
- [Stripe Rate Limit Error]({{< relref "/tools/stripe/stripe-rate-limit" >}}) — Too Many Requests (429)
