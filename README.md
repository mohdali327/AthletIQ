# 🏅 AthletIQ — Grassroots Sports Intelligence Tracker

> *Mapping India's grassroots sports ecosystem to fuel CWG 2036 & Olympic 2032 medal dreams.*

---

## 📖 Overview

**AthletIQ** is a data-driven intelligence platform that tracks and analyzes India's grassroots sports ecosystem. It identifies emerging talent, maps academies and coaches, catalogs events from village-level dangals to state championships, and connects the ecosystem with CSR funding opportunities.

The platform focuses on:
- 🎯 **Talent Pipeline Discovery** — Identify high-potential athletes from Tier 2/3 cities and rural India
- 🏟️ **Event Intelligence** — Track tournaments, meets, and championships across 16+ states
- 🏋️ **Academy & Coach Mapping** — Database of training infrastructure and coaching talent
- 💰 **CSR Sponsor Matching** — Connect grassroots programs with corporate CSR budgets
- 🥇 **Medal Potential Scoring** — CWG 2036 and Olympic 2032 relevance scoring

---

## 📁 Project Structure

```
AthletIQ/
├── README.md                                   # Project documentation
├── data/
│   ├── athletiq_master_database.csv            # Master database (~160 rows)
│   │   ├── Events (~50)      — Tournaments, meets, dangals
│   │   ├── Academies (~40)   — Training centers, akhadas, clubs
│   │   ├── Athletes (~40)    — Grassroots talent profiles
│   │   └── Coaches (~30)     — Coaching talent directory
│   └── csr_sponsor_signals.csv                 # CSR funding prospects (~30 rows)
│       └── Top 30 Indian corporates with CSR analysis
└── app/
    ├── requirements.txt                        # Python dependencies
    └── dashboard.py                            # Streamlit interactive dashboard
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation & Running

```bash
# Clone the repository
git clone <repo-url>
cd AthletIQ

# Install dependencies
pip install -r app/requirements.txt

# Launch the dashboard
streamlit run app/dashboard.py
```

The dashboard will open at `http://localhost:8501`.

---

## 📊 Deliverables

| # | Deliverable | Description | Status |
|---|-------------|-------------|--------|
| 1 | **Master Database** | 160+ entity records (events, academies, athletes, coaches) across 16 states | ✅ Complete |
| 2 | **CSR Sponsor Signals** | 30 major Indian corporates analyzed for grassroots sport CSR fit | ✅ Complete |
| 3 | **Interactive Dashboard** | Streamlit app with filters, maps, and opportunity scoring | 🔧 In Progress |

---

## 🗂️ Data Schema

### Master Database (`athletiq_master_database.csv`)

| Column | Description |
|--------|-------------|
| `entity_type` | Event / Academy / Athlete / Coach |
| `name` | Name of entity |
| `sport` | Primary sport |
| `city`, `state` | Location |
| `tier` | Metro / Tier1 / Tier2 / Tier3 / Rural |
| `cwg_2036_relevance` | 1–10 CWG medal potential score |
| `olympic_2032_relevance` | 1–10 Olympic medal potential score |
| `digital_readiness` | 1–10 digitization score |
| `pipeline_stage` | Discovery / Development / Elite |
| `athletiq_opportunity_score` | 1–10 composite opportunity score |
| `funding_status` | Unfunded / Partially_Funded / Fully_Funded |

### CSR Sponsor Signals (`csr_sponsor_signals.csv`)

| Column | Description |
|--------|-------------|
| `company_name` | Indian corporate name |
| `annual_csr_budget_cr` | Annual CSR budget in ₹ crores |
| `current_sport_allocation_pct` | % of CSR going to sports |
| `csr_alignment_score` | 1–10 alignment with grassroots sport |
| `athletiq_fit_score` | 1–10 fit for AthletIQ platform |
| `contact_potential` | Cold / Warm / Hot |

---

## 🌍 Coverage

**16 States**: Haryana, Uttar Pradesh, Maharashtra, Tamil Nadu, Kerala, Punjab, Madhya Pradesh, Jharkhand, Manipur, Rajasthan, Karnataka, West Bengal, Odisha, Assam, Telangana, Gujarat

**14+ Sports**: Wrestling, Boxing, Shooting, Athletics, Badminton, Weightlifting, Hockey, Kabaddi, Archery, Football, Chess, Table Tennis, Swimming, Cycling

---

## 📈 Scoring Methodology

- **CWG 2036 Relevance**: Based on sport inclusion in Commonwealth Games, India's historical medal tally, and current talent pipeline depth
- **Olympic 2032 Relevance**: India's realistic medal chances at Brisbane 2032, based on world rankings and development trajectory
- **AthletIQ Opportunity Score**: Composite of medal potential, geographic reach, funding gaps, digital readiness, and data availability

---

## 📝 Data Sources

- Khelo India portal & results archives
- Sports Authority of India (SAI) records
- State sports department publications
- National Sports Federation reports
- Ministry of Corporate Affairs CSR data
- Company annual reports & sustainability disclosures
- News reports and sports journalism

---

## 📄 License

This project is for educational and research purposes.

---

*Built with ❤️ for Indian grassroots sports*
