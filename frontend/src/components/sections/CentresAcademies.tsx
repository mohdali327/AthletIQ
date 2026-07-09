"use client";
import { motion } from 'framer-motion';
import { Building2, Users } from 'lucide-react';

export default function CentresAcademies() {
  return (
    <section id="centres" className="min-h-screen pt-32 pb-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8 }}
      >
        <span className="inline-block px-3 py-1 mb-6 text-xs font-bold tracking-widest text-[#10E5B3] bg-[#10E5B3]/10 border border-[#10E5B3]/20 rounded-full uppercase">
          Ecosystem Directory
        </span>
        <h2 className="text-5xl font-black mb-8 text-gradient">Centres & Academies</h2>
        
        <p className="text-xl text-white/60 max-w-3xl mb-16 leading-relaxed">
          Monitor infrastructure, coaching capacity, and academies. Identify gaps in Coach-to-Athlete ratios and track SAI Training Networks.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <motion.div 
            whileHover={{ scale: 1.02 }}
            className="glass-card p-8 rounded-3xl"
          >
            <Building2 className="w-10 h-10 text-[#10E5B3] mb-6" />
            <h3 className="text-3xl font-bold mb-2">42</h3>
            <p className="text-white/60 text-sm uppercase tracking-widest font-bold">Active SAI Centres</p>
          </motion.div>
          
          <motion.div 
            whileHover={{ scale: 1.02 }}
            className="glass-card p-8 rounded-3xl"
          >
            <Users className="w-10 h-10 text-[#683DE4] mb-6" />
            <h3 className="text-3xl font-bold mb-2">1:28</h3>
            <p className="text-white/60 text-sm uppercase tracking-widest font-bold">National Coach Ratio</p>
            <p className="text-xs text-[#F28B82] mt-2">Critical Shortage in Tier-3 Districts</p>
          </motion.div>
        </div>
      </motion.div>
    </section>
  );
}
