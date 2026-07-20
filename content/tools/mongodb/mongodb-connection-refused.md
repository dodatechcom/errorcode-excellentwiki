---
title: "[Solution] MongoDB Connection Refused"
description: "Fix MongoDB connection refused error on port 27017"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Connection Refused Error

The `connection refused` error means the client cannot establish a TCP connection to the MongoDB server. Typical messages:

```
MongoNetworkError: connect ECONNREFUSED 127.0.0.1:27017
```

```
Error: connect ECONNREFUSED ::1:27017
```

## Common Causes

- MongoDB service is not running
- MongoDB is listening on a different port or interface
- A firewall is blocking port 27017
- The `bindIp` configuration in `mongod.conf` does not include the client's address
- SELinux or AppArmor is blocking the connection
- MongoDB is bound to `127.0.0.1` only, and the client connects remotely
- Port 27017 is already in use by another process
- Docker container networking misconfiguration
- Cloud security group rules do not allow inbound traffic on 27017

## How to Fix

### 1. Check if MongoDB is running

```bash
sudo systemctl status mongod
# or on newer systems
sudo systemctl status mongodb
```

### 2. Start MongoDB if it is not running

```bash
sudo systemctl start mongod
sudo systemctl enable mongod
```

### 3. Verify the listening address and port

```bash
ss -tlnp | grep 27017
# or
netstat -tlnp | grep 27017
```

### 4. Update bindIp in mongod.conf

```yaml
# /etc/mongod.conf
net:
  port: 27017
  bindIp: 0.0.0.0   # Listen on all interfaces
```

Then restart:

```bash
sudo systemctl restart mongod
```

### 5. Configure the firewall

```bash
# UFW
sudo ufw allow 27017/tcp

# firewalld
sudo firewall-cmd --permanent --add-port=27017/tcp
sudo firewall-cmd --reload

# iptables
sudo iptables -A INPUT -p tcp --dport 27017 -j ACCEPT
```

## Examples

```bash
# Test connection with mongosh
mongosh --host 127.0.0.1 --port 27017

# Check if the port is open
nc -zv 127.0.0.1 27017

# Verify MongoDB log for binding issues
sudo tail -50 /var/log/mongodb/mongod.log | grep -i "waiting for connections\|error\|address already in use"

# Verify Docker container is exposing the port
docker ps | grep mongo
docker logs <container_name> --tail 50
```