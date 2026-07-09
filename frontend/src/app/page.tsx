"use client";

import { motion, useScroll, useTransform } from "framer-motion";
import { useEffect, useState } from "react";
import { ArrowRight, Activity, Users, MapPin, Database } from "lucide-react";

export default function Home() {
  const { scrollYProgress } = useScroll();
  const yBg = useTransform(scrollYProgress, [0, 1], ["0%", "50%"]);
  
  const [metrics, setMetrics] = useState({
    active_profiles: "34K+",
    talent_clusters: 9,
    live_leagues: 24,
    pipeline_drops: { state_to_zonal: "42%", national_to_elite: "68%" }
  });

  useEffect(() => {
    // In production, this fetches from the FastAPI backend:
    // fetch("http://localhost:8000/api/metrics/pipeline").then(res => res.json()).then(setMetrics)
  }, []);

  return (
    <main className="relative min-h-screen">
      <div className="editions-bg" />

      {/* Hero Section */}
      <section className="relative h-screen flex flex-col items-center justify-center overflow-hidden px-4">
        <motion.div 
          initial={{ opacity: 0, y: 30, filter: "blur(10px)" }}
          animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
          transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
          className="inline-block px-4 py-1.5 rounded-full border border-white/20 bg-white/5 backdrop-blur-md mb-8 text-sm font-bold tracking-[0.2em] uppercase"
        >
          ✦ Spring 2026 Edition ✦
        </motion.div>

        <motion.h1 
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.2, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          className="text-6xl md:text-8xl lg:text-9xl font-black text-center leading-[0.9] tracking-tighter text-gradient mb-6"
        >
          ATHLETIQ<br />INTELLIGENCE
        </motion.h1>

        <motion.p 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 0.4 }}
          className="text-lg md:text-xl text-white/60 text-center max-w-2xl mb-12"
        >
          Scouting, coaching, and funding intelligence for India's grassroots-to-medal pathways. 
          Experience our most immersive data pipeline yet.
        </motion.p>

        <motion.button
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, delay: 0.6 }}
          className="group relative px-8 py-4 bg-white text-black font-bold rounded-full overflow-hidden flex items-center gap-2 hover:scale-105 transition-transform"
        >
          <span>Enter Dashboard</span>
          <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
        </motion.button>
      </section>

      {/* Live Metrics Section (Scroll Animated) */}
      <section className="py-32 px-4 max-w-6xl mx-auto">
        <motion.div 
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 0.8 }}
          className="text-center mb-20"
        >
          <h2 className="text-4xl md:text-5xl font-bold mb-4">Pipeline Sync is Live</h2>
          <p className="text-white/60">Monitoring the entire nation's athletic pulse in real-time.</p>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <MetricCard 
            icon={<Users className="w-8 h-8 text-[#10E5B3]" />}
            value={metrics.active_profiles}
            label="Active Profiles"
            delay={0.1}
          />
          <MetricCard 
            icon={<MapPin className="w-8 h-8 text-[#683DE4]" />}
            value={metrics.talent_clusters}
            label="Talent Clusters"
            delay={0.2}
          />
          <MetricCard 
            icon={<Activity className="w-8 h-8 text-[#FDD663]" />}
            value={metrics.live_leagues}
            label="Live Leagues"
            delay={0.3}
          />
        </div>
      </section>
      
      {/* Footer */}
      <footer className="py-12 text-center text-white/30 text-sm">
        <p>Built with Next.js & Framer Motion. Connected to AthletIQ Python Backend.</p>
      </footer>
    </main>
  );
}

function MetricCard({ icon, value, label, delay }: { icon: React.ReactNode, value: string | number, label: string, delay: number }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.8, delay }}
      className="glass-card p-8 rounded-3xl flex flex-col items-center justify-center text-center"
    >
      <div className="mb-6 p-4 bg-white/5 rounded-2xl">
        {icon}
      </div>
      <div className="text-5xl font-black mb-2">{value}</div>
      <div className="text-sm font-bold text-white/50 uppercase tracking-widest">{label}</div>
    </motion.div>
  );
}
