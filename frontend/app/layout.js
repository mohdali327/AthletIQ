import './globals.css';

export const metadata = {
  title: 'AthletIQ Intelligence Platform',
  description: 'AI-Driven Decision-Making Dashboard',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="orb orb-1"></div>
        <div className="orb orb-2"></div>
        <div className="orb orb-3"></div>
        <div className="grid-3d"></div>
        {children}
      </body>
    </html>
  );
}
