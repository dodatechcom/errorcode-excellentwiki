---
title: "[Solution] Rails Authorization Error — How to Fix"
description: "Fix Rails authorization errors. Resolve permission denied, CanCanCan errors, and role-based access issues."
frameworks: ["rails"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Rails authorization error occurs when a user is authenticated but not authorized to perform an action.

## Why It Happens

Authorization errors stem from missing ability definitions, incorrect role checks, undefined permission methods, or policy mismatches.

## Common Error Messages

```
CanCan::AccessDenied: You are not authorized to access this page.
```

```
Pundit::NotDefinedError: unable to find policy UserPolicy#destroy
```

```
ActionController::ForbiddenAttributesError
```

```
NoMethodError: undefined method `admin?' for nil:NilClass
```

## How to Fix It

### 1. Define Ability with CanCanCan

Set up comprehensive authorization rules.

```ruby
class Ability
  include CanCan::Ability

  def initialize(user)
    user ||= User.new
    if user.admin?
      can :manage, :all
    elsif user.editor?
      can [:read, :create, :update], [Article, Comment]
      can :destroy, Comment, user_id: user.id
    else
      can :read, :all
      can :create, Comment
    end
  end
end
```

### 2. Implement Pundit Policies

Use Pundit for object-level authorization.

```ruby
class UserPolicy < ApplicationPolicy
  def show?
    user.admin? || record == user
  end

  def destroy?
    user.admin?
  end

  class Scope < Scope
    def resolve
      user.admin? ? scope.all : scope.where(id: user.id)
    end
  end
end
```

### 3. Check Permissions Before Actions

Use before_action to verify authorization.

```ruby
class Admin::UsersController < ApplicationController
  before_action :require_admin

  private
  def require_admin
    unless current_user.admin?
      redirect_to root_path, alert: 'Access denied'
    end
  end
end
```

### 4. Handle Authorization Errors

Provide user-friendly error responses.

```ruby
class ApplicationController < ActionController::Base
  rescue_from CanCan::AccessDenied do |exception|
    respond_to do |format|
      format.html { redirect_to root_path, alert: exception.message }
      format.json { render json: { error: 'Forbidden' }, status: :forbidden }
    end
  end
end
```

## Common Scenarios

**Scenario 1: Admin page returns 403 for admins.**
Check that `current_user.admin?` returns true.

**Scenario 2: API returns 403 for authorized users.**
Ensure authorization method is called with correct context.

**Scenario 3: New role has wrong permissions.**
Update the ability definition.

## Prevent It

1. **Write authorization tests.**
Test access for all roles.

2. **Use authorization gems.**
Use CanCanCan or Pundit.

3. **Audit permissions regularly.**
Review ability definitions periodically.

