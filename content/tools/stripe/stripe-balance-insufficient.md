---
title: "[Solution] Stripe Balance Insufficient Error — Not Enough Funds"
description: "Fix Stripe insufficient balance errors. Resolve Stripe account balance issues and pending funds problems."
tools: ["stripe"]
error-types: ["tool-error"]
severities: ["error"]
weight: 10
---

A Stripe balance insufficient error occurs when your Stripe account does not have enough available funds to complete a payout or transfer. This is different from a card decline due to customer insufficient funds.

## What This Error Means

When your Stripe account balance is too low, the API returns:

```json
{
  "error": {
    "type": "invalid_request_error",
    "code": "balance_insufficient",
    "message": "The amount you are attempting to transfer exceeds your available balance"
  }
}
```

Stripe distinguishes between your `available` balance (funds that can be paid out) and `pending` balance (funds still being processed).

## Why It Happens

- Attempting a payout larger than your available balance
- Pending funds have not settled yet (typically 2-7 business days)
- Funds are held due to Stripe's rolling reserve
- Previous payouts or refunds reduced your available balance
- Dispute or chargeback holds have locked some funds

## How to Fix It

### Check Your Balance

```javascript
const balance = await stripe.balance.retrieve();

console.log('Available:', balance.available);
console.log('Pending:', balance.pending);

// Available funds you can payout
const availableAmount = balance.available[0].amount;
console.log(`You can payout up to: $${availableAmount / 100}`);
```

### Safe Payout with Balance Check

```javascript
async function safePayout(amount, currency = 'usd') {
  const balance = await stripe.balance.retrieve();
  const available = balance.available.find(
    b => b.currency === currency
  );

  if (!available || available.amount < amount) {
    const availAmount = available ? available.amount / 100 : 0;
    throw new Error(
      `Insufficient balance. Available: $${availAmount}, ` +
      `Requested: $${amount / 100}`
    );
  }

  return stripe.transfers.create({
    amount,
    currency,
    destination: 'acct_connected_account_id',
  });
}
```

### Python Example

```python
import stripe

balance = stripe.Balance.retrieve()

# Check available funds
available_usd = next(
    (b for b in balance.available if b.currency == 'usd'),
    None
)

if available_usd and available_usd.amount >= 5000:
    # Proceed with payout
    stripe.Payout.create(amount=5000, currency='usd')
else:
    avail = available_usd.amount / 100 if available_usd else 0
    print(f"Insufficient balance. Available: ${avail}")
```

### Monitor Balance with Webhooks

```javascript
// Listen for balance changes
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  const event = stripe.webhooks.constructEvent(
    req.body,
    req.headers['stripe-signature'],
    process.env.STRIPE_WEBHOOK_SECRET
  );

  if (event.type === 'balance.available') {
    const balance = event.data.object;
    const available = balance.available[0].amount;
    if (available < 10000) {
      alertAdmin(`Low balance: $${available / 100}`);
    }
  }

  res.json({ received: true });
});
```

### Set Up Balance Alerts

```javascript
async function checkAndAlertBalance() {
  const balance = await stripe.balance.retrieve();
  const available = balance.available[0].amount;

  if (available < 50000) { // Less than $500
    console.warn(
      `Warning: Low Stripe balance. ` +
      `Available: $${available / 100}`
    );
  }
}

// Run daily
setInterval(checkAndAlertBalance, 24 * 60 * 60 * 1000);
```

## Common Mistakes

- Attempting payouts without checking available balance first
- Not accounting for pending funds that are not yet available
- Ignoring rolling reserve requirements
- Not monitoring balance before high-volume payout days
- Confusing pending balance with available balance

## Related Pages

- [Stripe Card Declined]({{< relref "/tools/stripe/stripe-card-declined" >}}) — Your card was declined
- [Stripe Payment Intent Failed]({{< relref "/tools/stripe/stripe-payment-intent-failed" >}}) — PaymentIntent confirmation failed
