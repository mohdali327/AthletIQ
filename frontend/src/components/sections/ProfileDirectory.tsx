"use client";
import { motion } from 'framer-motion';
import { UserCircle } from 'lucide-react';

export default function ProfileDirectory() {
  const profiles = [
    { name: "Priya Sharma", role: "Athlete", sport: "Archery", age: 16 },
    { name: "Rahul Deshmukh", role: "Coach", sport: "Wrestling", age: 45 },
    { name: "Anita Kumar", role: "Athlete", sport: "Athletics", age: 14 }
  ];

  return (
    <section id="profiles" className="min-h-screen pt-32 pb-24">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8 }}
      >
        <span className="inline-block px-3 py-1 mb-6 text-xs font-bold tracking-widest text-[#10E5B3] bg-[#10E5B3]/10 border border-[#10E5B3]/20 rounded-full uppercase">
          Athlete & Coach Bios
        </span>
        <h2 className="text-5xl font-black mb-8 text-gradient">Profile Directory</h2>
        
        <p className="text-xl text-white/60 max-w-3xl mb-16 leading-relaxed">
          Comprehensive biometric, performance, and demographic data for registered athletes and certified coaches.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {profiles.map((profile, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, scale: 0.9 }}
              whileInView={{ opacity: 1, scale: 1 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: i * 0.1 }}
              className="glass-card p-8 rounded-3xl text-center group hover:-translate-y-2 transition-transform cursor-pointer"
            >
              <UserCircle className="w-16 h-16 mx-auto mb-4 text-[#683DE4] group-hover:text-[#10E5B3] transition-colors" />
              <h3 className="text-xl font-bold mb-1">{profile.name}</h3>
              <p className="text-[#10E5B3] font-bold text-sm uppercase tracking-wider mb-4">{profile.role}</p>
              
              <div className="flex justify-center gap-4 text-sm text-white/50 border-t border-white/10 pt-4">
                <span>{profile.sport}</span>
                <span>•</span>
                <span>Age: {profile.age}</span>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}
