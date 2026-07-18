---
title: "[Solution] Stripe Insufficient Stripe Balance Error — How to Fix"
description: "Fix Stripe insufficient balance errors by checking available funds, resolving holds, adjusting payout timing, and managing rolling reserves"
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 10
comments: true
---

# Stripe Insufficient Stripe Balance Error

This error means your Stripe account does not have enough available funds to complete a payout, transfer, or refund. Stripe holds funds during processing and dispute periods, reducing the amount available for immediate use.

## Why It Happens

- Pending charges have not yet settled (2-7 business day hold)
- Refunds or dispute holds have reduced available balance
- A rolling reserve is withholding a percentage of each charge
- The requested payout exceeds the available balance
- Stripe's minimum payout threshold has not been met
- The payout bank account was recently changed and funds are in transit
- Multiple simultaneous payout requests compete for the same balance

## Common Error Messages

```
{
  "error": {
    "type": "invalid_request_error",
    "code": "balance_insufficient",
    "message": "The amount you are attempting to transfer exceeds your available balance."
  }
}
```

```
{
  "error": {
    "type": "invalid_request_error",
    "message": "Insufficient funds in your Stripe balance for this payout."
  }
}
```

```
{
  "object": "balance",
  "available": [{"amount": 0, "currency": "usd"}],
  "pending": [{"amount": 50000, "currency": "usd"}]
}
```

## How to Fix It

### 1. Check Your Full Balance

```javascript
const balance = await stripe.balance.retrieve();

console.log('Available:', balance.available);
console.log('Pending:', balance.pending);
console.log('Connect reserved:', balance.connect_reserved);

// Available funds for payout
const availableUSD = balance.available.find(b => b.currency === 'usd');
console.log('Available for payout:', availableUSD?.amount / 100 || 0);
```

### 2. Safe Payout with Balance Check

```python
import stripe

balance = stripe.Balance.retrieve()

available_usd = next(
    (b for b in balance.available if b.currency == 'usd'),
    None
)

payout_amount = 10000  # $100.00

if not available_usd or available_usd.amount < payout_amount:
    avail = available_usd.amount / 100 if available_usd else 0
    raise Exception(
        f"Insufficient balance. Available: ${avail}, Requested: ${payout_amount / 100}"
    )

# Proceed with payout
payout = stripe.Payout.create(amount=payout_amount, currency='usd')
print(f"Payout created: {payout.id}")
```

### 3. Reduce Rolling Reserve

```javascript
// Check if a reserve is holding funds
const balance = await stripe.balance.retrieve();
const reserved = balance.connect_reserved.find(b => b.currency === 'usd');

if (reserved) {
  console.log('Reserved amount:', reserved.amount / 100);
}

// Contact Stripe support to review reserve settings
// via the Dashboard or email
```

### 4. Delay Payout Until Funds Settle

```javascript
// Set automatic payout schedule to weekly instead of daily
await stripe.accounts.update('acct_abc123', {
  settings: {
    payouts: {
      schedule: {
        interval: 'weekly',
        weekly_anchor: 'friday'
      }
    }
  }
});
```

### 5. Monitor Balance via Webhooks

```javascript
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const event = stripe.webhooks.constructEvent(
    req.body,
    req.headers['stripe-signature'],
    process.env.STRIPE_WEBHOOK_SECRET
  );

  if (event.type === 'balance.available') {
    const balance = event.data.object;
    const available = balance.available[0].amount;
    if (available < 10000) { // Less than $100
      alertAdmin(`Low Stripe balance: $${available / 100}`);
    }
  }

  res.json({ received: true });
});
```

## Common Scenarios

- **Holiday payout**: A merchant wants to payout all available funds before Christmas, but pending charges from the weekend have not settled. Check available balance and schedule the payout for Tuesday.
- **High refund period**: After a product recall, 30% of charges are refunded, leaving little available balance. Wait for refunds to settle before initiating payouts.
- **Connected account platform**: A marketplace platform tries to transfer funds to a connected account, but the platform's own balance is insufficient. Ensure the platform collects funds before distributing.

## Prevent It

- Monitor available balance continuously and alert when it drops below your minimum payout threshold
- Use weekly payout schedules instead of daily if charges take time to settle
- Keep a buffer in the Stripe account by setting a minimum payout balance

## Related Pages

- [Stripe Payout Error](/tools/stripe/stripe-payout-error)
- [Stripe Charge Disputed](/tools/stripe/stripe-charge-disputed)
- [Stripe Account Restricted](/tools/stripe/stripe-account-restricted)
