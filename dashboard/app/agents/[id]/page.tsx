import { notFound } from "next/navigation";
import Link from "next/link";

const agentsData: Record<string, { name: string; role: string; model: string; frameworks: string[] }> = {
  strategist: {
    name: "Stratège",
    role: "Briefs, positionnement, stratégie éditoriale",
    model: "Opus",
    frameworks: ["StoryBrand", "Value Proposition Canvas", "Jobs To Be Done", "SCQA"],
  },
  creator: {
    name: "Créateur",
    role: "Posts, carrousels, scripts, hooks",
    model: "Sonnet",
    frameworks: ["PAS", "AIDA", "FAB", "Hook-Story-Offer"],
  },
  designer: {
    name: "Designer",
    role: "Prompts images, visuels, miniatures",
    model: "Sonnet",
    frameworks: ["Palette NAIOM", "Formats 16:9 / 1:1 / 9:16"],
  },
  analyst: {
    name: "Analyste",
    role: "Analytics, reporting, recommandations",
    model: "Opus",
    frameworks: ["OKR", "Funnel Analysis", "Cohort Analysis"],
  },
  presenter: {
    name: "Présentateur",
    role: "Deck PDF, pitch prospects",
    model: "Sonnet",
    frameworks: ["SCQA", "Structure 21 min / 10 slides"],
  },
};

export default function AgentPage({ params }: { params: { id: string } }) {
  const agent = agentsData[params.id];
  if (!agent) notFound();

  return (
    <div className="min-h-screen p-8">
      <Link href="/" className="text-naiom-teal hover:underline mb-8 inline-block">&larr; Retour</Link>
      <h1 className="text-3xl font-bold text-naiom-purple">{agent.name}</h1>
      <p className="text-gray-400 mt-2">{agent.role}</p>
      <p className="mt-6">
        <span className="font-semibold">Modèle :</span> {agent.model}
      </p>
      <h2 className="text-xl font-semibold mt-6 mb-3">Frameworks</h2>
      <ul className="list-disc list-inside space-y-1 text-gray-300">
        {agent.frameworks.map((f) => <li key={f}>{f}</li>)}
      </ul>
    </div>
  );
}
