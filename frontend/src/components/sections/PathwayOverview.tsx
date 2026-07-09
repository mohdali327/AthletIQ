"use client";
import { motion } from 'framer-motion';
import { ShieldAlert, TrendingUp, Anchor, Activity } from 'lucide-react';

export default function PathwayOverview() {
  const blockers = [
    {
      level: "District ➔ State Transition",
      blocker: "Lack of standardized equipment kits & travel funding in Tier-3 districts.",
      solution: "Support village-level league travel grants.",
      color: "border-[#683DE4]"
    },
    {
      level: "State ➔ Zonal Transition",
      blocker: "Insufficient NIS certified coaches and sports science clinics at state levels.",
      solution: "Train former state athletes as district coaches.",
      color: "border-[#10E5B3]"
    },
    {
      level: "Zonal ➔ National Transition",
      blocker: "Lack of specialized residential sports academy placements and advanced nutrition.",
      solution: "Partner with private/SAI NCOE centres.",
      color: "border-[#FDD663]"
    },
    {
      level: "National ➔ Elite Transition",
      blocker: "Insufficient corporate sponsorship for international exposure tournaments.",
      solution: "Align private sponsor contracts to elite athletes.",
      color: "border-[#F28B82]"
    }
  ];

  return (
    <section id="pathway" className="min-h-screen pt-32 pb-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8 }}
      >
        <span className="inline-block px-3 py-1 mb-6 text-xs font-bold tracking-widest text-[#10E5B3] bg-[#10E5B3]/10 border border-[#10E5B3]/20 rounded-full uppercase">
          Strategic Dashboard Homepage
        </span>
        <h2 className="text-5xl font-black mb-8 text-gradient">Pathway Overview</h2>
        
        <p className="text-xl text-white/60 max-w-3xl mb-16 leading-relaxed">
          The athlete development pipeline tracks the progression of talent from district-level grassroots participation, through state and zonal championships, into national coaching camps (like SAI NCOEs), and finally to elite international podium finishes. Currently, significant drop-offs occur at the state-to-zonal and national-to-elite transitions due to funding and coaching bottlenecks.
        </p>

        <h3 className="text-2xl font-bold mb-8 flex items-center gap-3">
          <Activity className="w-6 h-6 text-[#10E5B3]" /> 
          Pipeline Blocker & Leakage Analysis
        </h3>

        <div className="grid grid-cols-1 gap-6">
          {blockers.map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.6, delay: index * 0.15 }}
              className={`glass-card p-6 rounded-2xl border-l-4 ${item.color} hover:bg-white/5 transition-colors`}
            >
              <h4 className="text-xl font-bold text-white mb-3">{item.level}</h4>
              <div className="text-sm text-white/60 mb-2">
                <span className="font-bold text-white/80">Leakage Blocker:</span> {item.blocker}
              </div>
              <div className="text-sm text-[#10E5B3]">
                <span className="font-bold">Recommended Intervention:</span> {item.solution}
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}
