---
title: "[Solution] AxiosError: Request Failed with Status Code Fix"
description: "Fix Axios errors when HTTP requests fail with non-2xx status codes. Handle 4xx/5xx responses, timeouts, and network failures with interceptors."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# AxiosError: Request Failed with Status Code

This error occurs when an Axios HTTP request receives a response with a status code outside the 2xx range. By default, Axios rejects the promise for any non-success status code.

## What This Error Means

Common error messages:

- `AxiosError: Request failed with status code 404`
- `AxiosError: Request failed with status code 500`
- `AxiosError: Network Error`
- `AxiosError: timeout of 5000ms exceeded`
- `AxiosError: ERR_BAD_REQUEST`

Axios throws `AxiosError` when the response status is not in the `2xx` range (unless `validateStatus` is configured). The error object contains the response, request, config, and status code.

## Common Causes

```javascript
// Cause 1: Server returns 4xx/5xx error
const res = await axios.get('/api/users/999'); // 404 Not Found

// Cause 2: Invalid request body
await axios.post('/api/users', { name: '' }); // 400 Bad Request

// Cause 3: Missing or invalid authentication
await axios.get('/api/admin'); // 401 Unauthorized

// Cause 4: Rate limiting
await axios.post('/api/submit', data); // 429 Too Many Requests

// Cause 5: Server-side crash
await axios.get('/api/broken'); // 500 Internal Server Error
```

## How to Fix

### Fix 1: Handle specific status codes

```javascript
async function fetchData() {
  try {
    const res = await axios.get('/api/data');
    return res.data;
  } catch (err) {
    if (err.response) {
      const status = err.response.status;
      if (status === 404) {
        console.error('Resource not found');
      } else if (status === 401) {
        console.error('Authentication required');
      } else if (status === 429) {
        console.error('Rate limited, retry later');
      } else if (status >= 500) {
        console.error('Server error');
      }
    } else if (err.code === 'ECONNABORTED') {
      console.error('Request timed out');
    } else {
      console.error('Network error:', err.message);
    }
    throw err;
  }
}
```

### Fix 2: Configure default timeout and retries

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
  validateStatus: (status) => status < 500, // don't throw for 4xx
});
```

### Fix 3: Add response interceptors

```javascript
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Refresh token or redirect to login
      redirectToLogin();
    }
    if (error.response?.status === 429) {
      const retryAfter = error.response.headers['retry-after'] || 60;
      return new Promise((resolve) => {
        setTimeout(() => resolve(api(error.config)), retryAfter * 1000);
      });
    }
    return Promise.reject(error);
  }
);
```

### Fix 4: Add retry with exponential backoff

```javascript
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      return await axios.get(url);
    } catch (err) {
      if (i === retries - 1 || !err.response || err.response.status < 500) {
        throw err;
      }
      await new Promise(r => setTimeout(r, 1000 * 2 ** i));
    }
  }
}
```

## Examples

```
AxiosError: Request failed with status code 404
    at settle (axios/lib/core/settle.js:19:12)
    at IncomingMessage.handleStreamEnd (axios/lib/adapters/http.js:322:11)
```

```javascript
// Fix: use validateStatus to not throw for expected errors
const res = await axios.get('/api/users', {
  validateStatus: (status) => status < 500,
});

if (res.status === 404) {
  console.log('No users found');
} else {
  console.log(res.data);
}
```

## Related Errors

- [Axios Error]({{< relref "/languages/javascript/axios-error" >}}) — basic axios error
- [Fetch Network Error]({{< relref "/languages/javascript/fetch-network-error" >}}) — fetch failed
- [HTTP Status Code]({{< relref "/languages/javascript/err-http1-status-code" >}}) — HTTP status code error
