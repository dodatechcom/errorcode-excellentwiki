---
title: "[Solution] Rails Action Mailbox Router Error"
description: "Fix Rails Action Mailbox inbound mailbox not found or routing error. Resolve mailbox routing configuration issues."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

This error occurs when an inbound email cannot be routed to a matching mailbox in Action Mailbox.

## Common Causes

- No mailbox class matches the inbound email address
- `routes` method in the mailbox does not have a matching rule
- Mailbox class is missing the `Receive` method
- Inbound email address format does not match the route pattern
- Action Mailbox migrations have not been run

## How to Fix

1. Define routing rules in `config/routes.rb`:

```ruby
Rails.application.routes.draw do
  mount ActionMailbox::Engine => "/mailbox"
end
```

2. Create a mailbox with proper routing:

```ruby
# app/mailboxes/inbound/SupportMailbox.rb
class Inbound::SupportMailbox < ApplicationMailbox
  before_processing :ensure_sender_is_customer

  def process
    ticket = Ticket.create!(
      subject: mail.subject,
      body: mail.text_part.decoded,
      sender_email: mail.from.first
    )
    TicketMailer.confirmation(ticket).deliver_now
  end

  private

  def ensure_sender_is_customer
    unless Customer.exists?(email: mail.from.first)
      bounce_with Inbound::UnknownSenderMailbox
    end
  end
end
```

3. Run Action Mailbox migrations:

```bash
rails action_mailbox:install:migrations
rails db:migrate
```

4. Test with the fixture:

```ruby
# test/mailboxes/support_mailbox_test.rb
class SupportMailboxTest < ActionMailbox::TestCase
  test "creates a ticket from support email" do
    receive_inbound_email(
      from: "customer@example.com",
      to: "support@yourdomain.com",
      subject: "Help needed",
      body: "I have an issue"
    )
    assert_equal 1, Ticket.count
  end
end
```

## Examples

```ruby
# Mailbox not found for unmatched address
# ActionMailbox::InboundEmail -> no matching mailbox
# Received email at billing@yourdomain.com but no BillingMailbox

# Fix by adding routing
class ApplicationMailbox < ActionMailbox::Base
  routing /support@/i => :support
  routing /billing@/i => :billing
  routing /.*@/i      => :fallback
end
```
