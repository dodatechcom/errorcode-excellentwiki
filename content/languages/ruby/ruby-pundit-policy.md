---
title: "[Solution] Ruby Pundit — Policy Scope, Authorize, Permitted Attributes Errors"
description: "Fix Ruby Pundit errors. Handle policy scope, authorize, permitted_attributes, and not_authorized errors."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, pundit, authorization, policy"]
severity: "error"
---

# Ruby Pundit Policy Errors

## Error Message

```
Pundit::NotDefinedError: unable to find policy `UserPolicy`
# or
Pundit::NotAuthorizedError: not allowed to `show?` for #<User>
# or
Pundit::PolicyNotFoundError: ...
```

## Common Causes

- Policy class not defined for the model
- Method name doesn't match the action name
- Missing `include Pundit` in ApplicationController
- Not calling `authorize` before actions

## Solutions

### Solution 1: Create Proper Policy Classes

Define policies for each model with action methods.

```ruby
# app/policies/user_policy.rb
class UserPolicy < ApplicationPolicy
  def show?
    true  # anyone can view
  end

  def update?
    user.admin? || record == user
  end

  def destroy?
    user.admin?
  end

  class Scope < Scope
    def resolve
      if user.admin?
        scope.all
      else
        scope.where(id: user.id)
      end
    end
  end
end
```

### Solution 2: Use authorize in Controllers

Call `authorize` before actions to enforce permissions.

```ruby
class UsersController < ApplicationController
  def index
    @users = policy_scope(User)
  end

  def show
    @user = User.find(params[:id])
    authorize @user
  end

  def update
    @user = User.find(params[:id])
    authorize @user

    if @user.update(user_params)
      redirect_to @user
    else
      render :edit
    end
  end

  private

  def user_params
    params.require(:user).permit(*policy(@user).permitted_attributes)
  end
end
```

### Solution 3: Handle Pundit Errors in ApplicationController

Rescue authorization failures gracefully.

```ruby
class ApplicationController < ActionController::Base
  include Pundit::Authorization

  rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized

  private

  def user_not_authorized
    flash[:alert] = "You are not authorized to perform this action."
    redirect_back(fallback_location: root_path)
  end
end
```

### Solution 4: Use Permitted Attributes Safely

Define permitted attributes in policies for strong parameters.

```ruby
class UserPolicy < ApplicationPolicy
  def permitted_attributes
    if user.admin?
      [:name, :email, :role, :active]
    else
      [:name, :email]
    end
  end
end

# In controller
def user_params
  params.require(:user).permit(*policy(@user).permitted_attributes)
end

# In form
<%= form_with model: @user do |f| %>
  <%= f.text_field :name %>
  <%= f.email_field :email %>
  <% if policy(@user).permitted_attributes.include?(:role) %>
    <%= f.select :role, ["user", "admin"] %>
  <% end %>
<% end %>
```

## Prevention Tips

- Include `Pundit::Authorization` in ApplicationController
- Call `authorize` before every action that needs authorization
- Use `policy_scope` for index actions to filter records
- Define `permitted_attributes` in policies for strong parameters

## Related Errors

- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
- [ActiveRecord::RecordNotFound]({{< relref "/languages/ruby/activerecord-error" >}})
- [ArgumentError]({{< relref "/languages/ruby/argument-error" >}})
