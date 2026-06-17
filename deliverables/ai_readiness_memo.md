# AthletIQ Intelligence — AI Readiness Memo

> **Version**: 1.0 · **Last Updated**: June 2026  
> **Classification**: Internal — Leadership & Engineering  
> **Purpose**: Technical assessment of data maturity, AI/ML use cases, architecture, privacy framework, and 6-month roadmap for the AthletIQ Intelligence module

---

## 1. Current Data Maturity Assessment

### 1.1 Data Inventory

| Data Domain | What We Have | Volume (Est.) | Format | Primary Source |
|------------|-------------|---------------|--------|---------------|
| **Athlete Profiles** | Name, age, sport, weight class, geography, competition history | ~5,000 records | Spreadsheets, WhatsApp messages, paper forms | Field team manual entry, event registrations |
| **Event Results** | State/district competition results, rankings, timings | ~800 events (2 years) | PDFs, newspaper clippings, Excel sheets | Federation websites, media reports, on-ground collection |
| **Academy Information** | Academy name, location, coach details, sport, capacity | ~400 academies mapped | Google Sheets, field notes | Outreach team surveys |
| **Geographic Data** | District-level talent density estimates, infrastructure mapping | 150+ districts | GIS layers, CSV | Census data, SAI reports, field estimates |
| **Video Footage** | Training clips, competition recordings | ~200 clips (untagged) | MP4, WhatsApp-compressed video | Coaches, local media, field team |
| **CSR Records** | Corporate CSR spend on sports, foundation contacts, grant history | ~60 entities | Spreadsheet | MCA filings, annual reports, manual research |
| **Federation Data** | Federation structures, selection criteria, competition calendars | 10 sports | Documents, web scrapes | Federation websites, contacts |

### 1.2 Data Maturity Levels

We assess each data domain against a 5-level maturity model:

| Level | Name | Description |
|-------|------|-------------|
| 1 | **Ad-hoc** | Data collected sporadically, no standards, mostly unstructured |
| 2 | **Managed** | Some structure, basic spreadsheets, inconsistent quality |
| 3 | **Defined** | Standardised schemas, regular collection, validation rules |
| 4 | **Measured** | Quality metrics tracked, automated pipelines, dashboards |
| 5 | **Optimised** | ML-ready, real-time updates, feedback loops, self-improving |

| Data Domain | Current Level | Target (6 months) | Key Gap |
|------------|--------------|-------------------|---------|
| Athlete Profiles | Level 2 | Level 3 | No unique ID system; duplicate records; missing fields (DOB, contact) in 40% of records |
| Event Results | Level 1–2 | Level 3 | Results in PDFs and newspaper clippings; no standardised format; missing event metadata |
| Academy Information | Level 2 | Level 3 | Self-reported data; no verification; facility quality scores missing |
| Geographic Data | Level 2 | Level 4 | Good district-level coverage; need block/village level; infrastructure data incomplete |
| Video Footage | Level 1 | Level 2 | Untagged, unorganised, heavily compressed; no metadata (athlete, sport, date) |
| CSR Records | Level 2 | Level 3 | Incomplete coverage; historical spend data patchy; no grant tracking workflow |
| Federation Data | Level 1 | Level 2 | Scraped and manual; outdated; contact information unreliable |

### 1.3 Structured vs Unstructured Data Mix

```
Current data composition (approximate):

Structured (database-ready):     25%   ████░░░░░░░░░░░░░░░░
Semi-structured (spreadsheets):  40%   ████████░░░░░░░░░░░░
Unstructured (PDFs, video, text): 35%  ███████░░░░░░░░░░░░░
```

**Critical gaps**:
- **Unique Athlete Identifier**: No system to prevent duplicates across events/sources. Estimated 15–20% duplicate rate in current profiles
- **Longitudinal Tracking**: Cannot trace an athlete's progression over time — events and profiles are disconnected
- **Coaching Data**: Near-zero structured data on training methodologies, session plans, or coaching quality
- **Nutrition/Health Data**: Not collected; critical for performance prediction models
- **Financial Data**: Per-athlete funding/cost data does not exist at grassroots level

---

## 2. AI/ML Use Cases — Priority Order

### UC-1: Computer Vision for Talent Identification

| Attribute | Detail |
|-----------|--------|
| **Description** | Use smartphone cameras to capture athlete movement and extract biomechanical features for talent screening. No specialised hardware required — works with any phone camera recording at 30fps. Sport-specific models assess posture, balance, power generation, and movement efficiency |
| **Input Data** | Video footage (MP4/MOV, minimum 720p, 30fps): training drills, competition bouts, standardised movement tests |
| **Technical Approach** | MediaPipe Pose (33 key body landmarks) for pose estimation → sport-specific feature extraction (joint angles, centre of mass, velocity profiles) → classification model (talent potential: High/Medium/Low) |
| **Sport-Specific Models** | **Wrestling**: Stance width, hip angle, takedown initiation speed, balance recovery. **Athletics (sprints)**: Stride length/frequency ratio, knee drive angle, ground contact time, arm swing symmetry. **Boxing**: Guard position, punch trajectory, footwork pattern, head movement range |
| **Expected Output** | Talent screening report per athlete: biomechanical scores (0–100), comparison to age-group benchmarks, improvement recommendations, video highlights with annotated key frames |
| **Impact** | 🔴 **Transformative** — Enables talent screening at scale in rural areas with zero infrastructure; a single phone replaces a biomechanics lab |
| **Technical Complexity** | High — Requires custom model training on Indian athlete data; sport-specific feature engineering; edge deployment for offline use |
| **Timeline** | Month 3–4 (prototype for wrestling + athletics) |
| **Data Requirements** | Minimum 500 annotated videos per sport for v1 model; 2,000+ for production quality |

### UC-2: Performance Prediction Models

| Attribute | Detail |
|-----------|--------|
| **Description** | Time-series models that predict athlete development trajectories based on age, sport, region, training intensity, competition results, and physiological markers. Identify athletes likely to breakthrough vs plateau |
| **Input Data** | Longitudinal athlete data: competition results over time, age, physical measurements, training frequency, coaching quality scores, geography |
| **Technical Approach** | Gradient-boosted models (XGBoost/LightGBM) for tabular prediction; LSTM/Transformer for time-series trajectories; Bayesian approaches for uncertainty quantification given sparse data |
| **Expected Output** | Per-athlete: predicted performance in 1/2/3 years, probability of reaching state/national/international level, optimal training load recommendations, comparison to successful athletes with similar starting profiles |
| **Impact** | 🟠 **High** — Enables data-driven selection and resource allocation; prevents talent loss due to late identification |
| **Technical Complexity** | Medium — Standard ML pipelines; main challenge is data sparsity and building representative training sets across sports/regions |
| **Timeline** | Month 3–5 (v1 with available data; improves as data grows) |
| **Data Requirements** | Minimum 3 years of longitudinal data for 200+ athletes per sport; currently available for ~50 athletes (athletics only) |

### UC-3: NLP for Scouting Reports

| Attribute | Detail |
|-----------|--------|
| **Description** | Auto-generate structured athlete scouting reports from event data, coaching notes, and WhatsApp messages. Transform scattered, multilingual data points into standardised, readable profiles |
| **Input Data** | Event results (structured), coaching feedback (WhatsApp text — Hindi/English/regional), social media mentions, newspaper reports |
| **Technical Approach** | Template-based generation for structured data → LLM (fine-tuned GPT/Gemini) for unstructured summarisation → Multi-language processing (Hindi, Tamil, Manipuri, Bengali) via mT5 or IndicBERT → Sentiment analysis on coaching feedback |
| **Expected Output** | Standardised scouting report per athlete: bio, competition record, coaching assessment, strengths/weaknesses, development recommendations, comparable athlete profiles |
| **Impact** | 🟡 **Medium-High** — Saves 5–10 hours per athlete profile creation; enables scaling to thousands of profiles |
| **Technical Complexity** | Medium — Pre-trained multilingual models available; main challenge is template design and quality assurance of auto-generated content |
| **Timeline** | Month 4–5 |
| **Data Requirements** | 100+ manually created scouting reports as templates/training examples |

### UC-4: Academy Benchmarking Engine

| Attribute | Detail |
|-----------|--------|
| **Description** | Multi-dimensional scoring engine that rates sports academies/training centres against national standards. Enables comparison, ranking, and improvement roadmapping |
| **Input Data** | Academy surveys (facilities, coaching staff, athlete roster, results, funding), athlete progression data, external benchmarks (SAI standards, federation criteria) |
| **Technical Approach** | Weighted multi-criteria scoring (similar to AthletIQ Opportunity Score) → Peer clustering (k-means/hierarchical) to group similar academies → Gap analysis algorithms → Recommendation engine for improvement priorities |
| **Expected Output** | Academy scorecard (0–100 across 6 dimensions), peer comparison dashboard, improvement roadmap with prioritised actions, estimated cost of improvements |
| **Impact** | 🟠 **High** — Direct value for CSR reporting ("your funded academy improved from 45 to 72"); enables quality standardisation |
| **Technical Complexity** | Low-Medium — Primarily rule-based with statistical analysis; well-understood problem space |
| **Timeline** | Month 5–6 |
| **Data Requirements** | Complete survey data for 50+ academies (currently available for ~20) |

### UC-5: CSR-Athlete Matching Algorithm

| Attribute | Detail |
|-----------|--------|
| **Description** | Optimisation algorithm that connects CSR funding to highest-impact athletes based on potential, need, alignment with funder preferences, and portfolio diversity constraints |
| **Input Data** | Athlete profiles (potential score, financial need, geography, sport, gender), CSR funder profiles (budget, sport preferences, geographic focus, impact goals, Schedule VII requirements) |
| **Technical Approach** | Multi-objective optimisation (maximise impact per rupee, maximise geographic diversity, satisfy funder constraints) → Assignment algorithm (modified Hungarian/auction) → Impact prediction model per funded athlete |
| **Expected Output** | Matched portfolio of athletes per CSR funder, predicted impact metrics (medals, progression, social impact score), quarterly impact reports, portfolio rebalancing recommendations |
| **Impact** | 🟠 **High** — Directly drives revenue; makes CSR-to-sports conversion measurable and scalable |
| **Technical Complexity** | Medium — Constrained optimisation is well-studied; challenge is defining "impact" metrics credibly |
| **Timeline** | Month 5–6 (v1) |
| **Data Requirements** | 200+ athlete profiles with need/potential scores; 20+ CSR funder profiles with preferences |

### UC-6: Event Intelligence

| Attribute | Detail |
|-----------|--------|
| **Description** | Predict event participation, optimise scheduling/location, and analyse geographic coverage gaps in the event calendar |
| **Input Data** | Historical event data (participation, location, date, sport, results), athlete locations, travel distances, competing events calendar |
| **Technical Approach** | Demand forecasting (Prophet/ARIMA) for participation prediction → Calendar optimisation (constraint satisfaction) → Geographic coverage analysis (Voronoi diagrams, accessibility modelling) → Travel cost optimisation for athlete participation |
| **Expected Output** | Event demand forecast, optimal calendar with minimal conflicts, geographic coverage heatmap showing under-served areas, recommended new event locations |
| **Impact** | 🟡 **Medium** — Improves FitEvents OS event planning; secondary priority vs talent-focused models |
| **Technical Complexity** | Low-Medium — Standard forecasting and optimisation; limited by historical data availability |
| **Timeline** | Month 6+ |
| **Data Requirements** | 3+ years of event data with participation figures; currently available for ~300 events |

---

## 3. Data Pipeline Architecture

### 3.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SOURCE LAYER                                 │
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ WhatsApp │ │ FitEvents│ │  Manual  │ │  Video   │ │Federation│ │
│  │   Bot    │ │    OS    │ │  Entry   │ │ Uploads  │ │   APIs   │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       │             │            │             │             │       │
└───────┼─────────────┼────────────┼─────────────┼─────────────┼──────┘
        │             │            │             │             │
        ▼             ▼            ▼             ▼             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     INGESTION & PROCESSING                          │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  API Gateway / Message Queue (Apache Kafka / RabbitMQ)       │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                              │                                       │
│  ┌──────────┐ ┌──────────┐ ┌┴─────────┐ ┌──────────┐              │
│  │  Schema  │ │   Data   │ │   Dedup  │ │ Quality  │              │
│  │Validation│→│   ETL    │→│  Engine  │→│ Scoring  │              │
│  └──────────┘ └──────────┘ └──────────┘ └────┬─────┘              │
│                                               │                     │
└───────────────────────────────────────────────┼─────────────────────┘
                                                │
                                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        STORAGE LAYER                                │
│                                                                     │
│  ┌──────────────┐  ┌────────────────┐  ┌──────────────────┐        │
│  │   Data Lake   │  │ Data Warehouse │  │   Feature Store  │        │
│  │  (Raw / S3)   │→│  (PostgreSQL)  │→│  (ML-Ready)      │        │
│  │               │  │                │  │                  │        │
│  │ - Raw videos  │  │ - Athletes     │  │ - Athlete        │        │
│  │ - PDFs        │  │ - Events       │  │   feature vectors│        │
│  │ - WhatsApp    │  │ - Academies    │  │ - Event features │        │
│  │   messages    │  │ - Results      │  │ - Academy scores │        │
│  │ - Unprocessed │  │ - CSR records  │  │ - Predictions    │        │
│  └──────────────┘  └────────────────┘  └──────────────────┘        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     INTELLIGENCE LAYER                              │
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐              │
│  │ Computer │ │  Perf.   │ │  NLP     │ │  Academy │              │
│  │ Vision   │ │Prediction│ │ Reports  │ │Benchmark │              │
│  │ Models   │ │ Models   │ │ Engine   │ │ Engine   │              │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘              │
│       │             │            │             │                     │
│  ┌────┴─────────────┴────────────┴─────────────┴────┐              │
│  │          Model Serving (FastAPI / TensorFlow Serving)│           │
│  └──────────────────────┬───────────────────────────────┘           │
│                          │                                           │
└──────────────────────────┼──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        OUTPUT LAYER                                 │
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐              │
│  │Dashboards│ │  Reports │ │   API    │ │ WhatsApp │              │
│  │ (Metabase│ │  (PDF /  │ │Endpoints │ │  Alerts  │              │
│  │/ Grafana)│ │  Email)  │ │ (REST)   │ │          │              │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Source Layer — Details

| Source | Data Type | Frequency | Volume | Integration Method |
|--------|-----------|-----------|--------|-------------------|
| **WhatsApp Bot** | Athlete registrations, attendance, feedback, training updates | Real-time | ~500 messages/day (at scale) | WhatsApp Business API → Webhook → Kafka |
| **FitEvents OS** | Event registrations, live results, athlete check-ins, scoring | Event-driven | ~50 events/month (at scale) | Direct API integration (internal) |
| **Manual Entry** | Academy surveys, field reports, coaching assessments | Weekly batches | ~100 records/week | Web forms (React frontend) → REST API |
| **Video Uploads** | Training footage, competition recordings | Async uploads | ~20 videos/day | Presigned S3 URLs → Processing queue |
| **Federation APIs** | Competition calendars, rankings, selection criteria | Daily sync | ~10 federations | Web scraping → Structured extraction (for federations without APIs) |
| **Khelo India Data** | National-level athlete records, competition results | Monthly (via MOU) | Bulk batches | Secure file transfer → ETL |

### 3.3 Processing Layer — Details

#### Schema Validation
- JSON Schema validation for all API inputs
- Sport-specific validation rules (e.g., weight class must exist for wrestling/boxing/weightlifting)
- Geography validation against master district database
- Age range checks by pipeline stage

#### ETL Pipeline
- **Orchestrator**: Apache Airflow (managed) for batch processing; event-driven processing via Kafka consumers
- **Transformations**: 
  - Standardise names (transliteration from Hindi/regional → English)
  - Normalise competition results (times, distances, scores) to comparable units
  - Geo-coding of addresses to lat/long → district → state mapping
  - Video processing: extract frames, compress, generate thumbnails

#### Deduplication Engine
- Fuzzy matching on athlete records (name + DOB + sport + district = probable match)
- Configurable thresholds (> 85% similarity → flag for review; > 95% → auto-merge)
- Merge rules: retain most recent data, preserve all competition records
- Audit trail for all merge/dedup decisions

#### Quality Scoring
- Each record assigned a quality score (0–100) based on completeness, recency, and source reliability
- Fields weighted by importance (name: 15, DOB: 10, sport: 10, competition history: 25, contact: 10, geography: 15, physical measurements: 15)
- Records below quality threshold (< 40) flagged for manual enrichment
- Dashboard tracking quality trends by source and data domain

### 3.4 Storage Layer — Details

| Layer | Technology | Purpose | Retention |
|-------|-----------|---------|-----------|
| **Data Lake** | AWS S3 / MinIO (self-hosted option) | Raw data preservation; video/PDF/image storage | Indefinite |
| **Data Warehouse** | PostgreSQL 16 (with PostGIS for geo queries) | Structured, queryable data; analytics workloads | Indefinite |
| **Feature Store** | Feast (open-source) or custom PostgreSQL tables | Pre-computed ML features; training data management | Rolling 3 years |
| **Cache** | Redis | Real-time dashboard data; session management; WhatsApp bot state | TTL-based |
| **Search** | Elasticsearch | Full-text search across athlete profiles, events, reports | Sync from PostgreSQL |

---

## 4. Privacy & Data Ownership Framework

### 4.1 Core Principles

1. **Athlete-First**: Athletes own their data. AthletIQ is a custodian, not an owner.
2. **Minimum Collection**: Collect only what is necessary for the stated purpose.
3. **Transparency**: Athletes and guardians can see exactly what data is held and how it's used.
4. **Portability**: Data can be exported in standard formats at any time.
5. **Compliance**: Full adherence to the Digital Personal Data Protection Act, 2023 (DPDP Act).

### 4.2 Sports Passport — Athlete Data Portability

The **AthletIQ Sports Passport** is a portable, athlete-owned data profile that travels with the athlete across academies, events, and federations:

| Component | Contents | Portability |
|-----------|----------|-------------|
| **Identity** | Name, DOB, photo, Aadhaar (hashed), sport, weight class | Exportable as verified JSON |
| **Competition Record** | All registered competition results, rankings, timings | Exportable as CSV/PDF |
| **Training History** | Academy enrolments, attendance, coaching notes (anonymised) | Exportable with academy consent |
| **Performance Data** | Biomechanical assessments, fitness test results, progression curves | Exportable as structured data |
| **Funding History** | CSR funding received, scholarship status, equipment grants | Exportable for audit |
| **Medical/Health** | Only if voluntarily provided; encrypted separately | Athlete-controlled access only |

**Portability mechanism**: Athletes receive a unique AthletIQ ID and can request full data export via WhatsApp bot or web portal. Standard export format: JSON (machine-readable) + PDF (human-readable).

### 4.3 Consent Management for Minors

Given that the Discovery pipeline stage involves athletes aged 8–14, robust minor consent is critical:

| Age Group | Consent Requirement | Mechanism |
|-----------|-------------------|-----------|
| **Under 14** | Verifiable parental/guardian consent required for all data collection | Parent signs digital consent form (OTP-verified phone number); physical consent form option for rural areas |
| **14–18** | Dual consent (minor + parent/guardian) for sensitive data; minor consent sufficient for basic profile | In-app consent flow with parent verification |
| **18+** | Self-consent | Standard consent flow |

**Consent is granular**:
- Basic profile (name, age, sport) — required for platform access
- Competition data — required for event participation
- Video footage — separate opt-in consent
- Health/medical data — separate, explicit consent
- Third-party sharing (federation/CSR) — separate, per-entity consent

**Consent withdrawal**: Available at any time via WhatsApp bot ("Delete my data") or web portal. 30-day processing window as per DPDP Act.

### 4.4 Federation Data Sharing Agreements

| Data Type | Shared With | Purpose | Retention | Conditions |
|-----------|------------|---------|-----------|------------|
| Aggregated statistics | Federations, SAI | Talent pipeline analysis, selection support | Duration of agreement | No individual identification without athlete consent |
| Individual athlete profiles | Federation (specific sport) | Selection consideration, ranking | Competition cycle | Athlete opt-in required; revocable |
| Academy benchmarking scores | State sports departments | Infrastructure planning | Annual refresh | Academy opt-in; right to contest scores |
| Event analytics | Event organisers | Operational improvement | 1 year post-event | Aggregated only; no PII |
| Impact reports | CSR funders | CSR compliance reporting | Funding period + 3 years | Anonymised or athlete-consented |

### 4.5 DPDP Act 2023 Compliance

| DPDP Requirement | AthletIQ Implementation |
|------------------|------------------------|
| **Consent (Section 6)** | Granular, informed consent at data collection; separate consents for different purposes; consent withdrawal mechanism |
| **Purpose Limitation (Section 5)** | Data used only for stated purposes (talent development, event management, CSR matching); no sale of data |
| **Data Minimisation** | Collection limited to fields necessary for specific functions; periodic review of collected fields |
| **Data Accuracy** | Quality scoring engine; athlete self-correction via WhatsApp bot; annual data verification drives |
| **Storage Limitation** | Defined retention periods per data type; automated deletion workflows |
| **Security (Section 8)** | Encryption at rest (AES-256) and in transit (TLS 1.3); access controls (RBAC); audit logging; annual security assessments |
| **Data Breach Notification (Section 8(6))** | Incident response plan; 72-hour notification to Data Protection Board; affected individuals notified via SMS/WhatsApp |
| **Data Protection Officer** | Designated DPO for compliance oversight; contact published on platform |
| **Cross-Border Transfer** | All primary data stored in India (AWS Mumbai / ap-south-1); no cross-border transfer without explicit consent and adequacy assessment |
| **Children's Data (Section 9)** | Verifiable parental consent; no behavioural tracking of minors; no targeted advertising |

### 4.6 Data Classification

| Classification | Definition | Examples | Access Control |
|---------------|-----------|----------|---------------|
| **Public** | Available to anyone | Aggregated sport statistics, published competition results, academy listings | Open API |
| **Internal** | Available to AthletIQ team | Quality scores, pipeline analytics, internal dashboards | Role-based (all employees) |
| **Confidential** | Restricted to authorised personnel | Individual athlete profiles, performance predictions, CSR funder details | Role-based (need-to-know) |
| **Restricted** | Highest sensitivity | Health data, Aadhaar hashes, minor consent records, financial data | Encrypted; named-access only; audit logged |

---

## 5. Six-Month Roadmap

### Phase 1: Foundation (Month 1–2)

**Theme**: *Build the pipes, start the data flowing*

| Deliverable | Details | Success Metric |
|------------|---------|----------------|
| **Data Pipeline MVP** | Kafka + Airflow + PostgreSQL deployed on AWS. Ingestion from 3 sources (WhatsApp, manual entry, FitEvents OS) | Pipeline processes 100+ records/day with < 5% error rate |
| **WhatsApp Bot MVP** | Registration flow (athlete profile creation), event result entry, basic queries ("my results", "upcoming events") | 200+ athletes registered via bot in pilot geography |
| **Athlete ID System** | Unique AthletIQ ID generation; deduplication engine v1 (fuzzy name matching) | < 10% duplicate rate in new registrations |
| **Data Collection Sprint** | On-ground team deploys to Haryana (wrestling) and Tamil Nadu (athletics) for baseline data collection | 500+ athlete profiles, 25+ academy profiles, 50+ event results collected |
| **Master Database Schema** | PostgreSQL schema finalised for all entity types; scoring framework tables; tagging taxonomy | Schema supports all tags defined in scoring_framework.md |
| **Consent Management v1** | Basic consent collection flow integrated into WhatsApp bot and web forms | 100% of new records have valid consent |

**Dependencies**: AWS account setup, WhatsApp Business API approval, field team deployment  
**Risks**: WhatsApp API approval delays (mitigation: apply immediately, build SMS fallback); rural connectivity issues (mitigation: offline-first bot design with sync)

### Phase 2: Intelligence (Month 3–4)

**Theme**: *First AI models, first wow moments*

| Deliverable | Details | Success Metric |
|------------|---------|----------------|
| **Computer Vision Prototype** | MediaPipe-based pose estimation for wrestling stance analysis and sprint biomechanics. Works on smartphone video (30fps, 720p+) | Process 50+ athlete videos; biomechanical scores correlate > 0.6 with coach assessments |
| **Performance Prediction v1** | XGBoost model for athletics events (100m, 200m, 400m, javelin): predict performance 1 year out based on age, current times, training frequency | Model trained on 200+ athlete trajectories; MAPE < 15% on validation set |
| **Academy Data Collection** | Structured surveys deployed to 50+ academies across 3 states (Haryana, TN, Manipur) | Complete survey data for 50 academies; benchmarking dimensions populated |
| **Dashboard v1** | Metabase/Grafana dashboards: talent pipeline funnel, geographic heatmaps, data quality metrics, AOS leaderboard | 5+ dashboards live; updated daily; accessible to leadership team |
| **NLP Scouting Report Template** | Template-based auto-generation of athlete profiles from structured data | Generate reports for top 50 pipeline athletes; 80% usable without editing |
| **Data Quality Engine** | Automated quality scoring for all records; flagging system for low-quality data; weekly quality reports | Quality score tracked for 100% of records; average quality > 60/100 |

**Dependencies**: Annotated video dataset (500+ clips), coach validation partnerships, compute resources for model training  
**Risks**: Insufficient training data for CV models (mitigation: synthetic data augmentation, transfer learning from public sports datasets); coach buy-in for validation (mitigation: compensated review programme)

### Phase 3: Product (Month 5–6)

**Theme**: *Demonstrate value, close partnerships*

| Deliverable | Details | Success Metric |
|------------|---------|----------------|
| **Academy Benchmarking Engine** | Multi-dimensional scoring system live. Academy scorecard generation (automated). Peer comparison dashboards. Improvement recommendations | 50+ academies benchmarked; 3 state sports departments receive reports |
| **CSR-Athlete Matching v1** | Matching algorithm deployed. Portfolio generation for pilot CSR partners. Impact prediction per funded athlete | Algorithm matches 100+ athletes to 5+ CSR funder profiles; 2 CSR partners receive matched portfolios |
| **Sports Passport v1** | Athlete-facing data export. QR-code based verification. PDF + JSON export functionality | 200+ athletes can export their Sports Passport; 1 federation accepts it for registration |
| **API v1** | REST API for external integrations (federation data pull, CSR dashboard embedding, event result push) | API documented (OpenAPI spec); 2+ external integrations live |
| **Impact Report Generator** | Automated CSR impact reports: athletes supported, progression tracked, geography covered, fund utilisation | Generate monthly reports for 3+ CSR partners; reports pass CSR audit requirements |
| **Event Intelligence v1** | Participation forecast for upcoming events; calendar optimisation recommendations | Predict participation within ±20% for 10+ events |

**Dependencies**: CSR partner agreements signed, federation MOU (at least 1), academy benchmarking criteria validated  
**Risks**: CSR sales cycle longer than expected (mitigation: start conversations in Month 1, have pipeline of 10+ targets); federation bureaucracy delays MOU (mitigation: start with state-level associations, not national)

---

## 6. Tech Stack Recommendation

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **Language** | Python 3.11+ | ML ecosystem, team familiarity, rapid prototyping |
| **Web Framework** | FastAPI | High-performance API; async support; auto-generated docs |
| **ML Frameworks** | PyTorch (deep learning), scikit-learn (classical ML), MediaPipe (pose estimation) | PyTorch for CV models; scikit-learn for tabular prediction; MediaPipe for efficient on-device pose |
| **Data Pipeline** | Apache Airflow (orchestration), Apache Kafka (streaming) | Industry standard; scalable; good monitoring |
| **Database** | PostgreSQL 16 + PostGIS | Robust, free, excellent geo-spatial support |
| **Data Lake** | AWS S3 | Cost-effective object storage for raw data and video |
| **Feature Store** | Feast (open-source) | ML feature management; point-in-time joins for training data |
| **Search** | Elasticsearch | Full-text search, athlete discovery, fuzzy matching |
| **Cache** | Redis | Bot state management, dashboard caching |
| **Dashboards** | Metabase (open-source) or Grafana | SQL-based dashboards; embeddable; team-friendly |
| **Monitoring** | Prometheus + Grafana (infra), Great Expectations (data quality) | Pipeline health, data quality tracking |
| **Cloud** | AWS (ap-south-1 Mumbai region) | DPDP compliance (data in India); comprehensive services; startup credits available |
| **CI/CD** | GitHub Actions | Automated testing, deployment pipelines |
| **Container** | Docker + ECS/EKS | Consistent environments; scalable deployment |
| **WhatsApp** | WhatsApp Business API (via Twilio/Gupshup) | Reach; penetration in target demographics; no app download required |

---

## 7. Team & Resource Requirements

### 7.1 Core Team (Month 1–6)

| Role | Count | Key Responsibilities |
|------|-------|---------------------|
| **ML Engineer** | 2 | Computer vision models, performance prediction, NLP pipelines |
| **Backend Engineer** | 2 | Data pipeline, API development, WhatsApp bot, database design |
| **Data Engineer** | 1 | ETL pipelines, data quality engine, Airflow DAGs |
| **Frontend Engineer** | 1 | Dashboards, web forms, academy survey interface |
| **Data Analyst** | 1 | Data collection coordination, quality audits, report generation |
| **Product Manager** | 1 | Roadmap execution, stakeholder management, prioritisation |
| **Field Team Lead** | 1 | On-ground data collection, academy relationships, pilot coordination |

**Total**: 9 people

### 7.2 Infrastructure Costs (Monthly Estimate)

| Item | Monthly Cost (Est.) |
|------|-------------------|
| AWS (compute, storage, networking) | ₹1.5–2.5 lakh |
| WhatsApp Business API | ₹30–50K |
| Third-party tools (monitoring, CI/CD) | ₹20–30K |
| **Total infra** | **₹2–3 lakh/month** |

> Costs will increase as data volume and model complexity grow. Budget ₹5 lakh/month by Month 6.

---

## 8. Key Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Insufficient training data for CV models | High | High | Transfer learning from public datasets (COCO, SportsPose); synthetic data augmentation; prioritise data collection in Month 1–2 |
| WhatsApp API approval delays | Medium | Medium | Apply in Week 1; build SMS fallback; consider Telegram as interim channel |
| Rural connectivity issues | High | Medium | Offline-first architecture; sync when connected; SMS-based fallback for critical data |
| Federation resistance to data sharing | Medium | High | Start with state associations (less bureaucratic); demonstrate value before asking for data; offer free tools |
| DPDP Act compliance complexity | Low | High | Engage legal counsel in Month 1; build consent management early; privacy-by-design approach |
| Team hiring delays | Medium | Medium | Start with 6-person core; use contractors for field data collection; internship pipeline for data labelling |

---

*This memo is a living document. Technical decisions should be validated through rapid prototyping. Architecture choices should be revisited at the end of each phase based on actual data volumes and model performance.*

*Next review: End of Month 2 (Phase 1 completion)*
