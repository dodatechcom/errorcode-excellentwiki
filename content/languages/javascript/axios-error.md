---
title: "[Solution] AxiosError: Request failed with status code Fix"
description: "Fix AxiosError when HTTP requests fail with error status codes. Handle 4xx/5xx responses, timeouts, and network errors with Axios."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AxiosError — Request failed with status code

This error occurs when an Axios HTTP request receives a response with a status code outside the 2xx range. By default, Axios throws for 4xx and 5xx responses.

## What This Error Means

Common error messages:

- `AxiosError: Request failed with status code 404`
- `AxiosError: Request failed with status code 500`
- `AxiosError: Network Error`

Axios rejects promises for non-2xx status codes by default. You can customize this behavior.

## Common Causes

```javascript
// Cause 1: Server returns error status
const res = await axios.get('/api/nonexistent'); // 404

// Cause 2: Validation error from server
const res = await axios.post('/api/users', { name: '' }); // 422

// Cause 3: Authentication required
const res = await axios.get('/api/admin'); // 401

// Cause 4: Network error
const res = await axios.get('http://nonexistent.com'); // ERR_NETWORK
```

## How to Fix

### Fix 1: Check status code in catch

```javascript
try {
  const res = await axios.get('/api/data');
} catch (err) {
  if (err.response) {
    // Server responded with error status
    console.error('Status:', err.response.status);
    console.error('Data:', err.response.data);
  } else if (err.request) {
    // No response received
    console.error('Network error');
  } else {
    console.error('Request setup error:', err.message);
  }
}
```

### Fix 2: Use validateStatus

```javascript
const res = await axios.get('/api/data', {
  validateStatus: (status) => status < 500, // accept 4xx
});

console.log(res.status); // 404, etc.
```

### Fix 3: Create axios instance with defaults

```javascript
const api = axios.create({
  baseURL: 'http://api.example.com',
  timeout: 10000,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // redirect to login
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);
```

### Fix 4: Add retry logic

```javascript
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await axios.get(url);
    } catch (err) {
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 1000 * (i + 1)));
    }
  }
}
```

## Examples

```javascript
// This triggers AxiosError
try {
  await axios.post('/api/users', { name: '' });
} catch (err) {
  if (err.response?.status === 422) {
    console.log('Validation error:', err.response.data.errors);
  }
}
```

## Related Errors

- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection refused
- [ETIMEDOUT]({{< relref "/languages/javascript/etimedout" >}}) — timeout
- [Socket.IO Error]({{< relref "/languages/javascript/socket-io-error" >}}) — Socket.IO error
