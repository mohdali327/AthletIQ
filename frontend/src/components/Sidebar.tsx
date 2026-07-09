"use client";
import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';

const NAV_ITEMS = [
  { id: 'pathway', label: 'Pathway Overview' },
  { id: 'discovery', label: 'Discovery & Leagues' },
  { id: 'regional', label: 'Regional Talent' },
  { id: 'centres', label: 'Centres & Academies' },
  { id: 'sponsors', label: 'Sponsor Pipeline' },
  { id: 'profiles', label: 'Profile Directory' }
];

export default function Sidebar() {
  const [activeId, setActiveId] = useState('pathway');

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        });
      },
      { rootMargin: '-20% 0px -70% 0px', threshold: 0.1 }
    );

    NAV_ITEMS.forEach((item) => {
      const element = document.getElementById(item.id);
      if (element) observer.observe(element);
    });

    return () => observer.disconnect();
  }, []);

  const scrollTo = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      const offset = 80;
      const bodyRect = document.body.getBoundingClientRect().top;
      const elementRect = el.getBoundingClientRect().top;
      const elementPosition = elementRect - bodyRect;
      const offsetPosition = elementPosition - offset;
      window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
    }
  };

  return (
    <nav className="hidden lg:flex flex-col sticky top-24 w-64 h-[calc(100vh-6rem)] py-8 border-r border-white/10">
      <div className="mb-12 px-6">
        <h2 className="text-xl font-black tracking-tighter bg-gradient-to-r from-white to-white/50 bg-clip-text text-transparent">
          ATHLETIQ<br/>INTELLIGENCE
        </h2>
        <div className="mt-2 text-xs font-bold text-[#10E5B3] tracking-widest uppercase">
          Spring 2026 Edition
        </div>
      </div>
      
      <ul className="flex flex-col gap-2 px-4">
        {NAV_ITEMS.map((item) => (
          <li key={item.id}>
            <button
              onClick={() => scrollTo(item.id)}
              className={`w-full text-left px-4 py-3 rounded-xl transition-all duration-300 relative ${
                activeId === item.id 
                  ? 'text-white font-bold' 
                  : 'text-white/40 hover:text-white/70 hover:bg-white/5'
              }`}
            >
              {activeId === item.id && (
                <motion.div
                  layoutId="activeTab"
                  className="absolute inset-0 bg-white/10 border border-white/20 rounded-xl -z-10"
                  transition={{ type: 'spring', stiffness: 300, damping: 30 }}
                />
              )}
              {item.label}
            </button>
          </li>
        ))}
      </ul>
    </nav>
  );
}
