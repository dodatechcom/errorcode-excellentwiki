---
title: "[Solution] Python Scrapy Spider Error — How to Fix"
description: "Fix Python Scrapy spider errors. Resolve request failures, pipeline issues, and middleware configuration problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Scrapy Spider Error

A `scrapy.exceptions.CloseSpider` or `scrapy.http.response.error` occurs when Scrapy spiders fail to make requests, encounter response errors, or when pipelines and middlewares are misconfigured.

## Why It Happens

Scrapy is a web scraping framework that manages requests asynchronously. Errors arise when spiders follow broken links, when item pipelines fail to process scraped data, when middlewares block requests, or when robots.txt restrictions are violated.

## Common Error Messages

- `CloseSpider: Crawled (404)` - page not found
- `ERROR: Spider error processing <url>`
- `DropItem: Missing required field in item`
- `twisted.internet.error.TimeoutError: User timeout exceeded`

## How to Fix It

### Fix 1: Handle request errors

```python
import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://example.com"]

    def parse(self, response):
        if response.status != 200:
            self.logger.warning(f"Bad response {response.status} from {response.url}")
            return

        for link in response.css("a.product::attr(href)").getall():
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response):
        yield {
            "name": response.css("h1.title::text").get(),
            "price": response.css("span.price::text").get(),
            "url": response.url,
        }

    def errback_httpbin(self, failure):
        self.logger.error(f"Request failed: {failure.request.url}")
```

### Fix 2: Configure item pipelines

```python
# pipelines.py
class ValidationPipeline:
    def process_item(self, item, spider):
        if not item.get("name"):
            from scrapy.exceptions import DropItem
            raise DropItem(f"Missing name in {item}")
        return item

class SavePipeline:
    def process_item(self, item, spider):
        # Save to database
        return item

# settings.py
ITEM_PIPELINES = {
    "mypipelines.ValidationPipeline": 100,
    "mypipelines.SavePipeline": 300,
}
```

### Fix 3: Configure middlewares

```python
# middlewares.py
class RetryMiddleware:
    def process_response(self, request, response, spider):
        if response.status in [500, 502, 503]:
            reason = f"HTTP {response.status}"
            return request.replace(dont_filter=True)
        return response

# settings.py
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504]
DOWNLOAD_TIMEOUT = 30
```

### Fix 4: Respect robots.txt and rate limiting

```python
# settings.py
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 4

# Auto throttle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
```

## Common Scenarios

- **403 Forbidden** — Target site blocks requests without proper User-Agent or cookies.
- **Missing items** — CSS selectors do not match the page structure due to site changes.
- **Pipeline drops** — Items fail validation and are dropped before saving.

## Prevent It

- Always implement `errback` handlers on requests to catch and log failures.
- Use `scrapy crawl` with `-s LOG_LEVEL=DEBUG` to diagnose pipeline issues.
- Configure `AUTOTHROTTLE` to avoid overwhelming target servers.

## Related Errors

- [CloseSpider](/languages/python/close-spider/) — spider closed by engine
- [DropItem](/languages/python/drop-item/) — item rejected by pipeline
- [TimeoutError](/languages/python/timeouterror/) — request timed out
