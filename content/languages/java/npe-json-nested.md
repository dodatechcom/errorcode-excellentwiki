---
title: "[Solution] Java NullPointerException"
description: "JSON Null Nested Field Access"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# accessing nested fields of objects from JSON where intermediate objects are null

A `accessing` is thrown when string city = order.getcustomer().getaddress().getcity();  // npe.

## Common Causes

```java
String city = order.getCustomer().getAddress().getCity();  // NPE
```

## Solutions

```java
// Fix: Optional chaining
String city = Optional.ofNullable(order)
    .map(Order::getCustomer).map(Customer::getAddress)
    .map(Address::getCity).orElse("Unknown");

// Fix: JsonNode safe traversal
String city = root.path("customer").path("address").path("city").asText("Unknown");
```

## Prevention Checklist

- Always assume nested JSON fields may be null.
- Use Optional for safe deep access.
- Use Jackson JsonNode for dynamic traversal.

## Related Errors

[NullPointerException](nullpointerexception), [JsonProcessingException](jackson-deserialization)
