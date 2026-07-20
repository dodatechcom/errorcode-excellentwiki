---
title: "[Solution] Python Scrapy Error — Spider and Crawler Failures"
description: "Fix Python Scrapy errors like Spider errors, middleware failures, item pipeline issues, and selector errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 423
---

# Python Scrapy Error — Spider and Crawler Failures

Scrapy errors occur when spiders fail to parse responses, middleware encounters exceptions, item pipelines reject data, or CSS/XPath selectors return empty results. These are common in large-scale crawling projects.

## Common Causes

```python
# Spider not found by Scrapy
# scrapy genspider example example.com  # typo in spider name

# Selector returns empty results
import scrapy
response = scrapy.Selector(text="<div>Hello</div>")
title = response.css("h1::text").get()  # None — h1 doesn't exist

# Item pipeline Drop exception
class ValidationPipeline:
    def process_item(self, item, spider):
        if not item.get("title"):
            raise scrapy.exceptions.DropItem("Missing title")

# Middleware import error
# DOWNLOADER_MIDDLEWARES = {"myproject.middlewares.CustomMiddleware": 400}
# but the class doesn't exist in the module

# Callback returns None instead of items
def parse(self, response):
    yield {"url": response.url}  # forgot yield from loop
```

## How to Fix

### Fix 1: Verify Spider Is Registered Correctly
Ensure the spider name matches and is discoverable by Scrapy.
```bash
scrapy list  # shows all available spiders
```
```python
class ExampleSpider(scrapy.Spider):
    name = "example"  # must match what you pass to scrapy crawl
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]
```

### Fix 2: Handle Empty Selector Results Safely
Always check for None before using selector results.
```python
import scrapy

def parse(self, response):
    title = response.css("h1::text").get()
    if title is None:
        title = response.css("h2::text").get(default="No title")
    yield {"title": title}
```

### Fix 3: Configure Middleware Correctly
Ensure middleware classes exist and are properly referenced.
```python
# settings.py
DOWNLOADER_MIDDLEWARES = {
    "myproject.middlewares.RetryMiddleware": 400,
}
```

### Fix 4: Validate Items in the Pipeline
Use proper error handling in pipeline classes.
```python
class ValidationPipeline:
    def process_item(self, item, spider):
        if not item.get("title"):
            spider.logger.warning("Item missing title: %s", item)
            raise scrapy.exceptions.DropItem("Missing title")
        return item
```

### Fix 5: Ensure All Callbacks Yield Items
Every parse method should yield or return items or requests.
```python
def parse(self, response):
    for article in response.css("article"):
        yield {
            "title": article.css("h2::text").get(),
            "url": article.css("a::attr(href)").get(),
        }
    next_page = response.css("a.next::attr(href)").get()
    if next_page:
        yield response.follow(next_page, self.parse)
```

## Examples

```python
# Complete spider with error handling
import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ["https://example.com/news"]

    def parse(self, response):
        for article in response.css("article.post"):
            yield {
                "title": article.css("h2.title::text").get(),
                "author": article.css("span.author::text").get(default="Unknown"),
                "date": article.css("time::attr(datetime)").get(),
            }

        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

## Related Errors

- [Python BeautifulSoup Error](/languages/python/python-beautifulsoup-error/)
- [Python Requests Error](/languages/python/python-requests-error/)
- [Python httpx Error](/languages/python/python-httpx-error/)
