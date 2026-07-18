# SEO Rules & Best Practices

Comprehensive SEO rules extracted from the Build SEO Strategy course. These rules apply to every page on errorcode.excellentwiki.com.

---

## 1. Title Tags

- **Under 60 characters** — Google truncates with "..."
- **Front-load the primary keyword** — first few words carry more weight
- Formula: `[Primary Keyword] + [Value Hook]`
- One primary keyword per page — don't stuff multiple keywords
- Match search intent exactly — if someone searches "how to fix", title should say "How to Fix"
- Pattern for this site: `[Solution] Error Name — Fix Description`

## 2. Meta Descriptions

- **Under 155 characters** (150-160 sweet spot)
- Formula: `[Action Verb] + [Benefit/Promise] + [Differentiator] + [CTA]`
- Action verbs: "Fix", "Resolve", "Solve", "Learn"
- Always deliver on the promise — if description says "5 steps", article must have 5 steps
- CTR is a confirmed ranking signal — better description = more clicks = better rankings

## 3. Content Hierarchy

- **Exactly one H1 per page** — contains primary keyword
- H2s = major sections, H3s = granular details under H2s
- Never create an "Orphaned H2" — every H2 must have 2-3+ paragraphs of content
- Headers allow users to skip irrelevant sections — builds trust
- Think: H1 = book title, H2s = chapters, H3s = sections within chapters

## 4. Content Formatting (The Lazy Reader Rules)

- **Three-Sentence Rule**: no paragraph exceeds 3 sentences
- Use white space aggressively — reduces cognitive load
- **1-2-Many Structure**: 1 sentence hook → 2 sentences context → bulleted list
- Never create "walls of text" — dense paragraphs cause immediate bounce
- Use H2/H3 headers, bold text, and bullet points as visual anchors
- Mobile Audit: scroll page on phone without reading — if "gray blocks" last longer than 2 thumb-scrolls, break them up

## 5. AI Overview Optimization (Critical for 2026)

- Goal: be the **source citation** inside AI-generated responses (AI Overviews, ChatGPT Search, Perplexity)
- **Direct Answer Block**: make core question an H2/H3 header, answer in 1-2 clear sentences immediately below
- **Inverted Pyramid**: Header → 30-40 word direct answer → then deep-dive below
- Convert dense paragraphs into structured data: bullet points, numbered lists, comparison tables
- Never write steps, features, or comparisons as standard paragraphs — always use lists or tables
- Before publishing: (1) target question is an explicit H2/H3, (2) direct answer comes first, (3) data is in lists/tables

## 6. Internal Linking

- Every page reachable within **3 clicks from homepage** (3-Click Rule)
- Place internal links **within body content** — editorial links carry more weight than nav/footer links
- Use **descriptive, keyword-rich anchor text** — never use "click here" or "read more"
- Vary anchor text for links to the same page — exact-match repetition looks manipulative
- Audit orphan pages: pages with zero internal links are invisible to Google
- Every new post: ask "Which existing pages should link to this?" and "Which pages should this link to?"
- Enable breadcrumbs (already done on this site)

## 7. Content Freshness

- Content Decay is real — even great content loses rankings without maintenance
- Google checks: publication date, last modified date, update frequency
- Superficial updates ("2024" → "2026") are not enough — need substantive changes
- **Evergreen content**: review every 6-12 months
- Always add a **"Last Updated: [Date]"** note to build trust
- Build a Content Calendar: Page URL → Last Updated → Next Review Date

## 8. E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

- Every page should demonstrate expertise through accurate, detailed solutions
- Use first-person experience where applicable ("In my experience...", "I've found that...")
- Include original code examples and real-world solutions — not generic advice
- Link to official documentation (MDN, official docs) as authoritative references
- Display transparency: clear about page, contact information, privacy policy

## 9. Technical SEO

- **HTTPS is non-negotiable** — confirmed ranking signal since 2014
- **Core Web Vitals targets**:
  - LCP: under 2.5 seconds
  - INP: under 200 milliseconds
  - CLS: under 0.1
- Compress all images to 150-200KB
- Set explicit width/height on images to prevent layout shifts
- Never block CSS/JS/images in robots.txt
- Submit sitemap to Google Search Console
- Fix all 404 errors with 301 redirects
- Keep redirect chains to one hop maximum

## 10. Schema Markup

- Schema powers Rich Snippets — can increase CTR by 20-30%
- This site uses: TechArticle (pages), WebSite (homepage), BreadcrumbList
- Always validate with Google's Rich Results Test
- FAQPage schema: requires 2+ visible Q&A pairs
- BreadcrumbList schema: shows navigation path in search results

## 11. Search Intent

- 4 core intents: Informational (learn), Navigational (find), Commercial (compare), Transactional (buy)
- This site is primarily **Informational** — people searching for error solutions
- Intent Match: match content format to what top results show
- Informational content: guides, tutorials, FAQ pages
- Never push hard sales on informational content

## 12. Keyword Strategy

- Target **long-tail keywords** — specific, multi-word phrases with higher buyer intent
- Ranking #1 for ten 50-search keywords beats ranking #50 for one 50,000-search keyword
- Use modifiers: "fix", "error", "solution", "how to resolve", "troubleshoot"
- Mine forums (Reddit, Stack Overflow) for natural conversational questions
- Create content for ALL stages: error identification → explanation → solution → prevention

## 13. Link Building

- One link from a reputable source beats 1,000 from random blogs
- Create link-worthy content: original research, comprehensive guides, free tools
- Never buy links, use PBNs, or automated link building
- Guest blog posts with genuine value earn real backlinks
- Monitor backlinks monthly via Google Search Console

## 14. Analytics & Measurement

- **Google Search Console**: how people find you (queries, indexing, technical issues)
- **Google Analytics 4**: what they do after arriving (engagement, conversions)
- 5 key SEO metrics: Organic Traffic, CTR, Average Position, Engagement Rate, Conversions
- Check monthly — don't get overwhelmed by daily data
- Troubleshooting traffic drops: check algorithm updates → manual actions → technical issues → lost backlinks → competitors → seasonality

---

## Rules Specific to This Site (Error Reference)

### Page Template Rules

Every error page MUST follow this structure:

```
# [Solution] Error Name — Short Description

## What This Error Means
(Direct answer in 1-2 sentences — AI-optimized)

## Why It Happens
(Bullet list of common causes)

## How to Fix It
(Code blocks with solutions)

## Common Mistakes
(What NOT to do)

## Prevention Tips
(How to avoid this error in the future)

## Related Pages
(Internal links to related errors)
```

### Title Tag Formula
```
[Solution] [Error Name] — [Fix Description]
```
Example: `[Solution] NullPointerException in Java — Fix and Prevent`

### Meta Description Formula
```
Fix [Error Name] with this step-by-step solution. [Benefit]. [CTA].
```
Example: `Fix NullPointerException in Java with this step-by-step solution. Learn common causes, code examples, and prevention tips.`

### Internal Linking Rules for This Site
- Every page links to its parent section index page
- Every page links to 2-3 related errors in the same section
- Cross-link between sections when relevant (e.g., Python ImportError links to pip errors)
- Use descriptive anchor text: "See our Python TypeError guide" not "click here"
