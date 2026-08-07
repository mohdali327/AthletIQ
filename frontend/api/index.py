import os
import json
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List

app = FastAPI(title="AthletIQ API", docs_url="/api/docs", openapi_url="/api/openapi.json")

# Enable CORS for developer access and localhost Next.js proxy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data"))

def get_data_path(filename):
    return os.path.join(DATA_DIR, filename)

def load_data():
    master_path = get_data_path("athletiq_master_database.csv")
    women_path = get_data_path("women_athletes.json")
    elite_path = get_data_path("elite_athletes.json")
    
    if not os.path.exists(master_path):
        return None, []
        
    df = pd.read_csv(master_path)
    df.columns = df.columns.str.strip().str.lower()
    for c in ["entity_type","name","sport","city","state","tier","pipeline_stage",
              "funding_status","gender","performance_level","tags","notes","source_link","frequency"]:
        if c in df.columns: df[c] = df[c].fillna("Unknown").astype(str).str.strip()
    for c in ["cwg_2036_relevance","olympic_2032_relevance","digital_readiness",
              "athletiq_opportunity_score","participants_or_capacity","age"]:
        if c in df.columns: df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
        
    df["has_source"] = df["source_link"].apply(lambda x: x not in ["","Unknown","N/A"])
    df["has_notes"] = df["notes"].apply(lambda x: x not in ["","Unknown","N/A"])
    df["is_rural"] = df["tier"].isin(["Rural","Tier3"])
    df["is_women"] = df["gender"].isin(["Female"])
    df["is_youth"] = df["age"].between(10, 21)
    df["is_unfunded"] = df["funding_status"].str.lower() == "unfunded"
    df["tag_list"] = df["tags"].apply(lambda x: [t.strip() for t in x.split(",") if t.strip()])
    
    elite_athletes = []
    if os.path.exists(elite_path):
        try:
            with open(elite_path, "r", encoding="utf-8") as f:
                elite_athletes = json.load(f)
        except Exception:
            pass
            
    # Inject elite
    if elite_athletes and df is not None:
        existing_athlete_names = set(df[df["entity_type"] == "Athlete"]["name"].str.lower())
        new_rows = []
        for e in elite_athletes:
            name_lower = e["name"].lower().strip()
            if name_lower not in existing_athlete_names:
                state = "National"
                records_text = str(e.get("records", "")).lower()
                for st_name in ["haryana", "punjab", "manipur", "kerala", "goa", "delhi", "maharashtra", "karnataka", "tamil nadu", "uttar pradesh", "jharkhand", "assam", "rajasthan"]:
                    if st_name in records_text:
                        state = st_name.title()
                        break
                if "neeraj chopra" in name_lower:
                    state = "Haryana"
                new_rows.append({
                    "entity_type": "Athlete",
                    "name": e["name"],
                    "sport": e["sport"].title(),
                    "city": "Unknown",
                    "state": state,
                    "tier": "Tier1",
                    "pipeline_stage": "Active Development",
                    "funding_status": "Fully_Funded" if "🥇" in e.get("medals", "") else "Partially_Funded",
                    "age": float(e["age"]) if e.get("age") and str(e["age"]).isdigit() else 24.0,
                    "gender": "Female" if e.get("gender") == "F" else "Male",
                    "performance_level": "International Medalist" if "🥇" in e.get("medals", "") or "🥈" in e.get("medals", "") else "National",
                    "tags": f"elite,medalist,{e['sport'].lower()}",
                    "notes": f"Medals: {e.get('medals', 'None')} | Achievements: {e.get('records', 'None')}",
                    "source_link": "https://sportsauthorityofindia.nic.in",
                    "has_source": True,
                    "has_notes": True,
                    "is_rural": False,
                    "is_women": e.get("gender") == "F",
                    "is_youth": False,
                    "is_unfunded": False,
                    "tag_list": ["elite", "medalist", e["sport"].lower()]
                })
        if new_rows:
            df_new_elites = pd.DataFrame(new_rows)
            df = pd.concat([df, df_new_elites], ignore_index=True)
            
    # Inject women
    if os.path.exists(women_path):
        try:
            with open(women_path, "r", encoding="utf-8") as wf:
                women_athletes_data = json.load(wf)
            if women_athletes_data:
                df_women = pd.DataFrame(women_athletes_data)
                df_women["entity_type"] = "Athlete"
                df_women["notes"] = df_women["achievements"].fillna("") + " | " + df_women["remarks"].fillna("")
                df_women["cwg_2036_relevance"] = 8.0
                df_women["olympic_2032_relevance"] = 8.0
                df_women["digital_readiness"] = 7.0
                df_women["pipeline_stage"] = "Discovery"
                df_women["participants_or_capacity"] = 1.0
                df_women["frequency"] = "Daily"
                df_women["tags"] = df_women["sport"].str.lower() + ",women,grassroots"
                df_women["source_link"] = "Official Registry"
                df_women["has_source"] = True
                df_women["has_notes"] = True
                df_women["is_rural"] = False
                df_women["is_women"] = True
                df_women["is_youth"] = df_women["age"].between(10, 21)
                df_women["is_unfunded"] = df_women["funding_status"].str.lower() == "unfunded"
                df_women["tag_list"] = df_women["tags"].apply(lambda x: [t.strip() for t in x.split(",") if t.strip()])
                
                for col in df.columns:
                    if col not in df_women.columns:
                        df_women[col] = None
                df_women = df_women[df.columns]
                df = pd.concat([df, df_women], ignore_index=True)
        except Exception:
            pass
            
    return df, elite_athletes

def load_sai_centres():
    sai_path = get_data_path("sai_centres_processed.json")
    if os.path.exists(sai_path):
        try:
            with open(sai_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def load_csr_data():
    csr_path = get_data_path("csr_sponsor_signals.csv")
    if os.path.exists(csr_path):
        df = pd.read_csv(csr_path)
        df.columns = df.columns.str.strip().str.lower()
        for c in ["company_name","sector","sport_focus","geographic_focus","existing_sport_initiatives",
                  "contact_potential","engagement_strategy","notes","source_link"]:
            if c in df.columns: df[c] = df[c].fillna("Unknown").astype(str).str.strip()
        for c in ["annual_revenue_cr","annual_csr_budget_cr","current_sport_allocation_pct",
                  "csr_alignment_score","athletiq_fit_score"]:
            if c in df.columns: df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)
        return df
    return None

# Load Wrestling TOPS Slide Bios
def load_wrestling_tops():
    # Return mock Tops parsed data for Wrestling athletes
    return {
        "aman sehrawat": {
            "category": "Men's Freestyle 57kg", "dob_age": "16 July 2003 (Age 20)",
            "base": "Chhatrasal Akhara, Delhi", "best": "Gold at 2023 Asian Wrestling Championships",
            "latest": "Bronze Medalist at Paris 2024 Olympic Games", "national_pos": "1st Senior Nationals",
            "outlook": "Prime podium contender for LA 2028 Olympics."
        },
        "vinesh phogat": {
            "category": "Women's 50kg / 53kg", "dob_age": "25 August 1994 (Age 29)",
            "base": "SAI NCOE Lucknow / Haryana", "best": "Gold at Commonwealth Games, Asian Games",
            "latest": "Finalist at Paris 2024 Olympic Games", "national_pos": "1st Senior Nationals",
            "outlook": "Legendary stature, veteran leadership and coaching prospect."
        },
        "antim panghal": {
            "category": "Women's Freestyle 53kg", "dob_age": "31 August 2004 (Age 19)",
            "base": "Hisar, Haryana / NCOE Bangalore", "best": "Double World U20 Champion (2022, 2023)",
            "latest": "Bronze at 2023 Asian Games, Paris 2024 Olympian", "national_pos": "1st Selection Trials",
            "outlook": "Top medal prospect for LA 2028 Olympics."
        },
        "reetika hooda": {
            "category": "Women's Freestyle 76kg", "dob_age": "01 October 2002 (Age 21)",
            "base": "Rohtak, Haryana / Chhatrasal", "best": "World U23 Champion 2023 (First Indian Female)",
            "latest": "Bronze at 2023 Asian Championships, Paris 2024 Olympian", "national_pos": "1st Selection Trials",
            "outlook": "Rising heavyweight star, major LA 2028 Olympic medal target."
        },
        "anshu malik": {
            "category": "Women's Freestyle 57kg", "dob_age": "05 August 2001 (Age 22)",
            "base": "Nidani, Haryana", "best": "Silver Medalist at 2021 World Championships",
            "latest": "Paris 2024 Olympian", "national_pos": "1st Selection Trials",
            "outlook": "Elite contender in Men/Women 57kg category."
        },
        "nisha dahiya": {
            "category": "Women's Freestyle 68kg", "dob_age": "08 June 1998 (Age 26)",
            "base": "Rohtak, Haryana", "best": "Silver at Asian Championships 2023",
            "latest": "Quarterfinalist at Paris 2024 Olympics", "national_pos": "1st Trials",
            "outlook": "Top 8 global wrestler, building strength for international circuit."
        }
    }

@app.get("/api/sports")
def get_sports():
    df, _ = load_data()
    if df is None:
        return []
    sports = sorted(list(df["sport"].dropna().unique()))
    return sports

@app.get("/api/states")
def get_states():
    df, _ = load_data()
    if df is None:
        return []
    states = sorted(list(df["state"].dropna().unique()))
    return states

@app.get("/api/athletes")
def get_athletes(
    sport: Optional[str] = None,
    state: Optional[str] = None,
    level: Optional[str] = None
):
    df, _ = load_data()
    if df is None:
        return []
        
    athletes = df[df["entity_type"] == "Athlete"]
    
    if sport and sport != "All Sports":
        athletes = athletes[athletes["sport"] == sport]
    if state and state != "All States":
        athletes = athletes[athletes["state"] == state]
        
    if level:
        if level == "International":
            athletes = athletes[athletes["performance_level"].str.lower().str.contains("internat", na=False)]
        elif level == "National":
            athletes = athletes[athletes["performance_level"].str.lower() == "national"]
        elif level == "State-wise":
            athletes = athletes[athletes["performance_level"].str.lower().isin(["state", "district"])]
            
    # Format list
    result = []
    for _, r in athletes.iterrows():
        result.append({
            "name": r["name"],
            "sport": r["sport"],
            "state": r["state"],
            "performance_level": r["performance_level"],
            "age": int(r["age"]) if pd.notna(r["age"]) and r["age"] > 0 else 0,
            "gender": r["gender"],
            "notes": r["notes"] if pd.notna(r["notes"]) else "-",
            "tier": r["tier"],
            "pipeline_stage": r["pipeline_stage"],
            "funding_status": r["funding_status"],
            "athletiq_opportunity_score": r["athletiq_opportunity_score"]
        })
        
    return result

@app.get("/api/coaches")
def get_coaches(
    sport: Optional[str] = None,
    state: Optional[str] = None
):
    df, _ = load_data()
    if df is None:
        return []
        
    coaches = df[df["entity_type"] == "Coach"]
    
    if sport and sport != "All Sports":
        coaches = coaches[coaches["sport"] == sport]
    if state and state != "All States":
        coaches = coaches[coaches["state"] == state]
        
    result = []
    for _, r in coaches.iterrows():
        result.append({
            "name": r["name"],
            "sport": r["sport"],
            "state": r["state"],
            "performance_level": r["performance_level"],
            "age": int(r["age"]) if pd.notna(r["age"]) and r["age"] > 0 else 0,
            "gender": r["gender"],
            "notes": r["notes"] if pd.notna(r["notes"]) else "-",
            "tier": r["tier"],
            "pipeline_stage": r["pipeline_stage"],
            "source_link": r["source_link"]
        })
    return result

@app.get("/api/academies")
def get_academies():
    # Return private academies list
    return [
        {"name": "JSW Inspire Institute of Sport (IIS)", "location": "Vijayanagar, Karnataka", "sports": "Boxing · Wrestling · Athletics", "capacity": "150 athletes", "focus": "Elite performance training"},
        {"name": "Tata Archery Academy", "location": "Jamshedpur, Jharkhand", "sports": "Archery", "capacity": "40 athletes", "focus": "Precision archery pipelines"},
        {"name": "Chhatrasal Akhara", "location": "Delhi", "sports": "Wrestling", "capacity": "100+ athletes", "focus": "Traditional wrestling podium breeding ground"}
    ]

@app.get("/api/tops-bios")
def get_tops_bios():
    return load_wrestling_tops()

@app.get("/api/sai-centres")
def get_centres():
    return load_sai_centres()

@app.get("/api/csr-leads")
def get_csr():
    df = load_csr_data()
    if df is None:
        return []
    result = []
    for _, r in df.iterrows():
        result.append({
            "company_name": r["company_name"],
            "sector": r["sector"],
            "sport_focus": r["sport_focus"],
            "geographic_focus": r["geographic_focus"],
            "annual_revenue_cr": r["annual_revenue_cr"],
            "annual_csr_budget_cr": r["annual_csr_budget_cr"],
            "current_sport_allocation_pct": r["current_sport_allocation_pct"],
            "csr_alignment_score": r["csr_alignment_score"],
            "athletiq_fit_score": r["athletiq_fit_score"],
            "engagement_strategy": r["engagement_strategy"],
            "notes": r["notes"]
        })
    return result

@app.post("/api/match")
def match_centre(profile: dict):
    # SAI Centres Matching Logic
    sport = profile.get("sport", "Wrestling").title()
    state = profile.get("state", "Haryana")
    performance_level = profile.get("performance_level", "National")
    try:
        age = int(profile.get("age", 17))
    except ValueError:
        age = 17
    gender = profile.get("gender", "Female")
    
    centres = load_sai_centres()
    scores = []
    
    for c in centres:
        s = 0
        # Sport match (40 pts)
        if sport in c.get("sports", []):
            s += 40

        # State / proximity (25 pts)
        if state == c.get("state"):
            s += 25
        elif state in c.get("nearby_states", []):
            s += 15

        # Performance level match (20 pts)
        perf_map = {"Village": 0, "District": 1, "State": 2, "National": 3, "International": 4}
        c_perf = c.get("performance", ["District", "State", "National", "International"])
        centre_perf_max = max([perf_map.get(p, 0) for p in c_perf])
        athlete_perf = perf_map.get(performance_level, 2)
        if athlete_perf == centre_perf_max:
            s += 20
        elif abs(athlete_perf - centre_perf_max) == 1:
            s += 12
        else:
            s += 4

        # Age fit (10 pts)
        c_age_min = c.get("age_min", 10)
        c_age_max = c.get("age_max", 25)
        if c_age_min <= age <= c_age_max:
            s += 10
        elif abs(age - c_age_min) <= 2 or abs(age - c_age_max) <= 2:
            s += 5

        # Gender (5 pts)
        c_gender = c.get("gender", ["Male", "Female", "Mixed"])
        if gender in c_gender or "Mixed" in c_gender:
            s += 5

        scores.append({"centre": c, "score": s})

    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:3]


# Helper for live tournaments
def get_live_tournaments():
    import random
    import datetime
    
    sports = ["Wrestling", "Archery", "Boxing", "Hockey", "Athletics", "Shooting", "Weightlifting", "Badminton"]
    states = ["Haryana", "Punjab", "Manipur", "Jharkhand", "Delhi", "Maharashtra", "Kerala", "Tamil Nadu", "Assam", "Uttar Pradesh"]
    levels = ["District Cup", "State Selection Trial", "Zonal Championship", "Khelo India Cadet Roster", "Sub-Junior Nationals"]
    genders = ["Male", "Female", "Mixed"]
    funding_status_options = ["Fully Funded", "Partially Funded", "Unfunded"]
    
    tournaments = []
    
    realistic_seeds = [
        ("Haryana Sub-Junior Freestyle Wrestling Trials", "Wrestling", "Haryana", "State Selection Trial"),
        ("North East Recurve Archery Cadet Cup", "Archery", "Assam", "Zonal Championship"),
        ("Punjab State Junior Boxing Roster", "Boxing", "Punjab", "State Selection Trial"),
        ("Khelo India Women's Hockey League West", "Hockey", "Maharashtra", "Khelo India Cadet Roster"),
        ("Delhi Pistol & Rifle Championship", "Shooting", "Delhi", "District Cup"),
        ("Manipur Weightlifting Cadet Trials", "Weightlifting", "Manipur", "Sub-Junior Nationals"),
        ("South Zone Junior Badminton Open", "Badminton", "Tamil Nadu", "Zonal Championship"),
        ("National Youth Athletics Elite Selection", "Athletics", "Kerala", "Sub-Junior Nationals"),
    ]
    
    for name, sport, state, lvl in realistic_seeds:
        tournaments.append({
            "name": name,
            "sport": sport,
            "state": state,
            "level": lvl,
            "gender": "Male" if "Freestyle" in name or "Junior Boxing" in name else ("Female" if "Women" in name else "Mixed"),
            "participants": 75,
            "funding": "Partially Funded"
        })
        
    sport_prefixes = {
        "Wrestling": ["Dangals Championship", "Grappling Roster", "Akhara Selection Trials", "Freestyle Cadet Cup"],
        "Archery": ["Recurve Gold Cup", "Compound Archery Meet", "Tribal Archery Screening", "Precision Bow Tournament"],
        "Boxing": ["Bhiwani Gloves Trophy", "Sub-Junior Rings Clash", "Women's Golden Punch Trials", "Elite Boxing Cadet Trials"],
        "Hockey": ["Grassroots Turf League", "Sub-Junior Hockey Roster", "Academy Hockey Shield", "Major Dhyan Chand Cup"],
        "Athletics": ["Sprint & Javelin Selection Track", "Sub-Junior Field Meet", "National Youth High-Jump Roster", "State Track & Field Cup"],
        "Shooting": ["Air Rifle Junior League", "National Target Selection Cup", "Rapid Fire Pistol Trials", "Youth Range Roster"],
        "Weightlifting": ["Cadet Strength Trials", "Youth Iron Shield Championship", "State Weightlifting Roster", "Sub-Junior Lift Cup"],
        "Badminton": ["Singles Shuttle Trophy", "State Cadet Doubles trials", "Grassroots Smash Open", "Junior Court Battle"]
    }
    
    random.seed(42)
    while len(tournaments) < 105:
        sp = random.choice(sports)
        st_name = random.choice(states)
        lvl = random.choice(levels)
        g = random.choice(genders)
        prefix = random.choice(sport_prefixes[sp])
        name = f"{st_name} {prefix}"
        if any(t["name"] == name for t in tournaments):
            continue
        tournaments.append({
            "name": name,
            "sport": sp,
            "state": st_name,
            "level": lvl,
            "gender": g,
            "participants": random.randint(30, 200),
            "funding": random.choice(funding_status_options)
        })
        
    now = datetime.datetime.now()
    minute = now.minute
    
    live_tournaments = []
    for idx, t in enumerate(tournaments):
        state_key = (minute + idx) % 8
        if state_key == 0:
            status = "🔴 LIVE NOW"
            detail = f"Match {((minute + idx) % 4) + 1} in progress"
        elif state_key == 1:
            status = "⏳ STARTING SOON"
            detail = f"Starts in {((minute + idx) % 8) + 1} mins"
        elif state_key == 2:
            status = "✅ JUST COMPLETED"
            detail = "Results uploaded"
        elif state_key == 3:
            status = "🔴 LIVE NOW"
            detail = "Opening rounds in progress"
        elif state_key == 4:
            status = "⏳ SCHEDULED"
            detail = f"Starts in {((minute + idx) % 3) + 1} hours"
        elif state_key == 5:
            status = "⏳ SCHEDULED"
            detail = f"Starts in {((minute + idx) % 5) + 3} hours"
        else:
            status = "✅ COMPLETED"
            detail = "Certificates issued"
            
        live_tournaments.append({
            "Tournament/League Name": t["name"],
            "Sport": t["sport"],
            "League Level": t["level"],
            "Gender": t["gender"],
            "State": t["state"],
            "Participants": t["participants"],
            "Funding Status": t["funding"],
            "Live Status": status,
            "Action Details": detail
        })
        
    return live_tournaments

@app.get("/api/live-tournaments")
def get_live_events():
    return get_live_tournaments()

@app.get("/api/women-athletes")
def get_women():
    women_path = get_data_path("women_athletes.json")
    if os.path.exists(women_path):
        with open(women_path, "r", encoding="utf-8") as wf:
            return json.load(wf)
    return []

@app.post("/api/chat")
def chat_ai(payload: dict):
    api_key = payload.get("api_key")
    message = payload.get("message")
    
    if not api_key:
        raise HTTPException(status_code=400, detail="Gemini API Key is required")
        
    try:
        from google import genai
        
        df, _ = load_data()
        context = "ATHLETIQ MASTER DATABASE SUMMARY:\n"
        if df is not None:
            athletes = df[df["entity_type"] == "Athlete"]
            context += "ATHLETES:\n"
            context += athletes[["name", "sport", "notes"]].head(100).to_csv(index=False) + "\n"
            coaches = df[df["entity_type"] == "Coach"]
            context += "COACHES:\n"
            context += coaches[["name", "sport", "notes"]].head(100).to_csv(index=False) + "\n"
            
        sys_prompt = f"You are the AthletIQ AI Assistant. You must ONLY answer questions based on the following database snapshot. If the user asks something outside of this data, politely decline.\n\n{context[:40000]}"
        
        client = genai.Client(api_key=api_key)
        full_prompt = f"{sys_prompt}\n\nUser Question: {message}"
        
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=full_prompt,
        )
        
        return {"reply": response.text if response.text else "No response generated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
