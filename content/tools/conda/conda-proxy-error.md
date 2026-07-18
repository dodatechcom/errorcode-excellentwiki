---
title: "[Solution] Conda Proxy Connection Refused Error — How to Fix"
description: "Fix conda proxy connection refused errors. Configure HTTP and HTTPS proxy settings for conda channels and resolve network routing issues."
tools: ["conda"]
error-types: ["proxy-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means conda cannot establish a connection to a proxy server when trying to reach package channels. The proxy either refuses the connection, is unreachable, or is misconfigured in conda's settings.

## Why It Happens

- The proxy server address or port is configured incorrectly in conda or system environment variables
- The proxy server is down or not accepting connections on the specified port
- A firewall blocks the connection between your machine and the proxy
- The proxy requires authentication but no credentials are provided
- You are behind a corporate proxy that uses a non-standard port or protocol
- `no_proxy` or `bypass_proxy` settings exclude the channel domain incorrectly

## Common Error Messages

```
ProxyError: HTTPSConnectionPool(host='repo.anaconda.com', port=443):
Max retries exceeded with url: /pkgs/main/noarch/...
Caused by ProxyError('Cannot connect to proxy'),
NewConnectionError: '[Errno 111] Connection refused'
```

```
ConnectionError: HTTPConnectionPool(host='conda.anaconda.org', port=80):
Max retries exceeded with url: /pkgs/main/...
Caused by NewConnectionError: '[Errno 111] Connection refused'
```

```
CondaError: CondaHTTPError: HTTP 000 CONNECTION FAILED for url
<https://repo.anaconda.com/pkgs/main/linux-64/repodata.json>
```

```
requests.exceptions.ConnectionError: HTTPSConnectionPool(...):
Max retries exceeded: ProxyDisposedError: Proxy connection refused
```

## How to Fix It

### 1. Configure Proxy in Conda Config

```bash
# Set HTTP proxy
conda config --set proxy_servers.http http://proxy.company.com:8080

# Set HTTPS proxy
conda config --set proxy_servers.https http://proxy.company.com:8084
```

Or edit `~/.condarc` directly:

```yaml
proxy_servers:
  http: http://proxy.company.com:8080
  https: http://proxy.company.com:8084
```

### 2. Use Environment Variables

```bash
export http_proxy=http://proxy.company.com:8080
export https_proxy=http://proxy.company.com:8084
export no_proxy=localhost,127.0.0.1,.internal.company.com

conda install numpy
```

Add these to your shell profile for persistence:

```bash
echo 'export http_proxy=http://proxy.company.com:8080' >> ~/.bashrc
echo 'export https_proxy=http://proxy.company.com:8084' >> ~/.bashrc
```

### 3. Authenticate with the Proxy

If the proxy requires a username and password:

```bash
conda config --set proxy_servers.https http://user:password@proxy.company.com:8084
```

Or use the URL-encoded format for special characters:

```bash
conda config --set proxy_servers.https http://user:%40password@proxy.company.com:8084
```

### 4. Test Proxy Connectivity

```bash
# Test if the proxy is reachable
curl -x http://proxy.company.com:8080 -I https://repo.anaconda.com

# Test direct connection (bypassing proxy)
unset http_proxy https_proxy
curl -I https://repo.anaconda.com

# Test with proxy
export http_proxy=http://proxy.company.com:8080
curl -x http://proxy.company.com:8080 -I https://repo.anaconda.com
```

### 5. Bypass Proxy for Internal Channels

If you have a local channel server that should not go through the proxy:

```bash
conda config --set proxy_servers.http ''
conda config --set proxy_servers.https ''
```

Then set `no_proxy` to exclude specific domains:

```bash
export no_proxy=repo.internal.company.com,localhost
```

### 6. Reset Proxy Settings

To remove all proxy configuration and start fresh:

```bash
conda config --remove-key proxy_servers
unset http_proxy https_proxy
```

## Common Scenarios

**Behind a corporate proxy with authentication.** Your proxy may require NTLM or Kerberos authentication. Standard HTTP proxy env vars do not support NTLM. Use `cntlm` as a local proxy that handles authentication and forwards to the corporate proxy:

```bash
# Install cntlm and configure it with your corporate proxy credentials
sudo apt install cntlm
cntlm -c /etc/cntlm.conf -I -D
```

**Docker container cannot reach external channels.** If your Docker host uses a proxy, pass it into the container:

```bash
docker run -e http_proxy=http://proxy:8080 \
           -e https_proxy=http://proxy:8080 \
           continuumio/miniconda3 conda install numpy
```

**Proxy works for curl but not for conda.** conda uses Python's `requests` library, which may not respect all proxy environment variable formats. Ensure the proxy URL includes the scheme (`http://` not just the host).

## Prevent It

1. Always test proxy settings with `curl` before configuring them in conda to confirm the proxy is reachable
2. Use `.condarc` for persistent proxy configuration instead of relying on environment variables that may not persist across sessions
3. Set up a `no_proxy` list for internal package channels to avoid routing local traffic through the proxy unnecessarily
