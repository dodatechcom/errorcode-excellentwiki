---
title: "[Solution] Ruby CanCan::AccessDenied Fix"
description: "Fix CanCan::AccessDenied in Rails. Learn why CanCanCan authorization fails and how to define and check abilities."
languages: ["ruby"]
severities: ["error"]
error-types: ["authorization-error"]
tags: ["cancancan", "authorization", "access-denied", "rails", "ruby"]
weight: 5
---

## What This Error Means

A `CanCan::AccessDenied` is raised when a user tries to perform an action they're not authorized to perform according to your CanCanCan ability definitions. This is an authorization failure, not an authentication failure.

## Common Causes

- Ability not defined for the action
- User doesn't have required role
- Wrong ability class
- Missing `load_and_authorize_resource`

## How to Fix

```ruby
# WRONG: No ability defined
class Ability
  include CanCan::Ability
  def initialize(user)
    # No :read ability for Post defined
  end
end

# CORRECT: Define abilities
class Ability
  include CanCan::Ability
  def initialize(user)
    can :read, Post
    can :manage, Post, user_id: user.id
  end
end
```

```ruby
# WRONG: Not authorizing in controller
class PostsController < ApplicationController
  def show
    @post = Post.find(params[:id])  # No authorization check
  end
end

# CORRECT: Use load_and_authorize_resource
class PostsController < ApplicationController
  load_and_authorize_resource
  def show
    # @post is authorized automatically
  end
end
```

```ruby
# WRONG: Ability not matching user type
class Ability
  include CanCan::Ability
  def initialize(user)
    can :manage, :all if user.admin?  # Wrong: user may be nil
  end
end

# CORRECT: Check for nil user
class Ability
  include CanCan::Ability
  def initialize(user)
    user ||= User.new
    can :read, Post
    can :manage, :all if user.admin?
  end
end
```

## Examples

```ruby
# Example 1: Check ability
can?(:read, Post)  # true/false
cannot?(:delete, Post)  # true/false

# Example 2: Rescue AccessDenied
rescue_from CanCan::AccessDenied do |exception|
  redirect_to root_path, alert: exception.message
end

# Example 3: Custom ability
class Ability
  include CanCan::Ability
  def initialize(user)
    if user.admin?
      can :manage, :all
    else
      can :read, :all
    end
  end
end
```

## Related Errors

- [Pundit::NotAuthorizedError](rails-pundit-error) — Pundit authorization failed
- [Devise authentication error](rails-devise-error) — authentication failed
- [ActionController::InvalidAuthenticityToken](rails-controller) — CSRF token invalid
