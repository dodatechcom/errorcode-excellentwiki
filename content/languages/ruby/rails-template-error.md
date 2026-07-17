---
title: "[Solution] Rails ActionView::MissingTemplate Fix"
description: "Fix Rails template errors when a view template file is missing."
languages: ["ruby"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ActionView", "missing-template", "view", "rails", "ruby"]
weight: 5
---

# Rails ActionView::MissingTemplate Fix

A Rails template error occurs when a controller action tries to render a template that doesn't exist.

## What This Error Means

Rails looks for templates in `app/views/<controller>/<action>.html.erb` by default. If the template file is missing, Rails raises `ActionView::MissingTemplate`.

## Common Causes

- Template file not created yet
- Wrong format or variant specified
- Template name mismatch (typo)
- Missing template for a specific response format

## How to Fix

### 1. Create the missing template

```ruby
# CORRECT: Create app/views/users/show.html.erb
<h1><%= @user.name %></h1>
<p><%= @user.email %></p>
```

### 2. Specify template explicitly

```ruby
# CORRECT: Render specific template
def show
  @user = User.find(params[:id])
  render template: "users/profile"
end
```

### 3. Handle multiple formats

```ruby
# CORRECT: Templates for different formats
# app/views/users/show.html.erb
# app/views/users/show.json.jbuilder
# app/views/users/show.xml.builder

def show
  @user = User.find(params[:id])
  respond_to do |format|
    format.html
    format.json { render json: @user }
  end
end
```

### 4. Use render to avoid template lookup

```ruby
# CORRECT: Inline render without template
def create
  @user = User.create(user_params)
  if @user.persisted?
    redirect_to @user
  else
    render :new  # Renders app/views/users/new.html.erb
  end
end
```

## Related Errors

- [Rails Routing Error](rails-routing-error) — route not found
- [Rails Controller Error](rails-controller-error) — controller issues
- [Rails Mailer Error](rails-mailer-error) — mailer issues
