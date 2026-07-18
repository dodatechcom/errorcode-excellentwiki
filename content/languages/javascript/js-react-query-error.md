---
title: "Solved JavaScript react-query Error — How to Fix"
date: 2026-03-20T16:10:45+00:00
description: "Learn how to resolve JavaScript TanStack React Query data fetching and caching errors."
categories: ["javascript"]
keywords: ["react query error", "tanstack query", "query cache", "data fetching", "query invalidation"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

React Query errors occur when query keys don't match, mutations fail without error handling, or cache invalidation logic is incorrect. The library manages server state but requires proper key management.

Common causes include:
- Query keys not consistent between calls
- Missing error handling in mutations
- Incorrect cache invalidation patterns
- Using stale data after mutations
- QueryClient not provided to app

## Common Error Messages

```
Error: No QueryClient set, use QueryClientProvider to set one
```

```
Error: Maximum update depth exceeded
```

```
Warning: Query data cannot be undefined when using a query key array
```

## How to Fix It

### 1. Configure React Query

Set up QueryClient properly.

```jsx
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5 minutes
      cacheTime: 30 * 60 * 1000, // 30 minutes
      refetchOnWindowFocus: false,
      retry: 1
    },
    mutations: {
      retry: 0
    }
  }
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <YourApp />
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  );
}
```

### 2. Use Queries Properly

Fetch data with queries.

```jsx
import { useQuery } from "@tanstack/react-query";

// Fetch single item
function UserDetail({ userId }) {
  const {
    data: user,
    isLoading,
    error,
    refetch
  } = useQuery({
    queryKey: ["user", userId],
    queryFn: () => fetchUser(userId),
    enabled: !!userId
  });
  
  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
      <button onClick={refetch}>Refresh</button>
    </div>
  );
}

// Fetch list with filters
function UserList({ filters }) {
  const { data: users } = useQuery({
    queryKey: ["users", filters],
    queryFn: () => fetchUsers(filters),
    keepPreviousData: true
  });
  
  return (
    <ul>
      {users?.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}
```

### 3. Handle Mutations

Create and update data.

```jsx
import { useMutation, useQueryClient } from "@tanstack/react-query";

function CreateUserForm() {
  const queryClient = useQueryClient();
  
  const mutation = useMutation({
    mutationFn: createUser,
    onSuccess: (newUser) => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: ["users"] });
      
      // Or update cache directly
      queryClient.setQueryData(["user", newUser.id], newUser);
    },
    onError: (error) => {
      console.error("Create failed:", error);
    }
  });
  
  const handleSubmit = (data) => {
    mutation.mutate(data);
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <input name="name" />
      <input name="email" />
      <button type="submit" disabled={mutation.isLoading}>
        {mutation.isLoading ? "Creating..." : "Create User"}
      </button>
      {mutation.error && <p>Error: {mutation.error.message}</p>}
    </form>
  );
}
```

## Common Scenarios

### Scenario 1: Infinite Queries

Implement infinite scrolling:

```jsx
import { useInfiniteQuery } from "@tanstack/react-query";

function InfiniteList() {
  const {
    data,
    fetchNextPage,
    hasNextPage,
    isFetchingNextPage
  } = useInfiniteQuery({
    queryKey: ["items"],
    queryFn: ({ pageParam = 1 }) => fetchItems(pageParam),
    getNextPageParam: (lastPage) => lastPage.nextCursor
  });
  
  return (
    <div>
      {data?.pages.map((page, i) => (
        <React.Fragment key={i}>
          {page.items.map((item) => (
            <div key={item.id}>{item.name}</div>
          ))}
        </React.Fragment>
      ))}
      
      <button
        onClick={() => fetchNextPage()}
        disabled={!hasNextPage || isFetchingNextPage}
      >
        {isFetchingNextPage
          ? "Loading more..."
          : hasNextPage
          ? "Load More"
          : "No more items"}
      </button>
    </div>
  );
}
```

### Scenario 2: Optimistic Updates

Update UI immediately:

```jsx
function TodoList() {
  const queryClient = useQueryClient();
  
  const mutation = useMutation({
    mutationFn: toggleTodo,
    onMutate: async (newTodo) => {
      await queryClient.cancelQueries({ queryKey: ["todos"] });
      
      const previousTodos = queryClient.getQueryData(["todos"]);
      
      queryClient.setQueryData(["todos"], (old) =>
        old.map((todo) =>
          todo.id === newTodo.id ? { ...todo, done: !todo.done } : todo
        )
      );
      
      return { previousTodos };
    },
    onError: (err, newTodo, context) => {
      queryClient.setQueryData(["todos"], context.previousTodos);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] });
    }
  });
  
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.id} onClick={() => mutation.mutate(todo)}>
          {todo.text}
        </li>
      ))}
    </ul>
  );
}
```

## Prevent It

- Keep query keys consistent and descriptive
- Always wrap app in `<QueryClientProvider>`
- Use `invalidateQueries` after mutations
- Implement proper error boundaries
- Use `keepPreviousData` for filter/sort transitions