---
title: "[Solution] Java NullPointerException"
description: "Method Chaining on Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# an intermediate method in a chain returns null

A `an` is thrown when string city = order.getcustomer().getaddress().getcity();  // npe if any is null.

## Common Causes

```java
String city = order.getCustomer().getAddress().getCity();  // NPE if any is null
```

## Solutions

```java
// Fix: use Optional
String city = Optional.ofNullable(order)
    .map(Order::getCustomer).map(Customer::getAddress)
    .map(Address::getCity).orElse("Unknown");

// Fix: null check each step
String city = null;
if (order != null && order.getCustomer() != null) {
    Address a = order.getCustomer().getAddress();
    if (a != null) city = a.getCity();
}
```

## Prevention Checklist

- Limit chain depth to 2-3 calls.
- Use Optional for null-safe chaining.
- Use @NonNull annotations.

## Related Errors

[NullPointerException](nullpointerexception), [IllegalStateException](illegalstateexception)
