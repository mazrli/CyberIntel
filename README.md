# CyberIntel
CyberIntel is an open-source cyber threat intelligence platform that collects, normalizes, and stores cybersecurity news from trusted RSS feeds. Built for scalable data ingestion, threat intelligence, analytics, and future AI-powered security applications.


# Cyber Intelligence Aggregator

A production-ready, open-source platform for collecting, normalizing, and analyzing cybersecurity intelligence from hundreds of RSS sources.

The project is designed around a scalable data ingestion pipeline and serves as the backend foundation for threat intelligence dashboards, search systems, machine learning experiments, and security monitoring platforms.

## Features

* Collect cybersecurity news from hundreds of trusted RSS feeds.
* Import sources directly from OPML files.
* Automatically create the database schema on first execution.
* Normalize publication dates into UTC.
* Prevent duplicate articles using GUID hashing.
* Store complete article metadata including title, link, summary and content.
* Support multiple source categories (News, Research, Vulnerabilities, Malware, Threat Intelligence, Podcasts, Videos).
* Designed with a modular architecture that can later evolve into REST APIs, scheduled workers and distributed processing.

## Technology Stack

### Backend

* Python 3.12+
* Feedparser
* OPML
* MySQL
* python-dateutil

### Database

* MySQL 8+

### Future Backend

* ASP.NET Core Web API
* Entity Framework Core
* Redis
* RabbitMQ
* Docker

### Future Frontend

* React
* Next.js
* Tailwind CSS

## Project Structure

```text
cyber-intelligence/

├── importer.py
├── config.py
├── database.py
├── repositories.py
├── opml_reader.py
├── rss_reader.py
├── feeds.opml
├── requirements.txt
└── README.md
```

## Data Flow

```text
OPML
        │
        ▼
Read Feed Sources
        │
        ▼
Download RSS Feed
        │
        ▼
Normalize Data
        │
        ▼
Deduplicate
        │
        ▼
Store in MySQL
        │
        ▼
REST API / Dashboard / Search
```

## Installation

Clone the repository.

```bash
git clone https://github.com/mazrli/CyberIntel.git

cd cyber-intelligence
```

Install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```bash
python importer.py article feeds.opml
```

Example:

```bash
python importer.py article feeds.opml

python importer.py podcast podcasts.opml

python importer.py vulnerability cve.opml
```

## Database

The importer automatically creates the required tables if they do not already exist.

### feeds

Stores metadata about RSS sources.

### entries

Stores normalized RSS articles.

## Roadmap

### Phase 1

* RSS Importer
* OPML Import
* MySQL Storage
* Duplicate Detection

### Phase 2

* REST API
* Search API
* Pagination
* Filtering
* Full-text Search

### Phase 3

* Docker
* Background Scheduler
* Incremental Updates
* Multi-threaded Import

### Phase 4

* AI Classification
* Threat Scoring
* Automatic Tagging
* Embedding Search
* LLM Summaries

### Phase 5

* Web Dashboard
* Analytics
* Trend Detection
* Threat Timeline

## Possible Use Cases

* Cyber Threat Intelligence
* Security Operations Center (SOC)
* Threat Hunting
* Malware Research
* Vulnerability Monitoring
* Security Dashboards
* AI Training Dataset
* OSINT Collection

## License

MIT License
