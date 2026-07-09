"use client";
import { motion } from 'framer-motion';
import { Target, Medal, Calendar } from 'lucide-react';

export default function DiscoveryLeagues() {
  const leagues = [
    { name: "Khelo India Youth Games", sport: "Multi-Sport", state: "Haryana", status: "Active" },
    { name: "National Archery Sub-Junior", sport: "Archery", state: "Jharkhand", status: "Upcoming" },
    { name: "State Level Wrestling Championship", sport: "Wrestling", state: "Maharashtra", status: "Active" },
    { name: "Inter-District Athletics Meet", sport: "Athletics", state: "Kerala", status: "Completed" }
  ];

  return (
    <section id="discovery" className="min-h-screen pt-32 pb-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8 }}
      >
        <span className="inline-block px-3 py-1 mb-6 text-xs font-bold tracking-widest text-[#683DE4] bg-[#683DE4]/10 border border-[#683DE4]/20 rounded-full uppercase">
          Live Grassroots & Emerging Athlete Prospects
        </span>
        <h2 className="text-5xl font-black mb-8 text-gradient">Discovery & Leagues</h2>
        
        <p className="text-xl text-white/60 max-w-3xl mb-16 leading-relaxed">
          Track rising talent from local and state leagues in real-time. Connect with emerging prospects before they enter the national tier.
        </p>

        <h3 className="text-2xl font-bold mb-8 flex items-center gap-3">
          <Target className="w-6 h-6 text-[#683DE4]" /> 
          Live Grassroots Leagues & Tournaments
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-16">
          {leagues.map((league, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              className="glass-card p-6 rounded-2xl flex items-center justify-between group cursor-pointer hover:bg-white/5"
            >
              <div>
                <h4 className="font-bold text-lg text-white mb-2 group-hover:text-[#683DE4] transition-colors">{league.name}</h4>
                <div className="flex gap-4 text-sm text-white/50">
                  <span className="flex items-center gap-1"><Medal className="w-4 h-4"/> {league.sport}</span>
                  <span className="flex items-center gap-1"><Target className="w-4 h-4"/> {league.state}</span>
                </div>
              </div>
              <div className={`px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider
                ${league.status === 'Active' ? 'bg-[#10E5B3]/20 text-[#10E5B3]' : 
                  league.status === 'Upcoming' ? 'bg-[#FDD663]/20 text-[#FDD663]' : 
                  'bg-white/10 text-white/50'}`}>
                {league.status}
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}
