"use client";
import { motion } from 'framer-motion';
import { Map, BarChart2 } from 'lucide-react';

export default function RegionalTalent() {
  return (
    <section id="regional" className="min-h-screen pt-32 pb-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8 }}
      >
        <span className="inline-block px-3 py-1 mb-6 text-xs font-bold tracking-widest text-[#FDD663] bg-[#FDD663]/10 border border-[#FDD663]/20 rounded-full uppercase">
          Top Regional Clusters
        </span>
        <h2 className="text-5xl font-black mb-8 text-gradient">Regional Talent</h2>
        
        <p className="text-xl text-white/60 max-w-3xl mb-16 leading-relaxed">
          Analyze top states, sports, and regional talent clusters to identify where to focus scouting operations.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="glass-card p-8 rounded-3xl"
          >
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <Map className="w-6 h-6 text-[#FDD663]" /> Top States
            </h3>
            <div className="space-y-4">
              {['Haryana - 24%', 'Maharashtra - 18%', 'Punjab - 15%', 'Kerala - 12%'].map((item, i) => (
                <div key={i} className="flex items-center gap-4">
                  <div className="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                    <motion.div 
                      initial={{ width: 0 }}
                      whileInView={{ width: item.split(' - ')[1] }}
                      transition={{ duration: 1, delay: i * 0.1 }}
                      className="h-full bg-gradient-to-r from-[#FDD663] to-[#10E5B3]"
                    />
                  </div>
                  <div className="w-32 text-sm font-bold text-white/80">{item}</div>
                </div>
              ))}
            </div>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            className="glass-card p-8 rounded-3xl"
          >
            <h3 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <BarChart2 className="w-6 h-6 text-[#10E5B3]" /> Top Sports
            </h3>
            <div className="space-y-4">
              {['Wrestling - 30%', 'Athletics - 25%', 'Boxing - 15%', 'Archery - 10%'].map((item, i) => (
                <div key={i} className="flex items-center gap-4">
                  <div className="w-32 text-sm font-bold text-white/80">{item}</div>
                  <div className="flex-1 h-2 bg-white/10 rounded-full overflow-hidden">
                    <motion.div 
                      initial={{ width: 0 }}
                      whileInView={{ width: item.split(' - ')[1] }}
                      transition={{ duration: 1, delay: i * 0.1 }}
                      className="h-full bg-gradient-to-r from-[#10E5B3] to-[#683DE4]"
                    />
                  </div>
                </div>
              ))}
            </div>
          </motion.div>
        </div>
      </motion.div>
    </section>
  );
}
