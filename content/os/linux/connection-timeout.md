---
title: "[Solution] Linux: connection-timeout — connection timeout error"
description: "Fix Linux connection-timeout errors. connection timeout error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 8
---
# Linux: Connection Timeout

Connection timeout means the client waited for a response from the server but none arrived within the timeout period. The server may be unreachable or too slow to respond.

## Common Causes

- Firewall dropping packets (silent drop, not reject)
- Server overloaded and unable to respond in time
- Network congestion or high latency link
- Routing issues causing packet loss
- DNS resolution working but server not reachable on the port

## How to Fix

### 1. Test Basic Connectivity

```bash
ping -c 4 <target>
ping -c 10 <target>  # Check for packet loss
```

### 2. Trace Route

```bash
traceroute -n <target>
mtr <target>
```

### 3. Check for Firewall Drops

```bash
# On the client
sudo tcpdump -i any host <target> and port <port>

# Check if packets are being dropped
sudo netstat -s | grep -i "drop\|overflow\|retransmit"
```

### 4. Increase Timeout

```bash
# SSH
ssh -o ConnectTimeout=30 user@host
# curl
curl --connect-timeout 30 http://host:port
```

## Examples

```bash
$ ping -c 4 192.168.1.100
PING 192.168.1.100 (192.168.1.100) 56(84) bytes of data.
--- 192.168.1.100 ping statistics ---
4 packets transmitted, 0 received, 100% packet loss, time 3000ms

$ traceroute -n 192.168.1.100
traceroute to 192.168.1.100 (192.168.1.100), 30 hops max, 60 byte packets
 1  192.168.1.1   0.345 ms  0.289 ms  0.256 ms
 2  * * *
 3  * * *
```
