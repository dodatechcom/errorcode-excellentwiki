---
title: "[Solution] Ruby Pundit::NotAuthorizedError Fix"
description: "Fix Pundit::NotAuthorizedError in Rails. Learn why Pundit authorization fails and how to define and use policies."
languages: ["ruby"]
severities: ["error"]
error-types: ["authorization-error"]
weight: 5
---

## What This Error Means

A `Pundit::NotAuthorizedError` is raised when a Pundit policy method returns `false` for an authorization check. This means the current user is not authorized to perform the requested action on the given resource.

## Common Causes

- Policy method returns false
- Missing policy for the resource
- Wrong user passed to policy
- Policy method not defined

## How to Fix

```ruby
# WRONG: Policy returns false
class PostPolicy < ApplicationPolicy
  def update?
    false  # Never allows update
  end
end

# CORRECT: Define proper authorization logic
class PostPolicy < ApplicationPolicy
  def update?
    user.present? && (record.user == user || user.admin?)
  end
end
```

```ruby
# WRONG: Not using authorize in controller
class PostsController < ApplicationController
  def update
    @post = Post.find(params[:id])
    @post.update(post_params)  # No Pundit authorization
  end
end

# CORRECT: Authorize in controller
class PostsController < ApplicationController
  def update
    @post = Post.find(params[:id])
    authorize @post  # Raises NotAuthorizedError if policy returns false
    @post.update(post_params)
  end
end
```

```ruby
# WRONG: Policy method missing
class PostPolicy < ApplicationPolicy
  # delete? method not defined
end
# policy(@post).delete?  # NoMethodError

# CORRECT: Define all needed policy methods
class PostPolicy < ApplicationPolicy
  def delete?
    user.admin?
  end
end
```

## Examples

```ruby
# Example 1: Check policy
policy(@post).update?  # true/false

# Example 2: Rescue NotAuthorizedError
rescue_from Pundit::NotAuthorizedError do
  redirect_to root_path, alert: "Not authorized"
end

# Example 3: Policy with scope
class PostPolicy < ApplicationPolicy
  class Scope < Scope
    def resolve
      scope.where(user: user)
    end
  end
end
```

## Related Errors

- [CanCan::AccessDenied](rails-can-can-can) — CanCanCan authorization denied
- [Devise authentication error](rails-devise-error) — authentication failed
- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
