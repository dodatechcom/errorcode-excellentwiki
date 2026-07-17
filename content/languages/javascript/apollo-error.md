---
title: "[Solution] Apollo Client Network Error Fix"
description: "Fix Apollo Client network errors, GraphQL query failures, and cache issues. Handle authentication, error policies, and retry logic."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Apollo Client — Network error

This error occurs when Apollo Client cannot complete a GraphQL operation due to network issues, server errors, or misconfiguration.

## What This Error Means

Common error messages:

- `ApolloError: Network error: Failed to fetch`
- `ApolloError: Network error: Request failed with status code 401`
- `ApolloError: Response not successful: Received status code 403`

Apollo Client wraps network, GraphQL, and Apollo-specific errors under `ApolloError`.

## Common Causes

```javascript
// Cause 1: GraphQL endpoint not reachable
const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
});

// Cause 2: Authentication token expired
const client = new ApolloClient({
  uri: 'http://localhost:4000/graphql',
  headers: { authorization: 'Bearer expired-token' },
});

// Cause 3: CORS blocking requests
// Server doesn't allow requests from client origin

// Cause 4: Query errors
const { data, error } = useQuery gql`
  query GetUser($id: ID!) {
    user(id: $id) { email }
  }
`, { variables: { id: null } }); // null ID
```

## How to Fix

### Fix 1: Add error handling link

```javascript
import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client';
import { onError } from '@apollo/client/link/error';
import { setContext } from '@apollo/client/link/context';

const errorLink = onError(({ graphQLErrors, networkError }) => {
  if (graphQLErrors) {
    graphQLErrors.forEach(({ message, locations, path }) => {
      console.error(`GraphQL error: ${message}`);
    });
  }
  if (networkError) {
    console.error(`Network error: ${networkError}`);
  }
});
```

### Fix 2: Handle authentication

```javascript
const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem('token');
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : '',
    },
  };
});

const client = new ApolloClient({
  link: authLink.concat(errorLink).concat(httpLink),
  cache: new InMemoryCache(),
});
```

### Fix 3: Handle errors in components

```javascript
function UserProfile({ userId }) {
  const { loading, error, data } = useQuery(GET_USER, {
    variables: { id: userId },
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>{data.user.email}</div>;
}
```

### Fix 4: Configure error policy

```javascript
const { data, error } = useQuery(GET_USER, {
  errorPolicy: 'all', // include partial data with errors
  variables: { id: userId },
});
```

## Examples

```javascript
// This triggers Apollo error
const client = new ApolloClient({
  uri: 'http://nonexistent:4000/graphql',
  cache: new InMemoryCache(),
});

client.query({
  query: gql`{ users { id name } }`,
}).catch(err => {
  console.error(err.networkError.message);
  // "Network error: Failed to fetch"
});
```

## Related Errors

- [Axios Error]({{< relref "/languages/javascript/axios-error" >}}) — HTTP request failed
- [GraphQL Error]({{< relref "/languages/javascript/graphql-error" >}}) — null field
- [ECONNREFUSED]({{< relref "/languages/javascript/econnrefused-node" >}}) — connection refused
