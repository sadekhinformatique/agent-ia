import Link from "next/link";

const agents = [
  { id: "strategist", name: "Stratège", role: "Briefs, positionnement, stratégie éditoriale", icon: "🎯" },
  { id: "creator", name: "Créateur", role: "Posts, carrousels, scripts, hooks", icon: "✍️" },
  { id: "designer", name: "Designer", role: "Prompts images, visuels, miniatures", icon: "🎨" },
  { id: "analyst", name: "Analyste", role: "Analytics, reporting, recommandations", icon: "📊" },
  { id: "presenter", name: "Présentateur", role: "Deck PDF, pitch prospects", icon: "📽️" },
];

export default function Home() {
  return (
    <div className="min-h-screen p-8">
      <header className="mb-12">
        <h1 className="text-4xl font-bold text-naiom-purple">NAIOM</h1>
        <p className="text-lg text-naiom-teal mt-2">5 agents, 1 orchestrateur, 0 confusion</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {agents.map((agent) => (
          <Link key={agent.id} href={`/agents/${agent.id}`}>
            <div className="border border-naiom-purple/30 rounded-lg p-6 hover:border-naiom-teal transition-colors cursor-pointer bg-white/5">
              <div className="text-3xl mb-3">{agent.icon}</div>
              <h2 className="text-xl font-semibold text-naiom-text">{agent.name}</h2>
              <p className="text-sm text-gray-400 mt-1">{agent.role}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
