---
title: "[Solution] MongoDB DNS Resolution Failed"
description: "Fix DNS resolution failures when connecting to MongoDB"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB DNS Resolution Failed Error

When the MongoDB driver cannot resolve the hostname to an IP address, you will see:

```
MongoNetworkError: getaddrinfo ENOTFOUND mongo.example.com
```

```
MongoServerSelectionError: DNS resolution failed for mongo.example.com
```

## Common Causes

- The hostname is misspelled in the connection string
- DNS server is unreachable or misconfigured
- `/etc/resolv.conf` has incorrect nameserver entries
- The DNS record for the MongoDB host does not exist
- Private DNS zones are not accessible from the client network
- The hostname uses an internal domain not resolvable externally
- `/etc/hosts` file is missing the entry for the MongoDB host

## How to Fix

### 1. Verify the hostname resolves

```bash
nslookup mongo.example.com
host mongo.example.com
dig mongo.example.com
```

### 2. Check DNS configuration

```bash
cat /etc/resolv.conf
# Ensure nameserver entries are correct
nameserver 8.8.8.8
nameserver 8.8.4.4
```

### 3. Add an entry to /etc/hosts (temporary fix)

```bash
sudo bash -c 'echo "192.168.1.100  mongo.example.com" >> /etc/hosts'
```

### 4. Use IP address directly

```
mongodb://user:password@192.168.1.100:27017/mydb?authSource=admin
```

### 5. Configure SRV record for replica sets

For DNS seedlist connections (`mongodb+srv://`), ensure the SRV record exists:

```bash
dig _mongodb._tcp.mongo.example.com SRV
```

## Examples

```bash
# Test DNS resolution from the application server
python3 -c "import socket; print(socket.getaddrinfo('mongo.example.com', 27017))"

# Flush DNS cache
sudo systemd-resolve --flush-caches
sudo resolvectl flush-caches

# Test with dig to see full DNS info
dig mongo.example.com ANY

# Try connecting with the IP directly to confirm DNS is the issue
mongosh --host 192.168.1.100 --port 27017
```