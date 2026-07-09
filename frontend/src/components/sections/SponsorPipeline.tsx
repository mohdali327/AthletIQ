"use client";
import { motion } from 'framer-motion';
import { DollarSign } from 'lucide-react';

export default function SponsorPipeline() {
  const sponsors = [
    { name: "Reliance Foundation", sector: "Corporate CSR", type: "Academy Funding", status: "Hot Lead" },
    { name: "Tata Steel Sports", sector: "Corporate CSR", type: "Grassroots Tournaments", status: "Warm Lead" },
    { name: "JSW Sports", sector: "Private Equity", type: "Elite Athlete Sponsorship", status: "Cold Lead" },
  ];

  return (
    <section id="sponsors" className="min-h-screen pt-32 pb-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8 }}
      >
        <span className="inline-block px-3 py-1 mb-6 text-xs font-bold tracking-widest text-[#FDD663] bg-[#FDD663]/10 border border-[#FDD663]/20 rounded-full uppercase">
          Commercial Prospects & Packages
        </span>
        <h2 className="text-5xl font-black mb-8 text-gradient">Sponsor Pipeline</h2>
        
        <p className="text-xl text-white/60 max-w-3xl mb-16 leading-relaxed">
          Discover and match commercial sponsors with academies, sports, and athletes based on sector alignment and CSR goals.
        </p>

        <div className="space-y-4">
          {sponsors.map((sponsor, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.15 }}
              className="glass-card p-6 rounded-2xl flex items-center justify-between"
            >
              <div>
                <h4 className="font-bold text-lg text-white mb-1">{sponsor.name}</h4>
                <div className="flex gap-4 text-sm text-white/50">
                  <span>{sponsor.sector}</span>
                  <span>•</span>
                  <span>{sponsor.type}</span>
                </div>
              </div>
              <div className={`px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider flex items-center gap-2
                ${sponsor.status === 'Hot Lead' ? 'bg-[#F28B82]/20 text-[#F28B82]' : 
                  sponsor.status === 'Warm Lead' ? 'bg-[#FDD663]/20 text-[#FDD663]' : 
                  'bg-white/10 text-white/50'}`}>
                <DollarSign className="w-4 h-4" />
                {sponsor.status}
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}
