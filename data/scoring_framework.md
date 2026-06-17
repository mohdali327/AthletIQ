# AthletIQ Scoring & Tagging Framework

> **Version**: 1.0 · **Last Updated**: June 2026  
> **Purpose**: Standardised methodology for tagging, scoring, and prioritising every entity (athlete, academy, event, partnership, CSR opportunity) in the AthletIQ master database.

---

## 1. Tagging Taxonomy

Every entity in the database is tagged across the following nine dimensions. Tags are mandatory at the point of data entry; the system will reject records missing critical tags.

### 1.1 Sport Type

| Tag | Definition |
|-----|-----------|
| Wrestling | Includes Freestyle, Greco-Roman, and traditional *kushti/akhada* formats |
| Boxing | Amateur boxing aligned with IBA/BFI weight categories |
| Shooting | Air Rifle, Air Pistol, Shotgun — covers both civilian ranges and SAI centres |
| Athletics | Track & Field events; includes race-walking and combined events |
| Badminton | Singles, Doubles — court-sport with established academy pipeline |
| Weightlifting | Olympic weightlifting (Snatch, Clean & Jerk); excludes powerlifting |
| Hockey | Field Hockey — 11-a-side and variants (5-a-side for grassroots) |
| Kabaddi | Pro Kabaddi format and traditional mat-based formats |
| Table Tennis | Singles, Doubles — indoor racquet sport |
| Archery | Recurve (Olympic), Compound, and traditional formats |

> **Multi-sport tagging**: Entities such as multi-discipline events or cross-training academies may carry up to 3 Sport Type tags.

---

### 1.2 Geography Tier

| Tier | Population Threshold | Examples | Significance |
|------|---------------------|----------|-------------|
| **Metro** | > 10 million | Delhi, Mumbai, Bengaluru, Hyderabad, Chennai, Kolkata | Saturated ecosystem; high competition for talent, ample funding |
| **Tier-1** | 3–10 million | Pune, Ahmedabad, Jaipur, Lucknow, Chandigarh | Developing sports infrastructure; emerging academies |
| **Tier-2** | 1–3 million | Bhopal, Guwahati, Ranchi, Thiruvananthapuram, Vijayawada | Moderate infrastructure; significant untapped talent |
| **Tier-3** | 100K–1 million | Sonipat, Bhiwani, Imphal, Bellary, Cuttack | Minimal formal infrastructure; high raw talent density |
| **Rural** | < 100K / Village-level | Akhada villages in Haryana, tribal hamlets in Jharkhand | Near-zero formal structure; highest untapped potential |

> **Scoring implication**: Tier-2, Tier-3, and Rural geographies score *higher* on Geographic Reach because they represent under-served, high-potential talent pools where AthletIQ's intervention creates maximum impact.

---

### 1.3 CWG 2036 Relevance

| Level | Definition |
|-------|-----------|
| **High** | Sport is on the CWG programme; India has won medals in the discipline at past CWG; realistic medal contention by 2036 (e.g., Wrestling, Boxing, Shooting, Badminton, Weightlifting, Table Tennis, Athletics — select events) |
| **Medium** | Sport is on the CWG programme but India's medal record is thin; emerging pipeline exists (e.g., Hockey, Archery in certain events) |
| **Low** | Sport is not on the CWG programme or India has negligible competitive history (e.g., Kabaddi — not a CWG sport) |

---

### 1.4 Olympic 2032 Relevance

| Level | Definition |
|-------|-----------|
| **High** | Sport is on the Olympic programme; India has won Olympic medals or placed top-10 in recent cycles; Brisbane 2032 medal target is realistic (e.g., Wrestling, Boxing, Shooting, Badminton, Athletics — javelin/race-walk) |
| **Medium** | Sport is Olympic but India is outside top-15 globally; development trajectory could yield results by 2036 Olympics (e.g., Weightlifting, Table Tennis, Archery, Hockey) |
| **Low** | Sport is not Olympic (Kabaddi) or India's competitive gap is too large for 2032 (e.g., some Athletics events) |

---

### 1.5 Digital Readiness

| Level | Criteria |
|-------|---------|
| **High** | Entity already uses digital tools (registration portals, result databases, video analysis); data is structured and exportable; < 20% manual records |
| **Medium** | Partial digitisation; mix of Excel/paper records; some online presence; 20–60% manual records |
| **Low** | Entirely paper-based or oral record-keeping; no online presence; > 60% manual processes; typical of rural akhadas, village-level events |

---

### 1.6 CSR Alignment

| Level | Criteria |
|-------|---------|
| **Strong** | Entity serves under-privileged/rural populations; aligns with Schedule VII of Companies Act 2013 (sports promotion for rural/women/SC-ST); measurable social impact; clear reporting metrics |
| **Moderate** | Some alignment with CSR mandates; serves mixed demographics; impact measurable but not primarily social-uplift focused |
| **Weak** | Primarily serves urban/elite populations; limited CSR reportability; difficult to frame under Schedule VII |

---

### 1.7 Pipeline Stage

| Stage | Definition | Typical Age Band | Characteristics |
|-------|-----------|-----------------|----------------|
| **Discovery** | Grassroots talent identification; first-touch engagement; village/school level | 8–14 years | No formal coaching; talent spotted through school games, local tournaments, community events |
| **Development** | Structured training; academy-level coaching; state-level competition exposure | 14–19 years | Enrolled in recognised academy or SAI centre; competing at state/national sub-junior/junior level |
| **Elite** | National team consideration; international competition; professional pathway | 19+ years | Competing at Senior Nationals, international events; TOPS/SAI support eligible |

---

### 1.8 Gender

| Tag | Definition |
|-----|-----------|
| **Male** | Entity serves/comprises male athletes exclusively |
| **Female** | Entity serves/comprises female athletes exclusively |
| **Mixed** | Entity serves both genders or is gender-neutral |

---

### 1.9 Priority Flags

Multiple flags may be applied simultaneously. Flags are system-generated based on tag combinations and manual overrides.

| Flag | Trigger Criteria |
|------|-----------------|
| **CWG2036** | CWG 2036 Relevance = High AND Pipeline Stage ∈ {Discovery, Development} AND athlete age projects to competitive readiness by 2036 |
| **Olympic2032** | Olympic 2032 Relevance = High AND Pipeline Stage ∈ {Development, Elite} AND current ranking/trajectory suggests medal contention |
| **CSR-Ready** | CSR Alignment = Strong AND Funding Gap score ≥ 7 AND entity can produce impact reports |
| **Rural-Talent** | Geography Tier ∈ {Tier-3, Rural} AND Pipeline Stage = Discovery AND at least one high-medal-potential sport |
| **High-Potential** | AthletIQ Opportunity Score ≥ 8.0 across any entity type |
| **Data-Gap** | Data Availability score ≤ 3 AND entity is in a high-priority sport/geography combination |

---

## 2. AthletIQ Opportunity Score (AOS)

### 2.1 Overview

The **AthletIQ Opportunity Score** is a weighted composite score on a 1–10 scale that quantifies the strategic value of any entity in the database. It answers: *"Where should AthletIQ invest its next unit of effort for maximum impact?"*

### 2.2 Dimensions & Weights

| # | Dimension | Weight | What It Measures |
|---|-----------|--------|-----------------|
| 1 | **Medal Potential** | 25% | Sport's realistic medal chance at CWG 2036 / Olympics 2032 for the tagged geography and pipeline stage |
| 2 | **Geographic Reach** | 20% | Degree to which the entity accesses under-served talent pools (Tier-2/3/Rural score higher) |
| 3 | **Funding Gap** | 20% | Extent to which the entity is currently unfunded or under-funded relative to its potential |
| 4 | **Data Availability** | 15% | Volume and quality of existing performance data that can feed AthletIQ Intelligence models |
| 5 | **Scalability** | 10% | Can AthletIQ's technology (FitEvents OS, AI, WhatsApp bot) add measurable value here? |
| 6 | **Institutional Readiness** | 10% | Willingness and capacity of local bodies (federations, state govts, school boards) to partner |

### 2.3 Scoring Rubrics

#### Medal Potential (25%)

| Score | Criteria |
|-------|---------|
| **9–10** | India is a consistent medal winner in this sport/event at CWG; realistic Olympic medal contender. Examples: Wrestling (freestyle 57kg, 65kg), Boxing (51kg, 69kg women), Shooting (10m Air Pistol) |
| **7–8** | India has won medals sporadically; emerging talent pipeline is strong. Examples: Badminton, Athletics (javelin, 400m), Weightlifting (select categories) |
| **5–6** | India competes but rarely medals; building phase. Examples: Table Tennis, Archery, Hockey |
| **3–4** | India participates but is far from podium; long-term investment needed. Examples: Athletics (sprints, distance events), some Shooting events |
| **1–2** | Sport is not in target competition programme or India has negligible history. Example: Kabaddi at international multi-sport events (not in CWG/Olympics) |

#### Geographic Reach (20%)

| Score | Criteria |
|-------|---------|
| **9–10** | Rural or Tier-3 geography with documented but unstructured talent; no competing platforms present. Example: Akhada village in Jhajjar district, Haryana |
| **7–8** | Tier-2 city with growing sports culture but limited tech/data infrastructure. Example: Ranchi (archery), Imphal (boxing) |
| **5–6** | Tier-1 city with developing ecosystem; some competition from existing platforms. Example: Pune, Jaipur |
| **3–4** | Metro with established infrastructure; moderate AthletIQ opportunity. Example: Delhi, Bengaluru |
| **1–2** | Hyper-saturated metro market with dominant incumbents. Example: Mumbai cricket ecosystem |

#### Funding Gap (20%)

| Score | Criteria |
|-------|---------|
| **9–10** | Entity receives zero institutional funding; athletes self-fund or depend on family; no CSR engagement. Typical of rural academies and grassroots coaches |
| **7–8** | Minimal state government allocation (< ₹5 lakh/year); no private sponsorship; CSR-eligible but unapproached |
| **5–6** | Partial funding from state sports council or one small sponsor; significant gaps in equipment, travel, nutrition |
| **3–4** | SAI-supported centre or state-funded academy; has basic infrastructure but needs tech/data investment |
| **1–2** | Well-funded by TOPS, national federation, or major corporate sponsor; limited marginal opportunity for AthletIQ |

#### Data Availability (15%)

| Score | Criteria |
|-------|---------|
| **9–10** | Rich digital data already exists: athlete profiles, competition results, training logs, video footage. FitEvents OS or equivalent already deployed |
| **7–8** | Partial digital records; competition results in spreadsheets; some video footage available; basic athlete database |
| **5–6** | Mix of digital and paper; some results available online; no systematic data collection |
| **3–4** | Primarily paper-based; results published in newspapers or notice boards; limited searchable data |
| **1–2** | No data exists; oral traditions only; results not recorded systematically. Common in rural akhadas, village tournaments |

> **Important note**: For Data Availability, unlike other dimensions, a *low* score means *low* data but this represents a *data gap opportunity* — critical for the Data-Gap priority flag but scored as-is for the composite.

#### Scalability (10%)

| Score | Criteria |
|-------|---------|
| **9–10** | AthletIQ tech can be deployed immediately with transformative impact; WhatsApp bot for registration, FitEvents OS for event management, AI for talent ID. High replicability across similar entities |
| **7–8** | Tech deployment possible with minor customisation; good fit for at least 2 AthletIQ products |
| **5–6** | Some tech value but requires significant customisation or infrastructure prerequisites (e.g., reliable internet) |
| **3–4** | Limited tech applicability; mostly requires in-person intervention; low replicability |
| **1–2** | No clear tech angle; pure on-ground activation needed; one-off engagement |

#### Institutional Readiness (10%)

| Score | Criteria |
|-------|---------|
| **9–10** | Active interest from local authorities; existing MOU or partnership framework; designated point of contact; budget allocated for tech modernisation |
| **7–8** | Verbal commitment from key stakeholders; no formal agreement yet; positive reception in initial meetings |
| **5–6** | Neutral stance; willing to listen but no commitment; bureaucratic processes may slow engagement |
| **3–4** | Sceptical or indifferent; change-resistant institutional culture; multiple approvals needed |
| **1–2** | Actively hostile or highly politicised environment; significant barriers to entry; corruption concerns |

---

### 2.4 Composite Score Formula

```
AOS = (Medal Potential × 0.25) + (Geographic Reach × 0.20) + (Funding Gap × 0.20)
    + (Data Availability × 0.15) + (Scalability × 0.10) + (Institutional Readiness × 0.10)
```

**Interpretation**:

| AOS Range | Classification | Action |
|-----------|---------------|--------|
| 8.0–10.0 | 🔴 **Critical Priority** | Immediate engagement; assign dedicated team |
| 6.0–7.9 | 🟠 **High Priority** | Include in 3-month action plan |
| 4.0–5.9 | 🟡 **Medium Priority** | Monitor; engage when resources permit |
| 2.0–3.9 | 🟢 **Low Priority** | Log for future consideration |
| 1.0–1.9 | ⚪ **Deprioritise** | Not aligned with current strategy |

---

## 3. Worked Examples

### Example 1: Wrestling Akhada in Rural Haryana

**Entity**: Guru Baldev Singh Akhada, Village Kharkhoda, Sonipat District, Haryana  
**Type**: Academy  
**Tags**: Sport=Wrestling · Geography=Rural · CWG 2036=High · Olympic 2032=High · Digital Readiness=Low · CSR Alignment=Strong · Pipeline Stage=Discovery · Gender=Male · Flags=CWG2036, Rural-Talent, CSR-Ready, Data-Gap

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Medal Potential | **9** | Haryana wrestling has produced Olympic/CWG medallists (Bajrang Punia, Vinesh Phogat). This akhada trains 40+ boys in freestyle; 3 have competed at state-level in the last 2 years. Realistic CWG 2036 pipeline. |
| Geographic Reach | **10** | Rural village with population ~8,000. Zero digital sports infrastructure. No competing platform has mapped this akhada. AthletIQ would be the first tech intervention. |
| Funding Gap | **9** | Runs entirely on Guru-ji's personal funds and small parent contributions (~₹500/month per athlete). No government support. No CSR engagement. Athletes lack basic equipment (proper mats, shoes). |
| Data Availability | **2** | No written records. Results tracked orally. No video footage. Training attendance is informal. This is a significant data gap but also a greenfield opportunity for AthletIQ data collection. |
| Scalability | **8** | WhatsApp bot for athlete registration and attendance tracking can be deployed immediately (Guru-ji has a smartphone). FitEvents OS can manage local tournament results. Computer vision for wrestling stance analysis is a direct fit. Replicable across 200+ similar akhadas in Haryana. |
| Institutional Readiness | **7** | Guru-ji is enthusiastic about technology; expressed willingness to pilot during initial outreach. Sonipat District Sports Officer has been generally supportive of digitisation initiatives. No formal MOU yet. |

**Calculation**:
```
AOS = (9 × 0.25) + (10 × 0.20) + (9 × 0.20) + (2 × 0.15) + (8 × 0.10) + (7 × 0.10)
    = 2.25 + 2.00 + 1.80 + 0.30 + 0.80 + 0.70
    = 7.85
```

**AOS = 7.85 → 🟠 High Priority**

**Recommended Actions**:
1. Deploy WhatsApp bot for athlete registration within 2 weeks
2. Conduct baseline data collection sprint (athlete profiles, body measurements, training history)
3. Include in Haryana wrestling akhada network digitisation pilot
4. Flag for CSR funding outreach (Schedule VII — rural sports promotion)

---

### Example 2: State Athletics Championship in Tamil Nadu

**Entity**: Tamil Nadu State Junior Athletics Championship 2026, Jawaharlal Nehru Stadium, Chennai  
**Type**: Event  
**Tags**: Sport=Athletics · Geography=Metro (host city) but participants from Tier-2/3/Rural · CWG 2036=High · Olympic 2032=Medium · Digital Readiness=Medium · CSR Alignment=Moderate · Pipeline Stage=Development · Gender=Mixed · Flags=CWG2036

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Medal Potential | **7** | India's athletics medal prospects at CWG are growing (javelin, 400m, race-walk, steeplechase). Tamil Nadu has a strong athletics culture — multiple national-level athletes in sprints and jumps. Junior championship is a key talent pipeline event. |
| Geographic Reach | **7** | Hosted in Chennai (Metro) but draws athletes from across Tamil Nadu including Tier-2 (Coimbatore, Madurai), Tier-3 (Erode, Thoothukudi), and rural districts. AthletIQ can map talent origins to identify under-served geographies. |
| Funding Gap | **5** | Event is partially funded by Tamil Nadu State Athletics Association. Registration fees cover basic costs. However, no technology partner for result management, athlete tracking, or post-event analytics. Travel support for rural athletes is minimal. |
| Data Availability | **6** | Results are published in PDF format post-event. Manual timing for most events (FAT only for finals). No centralised athlete database linking past performance. Some video footage from local media. Better than grassroots but far from optimal. |
| Scalability | **9** | Perfect fit for FitEvents OS deployment: online registration, live result entry, instant ranking, digital certificates. WhatsApp bot for athlete updates. Video capture at finish line enables computer vision analysis of sprint biomechanics. Template is replicable across 28 state championships. |
| Institutional Readiness | **6** | State athletics association is moderately receptive. Secretary has attended one AthletIQ presentation. Decision-making involves committee approval (2-month cycle). Previous tech partners have underdelivered, creating slight scepticism. |

**Calculation**:
```
AOS = (7 × 0.25) + (7 × 0.20) + (5 × 0.20) + (6 × 0.15) + (9 × 0.10) + (6 × 0.10)
    = 1.75 + 1.40 + 1.00 + 0.90 + 0.90 + 0.60
    = 6.55
```

**AOS = 6.55 → 🟠 High Priority**

**Recommended Actions**:
1. Pitch FitEvents OS deployment for the 2026 championship (3-month timeline)
2. Offer free pilot: AthletIQ manages registration + live results in exchange for data access agreement
3. Set up finish-line video capture for sprint biomechanics analysis prototype
4. Use event as showcase for Tamil Nadu grassroots athletics pilot pitch to state government

---

### Example 3: CSR Partnership with a Tier-1 Corporation

**Entity**: JSW Foundation — Sports Excellence Programme Partnership  
**Type**: Partnership / CSR Target  
**Tags**: Sport=Multi-sport (Wrestling, Athletics, Boxing) · Geography=Multi (Bellary-Karnataka, Pan-India) · CWG 2036=High · Olympic 2032=High · Digital Readiness=High · CSR Alignment=Strong · Pipeline Stage=Development/Elite · Gender=Mixed · Flags=CSR-Ready, High-Potential

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Medal Potential | **9** | JSW Sports has backed Olympic/CWG medallists (Neeraj Chopra, Bajrang Punia, Saina Nehwal). Their portfolio spans wrestling, athletics, boxing — all high-medal-potential sports. Partnership would directly connect AthletIQ to medal-track athletes and their development ecosystems. |
| Geographic Reach | **5** | JSW Sports primarily operates through established centres (Inspire Institute of Sport — Bellary, SAI centres). Reach is significant but concentrated in existing high-performance environments, not grassroots. However, JSW Foundation's CSR arm has rural reach in Karnataka and Maharashtra. |
| Funding Gap | **3** | JSW is one of India's best-funded sports investors. They don't have a funding gap — rather, they *are* the funder. AthletIQ's opportunity is as a tech/data partner, not a funding recipient. Score reflects that the gap we fill is technology, not money. |
| Data Availability | **8** | JSW Sports maintains athlete performance databases, training logs, and competition records. Inspire Institute has sports science infrastructure (biomechanics lab, GPS tracking). Data exists but is siloed. AthletIQ can integrate and add intelligence layer. |
| Scalability | **8** | AthletIQ's Intelligence module can add significant value: AI-powered performance prediction, computer vision enhancement for their existing biomechanics setup, CSR-athlete matching for their Foundation arm, event intelligence for JSW-sponsored competitions. Multiple product touchpoints. |
| Institutional Readiness | **8** | JSW Sports is known for being progressive and technology-forward. They have an innovation team. Previous partnerships with sports tech companies exist. Key decision-maker (Head of Sports CSR) has been identified. Warm introduction possible through mutual contacts. |

**Calculation**:
```
AOS = (9 × 0.25) + (5 × 0.20) + (3 × 0.20) + (8 × 0.15) + (8 × 0.10) + (8 × 0.10)
    = 2.25 + 1.00 + 0.60 + 1.20 + 0.80 + 0.80
    = 6.65
```

**AOS = 6.65 → 🟠 High Priority**

**Recommended Actions**:
1. Prepare bespoke partnership deck: "AthletIQ Intelligence × JSW Sports — Powering India's Medal Missions with Data"
2. Target meeting with JSW Sports CSR Head within 6 weeks
3. Propose Phase 1: AthletIQ provides academy benchmarking engine for Inspire Institute (free pilot, 3-month)
4. Phase 2: Integrate AthletIQ's grassroots data with JSW's elite pipeline — create India's first end-to-end talent pathway data layer
5. Long-term: Co-branded CSR reporting for JSW Foundation using AthletIQ's impact dashboards

---

## 4. Score Maintenance & Governance

### 4.1 Update Frequency
- Scores are **recalculated quarterly** or upon any significant status change (new MOU, funding secured, competition result)
- The Intelligence module will auto-flag entities whose input data has changed materially

### 4.2 Override Policy
- Automated scores may be manually overridden with documented justification
- All overrides are logged with timestamp, user, and rationale
- Overrides expire after 90 days and must be re-confirmed

### 4.3 Calibration
- Cross-entity calibration sessions held monthly to ensure scoring consistency
- Top-10 and bottom-10 entities reviewed for scoring accuracy
- Rubrics updated quarterly based on field feedback

---

## 5. Implementation Notes

### 5.1 Data Entry Workflow
1. New entity enters system via WhatsApp bot, FitEvents OS, or manual entry
2. Mandatory tags are assigned at entry (Sport Type, Geography Tier, Pipeline Stage, Gender)
3. Remaining tags populated within 48 hours by data team
4. AOS auto-calculated once all 6 dimensions are scored
5. Priority flags auto-assigned based on tag combinations

### 5.2 Integration Points
- **FitEvents OS**: Automatically tags events with Sport Type, Geography, Digital Readiness
- **WhatsApp Bot**: Collects athlete-level tags during registration flow
- **Dashboard**: Displays AOS heatmaps, filterable by any tag combination
- **API**: Exposes tagged, scored entities for downstream Intelligence models

### 5.3 Quality Assurance
- Random 10% audit of tag assignments monthly
- Inter-rater reliability checks for subjective dimensions (Institutional Readiness, Scalability)
- Automated anomaly detection for score distributions (flag if > 30% of entities cluster in single score band)

---

*This framework is a living document. Feedback from field teams, data analysts, and leadership should be incorporated through the quarterly review cycle.*
