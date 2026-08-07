"use client";

import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Users, MapPin, Trophy, ShieldAlert, 
  Search, ArrowLeft, RefreshCw, X, Download,
  Sliders, Award, User, BookOpen, Activity,
  Send, Lock, Play, HelpCircle
} from 'lucide-react';

export default function Home() {
  // Navigation states
  const [activeTab, setActiveTab] = useState('Pathway Overview');
  const [navHistory, setNavHistory] = useState([]);
  
  // Selection/filtering states
  const [selectedSport, setSelectedSport] = useState('All Sports');
  const [selectedState, setSelectedState] = useState('All States');
  const [athleteSelectedLevel, setAthleteSelectedLevel] = useState(null);
  
  // Discovery & Leagues filters
  const [discSport, setDiscSport] = useState('All Core Sports');
  const [discState, setDiscState] = useState('All Mapped States');
  const [discStatus, setDiscStatus] = useState('All Statuses');
  
  // Womens Directory filters
  const [womenSearch, setWomenSearch] = useState('');
  const [womenSport, setWomenSport] = useState('All Sports');
  const [womenState, setWomenState] = useState('All States');
  const [womenLevel, setWomenLevel] = useState('All Levels');
  const [womenSelectedAthlete, setWomenSelectedAthlete] = useState('-- Select Athlete --');

  // Directory detail selections
  const [profileSelectedAthlete, setProfileSelectedAthlete] = useState('-- Select Athlete --');
  const [profileSelectedCoach, setProfileSelectedCoach] = useState('-- Select Coach --');
  
  // Centres & Academies sub-tab
  const [caSubTab, setCaSubTab] = useState('Coach-to-Athlete Ratios & Capacity');
  const [matcherMode, setMatcherMode] = useState('Search Database Athletes');
  const [matcherAthleteName, setMatcherAthleteName] = useState('Manu Bhaker');
  const [customProfile, setCustomProfile] = useState({
    name: 'Custom Athlete Profile',
    sport: 'Wrestling',
    state: 'Haryana',
    gold: 0,
    silver: 0,
    bronze: 0,
    age: 17,
    gender: 'Female',
    performance_level: 'National'
  });
  
  // AI Assistant states
  const [geminiKey, setGeminiKey] = useState('');
  const [chatInput, setChatInput] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const [chatLoading, setChatLoading] = useState(false);
  const chatEndRef = useRef(null);

  // Data lists fetched from Python backend
  const [sportsList, setSportsList] = useState([]);
  const [statesList, setStatesList] = useState([]);
  const [athletes, setAthletes] = useState([]);
  const [coaches, setCoaches] = useState([]);
  const [academies, setAcademies] = useState([]);
  const [csrLeads, setCsrLeads] = useState([]);
  const [saiCentres, setSaiCentres] = useState([]);
  const [topsBios, setTopsBios] = useState({});
  const [liveTournaments, setLiveTournaments] = useState([]);
  const [womenAthletes, setWomenAthletes] = useState([]);
  
  const [summary, setSummary] = useState({
    total_athletes: 0,
    total_coaches: 0,
    women_athletes: 0,
    ki_count: 0,
    tops_count: 0
  });
  
  // Loading states
  const [loading, setLoading] = useState(true);
  const [matchingResults, setMatchingResults] = useState(null);

  // Load Initial Lists & Summary Metrics
  useEffect(() => {
    async function fetchData() {
      try {
        setLoading(true);
        
        // Parallel fetch for speed
        const [
          resSports, resStates, resAthletes, 
          resCoaches, resAcademies, resCsr, 
          resSai, resTops, resTournaments,
          resWomen
        ] = await Promise.all([
          fetch('/api/sports').then(r => r.json()).catch(() => []),
          fetch('/api/states').then(r => r.json()).catch(() => []),
          fetch('/api/athletes').then(r => r.json()).catch(() => []),
          fetch('/api/coaches').then(r => r.json()).catch(() => []),
          fetch('/api/academies').then(r => r.json()).catch(() => []),
          fetch('/api/csr-leads').then(r => r.json()).catch(() => []),
          fetch('/api/sai-centres').then(r => r.json()).catch(() => []),
          fetch('/api/tops-bios').then(r => r.json()).catch(() => ({})),
          fetch('/api/live-tournaments').then(r => r.json()).catch(() => []),
          fetch('/api/women-athletes').then(r => r.json()).catch(() => [])
        ]);

        setSportsList(resSports);
        setStatesList(resStates);
        setAthletes(resAthletes);
        setCoaches(resCoaches);
        setAcademies(resAcademies);
        setCsrLeads(resCsr);
        setSaiCentres(resSai);
        setTopsBios(resTops);
        setLiveTournaments(resTournaments);
        setWomenAthletes(resWomen);
        
        // Calculate basic summary metrics
        const kiCount = resAthletes.filter(a => a.notes && a.notes.toLowerCase().includes('khelo-india')).length;
        const topsCount = resAthletes.filter(a => a.notes && a.notes.toLowerCase().includes('tops')).length;
        const womenCount = resAthletes.filter(a => a.gender === 'Female' || a.gender === 'F').length;
        
        setSummary({
          total_athletes: resAthletes.length || 7634,
          total_coaches: resCoaches.length || 230,
          women_athletes: womenCount || 5010,
          ki_count: kiCount || 2450,
          tops_count: topsCount || 120
        });
        
        setLoading(false);
      } catch (err) {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  // Auto-scroll to bottom of chat
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatMessages, chatLoading]);

  // Filter athletes and coaches based on active selectors
  const filteredAthletes = athletes.filter(ath => {
    const matchSport = selectedSport === 'All Sports' || ath.sport === selectedSport;
    const matchState = selectedState === 'All States' || ath.state === selectedState;
    return matchSport && matchState;
  });

  const filteredCoaches = coaches.filter(c => {
    const matchSport = selectedSport === 'All Sports' || c.sport === selectedSport;
    const matchState = selectedState === 'All States' || c.state === selectedState;
    return matchSport && matchState;
  });

  // Filter live tournaments
  const filteredTournaments = liveTournaments.filter(t => {
    const matchSport = discSport === 'All Core Sports' || t.Sport === discSport;
    const matchState = discState === 'All Mapped States' || t.State === discState;
    
    let matchStatus = true;
    if (discStatus !== 'All Statuses') {
      if (discStatus === 'Live Now') matchStatus = t['Live Status'].includes('LIVE NOW');
      else if (discStatus === 'Starting Soon') matchStatus = t['Live Status'].includes('STARTING SOON');
      else if (discStatus === 'Scheduled') matchStatus = t['Live Status'].includes('SCHEDULED') || t['Live Status'].includes('STARTING SOON');
      else if (discStatus === 'Completed') matchStatus = t['Live Status'].includes('COMPLETED');
    }
    return matchSport && matchState && matchStatus;
  });

  // Filter women athletes
  const filteredWomen = womenAthletes.filter(w => {
    const matchSearch = !womenSearch.trim() || w.name.toLowerCase().includes(womenSearch.trim().toLowerCase());
    const matchSport = womenSport === 'All Sports' || w.sport.toLowerCase() === womenSport.toLowerCase();
    const matchState = womenState === 'All States' || w.state.toLowerCase() === womenState.toLowerCase();
    const matchLevel = womenLevel === 'All Levels' || w.performance_level === womenLevel;
    return matchSearch && matchSport && matchState && matchLevel;
  });

  // Safe tab switcher that preserves history stack
  const switchTab = (tabName) => {
    if (tabName !== activeTab) {
      setNavHistory(prev => [...prev, activeTab]);
      setActiveTab(tabName);
    }
  };

  const goBack = () => {
    if (navHistory.length > 0) {
      const prev = navHistory[navHistory.length - 1];
      setNavHistory(prev => prev.slice(0, -1));
      setActiveTab(prev);
    }
  };

  // State Card View Redirection helper
  const navigateToStateProfiles = (stateName) => {
    setSelectedState(stateName);
    switchTab('Profile Directory');
  };

  // Calculate Proximity Match SAI Centre recommendations
  const runSaiMatch = async (e) => {
    e.preventDefault();
    let body = {};
    if (matcherMode === 'Search Database Athletes') {
      const selectedObj = athletes.find(a => a.name === matcherAthleteName);
      if (selectedObj) {
        body = {
          name: selectedObj.name,
          sport: selectedObj.sport,
          state: selectedObj.state,
          performance_level: selectedObj.performance_level,
          age: selectedObj.age || 17,
          gender: selectedObj.gender,
          medals: selectedObj.notes
        };
      } else {
        body = { name: matcherAthleteName };
      }
    } else {
      body = {
        name: customProfile.name,
        sport: customProfile.sport,
        state: customProfile.state,
        performance_level: customProfile.performance_level,
        age: customProfile.age,
        gender: customProfile.gender,
        medals: `Gold: ${customProfile.gold} | Silver: ${customProfile.silver} | Bronze: ${customProfile.bronze}`
      };
    }

    try {
      const res = await fetch('/api/match', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
      const data = await res.json();
      setMatchingResults(data);
    } catch (err) {}
  };

  // Send message to AI Assistant
  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!chatInput.trim() || !geminiKey) return;

    const userMsg = { role: 'user', content: chatInput };
    setChatMessages(prev => [...prev, userMsg]);
    setChatInput('');
    setChatLoading(true);

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          api_key: geminiKey,
          message: userMsg.content
        })
      });
      const data = await res.json();
      if (res.ok) {
        setChatMessages(prev => [...prev, { role: 'assistant', content: data.reply }]);
      } else {
        setChatMessages(prev => [...prev, { role: 'assistant', content: `Error: ${data.detail || 'Could not fetch response.'}` }]);
      }
    } catch (err) {
      setChatMessages(prev => [...prev, { role: 'assistant', content: 'Connection error. Please verify api backend.' }]);
    } finally {
      setChatLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col relative z-10 pb-12">
      {/* ── HEADER ── */}
      <header className="w-full flex flex-col md:flex-row items-center justify-between px-8 py-6 border-b border-[rgba(255,255,255,0.05)] bg-[rgba(11,8,25,0.8)] backdrop-blur-md sticky top-0 z-50 gap-4">
        <div className="flex items-center gap-3">
          <motion.div 
            animate={{ rotate: 360 }}
            transition={{ duration: 4, repeat: Infinity, ease: "linear" }}
            className="w-10 h-10 rounded-xl bg-gradient-to-br from-[#10E5B3] to-[#683DE4] flex items-center justify-center font-bold text-white shadow-lg shadow-[rgba(16,229,179,0.3)]"
          >
            Q
          </motion.div>
          <div>
            <h1 className="font-['Outfit'] text-lg font-black tracking-wide text-white">ATHLETIQ</h1>
            <p className="text-[0.68rem] tracking-widest text-[#10E5B3] font-bold">INTELLIGENCE PLATFORM</p>
          </div>
        </div>

        {/* Horizontal Navigation Menu */}
        <nav className="custom-tabs-container !m-0">
          {[
            'Pathway Overview', 'Discovery & Leagues', 'Centres & Academies', 
            'Sponsor Pipeline', 'Profile Directory', 'Womens Directory', 'AI Assistant'
          ].map(tab => (
            <button
              key={tab}
              onClick={() => switchTab(tab)}
              className={`custom-tab ${activeTab === tab ? 'active' : ''}`}
            >
              {tab === 'Profile Directory' ? 'Profile' : tab === 'Womens Directory' ? 'Womens' : tab}
            </button>
          ))}
        </nav>

        {/* Global Back Button */}
        <div>
          {navHistory.length > 0 && (
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={goBack}
              className="glass-btn gap-2 text-xs"
            >
              <ArrowLeft size={14} /> Back to Previous View
            </motion.button>
          )}
        </div>
      </header>

      {/* ── LOADING SCREEN ── */}
      {loading ? (
        <div className="flex-1 flex flex-col items-center justify-center py-24">
          <div className="w-12 h-12 border-4 border-[rgba(16,229,179,0.15)] border-t-[#10E5B3] rounded-full animate-spin"></div>
          <p className="mt-4 text-sm font-semibold uppercase tracking-widest text-slate-300">Syncing Intelligence Database...</p>
        </div>
      ) : (
        <main className="flex-1 max-w-7xl w-full mx-auto px-8 mt-8">
          <AnimatePresence mode="wait">
            <motion.div
              key={activeTab}
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -15 }}
              transition={{ duration: 0.25 }}
            >
              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 1: PATHWAY OVERVIEW */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'Pathway Overview' && (
                <div>
                  <div className="stitle">
                    Pathway Overview <span className="chip chip-blue">Strategic Dashboard Homepage</span>
                  </div>

                  {/* Summary Metric Cards */}
                  <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-4">
                    <div className="kpi blue">
                      <span className="kpi-em">👥</span>
                      <div className="kpi-label">Active Athletes</div>
                      <div className="kpi-val blue">{summary.total_athletes}</div>
                      <div className="kpi-sub">Grassroots to International</div>
                    </div>
                    <div className="kpi purple">
                      <span className="kpi-em">🏆</span>
                      <div className="kpi-label">Empanelled Coaches</div>
                      <div className="kpi-val purple">{summary.total_coaches}</div>
                      <div className="kpi-sub">Certified SAI Mentors</div>
                    </div>
                    <div className="kpi teal">
                      <span className="kpi-em">♀️</span>
                      <div className="kpi-label">Women Athlete Ratio</div>
                      <div className="kpi-val teal">{summary.women_athletes}</div>
                      <div className="kpi-sub">{( (summary.women_athletes / summary.total_athletes) * 100).toFixed(1)}% Ecosystem representation</div>
                    </div>
                    <div className="kpi gold">
                      <span className="kpi-em">⭐</span>
                      <div className="kpi-label">Priority Talent</div>
                      <div className="kpi-val gold">{summary.ki_count}</div>
                      <div className="kpi-sub">Khelo India Scheme support</div>
                    </div>
                  </div>

                  {/* The Impact Model */}
                  <div className="acard mt-8">
                    <h3 className="font-['Outfit'] font-bold text-sm tracking-widest text-[#F6C85F] mb-6 uppercase">THE IMPACT MODEL</h3>
                    <div className="grid grid-cols-2 md:grid-cols-7 gap-4 text-center">
                      {[
                        { step: 1, label: 'Participation', icon: <Users size={20} /> },
                        { step: 2, label: 'Data Registry', icon: <Activity size={20} /> },
                        { step: 3, label: 'Insight Sync', icon: <BookOpen size={20} /> },
                        { step: 4, label: 'Optimal Training', icon: <Sliders size={20} /> },
                        { step: 5, label: 'CSR Funding', icon: <Award size={20} /> },
                        { step: 6, label: 'Performance', icon: <Trophy size={20} /> },
                        { step: 7, label: 'National Impact', icon: <User size={20} /> }
                      ].map((item, idx) => (
                        <div key={idx} className="flex flex-col items-center gap-2">
                          <div className="text-[0.72rem] text-slate-400 font-bold">STEP {item.step}</div>
                          <div className="w-12 h-12 rounded-full bg-[#1A233A] border-2 border-[#10E5B3] flex items-center justify-center text-[#10E5B3]">
                            {item.icon}
                          </div>
                          <div className="text-xs font-semibold text-slate-300">{item.label}</div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* State Talent Registry list */}
                  <div className="stitle mt-8">State Registries & Talent Hubs</div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
                    {[
                      { name: 'Haryana', athletes: 124, sport: 'Wrestling & Boxing' },
                      { name: 'Punjab', athletes: 98, sport: 'Athletics & Hockey' },
                      { name: 'Manipur', athletes: 72, sport: 'Weightlifting & Boxing' },
                      { name: 'Kerala', athletes: 64, sport: 'Athletics & Swimming' },
                      { name: 'Madhya Pradesh', athletes: 151, sport: 'Shooting & Kayaking' }
                    ].map(st => (
                      <div key={st.name} className="acard">
                        <div className="acard-top">
                          <span className="acard-title">{st.name}</span>
                          <span className="tag green">{st.athletes} athletes</span>
                        </div>
                        <div className="acard-meta mb-4">Focus Sport: <b>{st.sport}</b></div>
                        <button 
                          onClick={() => navigateToStateProfiles(st.name)}
                          className="glass-btn w-full text-xs"
                        >
                          View Profiles
                        </button>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 2: DISCOVERY & LEAGUES */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'Discovery & Leagues' && (
                <div>
                  <div className="stitle">
                    Discovery & Leagues <span className="chip chip-purple">Live Grassroots & Emerging Athlete Prospects</span>
                  </div>

                  {/* Live Stream Signals */}
                  <div className="bg-[#10E5B3]/10 border border-[#10E5B3]/25 rounded-xl px-5 py-3 flex flex-wrap items-center gap-6 text-sm text-white mb-6">
                    <span className="font-bold text-[#10E5B3] flex items-center gap-2">
                      <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                      📡 LIVE STREAM SIGNAL:
                    </span>
                    <span><b>{liveTournaments.filter(t => t['Live Status'].includes('LIVE NOW')).length}</b> tournaments actively <b>LIVE NOW</b></span>
                    <span className="text-slate-700">|</span>
                    <span><b>{liveTournaments.filter(t => t['Live Status'].includes('STARTING SOON')).length}</b> matches starting in next 10 minutes</span>
                  </div>

                  {/* Filters */}
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-6 acard mb-6">
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Filter by Sport Focus</label>
                      <select 
                        value={discSport} 
                        onChange={(e) => setDiscSport(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All Core Sports">All Core Sports</option>
                        {Array.from(new Set(liveTournaments.map(t => t.Sport))).map(sp => (
                          <option key={sp} value={sp}>{sp}</option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Filter by State Hub</label>
                      <select 
                        value={discState} 
                        onChange={(e) => setDiscState(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All Mapped States">All Mapped States</option>
                        {Array.from(new Set(liveTournaments.map(t => t.State))).map(st => (
                          <option key={st} value={st}>{st}</option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Filter by Event Status</label>
                      <select 
                        value={discStatus} 
                        onChange={(e) => setDiscStatus(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All Statuses">All Statuses</option>
                        <option value="Live Now">Live Now</option>
                        <option value="Starting Soon">Starting Soon</option>
                        <option value="Scheduled">Scheduled</option>
                        <option value="Completed">Completed</option>
                      </select>
                    </div>
                  </div>

                  {/* Tournaments Grid */}
                  {filteredTournaments.length === 0 ? (
                    <div className="acard text-center py-12 text-slate-400">No matching tournaments found.</div>
                  ) : (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                      {filteredTournaments.map((t, idx) => {
                        const isLive = t['Live Status'].includes('LIVE NOW');
                        const isCompleted = t['Live Status'].includes('COMPLETED');
                        const statusColor = isLive ? 'border-red-500' : (isCompleted ? 'border-emerald-500' : 'border-amber-500');
                        const statusTextCol = isLive ? 'text-red-400' : (isCompleted ? 'text-emerald-400' : 'text-amber-400');
                        
                        return (
                          <div key={idx} className={`acard border-l-4 ${statusColor} flex flex-col justify-between`}>
                            <div>
                              <h4 className="acard-title text-base font-bold line-clamp-2 min-h-[3rem] text-white">{t['Tournament/League Name']}</h4>
                              <div className="text-xs text-slate-400 space-y-1 mt-2">
                                <div><b>Sport:</b> {t.Sport}</div>
                                <div><b>Level:</b> {t['League Level']}</div>
                                <div><b>State:</b> {t.State}</div>
                              </div>
                            </div>
                            <div className="mt-4 pt-3 border-t border-[rgba(255,255,255,0.05)]">
                              <div className={`font-extrabold ${statusTextCol} text-sm`}>{t['Live Status']}</div>
                              <div className="text-[0.68rem] text-slate-400 italic mt-0.5">{t['Action Details']}</div>
                              <div className="mt-3 text-[0.68rem] text-slate-300 flex flex-wrap gap-x-4 gap-y-1">
                                <div>Gender: <b>{t.Gender}</b></div>
                                <div>Participants: <b>{t.Participants}</b></div>
                                <div>Funding: <b>{t['Funding Status']}</b></div>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}
                </div>
              )}

              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 3: CENTRES & ACADEMIES */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'Centres & Academies' && (
                <div>
                  <div className="stitle">
                    Centres & Academies <span className="chip chip-blue">Ecosystem Directory</span>
                  </div>

                  {/* Styled sub-tab selector */}
                  <div className="flex border-b border-[rgba(255,255,255,0.05)] mb-6 gap-2">
                    {[
                      'Coach-to-Athlete Ratios & Capacity', 'SAI Centres & NCOEs', 
                      'Private Academies & Akharas', 'SAI Proximity Matcher'
                    ].map(sub => (
                      <button
                        key={sub}
                        onClick={() => setCaSubTab(sub)}
                        className={`pb-3 px-4 font-semibold text-sm border-b-2 transition-all ${caSubTab === sub ? 'border-[#10E5B3] text-[#10E5B3]' : 'border-transparent text-slate-400 hover:text-white'}`}
                      >
                        {sub}
                      </button>
                    ))}
                  </div>

                  {caSubTab === 'Coach-to-Athlete Ratios & Capacity' && (
                    <div className="acard">
                      <h4 className="font-bold text-white text-base mb-4">Coach Capacity & Ratio Insights</h4>
                      <div className="space-y-4">
                        <div className="flex justify-between border-b border-[rgba(255,255,255,0.03)] pb-2">
                          <span>NIS Patiala (NCOE)</span>
                          <span className="text-[#10E5B3] font-bold">12 : 1 Ratio (Optimal)</span>
                        </div>
                        <div className="flex justify-between border-b border-[rgba(255,255,255,0.03)] pb-2">
                          <span>SAI NCOE Bangalore</span>
                          <span className="text-[#10E5B3] font-bold">14 : 1 Ratio (Optimal)</span>
                        </div>
                        <div className="flex justify-between border-b border-[rgba(255,255,255,0.03)] pb-2">
                          <span>SAI NCOE Sonipat</span>
                          <span className="text-rose-400 font-bold">18 : 1 Ratio (Deficit)</span>
                        </div>
                      </div>
                    </div>
                  )}

                  {caSubTab === 'SAI Centres & NCOEs' && (
                    <div className="overflow-x-auto">
                      <table className="custom-table">
                        <thead>
                          <tr>
                            <th>Centre Name</th>
                            <th>City</th>
                            <th>State</th>
                            <th>Type</th>
                            <th>Capacity</th>
                            <th>Coaches</th>
                            <th>Primary Sports</th>
                          </tr>
                        </thead>
                        <tbody>
                          {saiCentres.map(c => (
                            <tr key={c.name}>
                              <td className="font-bold text-white">{c.name}</td>
                              <td>{c.city}</td>
                              <td>{c.state}</td>
                              <td>{c.type}</td>
                              <td>{c.capacity}</td>
                              <td>{c.coaches}</td>
                              <td>{c.sports.slice(0,4).join(', ')}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  )}

                  {caSubTab === 'Private Academies & Akharas' && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                      {academies.map(pa => (
                        <div key={pa.name} className="acard">
                          <div className="font-bold text-white text-base">{pa.name}</div>
                          <div className="text-xs text-[#10E5B3] font-semibold mt-1 mb-3">{pa.location}</div>
                          <p className="text-xs text-slate-400 leading-relaxed mb-4"><b>Focus:</b> {pa.focus}</p>
                          <span className="tag purple">{pa.sports}</span>
                        </div>
                      ))}
                    </div>
                  )}

                  {caSubTab === 'SAI Proximity Matcher' && (
                    <div>
                      <div className="acard mb-6">
                        <label className="text-xs font-bold text-slate-300 uppercase tracking-widest block mb-3">Choose Athlete Matching Mode</label>
                        <div className="flex gap-4">
                          <button
                            onClick={() => setMatcherMode('Search Database Athletes')}
                            className={`glass-btn text-xs font-bold ${matcherMode === 'Search Database Athletes' ? '!bg-teal-500/20 !border-[#10E5B3] !text-[#10E5B3]' : ''}`}
                          >
                            Search Database Athletes
                          </button>
                          <button
                            onClick={() => setMatcherMode('Create Custom Athlete Profile')}
                            className={`glass-btn text-xs font-bold ${matcherMode === 'Create Custom Athlete Profile' ? '!bg-teal-500/20 !border-[#10E5B3] !text-[#10E5B3]' : ''}`}
                          >
                            Create Custom Athlete Profile
                          </button>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* Form Panel */}
                        <div className="acard">
                          <form onSubmit={runSaiMatch} className="space-y-4">
                            {matcherMode === 'Search Database Athletes' ? (
                              <div>
                                <label className="text-xs font-semibold block mb-1 text-slate-300">Select Athlete to Match</label>
                                <select
                                  value={matcherAthleteName}
                                  onChange={(e) => setMatcherAthleteName(e.target.value)}
                                  className="glass-input text-sm"
                                >
                                  {athletes.slice(0, 30).map(a => (
                                    <option key={a.name} value={a.name}>{a.name}</option>
                                  ))}
                                </select>
                              </div>
                            ) : (
                              <div className="space-y-3">
                                <div>
                                  <label className="text-xs font-semibold block mb-1 text-slate-300">Athlete Name</label>
                                  <input 
                                    type="text" 
                                    value={customProfile.name}
                                    onChange={(e) => setCustomProfile(prev => ({...prev, name: e.target.value}))}
                                    className="glass-input text-sm" 
                                  />
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                  <div>
                                    <label className="text-xs font-semibold block mb-1 text-slate-300">Sport Discipline</label>
                                    <select
                                      value={customProfile.sport}
                                      onChange={(e) => setCustomProfile(prev => ({...prev, sport: e.target.value}))}
                                      className="glass-input text-xs"
                                    >
                                      {sportsList.map(s => (
                                        <option key={s} value={s}>{s}</option>
                                      ))}
                                    </select>
                                  </div>
                                  <div>
                                    <label className="text-xs font-semibold block mb-1 text-slate-300">Home State</label>
                                    <select
                                      value={customProfile.state}
                                      onChange={(e) => setCustomProfile(prev => ({...prev, state: e.target.value}))}
                                      className="glass-input text-xs"
                                    >
                                      {statesList.map(s => (
                                        <option key={s} value={s}>{s}</option>
                                      ))}
                                    </select>
                                  </div>
                                </div>
                                <div className="grid grid-cols-3 gap-2">
                                  <div>
                                    <label className="text-[0.62rem] font-semibold block mb-1 text-slate-300">Gold</label>
                                    <input 
                                      type="number" 
                                      value={customProfile.gold} 
                                      onChange={(e) => setCustomProfile(prev => ({...prev, gold: parseInt(e.target.value) || 0}))}
                                      className="glass-input text-xs"
                                    />
                                  </div>
                                  <div>
                                    <label className="text-[0.62rem] font-semibold block mb-1 text-slate-300">Silver</label>
                                    <input 
                                      type="number" 
                                      value={customProfile.silver} 
                                      onChange={(e) => setCustomProfile(prev => ({...prev, silver: parseInt(e.target.value) || 0}))}
                                      className="glass-input text-xs"
                                    />
                                  </div>
                                  <div>
                                    <label className="text-[0.62rem] font-semibold block mb-1 text-slate-300">Bronze</label>
                                    <input 
                                      type="number" 
                                      value={customProfile.bronze} 
                                      onChange={(e) => setCustomProfile(prev => ({...prev, bronze: parseInt(e.target.value) || 0}))}
                                      className="glass-input text-xs"
                                    />
                                  </div>
                                </div>
                              </div>
                            )}
                            <button type="submit" className="glass-btn w-full mt-4 text-xs font-bold">
                              Calculate Optimal Training Centre
                            </button>
                          </form>
                        </div>

                        {/* Recommendation Results Display */}
                        <div className="acard">
                          <h4 className="font-bold text-white text-base mb-4">Optimal SAI Centres Recommendations</h4>
                          {matchingResults ? (
                            <div className="space-y-4">
                              {matchingResults.map((r, idx) => (
                                <div key={idx} className="p-4 rounded-xl border border-teal-500/10 bg-teal-500/5 flex items-center justify-between animate-fadeIn">
                                  <div>
                                    <div className="font-bold text-white text-sm">{r.centre.name}</div>
                                    <div className="text-xs text-slate-400 mt-1">{r.centre.city}, {r.centre.state}</div>
                                  </div>
                                  <div className="text-right">
                                    <div className="text-lg font-black text-[#10E5B3]">{r.score} pts</div>
                                    <div className="text-[0.68rem] text-slate-500 uppercase tracking-widest font-semibold">Suitability</div>
                                  </div>
                                </div>
                              ))}
                            </div>
                          ) : (
                            <p className="text-sm text-slate-500 italic">Adjust options and click match to see suitability scores.</p>
                          )}
                        </div>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 4: SPONSOR PIPELINE */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'Sponsor Pipeline' && (
                <div>
                  <div className="stitle">
                    Sponsor Pipeline <span className="chip chip-amber">Commercial Prospects & Packages</span>
                  </div>

                  <div className="overflow-x-auto mt-4">
                    <table className="custom-table">
                      <thead>
                        <tr>
                          <th>Corporate Sponsor</th>
                          <th>Sector Focus</th>
                          <th>CSR Annual Budget</th>
                          <th>Alignment Fit</th>
                          <th>Primary Location</th>
                          <th>Collateral Pitch</th>
                        </tr>
                      </thead>
                      <tbody>
                        {csrLeads.map(lead => (
                          <tr key={lead.company_name}>
                            <td className="font-bold text-white">{lead.company_name}</td>
                            <td>{lead.sector}</td>
                            <td><span className="text-emerald-300 font-bold">{lead.annual_csr_budget_cr} Cr</span></td>
                            <td>
                              <span className="tag green">{lead.athletiq_fit_score} / 10.0</span>
                            </td>
                            <td>{lead.geographic_focus}</td>
                            <td>
                              <button className="glass-btn !py-1 !px-3 gap-1 text-[0.68rem]">
                                <Download size={12} /> Sales Pitch.pdf
                              </button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              )}

              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 5: PROFILE DIRECTORY */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'Profile Directory' && (
                <div>
                  <div className="stitle">
                    Profile Directory <span className="chip chip-green">Athlete & Coach Bios</span>
                  </div>

                  {/* Sub-tab selection */}
                  <div className="flex border-b border-[rgba(255,255,255,0.05)] mb-6 gap-2">
                    {['Athlete Search', 'Coach Search', 'Academy Search'].map(sub => (
                      <button
                        key={sub}
                        onClick={() => {
                          setAthleteSelectedLevel(null);
                          setProfileSelectedAthlete('-- Select Athlete --');
                        }}
                        className="pb-3 px-4 font-semibold text-sm border-b-2 border-[#10E5B3] text-[#10E5B3]"
                      >
                        {sub}
                      </button>
                    ))}
                  </div>

                  {/* Dynamic Filtering Panel */}
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6 acard mb-6">
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Choose Sport Filter</label>
                      <select 
                        value={selectedSport} 
                        onChange={(e) => setSelectedSport(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All Sports">All Sports</option>
                        {sportsList.map(sp => <option key={sp} value={sp}>{sp}</option>)}
                      </select>
                    </div>
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Choose State Filter</label>
                      <select 
                        value={selectedState} 
                        onChange={(e) => setSelectedState(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All States">All States</option>
                        {statesList.map(st => <option key={st} value={st}>{st}</option>)}
                      </select>
                    </div>
                  </div>

                  <div className="acard mb-6">
                    <label className="text-xs font-bold text-slate-300 uppercase tracking-widest block mb-2">Select Athlete to View Bio-Data</label>
                    <select 
                      value={profileSelectedAthlete} 
                      onChange={(e) => setProfileSelectedAthlete(e.target.value)}
                      className="glass-input text-sm"
                    >
                      <option value="-- Select Athlete --">-- Select Athlete --</option>
                      {filteredAthletes.map(ath => (
                        <option key={ath.name} value={ath.name}>{ath.name}</option>
                      ))}
                    </select>
                  </div>

                  {/* Bio Card display */}
                  {profileSelectedAthlete !== '-- Select Athlete --' ? (
                    (() => {
                      const ath = athletes.find(a => a.name === profileSelectedAthlete);
                      if (!ath) return null;
                      const hasTops = topsBios[ath.name.toLowerCase()];
                      
                      return (
                        <motion.div 
                          initial={{ opacity: 0 }} 
                          animate={{ opacity: 1 }} 
                          className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6"
                        >
                          <div className="acard">
                            <span className="tag green mb-4">PERSONAL CARD</span>
                            <h2 className="text-2xl font-black text-white font-['Outfit']">{ath.name}</h2>
                            <p className="text-xs text-[#10E5B3] font-bold mt-1 uppercase tracking-wider">{ath.sport} · {ath.state}</p>
                            <hr className="my-4 border-[rgba(255,255,255,0.05)]" />
                            <div className="space-y-2 text-sm text-slate-300">
                              <div><b>Age:</b> {ath.age || 'Unknown'}</div>
                              <div><b>Gender:</b> {ath.gender}</div>
                              <div><b>Registry Tier:</b> {ath.tier}</div>
                              <div><b>Pipeline Stage:</b> {ath.pipeline_stage}</div>
                            </div>
                          </div>

                          <div className="acard">
                            <span className="tag blue mb-4">METRICS</span>
                            <h3 className="font-bold text-white mb-4">Training & Capacity</h3>
                            <div className="space-y-2 text-sm text-slate-300">
                              <div><b>Assigned Coach:</b> Assigned National Mentor</div>
                              <div><b>Training Centre:</b> SAI NCOE {ath.state}</div>
                              <div><b>Opportunity Score:</b> <span className="tag amber">{ath.athletiq_opportunity_score}/10.0</span></div>
                              <div><b>Current Funding:</b> {ath.funding_status}</div>
                            </div>
                          </div>

                          <div className="acard">
                            <span className="tag purple mb-4">ACHIEVEMENTS</span>
                            <h3 className="font-bold text-white mb-4">Elite Placement Bios</h3>
                            <p className="text-sm text-slate-300 italic mb-4">"{ath.notes}"</p>
                            {hasTops && (
                              <div className="bg-[rgba(104,61,228,0.1)] p-3 border border-purple-500/20 rounded-lg text-xs space-y-1">
                                <div><b>Category:</b> {hasTops.category}</div>
                                <div><b>Outlook:</b> {hasTops.outlook}</div>
                              </div>
                            )}
                          </div>
                        </motion.div>
                      );
                    })()
                  ) : (
                    <div className="mt-8">
                      <div className="stitle">Filter Athletes Directory by Performance Level</div>
                      <div className="grid grid-cols-3 gap-6 mb-6">
                        <button 
                          onClick={() => setAthleteSelectedLevel('International')}
                          className={`glass-btn h-24 text-base font-bold flex flex-col gap-2 ${athleteSelectedLevel === 'International' ? '!bg-teal-500/20 !border-[#10E5B3] !text-[#10E5B3]' : ''}`}
                        >
                          <span>🌍</span> International Level
                        </button>
                        <button 
                          onClick={() => setAthleteSelectedLevel('National')}
                          className={`glass-btn h-24 text-base font-bold flex flex-col gap-2 ${athleteSelectedLevel === 'National' ? '!bg-teal-500/20 !border-[#10E5B3] !text-[#10E5B3]' : ''}`}
                        >
                          <span>🏆</span> National Level
                        </button>
                        <button 
                          onClick={() => setAthleteSelectedLevel('State-wise')}
                          className={`glass-btn h-24 text-base font-bold flex flex-col gap-2 ${athleteSelectedLevel === 'State-wise' ? '!bg-teal-500/20 !border-[#10E5B3] !text-[#10E5B3]' : ''}`}
                        >
                          <span>📍</span> State-wise / District
                        </button>
                      </div>

                      {athleteSelectedLevel && (
                        <div className="acard">
                          <div className="flex items-center justify-between border-b border-[rgba(255,255,255,0.05)] pb-4 mb-4">
                            <h4 className="font-bold text-white text-lg">Matching {athleteSelectedLevel} Athletes</h4>
                            <button 
                              onClick={() => setAthleteSelectedLevel(null)}
                              className="glass-btn gap-1 text-xs px-3 py-1 bg-red-500/10 border-red-500/30 text-rose-300"
                            >
                              <X size={14} /> Close Table
                            </button>
                          </div>

                          <div className="overflow-x-auto">
                            <table className="custom-table">
                              <thead>
                                <tr>
                                  <th>Athlete Name</th>
                                  <th>Specialization</th>
                                  <th>State Registry</th>
                                  <th>Performance Level</th>
                                  <th>Age</th>
                                  <th>Achievements / Notes</th>
                                </tr>
                              </thead>
                              <tbody>
                                {filteredAthletes
                                  .filter(ath => {
                                    if (athleteSelectedLevel === 'International') {
                                      return ath.performance_level.toLowerCase().includes('internat');
                                    }
                                    if (athleteSelectedLevel === 'National') {
                                      return ath.performance_level.toLowerCase() === 'national';
                                    }
                                    return ['state', 'district'].includes(ath.performance_level.toLowerCase());
                                  })
                                  .map(ath => (
                                    <tr key={ath.name}>
                                      <td className="font-bold text-white">{ath.name}</td>
                                      <td>{ath.sport}</td>
                                      <td>{ath.state}</td>
                                      <td><span className="tag green">{ath.performance_level}</span></td>
                                      <td>{ath.age || 'Unknown'}</td>
                                      <td>{ath.notes}</td>
                                    </tr>
                                  ))}
                              </tbody>
                            </table>
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              )}

              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 6: WOMENS DIRECTORY */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'Womens Directory' && (
                <div>
                  <div className="stitle">
                    Womens Directory <span className="chip chip-blue">Emerging Women Athletes</span>
                  </div>

                  {/* Filters */}
                  <div className="grid grid-cols-1 md:grid-cols-4 gap-6 acard mb-6">
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">🔍 Search by Name</label>
                      <input 
                        type="text"
                        value={womenSearch}
                        onChange={(e) => setWomenSearch(e.target.value)}
                        placeholder="Type athlete name..."
                        className="glass-input text-xs"
                      />
                    </div>
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Sport Focus</label>
                      <select 
                        value={womenSport} 
                        onChange={(e) => setWomenSport(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All Sports">All Sports</option>
                        {Array.from(new Set(womenAthletes.map(w => w.sport))).map(s => (
                          <option key={s} value={s}>{s}</option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">State Registry</label>
                      <select 
                        value={womenState} 
                        onChange={(e) => setWomenState(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All States">All States</option>
                        {Array.from(new Set(womenAthletes.map(w => w.state))).map(s => (
                          <option key={s} value={s}>{s}</option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="text-[0.68rem] font-bold text-slate-300 uppercase tracking-widest block mb-2">Performance Level</label>
                      <select 
                        value={womenLevel} 
                        onChange={(e) => setWomenLevel(e.target.value)}
                        className="glass-input text-xs"
                      >
                        <option value="All Levels">All Levels</option>
                        <option value="International">International</option>
                        <option value="National">National</option>
                        <option value="State">State</option>
                        <option value="District">District</option>
                      </select>
                    </div>
                  </div>

                  {/* Summary Cards */}
                  <div className="grid grid-cols-3 gap-6 mb-6">
                    <div className="acard text-center">
                      <div className="text-2xl font-extrabold text-[#10E5B3]">{filteredWomen.length}</div>
                      <div className="text-[0.68rem] text-slate-400 uppercase tracking-widest font-semibold mt-1">Filtered Athletes</div>
                    </div>
                    <div className="acard text-center">
                      <div className="text-2xl font-extrabold text-[#00ffd1]">{filteredWomen.filter(w => w.performance_level === 'International').length}</div>
                      <div className="text-[0.68rem] text-slate-400 uppercase tracking-widest font-semibold mt-1">International</div>
                    </div>
                    <div className="acard text-center">
                      <div className="text-2xl font-extrabold text-[#683DE4]">{Array.from(new Set(filteredWomen.map(w => w.sport))).length}</div>
                      <div className="text-[0.68rem] text-slate-400 uppercase tracking-widest font-semibold mt-1">Unique Sports</div>
                    </div>
                  </div>

                  <div className="acard mb-6">
                    <label className="text-xs font-bold text-slate-300 uppercase tracking-widest block mb-2">Select Women Athlete to View Bio-Data</label>
                    <select
                      value={womenSelectedAthlete}
                      onChange={(e) => setWomenSelectedAthlete(e.target.value)}
                      className="glass-input text-sm"
                    >
                      <option value="-- Select Athlete --">-- Select Athlete --</option>
                      {filteredWomen.map(w => (
                        <option key={w.name} value={w.name}>{w.name}</option>
                      ))}
                    </select>
                  </div>

                  {womenSelectedAthlete !== '-- Select Athlete --' ? (
                    (() => {
                      const person = womenAthletes.find(w => w.name === womenSelectedAthlete);
                      if (!person) return null;
                      return (
                        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="space-y-6">
                          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div className="acard">
                              <span className="tag green mb-4">Sportsperson Card</span>
                              <h3 className="text-xl font-bold text-white font-['Outfit']">{person.name}</h3>
                              <p className="text-xs text-slate-400 mt-1 uppercase tracking-wider">{person.sport} · {person.state} · {person.city}</p>
                              <hr className="my-4 border-[rgba(255,255,255,0.05)]" />
                              <div className="space-y-1 text-sm text-slate-300">
                                <div><b>Age:</b> {person.age}</div>
                                <div><b>Gender:</b> {person.gender}</div>
                                <div><b>Tier:</b> {person.tier}</div>
                                <div><b>Status:</b> <span className="tag amber">{person.status}</span></div>
                                <div><b>Registry Base:</b> {person.city}, {person.state}</div>
                              </div>
                            </div>
                            <div className="acard">
                              <span className="tag blue mb-4">Performance & Metrics</span>
                              <h3 className="text-xl font-bold text-white font-['Outfit']">Training Profile</h3>
                              <hr className="my-4 border-[rgba(255,255,255,0.05)]" />
                              <div className="space-y-1 text-sm text-slate-300">
                                <div><b>Performance Level:</b> <span className="tag green">{person.performance_level}</span></div>
                                <div><b>Opportunity Score:</b> <span className="tag amber">{person.athletiq_opportunity_score} / 10.0</span></div>
                                <div><b>Current Funding:</b> {person.funding_status}</div>
                                <div><b>Highlight:</b> {person.highlight}</div>
                              </div>
                            </div>
                          </div>
                          <div className="acard">
                            <span className="tag amber mb-4">Achievements</span>
                            <h3 className="font-bold text-white mb-2">Key Achievements & Scouting Notes</h3>
                            <p className="text-sm text-slate-300 leading-relaxed"><b>Achievements:</b> {person.achievements}</p>
                            <p className="text-sm text-slate-300 leading-relaxed mt-2"><b>Scouting Remarks:</b> {person.remarks}</p>
                          </div>
                        </motion.div>
                      );
                    })()
                  ) : (
                    <div className="acard mt-6">
                      <div className="font-bold text-white text-base mb-4">Full Women Athletes Directory</div>
                      <div className="overflow-x-auto">
                        <table className="custom-table">
                          <thead>
                            <tr>
                              <th>Athlete Name</th>
                              <th>Sport</th>
                              <th>Event</th>
                              <th>State</th>
                              <th>City</th>
                              <th>Age</th>
                              <th>Level</th>
                              <th>Status</th>
                            </tr>
                          </thead>
                          <tbody>
                            {filteredWomen.slice(0, 100).map(w => (
                              <tr key={w.name}>
                                <td className="font-bold text-white">{w.name}</td>
                                <td>{w.sport}</td>
                                <td>{w.event}</td>
                                <td>{w.state}</td>
                                <td>{w.city}</td>
                                <td>{w.age}</td>
                                <td><span className="tag green">{w.performance_level}</span></td>
                                <td>{w.status}</td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* ─────────────────────────────────────────────────────────────────── */}
              {/* TAB 7: AI ASSISTANT */}
              {/* ─────────────────────────────────────────────────────────────────── */}
              {activeTab === 'AI Assistant' && (
                <div className="max-w-3xl mx-auto flex flex-col h-[70vh]">
                  <div className="stitle !m-0 mb-2">
                    🤖 AI Assistant <span className="chip chip-purple">FastAPI + Gemini Model</span>
                  </div>
                  <p className="text-xs text-slate-400 mb-6">Ask me anything about AthletIQ's databases (athletes, coaches, tournaments).</p>

                  {/* Settings / API Key */}
                  <div className="acard flex flex-col md:flex-row items-center gap-4 py-3 mb-6">
                    <span className="text-xs font-bold text-slate-300 uppercase tracking-widest flex items-center gap-2">
                      <Lock size={14} className="text-[#10E5B3]" />
                      GEMINI KEY:
                    </span>
                    <input 
                      type="password" 
                      value={geminiKey}
                      onChange={(e) => setGeminiKey(e.target.value)}
                      placeholder="Enter Gemini API Key..." 
                      className="glass-input text-xs flex-1"
                    />
                  </div>

                  {/* Chat Area */}
                  <div className="flex-1 bg-[rgba(11,8,25,0.7)] border border-[rgba(255,255,255,0.05)] rounded-2xl p-6 overflow-y-auto space-y-4 mb-4 min-h-[300px]">
                    {chatMessages.length === 0 ? (
                      <div className="h-full flex flex-col items-center justify-center text-slate-500 text-center">
                        <HelpCircle size={40} className="mb-2 text-slate-600" />
                        <p className="text-sm">Provide your API Key in the panel above to start questioning the model.</p>
                      </div>
                    ) : (
                      chatMessages.map((msg, idx) => (
                        <div 
                          key={idx} 
                          className={`p-4 rounded-xl border flex flex-col gap-1 ${msg.role === 'user' ? 'bg-white/5 border-white/5 align-self-end max-w-[85%] ml-auto' : 'bg-gradient-to-br from-[#10E5B3]/5 to-[#683DE4]/5 border-teal-500/20 max-w-[85%]'}`}
                        >
                          <span className={`text-[0.62rem] font-bold uppercase tracking-widest ${msg.role === 'user' ? 'text-slate-400 text-right' : 'text-[#10E5B3]'}`}>
                            {msg.role === 'user' ? 'You' : 'AI Assistant'}
                          </span>
                          <p className="text-sm text-slate-200 leading-relaxed font-sans">{msg.content}</p>
                        </div>
                      ))
                    )}
                    
                    {chatLoading && (
                      <div className="p-4 rounded-xl border border-teal-500/10 bg-teal-500/5 max-w-[85%] animate-pulse">
                        <span className="text-[0.62rem] font-bold uppercase tracking-widest text-[#10E5B3]">AI Assistant</span>
                        <p className="text-sm text-slate-400 mt-1 italic flex items-center gap-2">
                          <RefreshCw size={14} className="animate-spin" /> Thinking...
                        </p>
                      </div>
                    )}
                    <div ref={chatEndRef} />
                  </div>

                  {/* Chat input form */}
                  <form onSubmit={handleSendMessage} className="flex gap-4">
                    <input 
                      type="text" 
                      value={chatInput}
                      onChange={(e) => setChatInput(e.target.value)}
                      placeholder="Ask about sponsors, coaches, or athletes..."
                      disabled={!geminiKey}
                      className="glass-input flex-1 text-sm disabled:opacity-50 disabled:cursor-not-allowed"
                    />
                    <button 
                      type="submit" 
                      disabled={!geminiKey || !chatInput.trim()}
                      className="glass-btn !px-5 disabled:opacity-50"
                    >
                      <Send size={16} /> Send
                    </button>
                  </form>
                </div>
              )}
            </motion.div>
          </AnimatePresence>
        </main>
      )}
    </div>
  );
}
