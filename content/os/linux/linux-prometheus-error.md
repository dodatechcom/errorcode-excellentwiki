---
title: "[Solution] Linux prometheus Scrape Error — Fix"
description: "Fix Linux 'prometheus: scrape error' and monitoring failures. Resolve Prometheus target scrape failures, configuration issues, and connectivity problems."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Linux: prometheus: scrape error

The `prometheus: scrape error` message means Prometheus failed to scrape (collect metrics from) one or more configured targets. This appears in the Prometheus web UI under Status → Targets as `DOWN` or with error messages. Scrape errors prevent metrics collection and can break alerting rules that depend on those metrics.

## What This Error Means

Prometheus periodically pulls (scrapes) metrics endpoints via HTTP/HTTPS. When a target is unreachable, returns an error, times out, or returns invalid metric data, Prometheus logs a scrape error. The target is marked as `DOWN` and no new data points are recorded until the scrape succeeds again.

## Common Causes

- Target service is down or not listening on the metrics port
- Firewall blocking Prometheus → target connection
- Metrics endpoint URL is incorrect in prometheus.yml
- Target requires authentication but none is configured
- TLS/certificate issues with HTTPS targets
- Target returning malformed metrics data
- Prometheus scrape timeout too short
- Network connectivity issues between Prometheus and targets

## How to Fix

### 1. Check Target Status

```bash
# Check targets via API
curl http://localhost:9090/api/v1/targets | jq .

# Or check the web UI
# Navigate to http://localhost:9090/targets

# Check Prometheus logs
sudo journalctl -u prometheus --since "10 minutes ago"
```

### 2. Verify Target Reachability

```bash
# Test if the metrics endpoint is accessible
curl -v http://target-host:9090/metrics

# Check from Prometheus server
curl http://target-host:9090/metrics

# Test with authentication if needed
curl -u user:pass http://target-host:9090/metrics
```

### 3. Check Firewall Rules

```bash
# Allow Prometheus to reach targets
sudo iptables -A OUTPUT -p tcp --dport 9090 -j ACCEPT

# On target hosts, allow incoming metrics connections
sudo iptables -A INPUT -p tcp --dport 9100 -s prometheus-server-ip -j ACCEPT

# With ufw
sudo ufw allow from prometheus-server-ip to any port 9100
```

### 4. Fix Prometheus Configuration

```bash
# Check configuration syntax
promtool check config /etc/prometheus/prometheus.yml

# Validate rules
promtool check rules /etc/prometheus/rules/*.yml

# Test specific scrape config
promtool check web-config /etc/prometheus/web-config.yml
```

### 5. Fix Authentication and TLS

```bash
# For HTTPS targets, configure TLS in prometheus.yml
# scrape_configs:
#   - job_name: 'secure-target'
#     scheme: https
#     tls_config:
#       ca_file: /etc/prometheus/ca.crt
#       insecure_skip_verify: false

# For basic auth targets
#     basic_auth:
#       username: prometheus
#       password_file: /etc/prometheus/password
```

### 6. Adjust Scrape Timeout

```bash
# Increase scrape timeout in prometheus.yml
# scrape_configs:
#   - job_name: 'slow-target'
#     scrape_timeout: 30s    # Default is 10s
#     scrape_interval: 30s

# Reload configuration
curl -X POST http://localhost:9090/-/reload
```

### 7. Check Service Discovery

```bash
# Verify service discovery targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[].discoveredLabels'

# Check if labels are correct
# Common issue: wrong label matching in relabel_configs
```

### 8. Debug with promtool

```bash
# Test a specific target scrape
promtool probe http://target-host:9090/metrics

# Check metrics output
curl -s http://target-host:9090/metrics | head -20

# Verify metric names are valid
curl -s http://target-host:9090/metrics | grep -v "^#" | head -10
```

## Examples

```bash
# Check targets
$ curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, health: .health}'
{
  "instance": "webserver1:9100",
  "health": "up"
}
{
  "instance": "webserver2:9100",
  "health": "down"
}

# Check why target is down
$ curl http://webserver2:9100/metrics
curl: (7) Failed to connect to webserver2 port 9100: Connection refused

# Node exporter not running on webserver2
$ ssh webserver2 "sudo systemctl start node_exporter"
$ curl http://webserver2:9100/metrics | head -5
# node_uname_info{...} 1
```

## Related Errors

- [Grafana dashboard error]({{< relref "/os/linux/linux-grafana-error" >}}) — Dashboard display issues
- [Elasticsearch cluster error]({{< relref "/os/linux/linux-elasticsearch-error" >}}) — Log storage issues
- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Network connectivity issues
