# GraphRecon

> Browser-powered web application dependency mapping and reconnaissance framework.

GraphRecon is an open-source browser-based reconnaissance framework designed to analyze modern web applications and generate a dependency graph of pages, resources, network traffic, and browser interactions.

Unlike traditional crawlers that only enumerate URLs, GraphRecon uses a real browser (Playwright) to observe how an application actually behaves, making it suitable for modern JavaScript-heavy applications.

> **Project Status:** 🚧 Active Development (Level 1 Scanner)

---

# Features

## Browser-based Crawling

- Chromium-powered crawling using Playwright
- Breadth-First Search (BFS) website traversal
- Same-domain crawling
- Automatic URL normalization
- Duplicate URL detection
- Configurable crawl limits

---

## Network Reconnaissance

Automatically captures:

- HTTP Requests
- HTTP Responses
- Resource Types
- Resource URLs
- Status Codes

Supported resource types include:

- HTML
- JavaScript
- CSS
- Images
- Fonts
- Documents
- Media

---

## Dependency Graph Generation

GraphRecon generates a relationship graph between pages and resources.

Example:

```
Homepage
├── styles.css
├── app.js
├── logo.png
└── catalogue/
      ├── page1.html
      └── page2.html
```

The graph is exported as structured JSON for further visualization and analysis.

---

## DOM Resource Extraction

GraphRecon parses rendered pages to discover resources loaded through the DOM, including dynamically referenced assets.

---

## Domain Discovery

Automatically extracts and catalogs discovered domains referenced during browsing.

---

## Structured Scan Output

Each scan generates a timestamped directory containing structured artifacts.

Example:

```
.scans/
└── 20260728_181442/
    ├── pages.json
    ├── requests.json
    ├── responses.json
    ├── resources.json
    ├── domains.json
    ├── dom_resources.json
    ├── graph.json
    └── metadata.json
```

---

# Architecture

```
                CLI
                 │
                 ▼
             Runtime
                 │
                 ▼
            BrowserManager
                 │
                 ▼
              Crawler
                 │
                 ▼
            Event System
                 │
 ┌───────────────┼────────────────┐
 │               │                │
 ▼               ▼                ▼
Collectors   Resource Graph   Storage
                 │
                 ▼
          Graph Generation
```

---

# Current Components

## Runtime

Coordinates the complete scanning workflow.

---

## Browser Manager

Responsible for:

- Browser lifecycle
- Browser context
- Page management
- Playwright integration

---

## Event Bus

A lightweight synchronous event system used for communication between browser events and collectors.

---

## Collectors

Implemented collectors:

- Page Collector
- Request Collector
- Response Collector
- Resource Collector
- Domain Collector
- DOM Collector

---

## Crawler

Features:

- Breadth-First Search traversal
- Internal link extraction
- Duplicate prevention
- Queue-based crawling
- Configurable crawl depth (planned)

---

## Storage

Automatically stores scan artifacts as structured JSON.

---

## Graph Engine

Generates dependency relationships between:

- Pages
- Resources
- Assets

---

# Example

Run a scan

```bash
graphrecon scan https://books.toscrape.com
```

Output

```
INFO Pages crawled: 25
INFO Resources: 282
INFO Graph: 257 nodes, 455 edges
INFO Scan saved to .scans/20260728_181442
```

---

# Project Structure

```
graphrecon/

├── browser/
├── cache/
├── cli/
├── collectors/
├── config/
├── crawler/
├── events/
├── graph/
├── models/
├── runtime/
├── storage/
├── utils/

.scans/
```

---

# Roadmap

## Level 1 — Scanner (Current)

- [x] Browser automation
- [x] Multi-page crawling
- [x] Event system
- [x] Network request collection
- [x] Network response collection
- [x] Resource collection
- [x] DOM resource discovery
- [x] Domain extraction
- [x] Dependency graph generation
- [ ] JavaScript analysis
- [ ] API discovery
- [ ] Technology fingerprinting
- [ ] Security header analysis
- [ ] Form discovery
- [ ] Browser storage analysis

---

## Level 2 — Visualization

- [ ] Interactive dependency graph
- [ ] Search
- [ ] Resource filters
- [ ] Node inspection
- [ ] Attack surface visualization

---

## Level 3 — Security Intelligence

- [ ] API relationship mapping
- [ ] Third-party dependency analysis
- [ ] Authentication flow mapping
- [ ] Secret detection
- [ ] Risk scoring
- [ ] Technology relationship graph

---

# Technology Stack

- Python 3.13+
- Playwright
- Typer
- Pydantic
- Rich

---

# Vision

GraphRecon aims to become an open-source browser reconnaissance platform capable of mapping how modern web applications are structured and connected.

The long-term goal is to provide researchers, penetration testers, and security engineers with a comprehensive understanding of a web application's architecture, dependencies, technologies, and attack surface through browser-driven analysis.

---

# License

MIT License
