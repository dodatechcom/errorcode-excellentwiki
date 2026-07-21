---
title: "[Solution] Elasticsearch SAML Authentication Error"
description: "Fix Elasticsearch SAML authentication error. Resolve SSO authentication issues."
tools: ["elasticsearch"]
error-types: ["tool-error"]
severities: ["error"]
---

# Elasticsearch SAML Authentication Error

SAML authentication fails. The Identity Provider is not reachable or the SAML response is invalid.

## Common Causes

- IdP metadata URL is wrong
- SP entityId does not match
- SAML response signature verification failed

## How to Fix

### Solution 1

```bash
grep 'xpack.security.authc.realms.saml' /etc/elasticsearch/elasticsearch.yml
```

## Related Pages

- [Elasticsearch Cluster Error]({{< relref "/tools/elasticsearch/elasticsearch-cluster-error" >}})
- [Elasticsearch Index Error]({{< relref "/tools/elasticsearch/elasticsearch-index-error" >}})
- [Elasticsearch Query Error]({{< relref "/tools/elasticsearch/elasticsearch-query-error" >}})
