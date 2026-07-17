---
title: "[Solution] Apollo Client: Network Error Fix"
description: "Fix Apollo Client network errors, connection failures, and cache inconsistencies. Handle offline scenarios and GraphQL request failures."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Apollo Client: Network Error

This error occurs when Apollo Client cannot complete a GraphQL request due to network issues, server unavailability, or misconfiguration. It differs from GraphQL errors (which come from the server) — network errors prevent any response from being received.

## What This Error Means

Common error messages:

- `Network error: Failed to fetch`
- `Network error: Load failed`
- `Network error: Request timeout`
- `ApolloError: Network error`
- `Error: Unexpected end of JSON input`

Apollo Client distinguishes between `graphQLErrors` (returned by server) and `networkError` (request/response failure). Network errors often mean the server was unreachable or returned an invalid response.

## Common Causes

```javascript
// Cause 1: Server unreachable
const client = new ApolloClient({
  uri: 'https://api.example.com/graphql', // server is down
});

// Cause 2: CORS error (browser blocks request)
// Client: http://localhost:5173 → Server: https://api.example.com

// Cause 3: Auth token expired mid-session
const client = new ApolloClient({
  uri: '/graphql',
  link: authLink.concat(httpLink), // token expired, 401 returned
});

// Cause 4: Large payload causes timeout
const query = gql`
  query {
    allUsers {
      posts { comments { author { posts { comments { ... } } } } }
    }
  }
`;

// Cause 5: Service worker intercepting the request
```

## How to Fix

### Fix 1: Add error link for retry and error handling

```javascript
import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client';
import { onError } from '@apollo/client/link/error';
import { setContext } from '@apollo/client/link/context';

const errorLink = onError(({ graphQLErrors, networkError, operation, forward }) => {
  if (graphQLErrors) {
    graphQLErrors.forEach(({ message, extensions }) => {
      console.error(`GraphQL Error: ${message}`);
      if (extensions?.code === 'UNAUTHENTICATED') {
        // Redirect to login
        window.location.href = '/login';
      }
    });
  }

  if (networkError) {
    console.error(`Network Error: ${networkError.message}`);
    if (networkError.statusCode === 429) {
      // Retry after delay
      return forward(operation);
    }
  }
});
```

### Fix 2: Add auth token refresh

```javascript
const authLink = setContext(async (_, { headers }) => {
  let token = localStorage.getItem('token');

  if (isTokenExpired(token)) {
    token = await refreshToken();
    localStorage.setItem('token', token);
  }

  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : '',
    },
  };
});
```

### Fix 3: Configure request timeout

```javascript
import { createHttpLink } from '@apollo/client';

const httpLink = createHttpLink({
  uri: '/graphql',
  fetch: (uri, options) => {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 15000);

    return fetch(uri, {
      ...options,
      signal: controller.signal,
    }).finally(() => clearTimeout(timeoutId));
  },
});
```

### Fix 4: Use retry link

```javascript
import { RetryLink } from '@apollo/client/link/retry';
import { split } from '@apollo/client';

const retryLink = new RetryLink({
  delay: { initial: 300, max: 5000, jitter: true },
  attempts: { max: 3, retryIf: (error) => !!error },
});

const client = new ApolloClient({
  link: from([errorLink, retryLink, authLink, httpLink]),
  cache: new InMemoryCache(),
});
```

## Examples

```
ApolloError: Network error: Failed to fetch
    at new ApolloError (ApolloError.js:52:28)
    at ObservableQuery.js:345:39
```

```javascript
// Fix: check network status before querying
import { useQuery } from '@apollo/client';
import { useState, useEffect } from 'react';

function UserList() {
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  useEffect(() => {
    const onOnline = () => setIsOnline(true);
    const onOffline = () => setIsOnline(false);
    window.addEventListener('online', onOnline);
    window.addEventListener('offline', onOffline);
    return () => {
      window.removeEventListener('online', onOnline);
      window.removeEventListener('offline', onOffline);
    };
  }, []);

  const { data, error, loading } = useQuery(GET_USERS, {
    skip: !isOnline,
  });

  if (!isOnline) return <div>You are offline</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>{/* render users */}</div>;
}
```

## Related Errors

- [Apollo Error]({{< relref "/languages/javascript/apollo-error" >}}) — basic Apollo error
- [GraphQL Error V2]({{< relref "/languages/javascript/graphql-error-v2" >}}) — GraphQL server errors
- [Fetch Network Error]({{< relref "/languages/javascript/fetch-network-error" >}}) — fetch failed
