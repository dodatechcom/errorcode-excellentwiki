---
title: "[Solution] Azure SQL — firewall rule blocked"
description: "Fix Azure SQL firewall rule blocked. Resolve SQL Database connectivity and firewall issues."
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Azure SQL firewall rule blocked error means the client IP address is not permitted by the SQL Database firewall rules. The connection is rejected at the network layer before reaching the database.

## What This Error Means

Azure SQL Database uses a firewall to control which IP addresses can connect. By default, all connections are denied — no IP is allowed. You must create firewall rules to permit specific IP addresses or Azure service endpoints. When a client attempts to connect from an IP not in any firewall rule, the connection is refused with error 40613 (`Database is not currently available`) or a TCP connection failure. Azure Portal, CLI, and SDK operations also require firewall rules if running from a client machine.

## Common Causes

- Client IP address not added to SQL Database firewall rules
- Dynamic IP address changed since firewall rule was created
- Missing "Allow Azure services" rule for services within Azure
- VNet firewall rules not configured for the client subnet
- SQL Database is in a different subscription with separate firewall
- Using the wrong server name or region in the connection string

## How to Fix

### Check Current Firewall Rules

```bash
az sql server firewall-rule list \
  --server my-server \
  --resource-group my-rg \
  --query '[].{name:name,startIp:startIpAddress,endIp:endIpAddress}'
```

### Add Client IP Rule

```bash
az sql server firewall-rule create \
  --server my-server \
  --resource-group my-rg \
  --name AllowMyIP \
  --start-ip-address 203.0.113.50 \
  --end-ip-address 203.0.113.50
```

### Allow Azure Services

```bash
az sql server firewall-rule create \
  --server my-server \
  --resource-group my-rg \
  --name AllowAllWindowsAzureIps \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0
```

### Use VNet Service Endpoints

```bash
az network vnet subnet update \
  --name my-subnet \
  --vnet-name my-vnet \
  --service-endpoints Microsoft.Sql
```

### Test Connectivity

```bash
# Test TCP connectivity
nc -zv my-server.database.windows.net 1433
telnet my-server.database.windows.net 1433
```

### Check SQL Server Exists

```bash
az sql server show \
  --name my-server \
  --resource-group my-rg \
  --query 'fullyQualifiedDomainName'
```

### Find Current Public IP

```bash
curl -s ifconfig.me
```

## Related Errors

- [Azure Cosmos Error]({{< relref "/cloud/azure/azure-cosmos-error-v2" >}}) — request rate too large
- [AWS RDS Error]({{< relref "/cloud/aws/aws-rds-error-v2" >}}) — MySQL connection failed
- [Azure Storage Error]({{< relref "/cloud/azure/azure-storage-error-v2" >}}) — authentication failed
