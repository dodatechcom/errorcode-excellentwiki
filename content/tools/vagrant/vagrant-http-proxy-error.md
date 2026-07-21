---
title: "[Solution] Vagrant HTTP Proxy Error"
description: "Fix Vagrant HTTP proxy errors when proxy configuration prevents box downloads or updates."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant HTTP Proxy Error

A Vagrant HTTP proxy error occurs when proxy settings prevent Vagrant from accessing the internet.

## Why This Happens

- Proxy environment variables not set
- Corporate proxy requires authentication
- Proxy certificate not trusted
- Incorrect proxy URL format
- No proxy bypass for local addresses

## Common Error Messages

- `vagrant_http_proxy_error`
- `vagrant_proxy_connection_refused`
- `vagrant_proxy_authentication_required`
- `vagrant_proxy_certificate_error`

## How to Fix It

### Solution 1: Set Proxy Environment Variables

```bash
export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080
export no_proxy=localhost,127.0.0.1
vagrant up
```

### Solution 2: Configure Proxy in Vagrantfile

```ruby
Vagrant.configure("2") do |config|
  config.proxy.http = "http://proxy.example.com:8080"
  config.proxy.https = "http://proxy.example.com:8080"
  config.proxy.no_proxy = "localhost,127.0.0.1"
end
```

### Solution 3: Install Proxy Plugin

```bash
vagrant plugin install vagrant-proxyconf
```

### Solution 4: Trust Proxy Certificate

```bash
# On the guest
sudo cp proxy.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

## Common Scenarios

- **Authentication required:** Configure proxy credentials
- **Certificate error:** Add proxy cert to trust store
- **Local access blocked:** Configure no_proxy correctly

## Prevent It

- Configure proxy before first vagrant up
- Use proxyconf plugin for multi-VM setups
- Document proxy requirements for team
