---
title: "[Solution] Azure Firewall Network Rule Error"
description: "Fix Azure Firewall network rule configuration failures blocking traffic flow."
cloud: ["azure"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 1
---

Firewall network rule errors prevent Azure Firewall from correctly routing or filtering network traffic. This can block legitimate traffic or allow unauthorized access.

## Common Causes

- Network rule has conflicting source or destination addresses
- Rule priority is too low and gets overridden by higher-priority rules
- Application FQDN tags are missing for required services
- Firewall policy is attached but rules are not associated with it

## How to Fix

### List network rules

```bash
az network firewall policy rule-collection-group list \
  --policy-name myPolicy \
  --resource-group myRG \
  --query "[].ruleCollections[].rules[].{Name:name,RuleType:ruleType}"
```

### Create a network rule

```bash
az network firewall policy rule-collection-group rule add-nat \
  --policy-name myPolicy \
  --rule-collection-group-name myCollectionGroup \
  --rule-collection-name myCollection \
  --name myRule \
  --source-addresses "10.0.0.0/16" \
  --destination-addresses "20.3.4.5" \
  --destination-ports "80" \
  --protocols TCP \
  --action DNAT \
  --translated-address 10.0.0.4 \
  --translated-port 8080
```

### Check firewall health

```bash
az network firewall show \
  --name myFirewall \
  --resource-group myRG \
  --query "provisioningState"
```

### Verify rule processing order

```bash
az network firewall policy rule-collection-group list \
  --policy-name myPolicy \
  --resource-group myRG
```

## Examples

- Network rule blocks all outbound traffic because the source address range is too broad
- DNAT rule conflicts with another rule and traffic is not translated correctly
- Firewall policy is associated with a different resource group than the firewall

## Related Errors

- [Azure Firewall Error]({{< relref "/cloud/azure/azure-firewall-error" >}}) -- General firewall errors.
- [Azure NSG Rule]({{< relref "/cloud/azure/azure-nsg-rule" >}}) -- NSG issues.
