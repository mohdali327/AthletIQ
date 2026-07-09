"use client";

import { motion } from "framer-motion";
import { ArrowDown } from "lucide-react";
import Sidebar from "@/components/Sidebar";
import PathwayOverview from "@/components/sections/PathwayOverview";
import DiscoveryLeagues from "@/components/sections/DiscoveryLeagues";
import RegionalTalent from "@/components/sections/RegionalTalent";
import CentresAcademies from "@/components/sections/CentresAcademies";
import SponsorPipeline from "@/components/sections/SponsorPipeline";
import ProfileDirectory from "@/components/sections/ProfileDirectory";

export default function Home() {
  return (
    <main className="relative min-h-screen bg-[#080611] text-white">
      {/* Immersive Background */}
      <div className="fixed inset-0 z-0 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[500px] h-[500px] bg-[#10E5B3]/20 blur-[120px] rounded-full animate-pulse-slow"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[600px] h-[600px] bg-[#683DE4]/20 blur-[120px] rounded-full animate-pulse-slow" style={{ animationDelay: '2s' }}></div>
      </div>

      {/* Hero Intro (Full Screen) */}
      <section className="relative z-10 min-h-screen flex flex-col items-center justify-center px-4">
        <motion.div 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.2, ease: [0.16, 1, 0.3, 1] }}
          className="inline-block px-4 py-1.5 rounded-full border border-white/20 bg-white/5 backdrop-blur-md mb-8 text-sm font-bold tracking-[0.2em] uppercase"
        >
          ✦ AthletIQ Frontend Rewrite ✦
        </motion.div>

        <motion.h1 
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1.2, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
          className="text-6xl md:text-8xl lg:text-9xl font-black text-center leading-[0.9] tracking-tighter text-gradient mb-6"
        >
          IMMERSIVE<br />PIPELINE
        </motion.h1>

        <motion.p 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 0.4 }}
          className="text-xl text-white/60 text-center max-w-2xl mb-16"
        >
          Your complete Streamlit dashboard reimagined as a premium, scroll-linked marketing experience.
        </motion.p>
        
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1, delay: 1 }}
          className="animate-bounce"
        >
          <ArrowDown className="w-8 h-8 text-white/40" />
        </motion.div>
      </section>

      {/* Main App Layout (Scroll-Spy) */}
      <div className="relative z-10 max-w-7xl mx-auto px-4 flex gap-12 pb-32">
        {/* Sticky Sidebar */}
        <Sidebar />

        {/* Scrollable Content Sections */}
        <div className="flex-1 w-full max-w-4xl">
          <PathwayOverview />
          <DiscoveryLeagues />
          <RegionalTalent />
          <CentresAcademies />
          <SponsorPipeline />
          <ProfileDirectory />
        </div>
      </div>
    </main>
  );
}
