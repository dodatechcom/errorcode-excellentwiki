---
title: "[Solution] Elixir Ecto Changeset or Query Error — How to Fix"
description: "Fix Elixir Ecto changeset and query errors. Learn how to validate data correctly, build composable queries, and handle database constraint violations."
languages: ["elixir"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 10
comments: true
---

## Why It Happens

Ecto is the database wrapper and query language for Elixir. Changeset errors occur when data validation fails, and query errors occur when the database rejects the query structure or the data types do not match.

The most common cause is validation failures in changesets. When you cast and validate data, any failed validation adds an error to the changeset, and `Repo.insert` or `Repo.update` returns `{:error, changeset}` instead of `{:ok, record}`.

Another frequent cause is database constraint violations. Unique constraints, foreign key constraints, and check constraints enforced at the database level cause `Repo.insert` to return an error changeset when violated.

Query errors occur when the query references columns or tables that do not exist. After a migration, if the schema does not match the database, queries fail with SQL errors.

Type casting errors happen when Ecto cannot convert a value to the expected type. Passing a string where an integer is expected, or a datetime where a date is expected, causes a casting error.

Dynamic query building can produce invalid SQL if the query fragments are not constructed correctly. Using `Ecto.Query.dynamic/2` incorrectly can create queries that the database cannot execute.

Schemaless changesets for ad-hoc data validation require explicit type definitions. Without proper type specifications, the changeset cannot validate the data correctly.

## Common Error Messages

```
** (Ecto.Changeset) #Ecto.Changeset<action: :insert, errors: [name: {"can't be blank", ...}]>
```

```
** (Postgrex.Error) ERROR 23505 (unique_violation) duplicate key value violates unique constraint
```

```
** (Ecto.QueryError) field `:nonexistent` in does not exist in schema MyApp.User
```

```
** (Ecto.NoResultsError) expected at least one result but got none in query
```

## How to Fix It

### Validate data properly with changesets

```elixir
defmodule MyApp.User do
  use Ecto.Schema

  schema "users" do
    field :name, :string
    field :email, :string
    field :age, :integer
  end

  def changeset(user, attrs) do
    user
    |> Ecto.Changeset.cast(attrs, [:name, :email, :age])
    |> Ecto.Changeset.validate_required([:name, :email])
    |> Ecto.Changeset.validate_format(:email, ~r/@/)
    |> Ecto.Changeset.validate_number(:age, greater_than: 0, less_than: 150)
    |> Ecto.Changeset.unique_constraint(:email)
  end
end
```

### Handle changeset errors in controllers

```elixir
case MyApp.Repo.insert(changeset) do
  {:ok, user} ->
    {:ok, user}

  {:error, changeset} ->
    {:error, changeset}
    # In Phoenix: render(:new, changeset: changeset)
end
```

### Build composable queries safely

```elixir
import Ecto.Query

def search_users(query \\ MyApp.User, opts \\ []) do
  query
  |> maybe_filter_name(opts[:name])
  |> maybe_filter_age(opts[:min_age])
end

defp maybe_filter_name(query, nil), do: query
defp maybe_filter_name(query, name) do
  where(query, [u], ilike(u.name, ^"%#{name}%"))
end

defp maybe_filter_age(query, nil), do: query
defp maybe_filter_age(query, min_age) do
  where(query, [u], u.age >= ^min_age)
end
```

### Handle database constraint violations

```elixir
case MyApp.Repo.insert(changeset) do
  {:ok, record} ->
    {:ok, record}

  {:error, changeset} ->
    case changeset.errors do
      [email: {"has already been taken", _}] ->
        {:error, :email_taken}

      _ ->
        {:error, changeset}
    end
end
```

### Use schemaless changesets for ad-hoc data

```elixir
import Ecto.Changeset

types = %{
  name: :string,
  email: :string,
  age: :integer
}

changeset =
  {%{}, types}
  |> cast(%{name: "Alice", email: "alice@example.com", age: 30}, [:name, :email, :age])
  |> validate_required([:name, :email])
  |> validate_format(:email, ~r/@/)
```

## Common Scenarios

- Validating user registration data before inserting into the database
- Building search queries with optional filters that compose cleanly
- Handling duplicate key violations when creating unique resources

## Prevent It

- Always check the return value of `Repo.insert` and `Repo.update` for error changesets
- Use `Ecto.Changeset.unique_constraint` to map database unique violations to user-friendly errors
- Write composable query functions with pattern matching on nil for optional filters
