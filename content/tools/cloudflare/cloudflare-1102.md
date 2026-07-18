---
title: "[Solution] Cloudflare 1102 Error — Worker Must Have a Script"
description: "Fix Cloudflare Error 1102 when a Worker route exists but no script is deployed. Upload or link a Worker script to the route to resolve the error."
tools: ["cloudflare"]
error-types: ["worker-error"]
severities: ["error"]
weight: 5
---

Cloudflare Error 1102 occurs when a route is configured to use a Cloudflare Worker but no script is deployed or assigned to that route.

## What This Error Means

A route in the Cloudflare dashboard (e.g., `subdomain.example.com/*`) is set to run a Worker, but the Worker does not exist or has not been deployed.

## Why It Happens

- The Worker was deployed but later deleted from the dashboard
- A route was created manually for a Worker that was never uploaded
- CI/CD pipeline deployed routes but failed to deploy the Worker script
- The Worker name in the route does not match any deployed Worker
- The Worker was deployed to a different environment (staging vs production)
- The Worker account was changed or transferred without migrating routes

## How to Fix It

### Check Deployed Workers

```bash
wrangler list
```

### Deploy a Worker to the Route

```bash
wrangler deploy
```

Or create a minimal script:

```javascript
export default {
  async fetch(request) {
    return new Response('Hello from Cloudflare Worker', {
      headers: { 'content-type': 'text/plain' },
    });
  },
};
```

### Check Route Configuration

```bash
curl -X GET "https://api.cloudflare.com/client/v4/zones/<zone-id>/workers/routes" \
  -H "Authorization: Bearer <api-token>"
```

### Remove Orphaned Routes

```bash
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/<zone-id>/workers/routes/<route-id>" \
  -H "Authorization: Bearer <api-token>"
```

### Verify Worker Name Matches Route

In the Cloudflare dashboard, ensure the route's Worker name exactly matches the deployed Worker name.

### Use a Staging Worker

Deploy a placeholder Worker to validate routes:

```bash
wrangler deploy --name health-check --script "export default { async fetch(request) { return new Response('OK'); } }"
```

## Common Mistakes

- Creating routes in the Cloudflare dashboard before deploying the Worker
- Deleting Workers without cleaning up associated routes
- Typographical mismatches between route Worker names and actual Worker names
- Forgetting to deploy Workers after CI/CD pipeline configuration changes

## Related Pages

- [Cloudflare 1101 Error]({{< relref "/tools/cloudflare/cloudflare-1101" >}}) -- Worker exception
- [Cloudflare 1019 Error]({{< relref "/tools/cloudflare/cloudflare-1019" >}}) -- Memory limit exceeded
- [Cloudflare 1020 Error]({{< relref "/tools/cloudflare/cloudflare-1020" >}}) -- Access denied
