---
title: "[Solution] Azure Service Bus Connection Error"
description: "Fix Azure Service Bus connection failures for message send and receive operations."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Service Bus connection errors prevent applications from sending or receiving messages. This breaks messaging workflows and event-driven architectures.

## Common Causes

- Connection string is invalid or contains expired credentials
- Service Bus namespace firewall blocks the client IP address
- Maximum number of connections has been reached
- AMQP port 5671 is blocked by a network firewall

## How to Fix

### Check connection string

```bash
az servicebus namespace authorization-rule keys list \
  --namespace-name myNamespace \
  --name RootManageSharedAccessKey \
  --resource-group myRG \
  --query "primaryConnectionString"
```

### Check namespace firewall

```bash
az servicebus namespace show \
  --name myNamespace \
  --resource-group myRG \
  --query "networkRuleSet"
```

### Add IP to firewall rules

```bash
az servicebus namespace network-rule add \
  --namespace-name myNamespace \
  --resource-group myRG \
  --ip-rule "203.0.113.0/24"
```

### Test connectivity

```bash
az servicebus namespace authorization-rule keys renew \
  --namespace-name myNamespace \
  --name RootManageSharedAccessKey \
  --resource-group myRG \
  --key PrimaryKey
```

## Examples

- Client receives `NamespaceNotFound` because the connection string points to a deleted namespace
- Connection is refused because the VNet integration does not include the client subnet
- AMQP connection fails because the corporate firewall blocks port 5671

## Related Errors

- [Azure Service Bus Error]({{< relref "/cloud/azure/azure-service-bus-error" >}}) -- General Service Bus errors.
- [Azure Connection Error]({{< relref "/cloud/azure/azure-connection-failed" >}}) -- Connection issues.
