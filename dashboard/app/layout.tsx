import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "NAIOM Platform",
  description: "5 agents, 1 orchestrateur, 0 confusion",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="fr">
      <body className="bg-naiom-bg text-naiom-text font-sans antialiased">
        {children}
      </body>
    </html>
  );
}
