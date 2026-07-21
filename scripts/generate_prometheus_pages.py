#!/usr/bin/env python3
"""Generate Prometheus error pages"""
import os

BASE = '/home/admin1/projects/ErrorCode.excellentwiki.com/content/tools/prometheus'
EXISTING = {f.replace('.md', '') for f in os.listdir(BASE) if f.endswith('.md')}

def make_page(title, desc, body):
    lines = [
        '---',
        f'title: "[Solution] {title}"',
        f'description: "{desc}"',
        'tools: ["prometheus"]',
        'error-types: ["tool-error"]',
        'severities: ["error"]',
        '---',
        '',
        body,
    ]
    return '\n'.join(lines)

PAGES = [
    (
        "prometheus-config-parse-error",
        "Prometheus Config Parse Error",
        "How to fix Prometheus configuration file parse errors in prometheus.yml",
        """## Common Causes

- Invalid YAML syntax in prometheus.yml
- Indentation errors in configuration
- Missing colons after keys
- Tab characters mixed with spaces
- Unterminated quotes in string values

## How to Fix

Validate the configuration file:

```bash
promtool check config prometheus.yml
```

Check YAML syntax manually:

```bash
python3 -c "import yaml; yaml.safe_load(open('prometheus.yml'))"
```

Use a YAML linter:

```bash
yamllint prometheus.yml
```

Common YAML syntax fixes:

```yaml
# Wrong (tab character)
->global:
->  scrape_interval: 15s

# Correct (spaces only)
global:
  scrape_interval: 15s
```

Fix unterminated strings:

```yaml
# Wrong
job_name: 'my-job

# Correct
job_name: 'my-job'
```

## Examples

```bash
# Validate config
promtool check config prometheus.yml

# Check with verbose output
promtool check config --verbose prometheus.yml

# View parsed config
prometheus --config.file=prometheus.yml --dry-run
```
"""
    ),
    (
        "prometheus-scrape-config-invalid",
        "Prometheus Scrape Config Invalid",
        "How to fix invalid scrape_config entries in Prometheus configuration",
        """## Common Causes

- Missing `job_name` in scrape_config
- Invalid `static_configs` format
- Wrong `scheme` value (must be http or https)
- Malformed `targets` list
- Unknown fields in scrape_config

## How to Fix

Validate scrape configuration:

```bash
promtool check config prometheus.yml
```

Correct scrape_config structure:

```yaml
scrape_configs:
  - job_name: 'my-app'
    static_configs:
      - targets: ['localhost:8080']
```

Check for typos in field names:

```yaml
# Wrong: scrape_config (missing s)
scrape_config:
  - job_name: 'app'

# Correct
scrape_configs:
  - job_name: 'app'
```

Verify target format:

```yaml
# Wrong
targets: 'localhost:8080'

# Correct
targets: ['localhost:8080']
```

## Examples

```bash
# Test specific scrape config
promtool check config prometheus.yml 2>&1 | grep scrape

# Reload configuration
kill -HUP $(pidof prometheus)

# View active scrape targets
curl http://localhost:9090/api/v1/targets
```
"""
    ),
    (
        "prometheus-job-name-missing",
        "Prometheus job_name Missing",
        "How to fix the missing job_name error in Prometheus scrape configuration",
        """## Common Causes

- `job_name` field omitted from scrape_config
- `job_name` is empty or null
- Multiple scrape_configs sharing the same job_name

## How to Fix

Add a unique `job_name` to each scrape config:

```yaml
scrape_configs:
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['localhost:9100']
  - job_name: 'app-metrics'
    static_configs:
      - targets: ['localhost:8080']
```

Verify no duplicate job names:

```bash
grep "job_name:" prometheus.yml | sort | uniq -d
```

Each scrape config must have a unique job name:

```bash
promtool check config prometheus.yml
```

## Examples

```yaml
# Valid scrape configs
scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['localhost:8080']
```

```bash
# Check for missing job_name
promtool check config prometheus.yml
```
"""
    ),
    (
        "prometheus-target-not-found",
        "Prometheus Target Not Found",
        "How to fix Prometheus target not found errors when scraping endpoints",
        """## Common Causes

- Target endpoint is down or unreachable
- Wrong hostname or port in target configuration
- Firewall blocking the connection
- DNS resolution failure for target hostname
- Target application not exposing metrics endpoint

## How to Fix

Check target status in Prometheus UI:

```bash
curl http://localhost:9090/api/v1/targets | python3 -m json.tool
```

Verify target is reachable:

```bash
curl -v http://target-host:9090/metrics
```

Check DNS resolution:

```bash
nslookup target-host.example.com
```

Verify firewall rules:

```bash
sudo iptables -L -n | grep 9090
```

Update target address if needed:

```yaml
scrape_configs:
  - job_name: 'app'
    static_configs:
      - targets: ['correct-host:8080']
```

## Examples

```bash
# List all targets and their status
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, health: .health}'

# Test connectivity to target
nc -zv target-host 8080

# Check target labels
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[].labels'
```
"""
    ),
    (
        "prometheus-target-timeout",
        "Prometheus Target Scrape Timeout",
        "How to fix Prometheus target scrape timeout when endpoints respond too slowly",
        """## Common Causes

- Target application is slow to respond
- Network latency between Prometheus and target
- `scrape_timeout` set too low
- Target under heavy load
- Large metrics payload taking too long to transfer

## How to Fix

Increase the scrape timeout:

```yaml
global:
  scrape_timeout: 30s
```

Per-job timeout override:

```yaml
scrape_configs:
  - job_name: 'slow-app'
    scrape_timeout: 60s
    static_configs:
      - targets: ['slow-host:8080']
```

Check if target responds within timeout:

```bash
time curl -s http://target-host:8080/metrics > /dev/null
```

Increase HTTP client timeout:

```yaml
scrape_configs:
  - job_name: 'app'
    scrape_timeout: 30s
    http_client_config:
      follow_redirects: true
```

## Examples

```bash
# Measure scrape duration
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrapeDuration: .lastScrapeDuration}'

# Test response time
curl -o /dev/null -s -w '%{time_total}\\n' http://target-host:8080/metrics
```
"""
    ),
    (
        "prometheus-metrics-path-error",
        "Prometheus Metrics Path Error",
        "How to fix Prometheus metrics endpoint path configuration errors",
        """## Common Causes

- `metrics_path` not set when target uses a non-default path
- Default path `/metrics` not exposed by the application
- Typo in the configured metrics path
- Application uses a different endpoint for metrics

## How to Fix

Set the correct metrics path in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    metrics_path: '/custom/metrics'
    static_configs:
      - targets: ['localhost:8080']
```

Verify the metrics endpoint exists:

```bash
curl -s http://target-host:8080/metrics | head -5
curl -s http://target-host:8080/custom/metrics | head -5
```

Check available endpoints:

```bash
curl -s http://target-host:8080/ | grep -i metric
```

Common alternative paths:

```yaml
# Spring Boot Actuator
metrics_path: '/actuator/prometheus'

# Custom path
metrics_path: '/internal/metrics'

# Debug endpoint
metrics_path: '/debug/vars'
```

## Examples

```bash
# Test different metrics paths
curl -s http://localhost:8080/metrics
curl -s http://localhost:8080/actuator/prometheus
curl -s http://localhost:8080/debug/metrics

# Check scrape config
promtool check config prometheus.yml
```
"""
    ),
    (
        "prometheus-scheme-invalid",
        "Prometheus Scrape Scheme Invalid",
        "How to fix invalid scheme configuration in Prometheus scrape targets",
        """## Common Causes

- `scheme` value is not `http` or `https`
- Typo in scheme field (e.g., `htps`, `httpss`)
- Using `https` without proper TLS configuration
- Scheme does not match the target endpoint

## How to Fix

Set valid scheme value:

```yaml
scrape_configs:
  - job_name: 'app'
    scheme: 'https'
    static_configs:
      - targets: ['localhost:8443']
```

Valid scheme values:

```yaml
scheme: 'http'   # default
scheme: 'https'
```

Verify target supports the scheme:

```bash
curl -k https://localhost:8443/metrics
curl http://localhost:8080/metrics
```

## Examples

```bash
# Test HTTP scheme
curl http://localhost:9090/metrics

# Test HTTPS scheme
curl -k https://localhost:9443/metrics

# Validate config
promtool check config prometheus.yml
```
"""
    ),
    (
        "prometheus-tls-config-error",
        "Prometheus TLS Config Error",
        "How to fix TLS configuration errors in Prometheus scrape and remote write",
        """## Common Causes

- Invalid or missing TLS certificate file
- Certificate and key mismatch
- Expired TLS certificate
- CA certificate not trusted
- Wrong file permissions on TLS files

## How to Fix

Configure TLS in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    scheme: 'https'
    tls_config:
      ca_file: /etc/prometheus/ca.crt
      cert_file: /etc/prometheus/client.crt
      key_file: /etc/prometheus/client.key
      insecure_skip_verify: false
```

Verify certificate validity:

```bash
openssl x509 -in /etc/prometheus/client.crt -noout -dates
```

Check certificate and key match:

```bash
diff <(openssl x509 -in client.crt -noout -modulus) \
     <(openssl rsa -in client.key -noout -modulus)
```

## Examples

```bash
# Test HTTPS connection
curl --cacert /etc/prometheus/ca.crt https://target:443/metrics

# Check certificate chain
openssl s_client -connect target:443 -CAfile /etc/prometheus/ca.crt

# Skip certificate verification (testing only)
tls_config:
  insecure_skip_verify: true
```
"""
    ),
    (
        "prometheus-basic-auth-error",
        "Prometheus Basic Auth Error",
        "How to fix basic authentication errors when scraping password-protected endpoints",
        """## Common Causes

- Wrong username or password in basic_auth config
- Password file not found or unreadable
- Target does not accept basic authentication
- Special characters in password not handled properly

## How to Fix

Configure basic auth in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    basic_auth:
      username: admin
      password: secret123
    static_configs:
      - targets: ['localhost:8080']
```

Use password file for security:

```yaml
scrape_configs:
  - job_name: 'app'
    basic_auth:
      username: admin
      password_file: /etc/prometheus/password
```

Create the password file:

```bash
echo 'secret123' > /etc/prometheus/password
chmod 600 /etc/prometheus/password
```

## Examples

```bash
# Test basic auth manually
curl -u admin:secret123 http://localhost:8080/metrics

# Verify credentials
curl -u admin:wrongpass http://localhost:8080/metrics
```
"""
    ),
    (
        "prometheus-bearer-token-error",
        "Prometheus Bearer Token Error",
        "How to fix bearer token authentication errors in Prometheus scrape configs",
        """## Common Causes

- Expired or invalid bearer token
- Token file missing or empty
- Wrong token format (should not include "Bearer" prefix)
- Target requires specific token scope

## How to Fix

Configure bearer token in scrape config:

```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    kubernetes_sd_configs:
      - role: pod
```

Inline token (not recommended for production):

```yaml
scrape_configs:
  - job_name: 'app'
    bearer_token: 'eyJhbGciOiJSUzI1NiIs...'
```

Refresh expired token:

```bash
# Kubernetes
kubectl get secret $(kubectl get sa prometheus -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 -d
```

## Examples

```bash
# Test bearer token
curl -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" https://kubernetes:443/metrics

# Verify token is valid
kubectl auth can-i get pods --as=system:serviceaccount:monitoring:prometheus
```
"""
    ),
    (
        "prometheus-oauth2-error",
        "Prometheus OAuth2 Error",
        "How to fix OAuth2 authentication errors in Prometheus scrape and remote write",
        """## Common Causes

- Invalid client_id or client_secret
- Token URL endpoint unreachable
- OAuth2 token expired and not refreshed
- Scopes not matching target requirements
- TLS errors connecting to OAuth2 provider

## How to Fix

Configure OAuth2 in scrape config:

```yaml
scrape_configs:
  - job_name: 'app'
    oauth2:
      client_id: my-client-id
      client_secret: my-client-secret
      token_url: https://auth.example.com/token
      scopes:
        - read:metrics
      tls_config:
        ca_file: /etc/prometheus/ca.crt
```

Use client credentials file:

```yaml
    oauth2:
      client_id: my-client-id
      client_secret_file: /etc/prometheus/client_secret
      token_url: https://auth.example.com/token
```

## Examples

```bash
# Test OAuth2 token retrieval
curl -X POST https://auth.example.com/token \
  -d 'grant_type=client_credentials&client_id=my-id&client_secret=my-secret'

# Check Prometheus logs for OAuth errors
journalctl -u prometheus | grep -i oauth
```
"""
    ),
    (
        "prometheus-scrape-timeout-exceeded",
        "Prometheus Scrape Timeout Exceeded",
        "How to fix Prometheus scrape timeout exceeded errors for slow targets",
        """## Common Causes

- Target application taking too long to respond
- Network congestion or packet loss
- Target exporting a very large number of metrics
- `scrape_timeout` too low for the workload

## How to Fix

Increase global scrape timeout:

```yaml
global:
  scrape_timeout: 30s
```

Per-target timeout configuration:

```yaml
scrape_configs:
  - job_name: 'large-app'
    scrape_timeout: 60s
    static_configs:
      - targets: ['large-host:8080']
```

Reduce metrics cardinality on target:

```bash
# Check metric count on target
curl -s http://target:8080/metrics | wc -l
```

## Examples

```bash
# Monitor scrape durations
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrape: .lastScrapeDuration}'

# Find slow targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.lastScrapeDuration > 10) | .labels.instance'
```
"""
    ),
    (
        "prometheus-sample-too-old",
        "Prometheus Sample Too Old Error",
        "How to fix Prometheus out-of-order or too-old sample errors during ingestion",
        """## Common Causes

- Target sending samples with timestamps too far in the past
- Clock skew between Prometheus server and target
- `out_of_order_time_window` exceeded
- Remote write lag causing stale timestamps

## How to Fix

Check time synchronization on all hosts:

```bash
chronyc tracking
timedatectl status
```

Enable out-of-order ingestion (Prometheus 2.39+):

```yaml
storage:
  tsdb:
    out_of_order_time_window: 30m
```

Increase tolerance for old samples:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
```

## Examples

```bash
# Check for out-of-order errors in logs
journalctl -u prometheus | grep "out of order"

# Verify time on servers
date -u; ssh target-host date -u

# Monitor ingestion errors
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data.headStats'
```
"""
    ),
    (
        "prometheus-duplicate-sample",
        "Prometheus Duplicate Sample Error",
        "How to fix Prometheus duplicate sample errors during metric ingestion",
        """## Common Causes

- Two targets writing the same metric with identical labels
- Misconfigured relabeling creating duplicate series
- Federation or remote write creating duplicate data
- Multiple Prometheus instances scraping the same target

## How to Fix

Check for duplicate series:

```bash
promtool tsdb analyze prometheus-data/
```

Review relabel configs:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance
        action: replace
```

Use unique identifiers in relabeling:

```yaml
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '.*,prometheus,.*'
        target_label: __param_target
```

## Examples

```bash
# Check for duplicate targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | .labels.instance' | sort | uniq -d

# Query for duplicate metric names
curl -s 'http://localhost:9090/api/v1/query?query=count by (__name__)({__name__!=""})' | jq '.data.result[] | select(.value[1] > "1")'
```
"""
    ),
    (
        "prometheus-stale-sample",
        "Prometheus Stale Sample Error",
        "How to fix Prometheus stale sample errors when targets disappear or stop reporting",
        """## Common Causes

- Target disappeared and stopped sending metrics
- Target restarted with a gap in metric reporting
- Series terminated without proper staleness marker
- Remote write connection dropped

## How to Fix

Configure scrape interval appropriately:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
```

Adjust staleness delta:

```yaml
storage:
  tsdb:
    staleness_delta: 5m
```

Use `honor_labels` when needed:

```yaml
scrape_configs:
  - job_name: 'app'
    honor_labels: true
```

## Examples

```bash
# Check for stale series
curl -s 'http://localhost:9090/api/v1/query?query=stale' | jq '.data.result'

# Monitor target uptime
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrape: .lastScrape}'
```
"""
    ),
    (
        "prometheus-label-limit-exceeded",
        "Prometheus Label Limit Exceeded",
        "How to fix Prometheus label limit exceeded errors during ingestion",
        """## Common Causes

- Target exporting metrics with too many labels
- Label cardinality too high causing memory pressure
- Default label limit reached per sample
- High-cardinality labels like user_id or request_id

## How to Fix

Increase the label limit:

```yaml
global:
  label_limit: 50
```

Per-scrape label limit:

```yaml
scrape_configs:
  - job_name: 'high-cardinality-app'
    label_limit: 100
    label_name_length_limit: 200
    label_value_length_limit: 4000
```

Reduce label cardinality on the target:

```python
# Bad: high cardinality label
REQUEST_COUNT.labels(url="/api/user/{id}", method="GET", status="200")

# Better: low cardinality labels
REQUEST_COUNT.labels(endpoint="/api/user", method="GET", status="200")
```

## Examples

```bash
# Check label count per metric
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq length

# Monitor label usage
promtool tsdb analyze prometheus-data/ 2>&1 | grep label
```
"""
    ),
    (
        "prometheus-label-name-invalid",
        "Prometheus Label Name Invalid",
        "How to fix invalid label name errors in Prometheus metrics",
        """## Common Causes

- Label name contains invalid characters (only [a-zA-Z0-9_])
- Label name starts with a digit
- Label name is empty
- Reserved label names used (e.g., __name__)

## How to Fix

Use only valid characters in label names:

```python
# Wrong
counter = Counter('my_counter', 'Help', ['my-label'])  # hyphen invalid
counter = Counter('my_counter', 'Help', ['123label'])   # starts with digit

# Correct
counter = Counter('my_counter', 'Help', ['my_label'])
counter = Counter('my_counter', 'Help', ['label123'])
```

Valid label name rules:

```bash
# Must match: [a-zA-Z][a-zA-Z0-9_]*
# Examples of valid names:
#   my_label
#   http_status_code
#   __meta_kubernetes
```

Check label names in existing metrics:

```bash
curl -s http://localhost:9090/api/v1/label/__name__/values
```

## Examples

```bash
# Query label names
curl -s 'http://localhost:9090/api/v1/labels' | jq '.data[]'

# Validate metric labels
curl -s http://target:8080/metrics | grep -E '^[a-zA-Z_][a-zA-Z0-9_]*\{'
```
"""
    ),
    (
        "prometheus-label-value-too-long",
        "Prometheus Label Value Too Long",
        "How to fix Prometheus label value length limit exceeded errors",
        """## Common Causes

- Label values exceeding the default 2048 character limit
- High-cardinality string labels
- Labels containing full URLs or paths
- Error messages used as label values

## How to Fix

Increase label value length limit:

```yaml
global:
  label_value_length_limit: 4096
```

Per-scrape configuration:

```yaml
scrape_configs:
  - job_name: 'app'
    label_value_length_limit: 8192
```

Reduce label value length in the application:

```python
# Bad: full URL as label value
REQUEST_COUNT.labels(url="/api/v1/users/1234567890/profile/settings")

# Better: sanitized label value
REQUEST_COUNT.labels(endpoint="/api/v1/users", operation="profile_settings")
```

## Examples

```bash
# Find long label values
curl -s http://target:8080/metrics | awk -F'=' '/\{.*=[^}]{200,}/' | head

# Check current limit
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml'
```
"""
    ),
    (
        "prometheus-label-conflict",
        "Prometheus Label Conflict Error",
        "How to fix Prometheus label conflict when target and relabeling clash",
        """## Common Causes

- Target exposes a label that conflicts with relabel target
- `honor_labels: false` causing target labels to be overwritten
- Multiple relabel rules writing to the same target label
- Reserved labels (`job`, `instance`) conflicting with target labels

## How to Fix

Use `honor_labels: true` to keep target labels:

```yaml
scrape_configs:
  - job_name: 'app'
    honor_labels: true
    static_configs:
      - targets: ['localhost:8080']
```

Check for label conflicts in logs:

```bash
journalctl -u prometheus | grep "label conflict"
```

Adjust relabeling to avoid conflicts:

```yaml
    relabel_configs:
      - source_labels: [__meta_consul_service]
        target_label: service_name
        action: replace
```

## Examples

```bash
# Check for conflicting labels
curl -s 'http://localhost:9090/api/v1/query?query={__name__!=""}' | jq '.data.result[0].metric' | sort

# View relabel configs
curl -s http://localhost:9090/api/v1/status/config | grep -A 10 relabel_configs
```
"""
    ),
    (
        "prometheus-metric-name-invalid",
        "Prometheus Metric Name Invalid",
        "How to fix invalid metric name errors in Prometheus",
        """## Common Causes

- Metric name contains invalid characters (only [a-zA-Z_:])
- Name starts with underscore or colon
- Name exceeds maximum length
- Reserved words used as metric names

## How to Fix

Use valid metric naming conventions:

```python
# Wrong
counter = Counter('my-metric', 'Help')       # hyphen invalid
counter = Counter('123metric', 'Help')        # starts with digit
counter = Counter('my.metric', 'Help')        # dot invalid

# Correct
counter = Counter('my_metric_total', 'Help')  # underscore + _total suffix
counter = Counter('http_requests_total', 'Help')
```

Valid metric name rules:

```bash
# Must match: [a-zA-Z_:][a-zA-Z0-9_:]*
# Convention: namespace_subsystem_name_unit_total/info/created
# Examples:
#   http_requests_total
#   node_cpu_seconds_total
#   go_goroutines
```

Check existing metric names:

```bash
curl -s http://localhost:9090/api/v1/label/__name__/values | jq '.data[]'
```

## Examples

```bash
# Query specific metric
curl -s 'http://localhost:9090/api/v1/query?query=http_requests_total'

# List all metric names
curl -s http://localhost:9090/api/v1/label/__name__/values | jq -r '.data[]' | head -20
```
"""
    ),
    (
        "prometheus-metric-family-name",
        "Prometheus Metric Family Name Error",
        "How to fix metric family name conflicts in Prometheus exposition format",
        """## Common Causes

- Same metric name with different types (counter vs gauge)
- Metric type changed without changing name
- Mixed metric types in the same output
- Exposition format errors causing type mismatch

## How to Fix

Ensure consistent metric types:

```python
# Wrong: changing type of existing metric
REGISTRY.unregister(old_counter)
REGISTRY.register(new_gauge)  # same name, different type

# Correct: use a new name
COUNTER_TOTAL = Counter('requests_total', 'Total requests')
GAUGE_CURRENT = Gauge('requests_current', 'Current requests')
```

Check metric types on a target:

```bash
curl -s http://target:8080/metrics | grep -E "^# TYPE"
```

Restart target after changing metric types:

```bash
sudo systemctl restart my-app
```

## Examples

```bash
# View metric types
curl -s http://localhost:8080/metrics | grep "^# TYPE"

# Check for type conflicts
curl -s http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_series
```
"""
    ),
    (
        "prometheus-help-text-parse-error",
        "Prometheus HELP Text Parse Error",
        "How to fix HELP text parsing errors in Prometheus exposition format",
        """## Common Causes

- Malformed HELP line in metrics output
- HELP text contains newline characters
- HELP text encoding issues (non-UTF8)
- HELP line does not match the metric name

## How to Fix

Ensure correct HELP format:

```python
# Wrong: HELP line with newline
HELP my_metric Description with\\nnewline

# Correct: single line HELP
HELP my_metric Description with spaces
```

Validate exposition format:

```bash
curl -s http://target:8080/metrics | grep -E "^# (HELP|TYPE)"
```

Check for encoding issues:

```bash
curl -s http://target:8080/metrics | file -
```

## Examples

```bash
# View HELP text for a metric
curl -s http://target:8080/metrics | grep -A 1 "# HELP my_metric"

# Validate all HELP lines
curl -s http://target:8080/metrics | grep "^# HELP" | head -10

# Check for parsing errors in logs
journalctl -u prometheus | grep "parse error"
```
"""
    ),
    (
        "prometheus-type-line-invalid",
        "Prometheus TYPE Line Invalid",
        "How to fix invalid TYPE declaration lines in Prometheus exposition format",
        """## Common Causes

- TYPE line does not match a following metric line
- Invalid type value (must be counter, gauge, histogram, summary, or untyped)
- TYPE declared after metric samples instead of before
- Multiple TYPE declarations for the same metric

## How to Fix

Ensure correct TYPE format:

```
# Wrong
# TYPE my_metric counter
# TYPE my_metric gauge
my_metric 42

# Correct
# TYPE my_metric gauge
my_metric 42
```

Valid TYPE values:

```
# TYPE my_counter counter
# TYPE my_gauge gauge
# TYPE my_histogram histogram
# TYPE my_summary summary
# TYPE my_metric untyped
```

Validate with promtool:

```bash
promtool check metrics < target-metrics.txt
```

## Examples

```bash
# Check TYPE lines on target
curl -s http://target:8080/metrics | grep "^# TYPE"

# Validate metrics format
curl -s http://target:8080/metrics | promtool check metrics

# View parsed metric types
curl -s 'http://localhost:9090/api/v1/query?query=metric_metadata'
```
"""
    ),
    (
        "prometheus-unit-metadata-error",
        "Prometheus UNIT Metadata Error",
        "How to fix UNIT metadata errors in Prometheus exposition format",
        """## Common Causes

- Unit suffix does not match metric name convention
- Invalid unit specified in metadata
- Unit not following Prometheus naming convention
- Deprecated unit format

## How to Fix

Follow Prometheus unit conventions:

```python
# Wrong: unit in wrong position or format
GAUGE = Gauge('my_gauge_seconds', 'Help', unit='sec')

# Correct: standard unit suffix
GAUGE = Gauge('my_gauge_seconds', 'Help')
```

Standard unit suffixes:

```bash
# _seconds, _milliseconds, _bytes, _bits, _total
# Examples:
#   http_request_duration_seconds
#   node_memory_total_bytes
#   go_gc_duration_seconds
```

## Examples

```bash
# View unit metadata
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_samples_appended_total'

# Check metric naming
curl -s http://target:8080/metrics | grep -E "^(# TYPE|# UNIT)"
```
"""
    ),
    (
        "prometheus-histogram-bucket-error",
        "Prometheus Histogram Bucket Error",
        "How to fix histogram bucket errors in Prometheus metrics",
        """## Common Causes

- Bucket boundaries not monotonically increasing
- Missing `_count` or `_sum` for histogram
- Bucket values not cumulative
- Custom bucket boundaries overlapping

## How to Fix

Define proper histogram buckets:

```python
from prometheus_client import Histogram

# Custom buckets must be monotonically increasing
HISTOGRAM = Histogram(
    'request_duration_seconds',
    'Request duration',
    buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
)
```

Use default buckets for standard metrics:

```python
# Default buckets: (.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10)
HISTOGRAM = Histogram('request_duration_seconds', 'Request duration')
```

Verify histogram output:

```bash
curl -s http://target:8080/metrics | grep "request_duration_seconds_bucket"
```

## Examples

```bash
# Query histogram quantiles
curl -s 'http://localhost:9090/api/v1/query?query=histogram_quantile(0.99,rate(request_duration_seconds_bucket[5m]))'

# View raw histogram buckets
curl -s http://target:8080/metrics | grep "request_duration_seconds_bucket"
```
"""
    ),
    (
        "prometheus-summary-quantile-error",
        "Prometheus Summary Quantile Error",
        "How to fix summary quantile calculation errors in Prometheus",
        """## Common Causes

- Quantile values showing NaN (insufficient data)
- Error margin too high in quantile estimation
- Summary not receiving new observations
- Moving average window too narrow

## How to Fix

Configure summary quantiles properly:

```python
from prometheus_client import Summary

SUMMARY = Summary(
    'request_duration_seconds',
    'Request duration',
    ['method'],
    quantiles={0.5: 0.05, 0.9: 0.01, 0.99: 0.001}
)
```

Check if summary is receiving observations:

```bash
curl -s http://target:8080/metrics | grep "request_duration_seconds_count"
```

Use histograms for better accuracy:

```python
from prometheus_client import Histogram

# Histogram allows server-side quantile calculation
HISTOGRAM = Histogram('request_duration_seconds', 'Request duration')
```

## Examples

```bash
# Query summary quantile
curl -s 'http://localhost:9090/api/v1/query?query=request_duration_seconds{quantile="0.99"}'

# Compare with histogram quantile
curl -s 'http://localhost:9090/api/v1/query?query=histogram_quantile(0.99,rate(request_duration_seconds_bucket[5m]))'
```
"""
    ),
    (
        "prometheus-gauge-set-error",
        "Prometheus Gauge Set Error",
        "How to fix errors when setting Prometheus gauge values",
        """## Common Causes

- Setting gauge to NaN or Inf
- Gauge value type mismatch (string where number expected)
- Gauge decremented below zero without tracking
- Concurrent gauge modifications causing race conditions

## How to Fix

Use proper gauge operations:

```python
from prometheus_client import Gauge

GAUGE = Gauge('connections', 'Active connections')

GAUGE.set(42)              # Set absolute value
GAUGE.inc()                # Increment by 1
GAUGE.inc(5)               # Increment by 5
GAUGE.dec()                # Decrement by 1
GAUGE.set_to_current_time() # Set to current timestamp
```

Avoid setting NaN:

```python
# Wrong
GAUGE.set(float('nan'))

# Correct
if value is not None and math.isfinite(value):
    GAUGE.set(value)
```

## Examples

```bash
# Check gauge value
curl -s 'http://localhost:9090/api/v1/query?query=connections'

# View gauge history
curl -s 'http://localhost:9090/api/v1/query_range?query=connections&start=1h ago&step=60s'
```
"""
    ),
    (
        "prometheus-counter-increment-error",
        "Prometheus Counter Increment Error",
        "How to fix errors when incrementing Prometheus counters",
        """## Common Causes

- Counter value going backwards (reset detected)
- Incrementing counter with negative value
- Counter label changes causing unexpected resets
- Counter renamed without migration plan

## How to Fix

Never decrement a counter:

```python
from prometheus_client import Counter

COUNTER = Counter('requests_total', 'Total requests')

COUNTER.inc()       # Increment by 1
COUNTER.inc(5)      # Increment by 5
COUNTER.inc(1.5)    # Increment by float

# Wrong: counter cannot go backwards
COUNTER.dec()       # This will cause an error
```

Handle counter resets gracefully:

```yaml
# In recording rules
- record: requests:rate5m
  expr: rate(requests_total[5m])
```

## Examples

```bash
# Check counter value
curl -s 'http://localhost:9090/api/v1/query?query=requests_total'

# Calculate rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(requests_total[5m])'

# Check for counter resets
curl -s 'http://localhost:9090/api/v1/query?query=changes(requests_total[1h])'
```
"""
    ),
    (
        "prometheus-nan-value",
        "Prometheus NaN Value Error",
        "How to fix NaN (Not a Number) values appearing in Prometheus metrics",
        """## Common Causes

- Division by zero in PromQL expressions
- Invalid arithmetic operations
- Missing data points in binary operations
- Logarithm of zero or negative numbers
- Histogram quantile with insufficient data

## How to Fix

Guard against division by zero:

```promql
# Wrong: may produce NaN
rate(errors_total[5m]) / rate(requests_total[5m])

# Correct: use > 0 filter
rate(errors_total[5m]) / (rate(requests_total[5m]) > 0)
```

Handle NaN in queries:

```promql
# Replace NaN with 0
clamp_min(metric_name, 0)

# Filter out NaN
metric_name == metric_name
```

Use `default` to handle missing data:

```promql
metric_a / on() group_left() metric_b or vector(0)
```

## Examples

```bash
# Find metrics with NaN
curl -s 'http://localhost:9090/api/v1/query?query=NaN'

# Safe division
curl -s 'http://localhost:9090/api/v1/query?query=rate(errors_total[5m]) / on() group_left() (rate(requests_total[5m]) > 0)'

# Replace NaN with zero
curl -s 'http://localhost:9090/api/v1/query?query=clamp_min(rate(errors_total[5m]) / rate(requests_total[5m]), 0)'
```
"""
    ),
    (
        "prometheus-infinity-value",
        "Prometheus Infinity Value Error",
        "How to fix Inf (Infinity) values appearing in Prometheus queries",
        """## Common Causes

- Division by zero producing positive or negative infinity
- Exponential function overflow
- Binary operations with mismatched series
- Incorrect rate calculation on counter resets

## How to Fix

Clamp infinite values:

```promql
# Clamp to a maximum value
clamp_max(metric_name, 1e9)

# Clamp to zero if infinite
metric_name == metric_name
```

Guard against zero denominators:

```promql
# Wrong: division by zero produces Inf
rate(errors_total[5m]) / rate(total[5m])

# Correct
(rate(errors_total[5m]) > 0) / (rate(total[5m]) > 0)
```

## Examples

```bash
# Find infinite values
curl -s 'http://localhost:9090/api/v1/query?query=metric_name == Inf'

# Safe query with clamping
curl -s 'http://localhost:9090/api/v1/query?query=clamp_max(rate(errors_total[5m]) / rate(total[5m]), 1)'
```
"""
    ),
    (
        "prometheus-exemplar-error",
        "Prometheus Exemplar Error",
        "How to fix exemplar-related errors in Prometheus metrics",
        """## Common Causes

- Exemplar trace ID format invalid
- Exemplar timestamp outside sample range
- Too many exemplars per sample
- Exemplar labels exceeding limits

## How to Fix

Configure exemplar support:

```yaml
scrape_configs:
  - job_name: 'app'
    scrape_interval: 15s
    exemplar_limits:
      max_exemplars_per_sample: 5
      max_label_length: 128
```

Add valid exemplars in the application:

```python
from prometheus_client import Counter

COUNTER = Counter('requests_total', 'Total requests')
COUNTER.inc(exemplars={'trace_id': 'abc123'})
```

Query exemplars:

```bash
curl -s 'http://localhost:9090/api/v1/query_exemplars?query=requests_total&start=1h ago&end=now'
```

## Examples

```bash
# View exemplars
curl -s 'http://localhost:9090/api/v1/query_exemplars?query=requests_total'

# Check exemplar configuration
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml' | grep exemplar
```
"""
    ),
    (
        "prometheus-native-histogram-error",
        "Prometheus Native Histogram Error",
        "How to fix native histogram errors in Prometheus",
        """## Common Causes

- Schema version not supported by Prometheus
- Bucket count mismatch with schema
- Native histogram not enabled in configuration
- Incompatible client library version

## How to Fix

Enable native histograms:

```yaml
storage:
  tsdb:
    enable_native_histograms: true
```

Use compatible client library:

```python
from prometheus_client import Histogram

# Native histogram with custom schema
HISTOGRAM = Histogram(
    'request_duration_seconds',
    'Request duration',
    buckets=[0.01, 0.1, 1, 10]
)
```

Query native histograms:

```promql
histogram_quantile(0.99, request_duration_seconds_bucket)
```

## Examples

```bash
# Check native histogram support
promtool version

# Query histogram bucket distribution
curl -s 'http://localhost:9090/api/v1/query?query=request_duration_seconds_bucket'

# Enable native histograms in config
prometheus --enable-feature=native-histograms
```
"""
    ),
    (
        "prometheus-remote-write-error",
        "Prometheus Remote Write Error",
        "How to fix Prometheus remote write errors when sending data to remote storage",
        """## Common Causes

- Remote storage endpoint unreachable
- Authentication failure with remote endpoint
- TLS certificate verification failed
- Remote storage returning HTTP 4xx/5xx errors
- Data format incompatibility

## How to Fix

Configure remote write:

```yaml
remote_write:
  - url: 'http://remote-storage:9201/api/v1/write'
    queue_config:
      max_samples_per_send: 5000
      batch_send_deadline: 5s
      max_shards: 200
    tls_config:
      ca_file: /etc/prometheus/ca.crt
```

Check remote write status:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.remoteWrite'
```

Verify remote endpoint:

```bash
curl -v http://remote-storage:9201/api/v1/write
```

## Examples

```bash
# Monitor remote write queue
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_storage_samples_total'

# Check remote write errors
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_storage_samples_failed_total'

# View queue configuration
curl -s http://localhost:9090/api/v1/status/config | grep -A 20 remote_write
```
"""
    ),
    (
        "prometheus-remote-write-queue",
        "Prometheus Remote Write Queue Backpressure",
        "How to fix Prometheus remote write queue buildup and backpressure",
        """## Common Causes

- Remote storage cannot keep up with ingestion rate
- Network bandwidth saturation
- Queue shards too low
- `max_samples_per_send` too small
- Remote storage under heavy load

## How to Fix

Tune queue configuration:

```yaml
remote_write:
  - url: 'http://remote-storage:9201/api/v1/write'
    queue_config:
      max_samples_per_send: 10000
      batch_send_deadline: 10s
      max_shards: 500
      min_shards: 10
      capacity: 10000
```

Monitor queue depth:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_storage_queue_highest_sent_timestamp_seconds'
```

Increase network bandwidth or add compression:

```yaml
    remote_write:
      - url: 'http://remote-storage:9201/api/v1/write'
        enable_http2: true
```

## Examples

```bash
# Check queue shards
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_storage_shards'

# Monitor send rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(prometheus_remote_storage_samples_sent_total[5m])'
```
"""
    ),
    (
        "prometheus-remote-read-error",
        "Prometheus Remote Read Error",
        "How to fix Prometheus remote read errors when querying remote storage",
        """## Common Causes

- Remote read endpoint unreachable
- Authentication or authorization failure
- Query timeout too short
- Data format mismatch between Prometheus and remote storage
- TLS configuration errors

## How to Fix

Configure remote read:

```yaml
remote_read:
  - url: 'http://remote-storage:9201/api/v1/read'
    read_recent: true
    tls_config:
      ca_file: /etc/prometheus/ca.crt
    basic_auth:
      username: prometheus
      password_file: /etc/prometheus/password
```

Check remote read status:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.remoteRead'
```

## Examples

```bash
# Test remote read endpoint
curl -X POST http://remote-storage:9201/api/v1/read -d '{}'

# Monitor remote read queries
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_read_queries_total'
```
"""
    ),
    (
        "prometheus-remote-read-timeout",
        "Prometheus Remote Read Timeout",
        "How to fix Prometheus remote read timeout errors",
        """## Common Causes

- Remote storage query taking too long
- Network latency to remote endpoint
- Query time range too large
- Remote storage overloaded

## How to Fix

Increase remote read timeout:

```yaml
remote_read:
  - url: 'http://remote-storage:9201/api/v1/read'
    timeout: 60s
```

Optimize query time range:

```yaml
# Use shorter evaluation intervals
global:
  evaluation_interval: 15s
```

Check network latency:

```bash
curl -o /dev/null -s -w '%{time_total}' http://remote-storage:9201/api/v1/read
```

## Examples

```bash
# Monitor remote read latency
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_read_duration_seconds'

# Check timeout configuration
curl -s http://localhost:9090/api/v1/status/config | grep -A 5 remote_read
```
"""
    ),
    (
        "prometheus-wal-corruption",
        "Prometheus WAL Corruption Error",
        "How to fix Prometheus Write-Ahead Log (WAL) corruption errors",
        """## Common Causes

- Power failure or unclean shutdown during writes
- Disk I/O error during WAL write
- Filesystem corruption
- Disk full during WAL operation

## How to Fix

Check WAL integrity:

```bash
promtool tsdb check-tombstones prometheus-data/
```

If WAL is corrupted, truncate and rebuild:

```bash
# Stop Prometheus
sudo systemctl stop prometheus

# Back up WAL directory
mv prometheus-data/wal prometheus-data/wal.bak

# Start Prometheus (will recreate WAL)
sudo systemctl start prometheus
```

Check disk health:

```bash
sudo smartctl -a /dev/sda
dmesg | grep -i error
```

Prevent future corruption with WAL config:

```yaml
storage:
  tsdb:
    wal_compression: true
```

## Examples

```bash
# Check WAL directory
ls -la prometheus-data/wal/

# Monitor WAL size
du -sh prometheus-data/wal/

# Check for corruption in logs
journalctl -u prometheus | grep -i "corrupt"
```
"""
    ),
    (
        "prometheus-wal-replay",
        "Prometheus WAL Replay Error",
        "How to fix errors during Prometheus WAL replay on startup",
        """## Common Causes

- WAL segments corrupted or incomplete
- Version mismatch between WAL writer and reader
- Insufficient disk space for WAL replay
- Memory limit exceeded during replay

## How to Fix

Check WAL replay status:

```bash
journalctl -u prometheus | grep -i "replay"
```

If replay fails, truncate WAL:

```bash
sudo systemctl stop prometheus

# Move corrupted WAL
mv prometheus-data/wal prometheus-data/wal.corrupted

# Start fresh
sudo systemctl start prometheus
```

Increase memory for large WAL:

```bash
prometheus --storage.tsdb.wal-compression --storage.tsdb.retention.time=30d
```

## Examples

```bash
# Monitor WAL replay progress
journalctl -u prometheus -f | grep replay

# Check WAL segment count
ls prometheus-data/wal/ | wc -l

# Check disk space before restart
df -h prometheus-data/
```
"""
    ),
    (
        "prometheus-tsdb-block-corrupt",
        "Prometheus TSDB Block Corruption Error",
        "How to fix Prometheus TSDB block corruption errors",
        """## Common Causes

- Disk I/O error during block write
- Power failure during compaction
- Filesystem corruption
- Insufficient disk space

## How to Fix

Check block integrity:

```bash
promtool tsdb analyze prometheus-data/
```

Identify and remove corrupted blocks:

```bash
sudo systemctl stop prometheus

# List blocks
ls -la prometheus-data/chunks_head/

# Remove corrupted block directories
rm -rf prometheus-data/chunks_head/<corrupted-block-id>

sudo systemctl start prometheus
```

Verify disk health:

```bash
sudo smartctl -a /dev/sda
```

## Examples

```bash
# Analyze TSDB
promtool tsdb analyze prometheus-data/

# Check block sizes
du -sh prometheus-data/chunks_head/*/

# Monitor compaction
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_compactions_total'
```
"""
    ),
    (
        "prometheus-tsdb-compaction-error",
        "Prometheus TSDB Compaction Error",
        "How to fix Prometheus TSDB compaction failures",
        """## Common Causes

- Insufficient disk space for compaction
- Too many blocks causing memory pressure
- I/O error during block merge
- Compaction running too frequently

## How to Fix

Check compaction status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_compactions_failed_total'
```

Ensure sufficient disk space (2x data size needed):

```bash
df -h prometheus-data/
du -sh prometheus-data/
```

Tune compaction settings:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
    retention.time: 15d
```

## Examples

```bash
# Check compaction metrics
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_compactions_total'

# Monitor block count
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_blocks_loaded'

# Check disk I/O
iostat -x 1 5
```
"""
    ),
    (
        "prometheus-chunk-not-found",
        "Prometheus Chunk Not Found Error",
        "How to fix Prometheus chunk not found errors during query execution",
        """## Common Causes

- Chunk deleted during compaction while being queried
- WAL corruption causing missing chunks
- Disk error removing chunk files
- Race condition between compaction and query

## How to Fix

Check chunk status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'
```

Restart Prometheus to rebuild chunk index:

```bash
sudo systemctl restart prometheus
```

Check disk for missing files:

```bash
ls -la prometheus-data/chunks_head/
```

## Examples

```bash
# Monitor chunk count
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'

# Check for chunk errors in logs
journalctl -u prometheus | grep -i "chunk not found"

# Analyze TSDB
promtool tsdb analyze prometheus-data/
```
"""
    ),
    (
        "prometheus-index-not-found",
        "Prometheus Index Not Found Error",
        "How to fix Prometheus TSDB index not found errors",
        """## Common Causes

- TSDB index files corrupted
- Index not built after fresh start
- Disk error during index creation
- Incomplete block after compaction

## How to Fix

Check index files:

```bash
ls -la prometheus-data/index/
```

Rebuild index by restarting:

```bash
sudo systemctl stop prometheus
sudo systemctl start prometheus
```

If persistent, clear data and re-scrape:

```bash
sudo systemctl stop prometheus
rm -rf prometheus-data/
sudo systemctl start prometheus
```

## Examples

```bash
# Check index status
curl -s 'http://localhost:9090/api/v1/status/tsdb' | jq '.data.indexStats'

# Monitor index operations
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_reloads_failures_total'
```
"""
    ),
    (
        "prometheus-tombstone-error",
        "Prometheus Tombstone Error",
        "How to fix Prometheus tombstone errors during data deletion",
        """## Common Causes

- Tombstone file corrupted
- Tombstone count exceeds limit
- Delete operation creating invalid tombstones
- Tombstone file not properly flushed

## How to Fix

Check tombstone file:

```bash
ls -la prometheus-data/tombstones
```

Validate tombstones:

```bash
promtool tsdb check-tombstones prometheus-data/
```

If corrupted, remove and rebuild:

```bash
sudo systemctl stop prometheus
mv prometheus-data/tombstones prometheus-data/tombstones.bak
sudo systemctl start prometheus
```

## Examples

```bash
# Check tombstone count
wc -l prometheus-data/tombstones

# Monitor deletion operations
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_series'

# Validate tombstones
promtool tsdb check-tombstones prometheus-data/
```
"""
    ),
    (
        "prometheus-memory-snapshot-error",
        "Prometheus Memory Snapshot Error",
        "How to fix Prometheus memory snapshot (head block) errors",
        """## Common Causes

- Insufficient memory for snapshot operation
- Too many active series during snapshot
- Memory limit exceeded during snapshot
- Snapshot blocked by query load

## How to Fix

Check head block status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'
```

Increase memory for large datasets:

```bash
prometheus --storage.tsdb.retention.time=15d --query.max-concurrency=20
```

Monitor memory during snapshot:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=process_resident_memory_bytes'
```

## Examples

```bash
# Monitor head block
curl -s 'http://localhost:9090/api/v1/status/tsdb' | jq '.data.headStats'

# Check memory usage
curl -s 'http://localhost:9090/api/v1/query?query=process_resident_memory_bytes'

# Monitor snapshots
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_head_truncations_total'
```
"""
    ),
    (
        "prometheus-head-compaction-error",
        "Prometheus Head Compaction Error",
        "How to fix Prometheus head compaction failures",
        """## Common Causes

- Head block too large for compaction
- Disk space insufficient for new block
- Memory pressure during compaction
- I/O error writing compacted block

## How to Fix

Check head compaction status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_compactions_failed_total'
```

Ensure sufficient disk space:

```bash
df -h prometheus-data/
```

Tune compaction interval:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
```

## Examples

```bash
# Monitor compaction
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_compactions_total'

# Check disk usage
du -sh prometheus-data/

# Monitor compaction duration
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_compactions_duration_seconds'
```
"""
    ),
    (
        "prometheus-block-too-large",
        "Prometheus Block Too Large Error",
        "How to fix Prometheus block size exceeding limits",
        """## Common Causes

- Too many samples in a single block
- High cardinality metrics creating large blocks
- Block duration too long
- Memory limit for block processing exceeded

## How to Fix

Adjust block duration:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 24h
```

Reduce metric cardinality:

```yaml
scrape_configs:
  - job_name: 'app'
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: 'high_cardinality_.*'
        action: drop
```

Monitor block sizes:

```bash
du -sh prometheus-data/chunks_head/*/
```

## Examples

```bash
# Check block count and sizes
curl -s 'http://localhost:9090/api/v1/status/tsdb' | jq '.data.blockStats'

# Monitor block creation
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'
```
"""
    ),
    (
        "prometheus-block-duration-error",
        "Prometheus Block Duration Error",
        "How to fix Prometheus block duration misconfiguration",
        """## Common Causes

- Block duration too short causing too many small blocks
- Block duration too long causing large memory usage
- min_block_duration greater than max_block_duration
- Overlap between block ranges

## How to Fix

Set proper block duration:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
```

For remote storage backends:

```yaml
storage:
  tsdb:
    min_block_duration: 5m
    max_block_duration: 1h
```

## Examples

```bash
# Check block durations
ls -la prometheus-data/chunks_head/ | head -10

# Monitor block creation rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(prometheus_tsdb_head_chunks_created_total[5m])'

# View TSDB status
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data'
```
"""
    ),
    (
        "prometheus-retention-expired",
        "Prometheus Retention Period Expired",
        "How to fix Prometheus data retention expiration issues",
        """## Common Causes

- Retention period too short for required data range
- Default retention (15 days) insufficient
- Disk space triggering early deletion
- Compaction removing data before retention period

## How to Fix

Increase retention period:

```yaml
storage:
  tsdb:
    retention.time: 30d
    retention.size: 50GB
```

Command-line configuration:

```bash
prometheus --storage.tsdb.retention.time=90d
```

Check current retention:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.storageRetention'
```

## Examples

```bash
# Check oldest data
curl -s 'http://localhost:9090/api/v1/query?query=min_over_time(up[30d])'

# Monitor disk usage
df -h prometheus-data/

# View retention config
curl -s http://localhost:9090/api/v1/status/config | grep retention
```
"""
    ),
    (
        "prometheus-relabel-config-error",
        "Prometheus Relabel Config Error",
        "How to fix Prometheus relabel configuration errors",
        """## Common Causes

- Invalid regex pattern in relabel_config
- Missing required fields (source_labels, target_label)
- Unknown action specified
- Regex match group index out of range

## How to Fix

Validate relabel config syntax:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__address__]
        regex: '(.*):(.*)'
        target_label: host
        replacement: '${1}'
        action: replace
```

Check regex pattern:

```bash
echo "localhost:8080" | grep -P '(.*):(.*)'
```

Valid relabel actions:

```yaml
# replace (default): regex match and replace
# keep: keep targets matching regex
# drop: drop targets matching regex
# hashmod: hash modulo
# labelmap: map label names
```

## Examples

```bash
# Test relabel regex
echo "10.0.0.1:8080" | grep -oP '(\d+\.\d+\.\d+\.\d+)'

# Check relabel configs
curl -s http://localhost:9090/api/v1/status/config | grep -A 10 relabel_configs

# Validate config
promtool check config prometheus.yml
```
"""
    ),
    (
        "prometheus-relabel-keep-action",
        "Prometheus Relabel Keep Action Error",
        "How to fix Prometheus relabel keep action dropping desired targets",
        """## Common Causes

- Regex pattern not matching any targets
- Wrong source_labels specified
- Regex is case-sensitive and does not match
- Missing leading or trailing anchors in regex

## How to Fix

Use correct keep action:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '.*,production,.*'
        action: keep
```

Test regex against label values:

```bash
echo "production,web,primary" | grep -P '.*,production,.*'
```

Use case-insensitive matching:

```yaml
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '(?i).*production.*'
        action: keep
```

## Examples

```bash
# Test regex
echo "staging,web" | grep -P '.*,production,.*'
# No match - target will be dropped

echo "production,web" | grep -P '.*,production,.*'
# Match - target will be kept
```
"""
    ),
    (
        "prometheus-relabel-drop-action",
        "Prometheus Relabel Drop Action Error",
        "How to fix Prometheus relabel drop action incorrectly filtering targets",
        """## Common Causes

- Regex matching too broadly, dropping desired targets
- Wrong source_labels causing unexpected drops
- Regex pattern too permissive
- Testing regex without considering label format

## How to Fix

Use precise drop action:

```yaml
scrape_configs:
  - job_name: 'app'
    relabel_configs:
      - source_labels: [__meta_consul_tags]
        regex: '.*,deprecated,.*'
        action: drop
```

Test regex carefully:

```bash
# Test what will be dropped
echo "deprecated,v1" | grep -P '.*,deprecated,.*'
# Match - will be dropped

echo "production,v2" | grep -P '.*,deprecated,.*'
# No match - will be kept
```

## Examples

```bash
# View active targets
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | .labels.instance'

# Check drop rules
curl -s http://localhost:9090/api/v1/status/config | grep -A 5 "action: drop"
```
"""
    ),
    (
        "prometheus-relabel-replace-action",
        "Prometheus Relabel Replace Action Error",
        "How to fix Prometheus relabel replace action not producing expected output",
        """## Common Causes

- Replacement string referencing non-existent capture groups
- Source labels not producing expected values
- Regex not matching the input
- Replacement using wrong group index

## How to Fix

Use correct replacement syntax:

```yaml
relabel_configs:
  - source_labels: [__address__]
    regex: '(.*):(.*)'
    target_label: host
    replacement: '${1}'
    action: replace
```

Valid capture group references:

```yaml
replacement: '${1}'        # First capture group
replacement: '${2}'        # Second capture group
replacement: '${1}:${2}'   # Combine groups
replacement: '${0}'        # Entire match
replacement: 'prefix_${1}' # Static prefix + group
```

Test regex and replacement:

```bash
echo "web-01:8080" | sed -E 's/(.*):(.*)/host=\1 port=\2/'
# Output: host=web-01 port=8080
```

## Examples

```bash
# Test replacement
echo "10.0.1.5:9090" | sed -E 's/([0-9]+\.[0-9]+\.[0-9]+)\.([0-9]+)/\1.0/'

# Check applied labels
curl -s 'http://localhost:9090/api/v1/query?query=up' | jq '.data.result[0].metric'
```
"""
    ),
    (
        "prometheus-relabel-hashmod-action",
        "Prometheus Relabel Hashmod Action Error",
        "How to fix Prometheus hashmod relabel action for shard-based scraping",
        """## Common Causes

- Hashmod value out of range for shard count
- Mismatch between hashmod and total_shards
- Wrong source_labels for hashing
- Hashmod action used with non-static targets

## How to Fix

Configure hashmod for sharded scraping:

```yaml
scrape_configs:
  - job_name: 'sharded-app'
    relabel_configs:
      - source_labels: [__address__]
        modulus: 3
        target_label: __tmp_hash
        action: hashmod
      - source_labels: [__tmp_hash]
        regex: 0
        action: keep
```

Each Prometheus instance uses a different hashmod value:

```yaml
# Instance 0
- source_labels: [__address__]
  modulus: 3
  target_label: __tmp_hash
  action: hashmod
- source_labels: [__tmp_hash]
  regex: 0
  action: keep

# Instance 1
- regex: 1
  action: keep

# Instance 2
- regex: 2
  action: keep
```

## Examples

```bash
# Check shard distribution
curl -s 'http://localhost:9090/api/v1/query?query=count by (job)(up)'

# Verify targets per shard
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets | length'
```
"""
    ),
    (
        "prometheus-relabel-labelmap-action",
        "Prometheus Relabel Labelmap Action Error",
        "How to fix Prometheus labelmap relabel action for label name mapping",
        """## Common Causes

- Regex pattern not matching any label names
- Wrong regex for label name mapping
- Label names contain unexpected characters
- labelmap applied after other relabel rules modified labels

## How to Fix

Use correct labelmap configuration:

```yaml
relabel_configs:
  - regex: '__meta_consul_service_(.+)'
    target_label: 'consul_\\1'
    action: labelmap
```

This maps labels like `__meta_consul_service_name` to `consul_name`.

Test regex against label names:

```bash
echo "__meta_consul_service_name" | grep -oP '__meta_consul_service_(.+)'
# Output: name
```

## Examples

```bash
# View meta labels
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[0].labels' | grep meta

# Test regex
echo "__meta_consul_tags" | grep -oP '__meta_consul_service_(.+)'
```
"""
    ),
    (
        "prometheus-target-labels-conflict",
        "Prometheus Target Labels Conflict",
        "How to fix target labels conflicting in Prometheus relabeling",
        """## Common Causes

- Two relabel rules writing to the same target label
- Target exposing a label that conflicts with `job` or `instance`
- Multiple relabel_configs overwriting the same label
- honor_labels not set when target labels should be preserved

## How to Fix

Use honor_labels to preserve target labels:

```yaml
scrape_configs:
  - job_name: 'app'
    honor_labels: true
```

Avoid conflicting relabel rules:

```yaml
relabel_configs:
  # Check that no two rules write to the same target_label
  - source_labels: [__meta_consul_service]
    target_label: service
    action: replace
  # Do not also write to 'service' label
```

## Examples

```bash
# Check for label conflicts in logs
journalctl -u prometheus | grep "label conflict"

# View target labels
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[0].labels'
```
"""
    ),
    (
        "prometheus-rule-evaluation-error",
        "Prometheus Rule Evaluation Error",
        "How to fix Prometheus rule evaluation errors in recording and alerting rules",
        """## Common Causes

- Invalid PromQL expression in rule file
- Circular dependency between recording rules
- Rule referencing non-existent metric
- Rule file syntax error

## How to Fix

Validate rule files:

```bash
promtool check rules rules.yml
```

Correct rule syntax:

```yaml
groups:
  - name: example
    rules:
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
```

Check for circular dependencies:

```bash
promtool check rules rules.yml 2>&1 | grep "circular"
```

Verify referenced metrics exist:

```bash
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq '.data[]' | grep http_requests
```

## Examples

```bash
# Validate all rule files
promtool check rules /etc/prometheus/rules/*.yml

# Check rule evaluation errors
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_rule_evaluation_failures_total'

# List recording rules
curl -s 'http://localhost:9090/api/v1/rules' | jq '.data.groups[] | .rules[] | select(.type == "recording")'
```
"""
    ),
    (
        "prometheus-recording-rule-error",
        "Prometheus Recording Rule Error",
        "How to fix Prometheus recording rule errors",
        """## Common Causes

- Recording rule expression producing NaN or Inf
- High cardinality output from recording rule
- Recording rule name collision with existing metric
- Expression referencing deleted metric

## How to Fix

Define recording rules with proper naming:

```yaml
groups:
  - name: http_stats
    rules:
      - record: job:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
```

Naming convention:

```yaml
# level:metric:operations
# Examples:
#   job:http_requests:rate5m
#   instance:node_cpu:utilization
```

Check recording rule output:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=job:http_requests:rate5m'
```

## Examples

```bash
# List recording rules
curl -s 'http://localhost:9090/api/v1/rules' | jq '.data.groups[].rules[] | select(.type == "recording")'

# Test recording rule expression
curl -s 'http://localhost:9090/api/v1/query?query=sum(rate(http_requests_total[5m])) by (job)'
```
"""
    ),
    (
        "prometheus-alerting-rule-error",
        "Prometheus Alerting Rule Error",
        "How to fix Prometheus alerting rule configuration errors",
        """## Common Causes

- Invalid PromQL expression in alert rule
- Missing `alert` or `expr` field
- `for` duration too short causing flapping
- Alert annotation templates with errors

## How to Fix

Define proper alerting rules:

```yaml
groups:
  - name: alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

Validate alert rules:

```bash
promtool check rules alert-rules.yml
```

## Examples

```bash
# Validate alert rules
promtool check rules /etc/prometheus/alerts/*.yml

# Test alert expression
curl -s 'http://localhost:9090/api/v1/query?query=rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.1'

# List active alerts
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | .labels.alertname'
```
"""
    ),
    (
        "prometheus-alert-fired",
        "Prometheus Alert Fired But Not Resolved",
        "How to fix Prometheus alerts that fire but do not resolve",
        """## Common Causes

- Condition still true when alert should resolve
- `for` duration too short, alert resolves before action taken
- Metric data gap causing repeated firing
- Alertmanager not receiving resolve notification

## How to Fix

Verify alert condition:

```bash
curl -s 'http://localhost:9090/api/v1/alerts' | jq '.data.alerts[] | select(.labels.alertname == "HighErrorRate")'
```

Check alert state transitions:

```bash
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | {name: .labels.alertname, state: .state, activeAt: .activeAt}'
```

Increase `for` duration for stability:

```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
  for: 10m  # Wait longer before firing
```

## Examples

```bash
# View all alerts
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[]'

# Check alert history
curl -s 'http://localhost:9090/api/v1/alerts?state=unresolved'

# Test resolve condition
curl -s 'http://localhost:9090/api/v1/query?query=rate(http_requests_total{status=~"5.."}[5m]) <= 0.1'
```
"""
    ),
    (
        "prometheus-alert-not-firing",
        "Prometheus Alert Not Firing",
        "How to fix Prometheus alerts that should fire but do not",
        """## Common Causes

- Alert expression evaluating to false
- Metric not available or missing labels
- `for` duration not yet satisfied
- Rule file not loaded or has syntax errors
- Evaluation interval too slow

## How to Fix

Test alert expression manually:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=<alert-expr>'
```

Check if rules are loaded:

```bash
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[].rules[] | select(.type == "alerting") | .name'
```

Validate rule file:

```bash
promtool check rules alert-rules.yml
```

Verify evaluation interval:

```yaml
groups:
  - name: alerts
    interval: 15s  # Default is global evaluation_interval
    rules:
      - alert: MyAlert
        expr: up == 0
        for: 2m
```

## Examples

```bash
# Check rule evaluation
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[] | .rules[] | select(.type == "alerting") | {name: .name, state: .state, evaluations: .evaluationFailures}'

# Test expression
curl -s 'http://localhost:9090/api/v1/query?query=up == 0'

# Reload rules
kill -HUP $(pidof prometheus)
```
"""
    ),
    (
        "prometheus-alertmanager-not-found",
        "Prometheus Alertmanager Not Found",
        "How to fix Prometheus cannot find or connect to Alertmanager",
        """## Common Causes

- Alertmanager URL misconfigured in Prometheus
- Alertmanager not running
- DNS resolution failure for Alertmanager host
- Network firewall blocking connection
- Alertmanager listening on different port

## How to Fix

Configure Alertmanager in prometheus.yml:

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          - 'localhost:9093'
```

Check Alertmanager status:

```bash
curl http://localhost:9093/-/healthy
curl http://localhost:9093/api/v2/status
```

Verify Prometheus can reach Alertmanager:

```bash
curl -s http://localhost:9090/api/v1/status/config | jq '.data.yaml' | grep -A 5 alerting
```

## Examples

```bash
# Check Alertmanager connectivity
curl http://localhost:9093/-/healthy

# Verify Prometheus targets include Alertmanager
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.labels.job == "alertmanager")'

# Check Alertmanager config
amtool config show --alertmanager.url=http://localhost:9093
```
"""
    ),
    (
        "prometheus-alertmanager-discovery-error",
        "Prometheus Alertmanager Discovery Error",
        "How to fix Prometheus Alertmanager service discovery errors",
        """## Common Causes

- DNS SRV record lookup failure for Alertmanager
- Consul/etcd discovery not returning Alertmanager targets
- Kubernetes service discovery misconfiguration
- Alertmanager cluster endpoints not resolvable

## How to Fix

Use DNS discovery:

```yaml
alerting:
  alertmanagers:
    - dns_sd_configs:
        - names:
            - '_alertmanager._tcp.example.com'
          type: SRV
          refresh_interval: 30s
```

Use static config as fallback:

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - 'alertmanager-1:9093'
            - 'alertmanager-2:9093'
```

## Examples

```bash
# Test DNS SRV lookup
dig _alertmanager._tcp.example.com SRV

# Check discovered Alertmanager targets
curl -s http://localhost:9090/api/v1/alertmanagers | jq '.data.activeAlertmanagers'
```
"""
    ),
    (
        "prometheus-alertmanager-timeout",
        "Prometheus Alertmanager Timeout Error",
        "How to fix Prometheus Alertmanager connection timeout errors",
        """## Common Causes

- Alertmanager under heavy load
- Network latency between Prometheus and Alertmanager
- Alertmanager processing large notification batch
- Timeout configuration too low

## How to Fix

Configure Alertmanager timeout:

```yaml
alerting:
  alertmanagers:
    - timeout: 30s
      static_configs:
        - targets:
          - 'localhost:9093'
```

Check Alertmanager response time:

```bash
time curl http://localhost:9093/api/v2/status
```

Increase Alertmanager resources:

```bash
# Check Alertmanager metrics
curl http://localhost:9093/metrics | grep "notification_duration"
```

## Examples

```bash
# Measure Alertmanager latency
curl -o /dev/null -s -w '%{time_total}\\n' http://localhost:9093/api/v2/alerts

# Check Alertmanager processing
curl http://localhost:9093/metrics | grep "alertmanager_notifications_total"
```
"""
    ),
    (
        "prometheus-alert-template-error",
        "Prometheus Alert Template Error",
        "How to fix Prometheus alert template syntax and rendering errors",
        """## Common Causes

- Invalid Go template syntax in annotations
- Referencing non-existent label or annotation
- Template function not available
- Missing or extra delimiters

## How to Fix

Use correct template syntax:

```yaml
annotations:
  summary: "High error rate on {{ $labels.instance }}"
  description: "Error rate is {{ $value | humanizePercentage }}"
```

Available template variables:

```yaml
# $labels  - all labels of the series
# $value   - current value of the expression
# $labels.instance - specific label
# $labels.job
```

Common template functions:

```yaml
{{ $value | humanize }}          # 1234567 -> 1.235M
{{ $value | humanizePercentage }} # 0.1532 -> 15.32%
{{ $value | humanizeDuration }}   # 365 -> 1h0m0s
```

## Examples

```bash
# Test template rendering
amtool template render --template-file=template.tmpl alertname=HighErrorRate instance=localhost:8080

# Check alert annotations
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[].annotations'
```
"""
    ),
    (
        "prometheus-amtool-error",
        "Prometheus amtool Error",
        "How to fix amtool command-line tool errors for Alertmanager",
        """## Common Causes

- Wrong Alertmanager URL in amtool config
- amtool version mismatch with Alertmanager version
- Network connectivity issue to Alertmanager
- Invalid alertmanager API request

## How to Fix

Configure amtool:

```bash
# Set Alertmanager URL
amtool --alertmanager.url=http://localhost:9093 alert query

# Or use configuration file
echo "alertmanager.url: http://localhost:9093" > ~/.config/amtool/config.yml
```

Check amtool version:

```bash
amtool --version
```

Test connectivity:

```bash
amtool --alertmanager.url=http://localhost:9093 config routes
```

## Examples

```bash
# List alerts
amtool --alertmanager.url=http://localhost:9093 alert query

# Add silence
amtool --alertmanager.url=http://localhost:9093 silence add alertname=HighErrorRate

# Check configuration
amtool --alertmanager.url=http://localhost:9093 config show
```
"""
    ),
    (
        "prometheus-silences-expired",
        "Prometheus Alertmanager Silences Expired",
        "How to handle expired silences in Alertmanager",
        """## Common Causes

- Silence duration too short
- Silence not renewed before expiration
- Default duration not sufficient
- Silences created with past end time

## How to Fix

Check active silences:

```bash
amtool --alertmanager.url=http://localhost:9093 silence query
```

Create longer silences:

```bash
amtool --alertmanager.url=http://localhost:9093 silence add \
  alertname=HighErrorRate \
  --duration=24h \
  --comment="Maintenance window"
```

List and manage silences:

```bash
amtool --alertmanager.url=http://localhost:9093 silence query --active
```

## Examples

```bash
# Query active silences
amtool silence query --alertmanager.url=http://localhost:9093

# Expire a specific silence
amtool silence expire <silence-id> --alertmanager.url=http://localhost:9093

# Create silence via API
curl -X POST http://localhost:9093/api/v2/silences -d '{"matchers":[{"name":"alertname","value":"HighErrorRate"}],"startsAt":"2024-01-01T00:00:00Z","endsAt":"2024-01-02T00:00:00Z"}'
```
"""
    ),
    (
        "prometheus-inhibition-rule-error",
        "Prometheus Alertmanager Inhibition Rule Error",
        "How to fix Alertmanager inhibition rules not suppressing alerts correctly",
        """## Common Causes

- Source and target matchers not matching correctly
- Inhibition rules applied in wrong order
- Label names case-sensitive mismatch
- Missing labels in inhibited alerts

## How to Fix

Configure inhibition rules:

```yaml
inhibit_rules:
  - source_matchers:
      - severity = critical
    target_matchers:
      - severity = warning
    equal: ['alertname', 'instance']
```

Test matcher expressions:

```bash
amtool --alertmanager.url=http://localhost:9093 config routes
```

Verify alert labels:

```bash
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | .labels'
```

## Examples

```bash
# Check inhibition rules
amtool --alertmanager.url=http://localhost:9093 config show | grep -A 10 inhibit_rules

# View inhibited alerts
curl -s http://localhost:9090/api/v1/alerts | jq '.data.alerts[] | select(.status.inhibitedBy != null)'
```
"""
    ),
    (
        "prometheus-routing-tree-error",
        "Prometheus Alertmanager Routing Tree Error",
        "How to fix Alertmanager routing tree configuration errors",
        """## Common Causes

- Invalid receiver name in route
- Circular route references
- Missing default receiver
- Route matchers with syntax errors

## How to Fix

Configure proper routing tree:

```yaml
route:
  receiver: 'default'
  group_by: ['alertname', 'cluster']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
    - match:
        severity: warning
      receiver: 'slack-warning'
```

Validate configuration:

```bash
amtool check-config alertmanager.yml
```

## Examples

```bash
# Validate routing config
amtool check-config /etc/alertmanager/alertmanager.yml

# Test route matching
amtool --alertmanager.url=http://localhost:9093 config routes --tree

# View active routes
curl http://localhost:9093/api/v2/status | jq '.config.original.route'
```
"""
    ),
    (
        "prometheus-receiver-not-found",
        "Prometheus Alertmanager Receiver Not Found",
        "How to fix Alertmanager receiver not found errors",
        """## Common Causes

- Receiver name in route does not match any defined receiver
- Typo in receiver name
- Receiver defined but not referenced in any route
- Receiver deleted but route still references it

## How to Fix

Check receiver names:

```yaml
receivers:
  - name: 'slack-notifications'
    slack_configs:
      - channel: '#alerts'
```

Verify route references existing receiver:

```yaml
route:
  receiver: 'slack-notifications'
```

List configured receivers:

```bash
amtool --alertmanager.url=http://localhost:9093 config show --format=json | jq '.route.receiver'
```

## Examples

```bash
# List receivers
amtool --alertmanager.url=http://localhost:9093 config show | grep "receiver:"

# Check receiver config
amtool check-config /etc/alertmanager/alertmanager.yml

# View all receivers
curl http://localhost:9093/api/v2/status | jq '.config.original.receivers[].name'
```
"""
    ),
    (
        "prometheus-webhook-receiver-error",
        "Prometheus Alertmanager Webhook Receiver Error",
        "How to fix Alertmanager webhook receiver errors",
        """## Common Causes

- Webhook endpoint URL unreachable
- HTTP timeout when sending notification
- Invalid JSON payload
- Webhook endpoint returning non-2xx status
- TLS certificate verification failure

## How to Fix

Configure webhook receiver:

```yaml
receivers:
  - name: 'webhook'
    webhook_configs:
      - url: 'http://webhook-handler:5001/alerts'
        send_resolved: true
        http_config:
          follow_redirects: true
```

Test webhook endpoint:

```bash
curl -X POST http://webhook-handler:5001/alerts -H 'Content-Type: application/json' -d '{"status":"firing","alerts":[]}'
```

## Examples

```bash
# Check webhook notification logs
curl http://localhost:9093/metrics | grep "alertmanager_notifications_failed_total"

# Test webhook endpoint
curl -v http://webhook-handler:5001/alerts

# View notification errors
amtool --alertmanager.url=http://localhost:9093 silence query
```
"""
    ),
    (
        "prometheus-email-receiver-error",
        "Prometheus Alertmanager Email Receiver Error",
        "How to fix Alertmanager email notification errors",
        """## Common Causes

- SMTP server unreachable or misconfigured
- Authentication failure with SMTP server
- Invalid email addresses in configuration
- SMTP TLS configuration error
- Email content exceeding size limit

## How to Fix

Configure email receiver:

```yaml
receivers:
  - name: 'email'
    email_configs:
      - to: 'ops-team@example.com'
        from: 'alertmanager@example.com'
        smarthost: 'smtp.example.com:587'
        auth_username: 'alertmanager@example.com'
        auth_password: 'password'
        require_tls: true
```

Test SMTP connectivity:

```bash
telnet smtp.example.com 587
```

## Examples

```bash
# Test email sending
echo "Test email" | mail -s "Alert Test" ops-team@example.com

# Check email notification status
curl http://localhost:9093/metrics | grep "alertmanager_notifications_total"

# Verify SMTP config
amtool check-config /etc/alertmanager/alertmanager.yml
```
"""
    ),
    (
        "prometheus-pagerduty-receiver-error",
        "Prometheus Alertmanager PagerDuty Receiver Error",
        "How to fix Alertmanager PagerDuty notification errors",
        """## Common Causes

- Invalid PagerDuty service key
- PagerDuty API endpoint unreachable
- Event payload exceeds size limit
- Service key rotated without updating config

## How to Fix

Configure PagerDuty receiver:

```yaml
receivers:
  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: 'your-pagerduty-integration-key'
        description: '{{ .CommonAnnotations.summary }}'
        details:
          firing: '{{ .Alerts.Firing | len }}'
          resolved: '{{ .Alerts.Resolved | len }}'
```

Verify service key:

```bash
curl -X POST https://events.pagerduty.com/v2/enqueue \
  -H 'Content-Type: application/json' \
  -d '{"routing_key":"YOUR_KEY","event_action":"trigger","payload":{"summary":"Test","severity":"critical","source":"prometheus"}}'
```

## Examples

```bash
# Check PagerDuty notification status
curl http://localhost:9093/metrics | grep "pagerduty"

# Test integration
curl -X POST https://events.pagerduty.com/v2/enqueue -d '{"routing_key":"YOUR_KEY","event_action":"trigger","payload":{"summary":"Test alert","severity":"warning","source":"test"}}'
```
"""
    ),
    (
        "prometheus-slack-receiver-error",
        "Prometheus Alertmanager Slack Receiver Error",
        "How to fix Alertmanager Slack notification errors",
        """## Common Causes

- Slack webhook URL expired or revoked
- Invalid channel name
- Message payload too large
- Slack API rate limit exceeded
- Webhook URL missing or malformed

## How to Fix

Configure Slack receiver:

```yaml
receivers:
  - name: 'slack'
    slack_configs:
      - channel: '#alerts'
        api_url: 'https://hooks.slack.com/services/T00/B00/xxx'
        send_resolved: true
        title: '{{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'
```

Test webhook URL:

```bash
curl -X POST https://hooks.slack.com/services/T00/B00/xxx \
  -H 'Content-Type: application/json' \
  -d '{"text":"Test alert notification"}'
```

## Examples

```bash
# Test Slack webhook
curl -X POST https://hooks.slack.com/services/T00/B00/xxx -d '{"text":"Alert test from Prometheus"}'

# Check Slack notification status
curl http://localhost:9093/metrics | grep "alertmanager_notifications_total"
```
"""
    ),
    (
        "prometheus-opsgenie-receiver-error",
        "Prometheus Alertmanager OpsGenie Receiver Error",
        "How to fix Alertmanager OpsGenie notification errors",
        """## Common Causes

- Invalid OpsGenie API key
- API endpoint misconfigured
- Message priority not set correctly
- Teams or responders not found in OpsGenie

## How to Fix

Configure OpsGenie receiver:

```yaml
receivers:
  - name: 'opsgenie'
    opsgenie_configs:
      - api_key: 'your-opsgenie-api-key'
        message: '{{ .CommonAnnotations.summary }}'
        description: '{{ .CommonAnnotations.description }}'
        teams: 'operations'
        priority: '{{ if eq .CommonLabels.severity "critical" }}P1{{ else }}P2{{ end }}'
```

## Examples

```bash
# Test OpsGenie API
curl -X POST https://api.opsgenie.com/v2/alerts \
  -H "Authorization: GenieKey YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message":"Test alert","alias":"test-alert","priority":"P2"}'
```
"""
    ),
    (
        "prometheus-victorops-receiver-error",
        "Prometheus Alertmanager VictorOps Receiver Error",
        "How to fix Alertmanager VictorOps notification errors",
        """## Common Causes

- Invalid VictorOps API key
- Routing key misconfigured
- VictorOps API endpoint unreachable
- Message format incompatible

## How to Fix

Configure VictorOps receiver:

```yaml
receivers:
  - name: 'victorops'
    victorops_configs:
      - api_key: 'your-victorops-api-key'
        routing_key: 'operations'
        message_type: '{{ if eq .CommonLabels.severity "critical" }}CRITICAL{{ else }}WARNING{{ end }}'
        state_message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Test VictorOps API
curl -X POST https://alert.victorops.com/integrations/generic/20131114/alert \
  -H "Content-Type: application/json" \
  -d '{"message_type":"CRITICAL","routing_key":"operations","state_message":"Test alert","entity_id":"test-123"}'
```
"""
    ),
    (
        "prometheus-pushover-receiver-error",
        "Prometheus Alertmanager Pushover Receiver Error",
        "How to fix Alertmanager Pushover notification errors",
        """## Common Causes

- Invalid Pushover user key or application token
- Pushover API unreachable
- Notification priority too high for user settings
- Message length exceeding Pushover limit

## How to Fix

Configure Pushover receiver:

```yaml
receivers:
  - name: 'pushover'
    pushover_configs:
      - user_key: 'your-user-key'
        token: 'your-application-token'
        title: '{{ .CommonAnnotations.summary }}'
        message: '{{ .CommonAnnotations.description }}'
        priority: '{{ if eq .CommonLabels.severity "critical" }}2{{ else }}0{{ end }}'
```

## Examples

```bash
# Test Pushover notification
curl -s \
  --form-string "token=YOUR_APP_TOKEN" \
  --form-string "user=YOUR_USER_KEY" \
  --form-string "message=Test alert from Prometheus" \
  https://api.pushover.net/1/messages.json
```
"""
    ),
    (
        "prometheus-wechat-receiver-error",
        "Prometheus Alertmanager WeChat Receiver Error",
        "How to fix Alertmanager WeChat notification errors",
        """## Common Causes

- Invalid WeChat Corp ID or agent secret
- WeChat API token expired
- Party or tag IDs not found
- Message template rendering error

## How to Fix

Configure WeChat receiver:

```yaml
receivers:
  - name: 'wechat'
    wechat_configs:
      - corp_id: 'your-corp-id'
        to_party: '1'
        to_tag: 'tag1'
        agent_id: 'your-agent-id'
        api_secret: 'your-api-secret'
        message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Test WeChat API token
curl "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=YOUR_ID&corpsecret=YOUR_SECRET"

# Send test message
curl -X POST "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=YOUR_TOKEN" \
  -d '{"touser":"@all","msgtype":"text","agentid":1,"text":{"content":"Test alert"}}'
```
"""
    ),
    (
        "prometheus-telegram-receiver-error",
        "Prometheus Alertmanager Telegram Receiver Error",
        "How to fix Alertmanager Telegram notification errors",
        """## Common Causes

- Invalid bot token
- Chat ID not found or bot not added to group
- Telegram API rate limit exceeded
- Message too long for Telegram limit

## How to Fix

Configure Telegram receiver:

```yaml
receivers:
  - name: 'telegram'
    telegram_configs:
      - bot_token: 'your-bot-token'
        chat_id: -1001234567890
        parse_mode: 'HTML'
        message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Get bot updates to find chat ID
curl "https://api.telegram.org/botYOUR_TOKEN/getUpdates"

# Send test message
curl -X POST "https://api.telegram.org/botYOUR_TOKEN/sendMessage" \
  -d "chat_id=-1001234567890&text=Test alert from Prometheus"
```
"""
    ),
    (
        "prometheus-discord-receiver-error",
        "Prometheus Alertmanager Discord Receiver Error",
        "How to fix Alertmanager Discord notification errors",
        """## Common Causes

- Invalid Discord webhook URL
- Webhook URL expired or deleted
- Message embeds exceeding Discord limits
- Bot permissions insufficient

## How to Fix

Configure Discord receiver:

```yaml
receivers:
  - name: 'discord'
    discord_configs:
      - api_url: 'https://discord.com/api/webhooks/YOUR_WEBHOOK'
        message: '{{ .CommonAnnotations.summary }}'
```

## Examples

```bash
# Test Discord webhook
curl -X POST https://discord.com/api/webhooks/YOUR_WEBHOOK \
  -H "Content-Type: application/json" \
  -d '{"content":"Test alert from Prometheus"}'
```
"""
    ),
    (
        "prometheus-http-client-error",
        "Prometheus HTTP Client Error",
        "How to fix Prometheus HTTP client errors when connecting to targets",
        """## Common Causes

- TLS certificate verification failure
- Connection refused by target
- HTTP redirect loop
- DNS resolution failure
- Connection timeout

## How to Fix

Configure HTTP client settings:

```yaml
scrape_configs:
  - job_name: 'app'
    http_client_config:
      tls_config:
        insecure_skip_verify: true  # For testing only
      follow_redirects: true
      proxy_url: 'http://proxy:8080'
```

Check target connectivity:

```bash
curl -v http://target-host:8080/metrics
```

## Examples

```bash
# Test HTTP connection
curl -v http://target:8080/metrics

# Check with proxy
curl -x http://proxy:8080 http://target:8080/metrics

# View client errors
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_target_sync_length'
```
"""
    ),
    (
        "prometheus-http-server-error",
        "Prometheus HTTP Server Error",
        "How to fix Prometheus HTTP server errors when exposing metrics and API",
        """## Common Causes

- Port already in use
- Insufficient permissions to bind port
- Too many concurrent connections
- Request handler panic

## How to Fix

Check if port is available:

```bash
ss -tlnp | grep 9090
lsof -i :9090
```

Start with custom listen address:

```bash
prometheus --web.listen-address=0.0.0.0:9090
```

Check Prometheus process status:

```bash
curl http://localhost:9090/-/healthy
```

## Examples

```bash
# Check Prometheus health
curl http://localhost:9090/-/healthy

# Monitor HTTP requests
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_http_requests_total'

# Check for errors
journalctl -u prometheus | grep -i "error"
```
"""
    ),
    (
        "prometheus-tls-server-cert",
        "Prometheus TLS Server Certificate Error",
        "How to fix Prometheus TLS server certificate errors for web UI and API",
        """## Common Causes

- TLS certificate expired
- Certificate does not match the server hostname
- Missing private key file
- Certificate chain incomplete

## How to Fix

Configure TLS for Prometheus web:

```bash
prometheus \
  --web.config.file=web-config.yml
```

Create web-config.yml:

```yaml
tls_server_config:
  cert_file: /etc/prometheus/server.crt
  key_file: /etc/prometheus/server.key
  client_auth_type: RequireAndVerifyClientCert
  client_ca_file: /etc/prometheus/ca.crt
```

## Examples

```bash
# Check certificate expiry
openssl x509 -in /etc/prometheus/server.crt -noout -dates

# Test HTTPS endpoint
curl -k https://localhost:9090/-/healthy

# Verify certificate chain
openssl s_client -connect localhost:9090 -CAfile /etc/prometheus/ca.crt
```
"""
    ),
    (
        "prometheus-cors-error",
        "Prometheus CORS Error",
        "How to fix Prometheus Cross-Origin Resource Sharing errors",
        """## Common Causes

- Browser blocking cross-origin requests to Prometheus API
- Missing CORS headers in Prometheus response
- Grafana or other tool accessing Prometheus from different origin
- Web configuration missing CORS settings

## How to Fix

Configure CORS in web-config.yml:

```yaml
tls_server_config:
  cert_file: /etc/prometheus/server.crt
  key_file: /etc/prometheus/server.key
```

Use Grafana proxy instead of direct access:

```ini
# grafana.ini
[auth.proxy]
enabled = true
```

## Examples

```bash
# Test CORS headers
curl -I -X OPTIONS -H "Origin: http://grafana:3000" http://localhost:9090/api/v1/query

# Check web configuration
curl -s http://localhost:9090/api/v1/status/config | grep -i cors
```
"""
    ),
    (
        "prometheus-query-timeout",
        "Prometheus Query Timeout Error",
        "How to fix Prometheus query timeout errors during PromQL execution",
        """## Common Causes

- Query too complex or scanning too much data
- Query time range too large
- `query.timeout` set too low
- Server under heavy query load

## How to Fix

Increase query timeout:

```yaml
global:
  query_timeout: 2m
```

Optimize queries:

```promql
# Wrong: scanning 30 days
rate(http_requests_total[30d])

# Better: use recording rules
# Pre-compute in recording rule
```

Check query performance:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.queryTimeout'
```

## Examples

```bash
# Test query timeout
curl -s --max-time 30 'http://localhost:9090/api/v1/query?query=rate(http_requests_total[1h])'

# Check query stats
curl -s http://localhost:9090/api/v1/status/stats | jq '.data.query'

# View slow queries
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_query_duration_seconds'
```
"""
    ),
    (
        "prometheus-query-too-expensive",
        "Prometheus Query Too Expensive Error",
        "How to fix Prometheus query too many samples or resources consumed",
        """## Common Causes

- Query scanning too many time series
- High cardinality metrics being queried
- `max_samples` limit exceeded
- Query touching too many blocks

## How to Fix

Increase max samples limit:

```yaml
global:
  query_max_samples: 500000
```

Optimize queries to reduce data scanned:

```promql
# Wrong: no label filter
rate(http_requests_total[5m])

# Better: filter to specific jobs
rate(http_requests_total{job="my-app"}[5m])

# Even better: use recording rules
job:http_requests:rate5m
```

## Examples

```bash
# Check sample count
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_query_samples_total'

# Find high-cardinality metrics
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data.seriesCountByMetricName[:10]'

# Test query cost
curl -s -w '\n%{time_total}' 'http://localhost:9090/api/v1/query?query=http_requests_total'
```
"""
    ),
    (
        "prometheus-query-tail-error",
        "Prometheus Query Tail Error",
        "How to fix Prometheus query tail (last values) errors",
        """## Common Causes

- Query returning no data for requested time range
- Step too large for data resolution
- Metric does not exist at query time
- Stale data markers causing gaps

## How to Fix

Adjust query step size:

```promql
# Better resolution with smaller step
http_requests_total[5m] offset 5m

# Check current step
curl -s 'http://localhost:9090/api/v1/query?query=http_requests_total&time=now'
```

Use `last_over_time` for current values:

```promql
last_over_time(http_requests_total[1h])
```

## Examples

```bash
# Get latest value
curl -s 'http://localhost:9090/api/v1/query?query=last_over_time(http_requests_total[5m])'

# Check data availability
curl -s 'http://localhost:9090/api/v1/query_range?query=http_requests_total&start=1h ago&end=now&step=60s' | jq '.data.result | length'
```
"""
    ),
    (
        "prometheus-max-concurrency",
        "Prometheus Max Concurrency Exceeded Error",
        "How to fix Prometheus maximum concurrent query limit exceeded",
        """## Common Causes

- Too many concurrent queries running
- `query.max-concurrency` too low
- Dashboard queries all executing simultaneously
- Heavy recording rules running in parallel

## How to Fix

Increase max concurrency:

```yaml
global:
  query_max_concurrency: 20
```

Monitor concurrent queries:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_queries_concurrent'
```

Check current limit:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.queryConcurrency'
```

## Examples

```bash
# Check concurrent queries
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_queries_concurrent'

# View query stats
curl -s http://localhost:9090/api/v1/status/stats | jq '.data.query'
```
"""
    ),
    (
        "prometheus-max-samples-error",
        "Prometheus Max Samples Limit Error",
        "How to fix Prometheus maximum samples exceeded during query",
        """## Common Causes

- Query result contains more than `max_samples` data points
- High cardinality metrics returning many series
- Large time range queried with small step
- Recording rules generating excessive samples

## How to Fix

Increase sample limit:

```yaml
global:
  query_max_samples: 1000000
```

Optimize query to reduce samples:

```promql
# Wrong: high cardinality
sum(rate(http_requests_total[5m]))

# Better: aggregate with labels
sum(rate(http_requests_total{job="app"}[5m])) by (status)
```

## Examples

```bash
# Check sample limit
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.queryMaxSamples'

# Count series
curl -s 'http://localhost:9090/api/v1/query?query=count({__name__!=""})'
```
"""
    ),
    (
        "prometheus-query-engine-error",
        "Prometheus Query Engine Error",
        "How to fix Prometheus query engine internal errors",
        """## Common Causes

- Bug in query engine version
- Unsupported PromQL feature used
- Internal state corruption
- Memory allocation failure during query

## How to Fix

Check Prometheus version:

```bash
prometheus --version
```

Upgrade to latest stable version:

```bash
# Download latest release
wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-*.linux-amd64.tar.gz
tar xzf prometheus-*.linux-amd64.tar.gz
```

Validate query syntax:

```bash
promtool query instant http://localhost:9090 'your_query_here'
```

## Examples

```bash
# Check engine errors
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_engine_query_duration_seconds'

# Validate query
promtool query instant http://localhost:9090 'rate(http_requests_total[5m])'

# Check Prometheus status
curl http://localhost:9090/api/v1/status/buildinfo | jq '.data.version'
```
"""
    ),
    (
        "prometheus-staleness-delta",
        "Prometheus Staleness Delta Error",
        "How to fix Prometheus staleness delta configuration issues",
        """## Common Causes

- Staleness delta too short causing false staleness markers
- Staleness delta too long delaying stale series cleanup
- Targets disappearing and reappearing within delta window
- Clock skew affecting staleness detection

## How to Fix

Configure staleness delta:

```yaml
storage:
  tsdb:
    staleness_delta: 5m
```

Default is 5 minutes. Increase for unreliable networks:

```yaml
storage:
  tsdb:
    staleness_delta: 10m
```

Check current staleness settings:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data'
```

## Examples

```bash
# Check for stale markers
curl -s 'http://localhost:9090/api/v1/query?query=stale_nan' | jq '.data.result | length'

# Monitor target uptime
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {instance: .labels.instance, lastScrape: .lastScrape}'
```
"""
    ),
    (
        "prometheus-lookback-delta",
        "Prometheus Lookback Delta Error",
        "How to fix Prometheus lookback delta configuration issues",
        """## Common Causes

- Lookback delta too short causing missing data points
- Lookback delta too long causing stale data inclusion
- Query returning unexpected results due to lookback window
- Metric with long gaps between samples

## How to Fix

Configure lookback delta:

```bash
prometheus --query.lookback-delta=5m
```

Check current setting:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.lookbackDelta'
```

Adjust based on scrape interval:

```bash
# Lookback should be at least 4x scrape interval
# For 15s scrape interval: 5m lookback (default)
# For 60s scrape interval: 5m lookback (still fine)
```

## Examples

```bash
# Check lookback delta
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.lookbackDelta'

# Test query with different lookback
curl -s 'http://localhost:9090/api/v1/query?query=up&time=now'
```
"""
    ),
    (
        "prometheus-recording-conflict",
        "Prometheus Recording Rule Conflict Error",
        "How to fix conflicts between recording rules in Prometheus",
        """## Common Causes

- Two recording rules writing to same metric name
- Recording rule output collides with scraped metric
- Circular dependency between recording rules
- Rule group order causing evaluation issues

## How to Fix

Use unique recording rule names:

```yaml
groups:
  - name: app_rules
    rules:
      - record: app:http_requests:rate5m
        expr: sum(rate(http_requests_total[5m])) by (job)
  - name: node_rules
    rules:
      - record: node:cpu:utilization
        expr: 1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))
```

Avoid recording rule names matching scraped metrics:

```bash
# Check if name conflicts with existing metric
curl -s 'http://localhost:9090/api/v1/label/__name__/values' | jq '.data[]' | grep "your_record_name"
```

## Examples

```bash
# List all recording rules
curl -s http://localhost:9090/api/v1/rules | jq '.data.groups[].rules[] | select(.type == "recording") | .name'

# Check for name conflicts
curl -s 'http://localhost:9090/api/v1/query?query=app:http_requests:rate5m'
```
"""
    ),
    (
        "prometheus-federation-error",
        "Prometheus Federation Error",
        "How to fix Prometheus federation endpoint errors",
        """## Common Causes

- Federation endpoint misconfigured
- Upstream Prometheus unreachable
- Too many metrics being federated
- Federation query timeout

## How to Fix

Configure federation:

```yaml
scrape_configs:
  - job_name: 'federate'
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]':
        - '{job="prometheus"}'
        - 'job:http_requests:rate5m'
    static_configs:
      - targets:
          - 'upstream-prometheus:9090'
```

## Examples

```bash
# Test federation endpoint
curl 'http://upstream:9090/federate?match[]={job="prometheus"}'

# Check federation status
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_target_sync_length{job="federate"}'
```
"""
    ),
    (
        "prometheus-federation-label",
        "Prometheus Federation Label Error",
        "How to fix label handling errors in Prometheus federation",
        """## Common Causes

- Label conflicts between federated and local metrics
- `honor_labels` not set causing label overwrite
- Federated labels missing required values
- Label duplication across federation targets

## How to Fix

Use `honor_labels` for federation:

```yaml
scrape_configs:
  - job_name: 'federate'
    honor_labels: true
    metrics_path: '/federate'
    params:
      'match[]':
        - '{__name__=~".+"}'
    static_configs:
      - targets:
          - 'upstream:9090'
```

## Examples

```bash
# Check label conflicts
curl -s 'http://localhost:9090/api/v1/query?query=up' | jq '.data.result[].metric'

# Verify honor_labels setting
curl -s http://localhost:9090/api/v1/status/config | grep honor_labels
```
"""
    ),
    (
        "prometheus-sd-kubernetes-error",
        "Prometheus Kubernetes Service Discovery Error",
        "How to fix Prometheus Kubernetes service discovery errors",
        """## Common Causes

- RBAC permissions insufficient for Prometheus
- Kubernetes API server unreachable
- Service account token expired or invalid
- Wrong API server URL or CA certificate

## How to Fix

Configure Kubernetes SD:

```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
        api_server: 'https://kubernetes.default.svc'
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
```

Check RBAC:

```bash
kubectl auth can-i get pods --as=system:serviceaccount:monitoring:prometheus
```

## Examples

```bash
# Check Prometheus service account
kubectl get sa prometheus -n monitoring

# Verify RBAC
kubectl auth can-i list pods --as=system:serviceaccount:monitoring:prometheus

# View discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.labels.job == "kubernetes-pods")'
```
"""
    ),
    (
        "prometheus-sd-file-error",
        "Prometheus File Service Discovery Error",
        "How to fix Prometheus file-based service discovery errors",
        """## Common Causes

- JSON or YAML file format incorrect
- File not readable by Prometheus process
- File path misconfigured
- File not updated after target changes

## How to Fix

Create proper file SD config:

```yaml
scrape_configs:
  - job_name: 'file-sd'
    file_sd_configs:
      - files:
          - '/etc/prometheus/targets/*.json'
        refresh_interval: 5m
```

JSON format:

```json
[
  {
    "targets": ["host1:8080", "host2:8080"],
    "labels": {
      "env": "production",
      "team": "backend"
    }
  }
]
```

## Examples

```bash
# Validate JSON file
python3 -m json.tool /etc/prometheus/targets/app.json

# Check file SD targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__param_targets != null)'
```
"""
    ),
    (
        "prometheus-sd-consul-error",
        "Prometheus Consul Service Discovery Error",
        "How to fix Prometheus Consul-based service discovery errors",
        """## Common Causes

- Consul agent unreachable
- Wrong Consul datacenter specified
- ACL token insufficient permissions
- Consul services not registered properly

## How to Fix

Configure Consul SD:

```yaml
scrape_configs:
  - job_name: 'consul'
    consul_sd_configs:
      - server: 'consul.example.com:8500'
        services: []
        tags: ['prometheus']
        token: 'your-consul-acl-token'
```

## Examples

```bash
# Test Consul connectivity
curl http://consul:8500/v1/agent/self

# List registered services
curl http://consul:8500/v1/catalog/services

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_consul_service != null)'
```
"""
    ),
    (
        "prometheus-sd-dns-error",
        "Prometheus DNS Service Discovery Error",
        "How to fix Prometheus DNS-based service discovery errors",
        """## Common Causes

- DNS SRV record lookup failure
- DNS server unreachable
- Wrong DNS name specified
- TTL expired on DNS records

## How to Fix

Configure DNS SD:

```yaml
scrape_configs:
  - job_name: 'dns-sd'
    dns_sd_configs:
      - names:
          - '_prometheus._tcp.example.com'
        type: SRV
        refresh_interval: 30s
```

## Examples

```bash
# Test DNS SRV lookup
dig _prometheus._tcp.example.com SRV

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_dns_name != null)'

# Test DNS resolution
nslookup example.com
```
"""
    ),
    (
        "prometheus-sd-ec2-error",
        "Prometheus EC2 Service Discovery Error",
        "How to fix Prometheus EC2-based service discovery errors",
        """## Common Causes

- AWS credentials missing or invalid
- IAM role permissions insufficient
- Wrong AWS region specified
- EC2 instances not tagged properly

## How to Fix

Configure EC2 SD:

```yaml
scrape_configs:
  - job_name: 'ec2'
    ec2_sd_configs:
      - region: us-east-1
        access_key: YOUR_ACCESS_KEY
        secret_key: YOUR_SECRET_KEY
        filters:
          - name: tag:prometheus
            values: ['true']
        port: 9090
```

Use IAM role instead of keys:

```yaml
    ec2_sd_configs:
      - region: us-east-1
        role_arn: arn:aws:iam::ACCOUNT:role/prometheus-discovery
```

## Examples

```bash
# Test AWS credentials
aws sts get-caller-identity

# List EC2 instances
aws ec2 describe-instances --filters "Name=tag:prometheus,Values=true"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_ec2_tag_prometheus != null)'
```
"""
    ),
    (
        "prometheus-sd-gce-error",
        "Prometheus GCE Service Discovery Error",
        "How to fix Prometheus GCE-based service discovery errors",
        """## Common Causes

- GCP credentials not configured
- Wrong GCP project ID
- Firewall rules blocking scrape port
- Instances not properly labeled

## How to Fix

Configure GCE SD:

```yaml
scrape_configs:
  - job_name: 'gce'
    gce_sd_configs:
      - project: my-gcp-project
        zone: us-central1-a
        filter: 'labels.prometheus=true'
```

## Examples

```bash
# Test GCP credentials
gcloud auth application-default print-access-token

# List GCE instances
gcloud compute instances list --filter="labels.prometheus=true"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_gce_label_prometheus != null)'
```
"""
    ),
    (
        "prometheus-sd-azure-error",
        "Prometheus Azure Service Discovery Error",
        "How to fix Prometheus Azure-based service discovery errors",
        """## Common Causes

- Azure credentials misconfigured
- Wrong subscription or resource group
- VM not properly tagged
- Network security group blocking port

## How to Fix

Configure Azure SD:

```yaml
scrape_configs:
  - job_name: 'azure'
    azure_sd_configs:
      - subscription_id: your-subscription-id
        resource_group: your-resource-group
        port: 80
```

## Examples

```bash
# Test Azure credentials
az login
az account show

# List VMs
az vm list --resource-group your-rg --output table

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_azure_vm != null)'
```
"""
    ),
    (
        "prometheus-sd-openstack-error",
        "Prometheus OpenStack Service Discovery Error",
        "How to fix Prometheus OpenStack-based service discovery errors",
        """## Common Causes

- OpenStack credentials invalid
- Wrong project/domain ID
- Nova API unreachable
- Security groups blocking scrape port

## How to Fix

Configure OpenStack SD:

```yaml
scrape_configs:
  - job_name: 'openstack'
    openstack_sd_configs:
      - role: instance
        identity_endpoint: https://identity.example.com/v3
        username: prometheus
        password: secret
        project_name: monitoring
        domain_name: Default
```

## Examples

```bash
# Test OpenStack credentials
openstack token issue

# List instances
openstack server list

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_openstack != null)'
```
"""
    ),
    (
        "prometheus-sd-digitalocean-error",
        "Prometheus DigitalOcean Service Discovery Error",
        "How to fix Prometheus DigitalOcean-based service discovery errors",
        """## Common Causes

- Invalid API token
- Rate limiting from DigitalOcean API
- Droplet not tagged properly
- Network blocking scrape port

## How to Fix

Configure DigitalOcean SD:

```yaml
scrape_configs:
  - job_name: 'digitalocean'
    digitalocean_sd_configs:
      - access_token: your-api-token
        port: 9100
```

## Examples

```bash
# Test API token
curl -X GET -H "Authorization: Bearer YOUR_TOKEN" "https://api.digitalocean.com/v2/account"

# List droplets
curl -X GET -H "Authorization: Bearer YOUR_TOKEN" "https://api.digitalocean.com/v2/droplets"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_digitalocean != null)'
```
"""
    ),
    (
        "prometheus-sd-docker-error",
        "Prometheus Docker Service Discovery Error",
        "How to fix Prometheus Docker-based service discovery errors",
        """## Common Causes

- Docker daemon unreachable
- Wrong Docker socket path
- Container not exposing metrics port
- Network mode preventing connection

## How to Fix

Configure Docker SD:

```yaml
scrape_configs:
  - job_name: 'docker'
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        filters:
          - name: label
            values: ['prometheus=true']
```

Add labels to containers:

```bash
docker run -l prometheus=true -l prometheus.port=8080 my-app
```

## Examples

```bash
# Test Docker socket
curl --unix-socket /var/run/docker.sock http://localhost/containers/json

# List containers with labels
docker ps --filter "label=prometheus=true"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_docker_container_label_prometheus != null)'
```
"""
    ),
    (
        "prometheus-sd-marathon-error",
        "Prometheus Marathon Service Discovery Error",
        "How to fix Prometheus Marathon-based service discovery errors",
        """## Common Causes

- Marathon API unreachable
- Wrong Marathon endpoint URL
- Application not exposing metrics port
- Health check failing for Marathon apps

## How to Fix

Configure Marathon SD:

```yaml
scrape_configs:
  - job_name: 'marathon'
    marathon_sd_configs:
      - servers:
          - 'http://marathon.example.com:8080'
        groups:
          - 'production'
```

## Examples

```bash
# Test Marathon API
curl http://marathon.example.com:8080/v2/info

# List applications
curl http://marathon.example.com:8080/v2/apps

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_marathon_app != null)'
```
"""
    ),
    (
        "prometheus-sd-eureka-error",
        "Prometheus Eureka Service Discovery Error",
        "How to fix Prometheus Eureka-based service discovery errors",
        """## Common Causes

- Eureka server unreachable
- Application not registered in Eureka
- Wrong metadata keys for Prometheus
- Eureka REST API version mismatch

## How to Fix

Configure Eureka SD:

```yaml
scrape_configs:
  - job_name: 'eureka'
    eureka_sd_configs:
      - servers:
          - 'http://eureka.example.com:8761'
        refresh_interval: 30s
```

## Examples

```bash
# Test Eureka API
curl http://eureka:8761/eureka/apps

# Check registered apps
curl http://eureka:8761/eureka/apps -H "Accept: application/json"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_eureka_app_name != null)'
```
"""
    ),
    (
        "prometheus-sd-http-sd-error",
        "Prometheus HTTP Service Discovery Error",
        "How to fix Prometheus HTTP-based service discovery errors",
        """## Common Causes

- HTTP endpoint unreachable
- Invalid JSON response format
- Authentication required but not provided
- Response too large causing timeout

## How to Fix

Configure HTTP SD:

```yaml
scrape_configs:
  - job_name: 'http-sd'
    http_sd_configs:
      - url: 'http://discovery-service:8080/targets'
        refresh_interval: 5m
```

Expected JSON format:

```json
[
  {
    "targets": ["host1:8080"],
    "labels": {
      "__meta_custom_label": "value"
    }
  }
]
```

## Examples

```bash
# Test HTTP SD endpoint
curl http://discovery-service:8080/targets | python3 -m json.tool

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_custom_label != null)'
```
"""
    ),
    (
        "prometheus-sd-linode-error",
        "Prometheus Linode Service Discovery Error",
        "How to fix Prometheus Linode-based service discovery errors",
        """## Common Causes

- Invalid Linode API token
- Linode API rate limiting
- Linode not tagged properly
- Network configuration blocking ports

## How to Fix

Configure Linode SD:

```yaml
scrape_configs:
  - job_name: 'linode'
    linode_sd_configs:
      - access_token: your-linode-api-token
        port: 9100
```

## Examples

```bash
# Test Linode API token
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.linode.com/v4/linode/instances

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_linode != null)'
```
"""
    ),
    (
        "prometheus-sd-hetzner-error",
        "Prometheus Hetzner Service Discovery Error",
        "How to fix Prometheus Hetzner-based service discovery errors",
        """## Common Causes

- Invalid Hetzner Cloud API token
- Server not accessible from Prometheus
- Wrong API endpoint
- Firewall blocking scrape port

## How to Fix

Configure Hetzner SD:

```yaml
scrape_configs:
  - job_name: 'hetzner'
    hetzner_sd_configs:
      - role: robot
        port: 9100
```

## Examples

```bash
# Test Hetzner API
curl -H "Authorization: Bearer YOUR_TOKEN" https://api.hetzner.cloud/v1/servers

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_hetzner != null)'
```
"""
    ),
    (
        "prometheus-sd-puppetdb-error",
        "Prometheus PuppetDB Service Discovery Error",
        "How to fix Prometheus PuppetDB-based service discovery errors",
        """## Common Causes

- PuppetDB API unreachable
- Wrong query language (PQL vs AST)
- SSL certificate not configured
- PuppetDB returned empty results

## How to Fix

Configure PuppetDB SD:

```yaml
scrape_configs:
  - job_name: 'puppetdb'
    puppetdb_sd_configs:
      - url: 'https://puppetdb.example.com:8081/pdb/query'
        query: 'inventory { facts.networking.ip != "0.0.0.0"}'
        port: 9100
```

## Examples

```bash
# Test PuppetDB API
curl -k https://puppetdb:8081/pdb/query/v4/status

# Query nodes
curl -k -X POST https://puppetdb:8081/pdb/query/v4/nodes -d '{"query":"nodes {}"}'

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_puppetdb != null)'
```
"""
    ),
    (
        "prometheus-sd-nomad-error",
        "Prometheus Nomad Service Discovery Error",
        "How to fix Prometheus Nomad-based service discovery errors",
        """## Common Causes

- Nomad API unreachable
- ACL token insufficient permissions
- Job not exposing metrics port
- Namespace filtering misconfigured

## How to Fix

Configure Nomad SD:

```yaml
scrape_configs:
  - job_name: 'nomad'
    nomad_sd_configs:
      - server: 'http://nomad.example.com:4646'
        token: 'your-nomad-acl-token'
        namespaces: ['production']
```

## Examples

```bash
# Test Nomad API
curl http://nomad:4646/v1/status/leader

# List jobs
curl -H "X-Nomad-Token: YOUR_TOKEN" http://nomad:4646/v1/jobs

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_nomad != null)'
```
"""
    ),
    (
        "prometheus-sd-triton-error",
        "Prometheus Triton Service Discovery Error",
        "How to fix Prometheus Triton-based service discovery errors",
        """## Common Causes

- Triton API unreachable
- Wrong datacenter specified
- Machine not provisioned with metrics port
- CloudAPI authentication failure

## How to Fix

Configure Triton SD:

```yaml
scrape_configs:
  - job_name: 'triton'
    triton_sd_configs:
      - endpoint: 'triton.example.com'
        account: 'your-account'
        dc: 'us-east-1'
        basic_auth:
          username: admin
          password: secret
```

## Examples

```bash
# Test Triton API
curl -k https://triton:8080/--cloudapi-/ping

# List instances
curl -k -u admin:secret https://triton:8080/--cloudapi-/machines

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_triton != null)'
```
"""
    ),
]

count = 0
for slug, title, desc, body in PAGES:
    if slug in EXISTING:
        print(f"SKIP (exists): {slug}")
        continue
    filepath = os.path.join(BASE, f'{slug}.md')
    with open(filepath, 'w') as f:
        f.write(make_page(title, desc, body))
    count += 1
    print(f"Created: {slug}")

print(f"\nTotal new pages: {count}")
print(f"Total files now: {len(os.listdir(BASE))}")
