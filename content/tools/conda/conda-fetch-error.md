---
title: "[Solution] Conda Fetch Error - Fix ConnectionError Fetching Package"
description: "Fix conda ConnectionError when fetching packages. Resolve network timeouts, proxy issues, and mirror configuration to complete downloads."
tools: ["conda"]
error-types: ["fetch-error"]
severities: ["error"]
weight: 5
---

This error means conda could not download a package from a remote channel. The network request failed due to connectivity issues, proxy misconfiguration, or server-side problems.

## What This Error Means

When conda tries to fetch a package or its metadata and the HTTP request fails, you see:

```
ConnectionError: HTTPConnectionPool(host='...')
# or
CondaHTTPError: HTTP 000 CONNECTION FAILED for url <...>
# or
SSLError: SSL certificate verification failed
```

The error interrupts package installation, environment creation, and even `conda update`. Network failures can be transient or persistent depending on the root cause.

## Why It Happens

- Your internet connection is down or unstable
- A corporate firewall or proxy blocks conda's HTTPS requests
- The conda channel server is temporarily unavailable
- DNS resolution fails for the channel hostname
- SSL certificates are expired or your system has an outdated CA bundle
- VPN or network restrictions prevent access to external repositories

## How to Fix It

### Test network connectivity

```bash
curl -I https://repo.anaconda.com/pkgs/main
ping repo.anaconda.com
```

If these fail, the issue is at the network level, not conda.

### Configure proxy settings

```bash
conda config --set proxy_servers.http http://proxy.company.com:8080
conda config --set proxy_servers.https http://proxy.company.com:8080
```

### Use a mirror or alternative channel

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
```

Many regions have faster mirrors that may be more reliable.

### Increase timeout values

```bash
conda config --set remote_connect_timeout_secs 30
conda config --set remote_read_timeout_secs 120
```

Default timeouts may be too short for slow connections.

### Fix SSL certificate issues

```bash
conda config --set ssl_verify false
```

Use this temporarily for corporate proxies with custom CA certificates. For production, install the proper CA bundle instead.

### Retry with verbose output

```bash
conda install <package> -vvv
```

Verbose mode shows exactly where the connection fails.

## Common Mistakes

- Assuming conda will auto-retry on transient network failures
- Not configuring proxy settings in corporate environments
- Using `ssl_verify false` as a permanent solution instead of fixing certificates
- Running large installs during peak network usage times
- Not checking DNS resolution before assuming a proxy issue

## Related Pages

- [Conda SSL Error]({{< relref "/tools/conda/conda-ssl-error" >}}) -- SSL certificate problems
- [Conda Channel Error]({{< relref "/tools/conda/conda-channel-error" >}}) -- channel configuration issues
- [Conda Disk Space]({{< relref "/tools/conda/conda-disk-space" >}}) -- disk space during downloads
