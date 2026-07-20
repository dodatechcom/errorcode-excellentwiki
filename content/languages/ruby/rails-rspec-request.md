---
title: "[Solution] Rails RSpec Request Specs — JSON Response, Headers, Status Code Errors"
description: "Fix Rails RSpec request spec errors. Handle JSON response parsing, header assertions, and status code issues."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, rails, rspec, request_spec, json"]
severity: "error"
---

# Rails RSpec Request Spec Errors

## Error Message

```
NoMethodError: undefined method `parsed_body' for ...
# or
RSpec::Expectations::ExpectationNotMetError: expected: 200 got: 401
# or
JSON::ParserError: unexpected token at '...'
```

## Common Causes

- Not including RSpec request helpers
- Parsing JSON response incorrectly
- Missing authentication in request specs
- Using wrong content type for JSON requests

## Solutions

### Solution 1: Set Up Request Spec Helpers

Include the necessary request spec modules.

```ruby
# spec/rails_helper.rb
RSpec.configure do |config|
  config.include Rails.application.routes.url_helpers, type: :request
  config.include FactoryBot::Syntax::Methods, type: :request
  config.include Devise::Test::IntegrationHelpers, type: :request
end
```

### Solution 2: Parse JSON Responses Correctly

Use the right methods to parse response bodies.

```ruby
# spec/requests/users_spec.rb
RSpec.describe "Users", type: :request do
  describe "GET /users" do
    it "returns JSON" do
      get users_path
      expect(response).to have_http_status(:ok)
      expect(response.content_type).to include("application/json")

      json = JSON.parse(response.body)
      expect(json).to be_an(Array)
      expect(json.first).to include("name")
    end
  end
end
```

### Solution 3: Set Headers for JSON Requests

Include proper headers for API requests.

```ruby
RSpec.describe "API", type: :request do
  before do
    headers = {
      "CONTENT_TYPE" => "application/json",
      "ACCEPT" => "application/json"
    }
  end

  it "creates a resource" do
    post "/api/users",
      params: { name: "Alice" }.to_json,
      headers: { "CONTENT_TYPE" => "application/json" }

    expect(response).to have_http_status(:created)
    json = JSON.parse(response.body)
    expect(json["name"]).to eq("Alice")
  end
end
```

### Solution 4: Handle Authentication in Request Specs

Authenticate users before making requests.

```ruby
RSpec.describe "Protected", type: :request do
  let(:user) { create(:user) }
  let(:headers) { { "Authorization" => "Bearer #{token_for(user)}" } }

  it "requires authentication" do
    get "/api/data"
    expect(response).to have_http_status(:unauthorized)
  end

  it "returns data when authenticated" do
    get "/api/data", headers: headers
    expect(response).to have_http_status(:ok)
    expect(JSON.parse(response.body)).to include("data")
  end
end
```

## Prevention Tips

- Use `type: :request` for request specs, not `type: :feature`
- Include Devise helpers for authentication in request specs
- Parse JSON with `JSON.parse(response.body)` for assertions
- Set `CONTENT_TYPE` and `ACCEPT` headers for API requests

## Related Errors

- [RSpec Expectation Error]({{< relref "/languages/ruby/rspec-expectation-error" >}})
- [ActiveRecord::RecordNotFound]({{< relref "/languages/ruby/activerecord-error" >}})
- [ActionController::InvalidAuthenticityToken]({{< relref "/languages/ruby/rails-csrf-error" >}})
