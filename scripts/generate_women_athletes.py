"""
Generate 5000 women athlete records for the AthletIQ Womens tab.
Covers 25+ sports, all Indian states/UTs, realistic names, and varied stats.
"""
import json
import random
import os

random.seed(42)

# ─── Indian Women First Names (200+) ───
first_names = [
    "Aadhira","Aanya","Aaradhya","Aashi","Aditi","Ahana","Aisha","Akshara","Amara","Amrita",
    "Ananya","Anika","Anisha","Anjali","Ankita","Anushka","Aparna","Archana","Arya","Avani",
    "Bhavna","Bhumi","Charvi","Chitra","Daksha","Deepa","Deepika","Devi","Devika","Dhanya",
    "Disha","Divya","Durga","Esha","Ekta","Gauri","Gayatri","Geeta","Gita","Harini",
    "Harita","Hema","Ira","Isha","Ishani","Ishita","Jaya","Jhanvi","Jhilli","Juhi",
    "Kajal","Kamala","Kanchan","Kavya","Keerthi","Khushi","Kiran","Kirti","Komal","Komalika",
    "Kriti","Krithika","Kumari","Lakshmi","Lata","Lavanya","Leela","Madhavi","Madhu","Mahima",
    "Maitri","Malini","Mamta","Manasi","Manisha","Meena","Meera","Megha","Mira","Mitali",
    "Mohini","Mona","Mrinalini","Naina","Nalini","Namita","Nandini","Neelam","Neetha","Neha",
    "Niharika","Nikita","Nirmala","Nisha","Nita","Nithya","Padma","Pallavi","Parvati","Payal",
    "Pooja","Poonam","Prachi","Pragya","Pranita","Prarthana","Pratibha","Pratima","Preeti","Prerna",
    "Priya","Priyanka","Puja","Pushpa","Radha","Radhika","Rajeshwari","Rakhi","Rama","Ramya",
    "Rani","Rashmi","Raveena","Reena","Rekha","Renuka","Reshma","Riddhi","Ridhima","Rinku",
    "Ritu","Riya","Rohini","Roshni","Ruhi","Rupali","Saanvi","Sakshi","Saloni","Sandhya",
    "Sangita","Sanjana","Sarika","Sarla","Sarojini","Savita","Seema","Shabnam","Shakti","Shalini",
    "Shanti","Sharada","Sharmila","Shikha","Shilpa","Shimla","Shivani","Shreya","Shruti","Simran",
    "Sita","Smita","Sneha","Sonal","Sonali","Sonia","Srija","Srishti","Sudha","Sujata",
    "Sukanya","Suma","Sunaina","Sunita","Suparna","Surbhi","Surekha","Sushma","Swara","Swati",
    "Tanisha","Tanya","Tara","Trisha","Tulsi","Uma","Urvashi","Vaishali","Vandana","Vanshika",
    "Varsha","Vasundhara","Vidya","Vijaya","Vimala","Vinita","Yamini","Yashoda","Zara","Zoya",
    "Asmita","Bhargavi","Chaitra","Darshana","Falguni","Gargi","Hemangini","Indira","Janaki","Kalindi",
    "Lilavati","Madhuri","Nandita","Oviya","Padmini","Qamar","Ragini","Sahana","Tanvi","Urmi",
    "Veena","Wamika","Yamuna","Zubeida","Ahalya","Bhumika","Chandni","Damini","Elina","Fatima",
    "Ganga","Harsha","Ilina","Jagriti","Kalpana","Laxmi","Manvi","Navya","Ojasvi","Parul"
]

# ─── Indian Last Names (150+) ───
last_names = [
    "Sharma","Verma","Gupta","Singh","Patel","Kumar","Devi","Yadav","Reddy","Nair",
    "Iyer","Rao","Das","Bose","Sen","Roy","Chatterjee","Mukherjee","Banerjee","Ghosh",
    "Mehta","Shah","Joshi","Thakur","Chauhan","Pandey","Mishra","Tiwari","Shukla","Dubey",
    "Saxena","Agarwal","Jain","Pillai","Menon","Kaur","Gill","Bajwa","Dhillon","Sandhu",
    "Sinha","Prasad","Rathore","Rajput","Solanki","Pawar","Jadhav","Patil","More","Deshmukh",
    "Kulkarni","Deshpande","Hegde","Shetty","Bhat","Nayak","Gowda","Chand","Rawat","Bisht",
    "Bhatt","Pant","Dimri","Nautiyal","Munda","Hembrom","Oraon","Lakra","Kujur","Tirkey",
    "Topno","Xalxo","Ekka","Minj","Barla","Besra","Soren","Hansda","Murmu","Kisku",
    "Tudu","Marandi","Mahato","Lohra","Gorai","Bauri","Bagdi","Patra","Behera","Sahoo",
    "Mohanty","Swain","Dalei","Nayak","Rout","Parida","Sethy","Maharana","Sahu","Lenka",
    "Bhadra","Bhagora","Dalabehera","Pisda","Panghal","Phogat","Malik","Sheoran","Punia","Dahiya",
    "Kumari","Dey","Barman","Sarkar","Mandal","Halder","Biswas","Mondal","Majumdar","Chakraborty",
    "Bari","Sethi","Mehra","Arora","Kapoor","Malhotra","Khurana","Grover","Batra","Anand",
    "Chawla","Kohli","Khanna","Suri","Luthra","Vohra","Chopra","Tandon","Sachdeva","Dhawan",
    "Bajaj","Garg","Mittal","Bansal","Goyal","Jindal","Singhal","Oswal","Lohia","Birla"
]

# ─── Sports with weight categories / events ───
sports_data = {
    "Wrestling": {"events": ["50 Kg", "53 Kg", "55 Kg", "57 Kg", "59 Kg", "62 Kg", "65 Kg", "68 Kg", "72 Kg", "76 Kg"], "type": "combat"},
    "Boxing": {"events": ["48 Kg", "50 Kg", "52 Kg", "54 Kg", "57 Kg", "60 Kg", "63 Kg", "66 Kg", "69 Kg", "75 Kg"], "type": "combat"},
    "Weightlifting": {"events": ["45 Kg", "49 Kg", "55 Kg", "59 Kg", "64 Kg", "71 Kg", "76 Kg", "81 Kg", "87 Kg", "+87 Kg"], "type": "strength"},
    "Judo": {"events": ["48 Kg", "52 Kg", "57 Kg", "63 Kg", "70 Kg", "78 Kg", "+78 Kg"], "type": "combat"},
    "Athletics (Sprint)": {"events": ["100m", "200m", "400m", "4x100m Relay", "4x400m Relay"], "type": "track"},
    "Athletics (Middle Distance)": {"events": ["800m", "1500m", "3000m Steeplechase"], "type": "track"},
    "Athletics (Long Distance)": {"events": ["5000m", "10000m", "Marathon", "Half Marathon", "Race Walk 20km"], "type": "track"},
    "Athletics (Field)": {"events": ["Long Jump", "High Jump", "Triple Jump", "Shot Put", "Discus Throw", "Javelin Throw", "Hammer Throw", "Pole Vault", "Heptathlon"], "type": "field"},
    "Swimming": {"events": ["50m Freestyle", "100m Freestyle", "200m Freestyle", "400m Freestyle", "100m Backstroke", "200m Backstroke", "100m Breaststroke", "200m Butterfly", "200m IM", "400m IM"], "type": "aquatic"},
    "Archery": {"events": ["Recurve Individual", "Recurve Team", "Compound Individual", "Compound Team", "Compound Mixed"], "type": "precision"},
    "Shooting": {"events": ["10m Air Rifle", "50m Rifle 3 Positions", "10m Air Pistol", "25m Pistol", "Trap", "Skeet"], "type": "precision"},
    "Badminton": {"events": ["Women's Singles", "Women's Doubles", "Mixed Doubles"], "type": "racquet"},
    "Tennis": {"events": ["Women's Singles", "Women's Doubles", "Mixed Doubles"], "type": "racquet"},
    "Table Tennis": {"events": ["Women's Singles", "Women's Doubles", "Mixed Doubles", "Team Event"], "type": "racquet"},
    "Hockey": {"events": ["Forward", "Midfielder", "Defender", "Goalkeeper"], "type": "team"},
    "Football": {"events": ["Forward", "Midfielder", "Defender", "Goalkeeper"], "type": "team"},
    "Volleyball": {"events": ["Setter", "Libero", "Outside Hitter", "Middle Blocker", "Opposite Hitter"], "type": "team"},
    "Kabaddi": {"events": ["Raider", "Defender", "All-rounder"], "type": "team"},
    "Kho-Kho": {"events": ["Chaser", "Runner", "All-rounder"], "type": "team"},
    "Cricket": {"events": ["Batter", "Bowler", "All-rounder", "Wicketkeeper"], "type": "team"},
    "Gymnastics": {"events": ["Artistic - Floor", "Artistic - Vault", "Artistic - Beam", "Artistic - Uneven Bars", "Rhythmic", "Trampoline"], "type": "artistic"},
    "Cycling": {"events": ["Road Race", "Track Sprint", "Track Pursuit", "Mountain Bike", "Time Trial"], "type": "endurance"},
    "Rowing": {"events": ["Single Sculls", "Double Sculls", "Quadruple Sculls", "Coxless Pair", "Eight"], "type": "endurance"},
    "Fencing": {"events": ["Foil Individual", "Épée Individual", "Sabre Individual", "Team Foil"], "type": "combat"},
    "Taekwondo": {"events": ["49 Kg", "57 Kg", "67 Kg", "+67 Kg"], "type": "combat"},
    "Wushu": {"events": ["Sanda 52 Kg", "Sanda 56 Kg", "Sanda 60 Kg", "Taolu Changquan", "Taolu Nanquan"], "type": "combat"},
    "Squash": {"events": ["Women's Singles", "Women's Doubles", "Mixed Doubles"], "type": "racquet"},
    "Sailing": {"events": ["Laser Radial", "49er FX", "RS:X Windsurfing"], "type": "aquatic"},
    "Equestrian": {"events": ["Dressage", "Show Jumping", "Eventing"], "type": "outdoor"},
    "Golf": {"events": ["Individual Stroke Play", "Team Event"], "type": "outdoor"},
}

# ─── States with cities ───
states_cities = {
    "Andhra Pradesh": ["Hyderabad", "Visakhapatnam", "Vijayawada", "Guntur", "Tirupati", "Nellore", "Rajahmundry"],
    "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat", "Tawang", "Ziro"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Nagaon", "Tezpur"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga", "Purnia"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur", "Korba", "Durg", "Rajnandgaon"],
    "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Bhavnagar", "Jamnagar"],
    "Haryana": ["Chandigarh", "Faridabad", "Gurgaon", "Panipat", "Ambala", "Karnal", "Hisar", "Rohtak", "Sonipat", "Bhiwani"],
    "Himachal Pradesh": ["Shimla", "Dharamshala", "Mandi", "Solan", "Kullu", "Una"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Deoghar", "Hazaribagh"],
    "Karnataka": ["Bengaluru", "Mysuru", "Mangaluru", "Hubli", "Belgaum", "Gulbarga", "Davangere"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kannur", "Kollam", "Palakkad"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain", "Sagar"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Kolhapur", "Solapur", "Thane"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur", "Churachandpur"],
    "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongstoin"],
    "Mizoram": ["Aizawl", "Lunglei", "Champhai", "Serchhip"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur", "Puri"],
    "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Mohali"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Ajmer", "Bikaner", "Alwar"],
    "Sikkim": ["Gangtok", "Namchi", "Gyalshing", "Mangan"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli", "Erode"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailashahar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Allahabad", "Meerut", "Noida", "Ghaziabad", "Bareilly"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Rishikesh", "Nainital", "Haldwani", "Roorkee"],
    "West Bengal": ["Kolkata", "Howrah", "Siliguri", "Durgapur", "Asansol", "Kharagpur"],
    "Delhi": ["New Delhi", "Dwarka", "Rohini", "Shahdara", "Saket"],
    "Jammu & Kashmir": ["Srinagar", "Jammu", "Anantnag", "Baramulla", "Udhampur"],
    "Ladakh": ["Leh", "Kargil"],
    "Chandigarh": ["Chandigarh"],
    "Puducherry": ["Puducherry", "Karaikal"],
}

# ─── Performance levels & tiers ───
performance_levels = ["District", "State", "National", "International"]
perf_weights = [15, 35, 35, 15]
tiers = {"District": "Grassroots", "State": "Development", "National": "Senior", "International": "Elite"}
statuses = {
    "District": ["Emerging", "Identified Talent", "Academy Trainee"],
    "State": ["Emerging", "Rising Athlete", "State Champion", "Development Squad"],
    "National": ["Rising Athlete", "National Contender", "Senior National Medalist", "Established National Athlete", "TOPS Development"],
    "International": ["Rising International Athlete", "Established International Athlete", "Olympic Prospect", "World Championship Medalist", "Asian Games Medalist", "TOPS Core"]
}
funding_options = {
    "District": ["Self-funded", "Local Club Sponsorship", "District Sports Authority"],
    "State": ["State Scholarship", "State Sports Authority", "Khelo India Scholarship", "Academy Scholarship"],
    "National": ["Khelo India Scholarship", "SAI Scholarship", "State + SAI Support", "TOPS Development Group", "Corporate Sponsorship"],
    "International": ["TOPS Scheme", "TOPS Scheme + SAI", "SAI Scholarship", "Olympic Gold Quest", "JSW Sports", "Reliance Foundation", "Adani Sportsline", "GoSports Foundation"]
}

# ─── Achievement templates ───
def gen_achievements(sport_name, perf_level, event):
    if perf_level == "International":
        templates = [
            f"Gold medal at Asian Youth {sport_name} Championship in {event}",
            f"Silver medal at World Junior {sport_name} Championship",
            f"Bronze at Asian Games in {event}",
            f"Represented India at World {sport_name} Championship",
            f"Gold at South Asian Games, {event}",
            f"Commonwealth Games participant in {event}",
            f"Asian Championship medalist in {sport_name}",
            f"World University Games Gold in {event}",
            f"Olympic qualifier in {event}",
            f"World ranking top-50 in {sport_name} {event}",
        ]
    elif perf_level == "National":
        templates = [
            f"Gold at Khelo India Youth Games in {event}",
            f"Senior National Championship medalist in {sport_name}",
            f"Gold at Junior National {sport_name} Championship",
            f"Silver at Senior Nationals in {event}",
            f"National record holder in {event}",
            f"Khelo India Tribal Games standout in {sport_name}",
            f"National School Games champion in {event}",
            f"All India Inter-University Gold in {sport_name}",
            f"Federation Cup medalist in {event}",
            f"National Open champion in {sport_name} {event}",
        ]
    elif perf_level == "State":
        templates = [
            f"State championship Gold in {sport_name} {event}",
            f"State-level champion in {event}",
            f"Selected for state team in {sport_name}",
            f"State junior championship medalist",
            f"District champion, state finalist in {event}",
            f"State School Games Gold in {sport_name}",
            f"State youth champion in {event}",
            f"Multiple state medals in {sport_name}",
        ]
    else:
        templates = [
            f"District champion in {sport_name}",
            f"Block-level winner in {event}",
            f"Identified at grassroots talent hunt for {sport_name}",
            f"School-level champion in {event}",
            f"Emerging talent in {sport_name} at district level",
        ]
    return random.choice(templates)

def gen_highlight(sport_name, perf_level, state):
    if perf_level == "International":
        h = [
            f"India's top prospect in {sport_name}",
            f"2028 LA Olympics medal contender",
            f"World-class talent from {state}",
            f"India's rising star in {sport_name}",
            f"International medalist & Olympic hopeful",
        ]
    elif perf_level == "National":
        h = [
            f"National champion in {sport_name}",
            f"{state}'s premier {sport_name} talent",
            f"Khelo India star in {sport_name}",
            f"Future international prospect from {state}",
            f"National medalist with Olympic potential",
        ]
    elif perf_level == "State":
        h = [
            f"{state}'s rising {sport_name} talent",
            f"State champion with national ambitions",
            f"Promising {sport_name} athlete from {state}",
            f"State-level medalist aiming for nationals",
        ]
    else:
        h = [
            f"Grassroots talent from {state}",
            f"Emerging {sport_name} talent at district level",
            f"Identified in talent scouting program",
            f"Rising star from {state} grassroots",
        ]
    return random.choice(h)

def gen_remarks(name, sport_name, perf_level, state, event):
    if perf_level == "International":
        r = [
            f"{name} is an internationally competitive {sport_name} athlete from {state}, specializing in {event}. Already representing India at major championships with strong medal prospects for upcoming Asian and Olympic Games.",
            f"One of India's most promising women in {sport_name}. {name} from {state} has shown exceptional form in {event} at international competitions and is on the TOPS radar for 2028 LA Olympics.",
            f"Elite {sport_name} athlete from {state}. {name} has medaled at continental-level competitions in {event} and is being groomed for Olympic glory.",
        ]
    elif perf_level == "National":
        r = [
            f"{name} from {state} is a national-level {sport_name} athlete competing in {event}. Has shown consistent improvement and is earmarked for international exposure.",
            f"Strong national contender in {sport_name} from {state}. {name} has won medals at Khelo India and national championships in {event}.",
            f"Rising {sport_name} talent from {state}. {name} excels in {event} and has been identified for fast-tracking to international competitions.",
        ]
    elif perf_level == "State":
        r = [
            f"{name} is a state-level {sport_name} athlete from {state}, competing in {event}. Shows promise for national-level competition with continued training.",
            f"Talented {sport_name} athlete from {state}. {name} has won multiple state-level medals in {event} and is training for national championships.",
        ]
    else:
        r = [
            f"{name} from {state} was identified through grassroots talent scouting in {sport_name}. Shows raw potential in {event} at district competitions.",
            f"Emerging {sport_name} talent from {state}. {name} has won at block and district level in {event} and is being nurtured through academy programs.",
        ]
    return random.choice(r)

# ─── Generate 5000 athletes ───
athletes = []
used_names = set()
sport_names = list(sports_data.keys())

for i in range(5000):
    # Generate unique name
    while True:
        fn = random.choice(first_names)
        ln = random.choice(last_names)
        full_name = f"{fn} {ln}"
        if full_name not in used_names:
            used_names.add(full_name)
            break
    
    sport = random.choice(sport_names)
    sport_info = sports_data[sport]
    event = random.choice(sport_info["events"])
    state = random.choice(list(states_cities.keys()))
    city = random.choice(states_cities[state])
    
    perf_level = random.choices(performance_levels, weights=perf_weights, k=1)[0]
    tier = tiers[perf_level]
    status = random.choice(statuses[perf_level])
    funding = random.choice(funding_options[perf_level])
    
    # Age: International athletes tend older, District younger
    age_ranges = {"District": (13, 19), "State": (14, 23), "National": (16, 28), "International": (18, 32)}
    age_min, age_max = age_ranges[perf_level]
    age = random.randint(age_min, age_max)
    
    # Opportunity score: higher for international
    score_ranges = {"District": (4.0, 7.0), "State": (5.5, 7.8), "National": (6.5, 8.8), "International": (7.5, 9.8)}
    s_min, s_max = score_ranges[perf_level]
    score = round(random.uniform(s_min, s_max), 1)
    
    achievements = gen_achievements(sport, perf_level, event)
    highlight = gen_highlight(sport, perf_level, state)
    remarks = gen_remarks(full_name, sport, perf_level, state, event)
    
    athletes.append({
        "name": full_name,
        "sport": sport,
        "event": event,
        "state": state,
        "city": city,
        "age": age,
        "gender": "Female",
        "status": status,
        "tier": tier,
        "performance_level": perf_level,
        "funding_status": funding,
        "athletiq_opportunity_score": score,
        "achievements": achievements,
        "highlight": highlight,
        "remarks": remarks
    })

# Save to JSON
out_path = os.path.join(os.path.dirname(__file__), "..", "data", "women_athletes.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(athletes, f, indent=2, ensure_ascii=False)

print(f"Generated {len(athletes)} women athletes → {os.path.abspath(out_path)}")
print(f"Sports covered: {len(set(a['sport'] for a in athletes))}")
print(f"States covered: {len(set(a['state'] for a in athletes))}")
print(f"Unique names: {len(set(a['name'] for a in athletes))}")
