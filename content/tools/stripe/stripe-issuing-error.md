---
title: "[Solution] Stripe Issuing Card Authorization Error — How to Fix"
description: "Fix Stripe Issuing card authorization errors by configuring spending controls, updating card status, handling insufficient balance, and debugging authorization rules"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Stripe Issuing Card Authorization Error

This error means a Stripe Issuing card transaction was declined during authorization. This can happen due to spending limits, card status issues, merchant category restrictions, or insufficient funds in the Stripe balance.

## Why It Happens

- The card's spending limit has been exceeded
- The card is paused or not active
- The merchant category code (MCC) is blocked by spending controls
- The Stripe account balance is insufficient to cover the authorization
- The card does not have enough remaining credit
- The transaction velocity limit was reached
- The merchant is in a blocked country
- The card was frozen due to suspicious activity

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "card_declined",
    "message": "The card has been declined."
  }
}
```

```
{
  "authorization": {
    "status": "declined",
    "request_history": [{
      "status": "declined",
      "reason": "exceeds_authorization_amount"
    }]
  }
}
```

```
{
  "authorization": {
    "status": "closed",
    "authorization_method": "online",
    "amount": 5000,
    "currency": "usd"
  }
}
```

## How to Fix It

### 1. Check Card Status and Limits

```javascript
const card = await stripe.issuing.cards.retrieve('ic_abc123');

console.log('Status:', card.status);
console.log('Spending limits:', card.spending_controls);
console.log('Currency:', card.currency);
```

### 2. Update Spending Controls

```javascript
// Increase the spending limit for a card
const card = await stripe.issuing.cards.update('ic_abc123', {
  spending_controls: {
    allowed_categories: [
      'airlines',
      'car_rental',
      'lodging',
      'restaurants',
      'gas_stations'
    ],
    spending_limits: [
      {
        amount: 100000,  // $1,000.00
        interval: 'monthly'
      },
      {
        amount: 10000,   // $100.00
        interval: 'daily'
      }
    ]
  }
});
```

### 3. Pause and Unpause Cards

```javascript
// Pause a card
await stripe.issuing.cards.update('ic_abc123', {
  status: 'paused'
});

// Unpause a card
await stripe.issuing.cards.update('ic_abc123', {
  status: 'active'
});
```

### 4. Approve Pending Authorizations

```javascript
// Approve a pending authorization
await stripe.issuing.authorizations.approve('ia_abc123');

// Decline a pending authorization
await stripe.issuing.authorizations.decline('ia_abc123');
```

### 5. Monitor Authorization Events

```javascript
// Listen for authorization events via webhooks
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const event = stripe.webhooks.constructEvent(
    req.body,
    req.headers['stripe-signature'],
    process.env.STRIPE_WEBHOOK_SECRET
  );

  if (event.type === 'issuing_authorization.request') {
    const auth = event.data.object;
    console.log('Authorization request:', auth.id);
    console.log('Amount:', auth.amount, auth.currency);
    console.log('Merchant:', auth.merchant_data.name);
    console.log('MCC:', auth.merchant_data.category);

    // Auto-approve based on your business rules
    if (auth.amount < 5000) { // Under $50
      stripe.issuing.authorizations.approve(auth.id);
    }
  }

  if (event.type === 'issuing_authorization.created') {
    const auth = event.data.object;
    console.log('New authorization:', auth.id, auth.status);
  }

  res.json({ received: true });
});
```

## Common Scenarios

- **Employee card overspent**: An employee's card hit the monthly limit. Increase the limit or issue a new card with higher controls.
- **Blocked merchant category**: A card is restricted to restaurants but the employee tries to use it at a gas station. Update the allowed categories.
- **Insufficient balance**: The Stripe account does not have enough funds to cover the authorization. Ensure the balance is topped up before authorizations are processed.

## Prevent It

- Set granular spending limits per card (daily, weekly, monthly) based on employee roles
- Use merchant category restrictions to limit where cards can be used
- Implement real-time alerts for authorizations over a threshold amount

## Related Pages

- [Stripe Balance Error](/tools/stripe/stripe-balance-error)
- [Stripe Account Restricted](/tools/stripe/stripe-account-restricted)
- [Stripe Charge Disputed](/tools/stripe/stripe-charge-disputed)
