import fs from "fs";
import path from "path";
import matter from "gray-matter";

const LIVRABLES_DIR = path.resolve(process.cwd(), "..");

type AgentType = "briefs" | "content" | "prompts-images" | "analytics" | "decks";

export function listLivrables(agent: AgentType) {
  const dir = path.join(LIVRABLES_DIR, agent);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((f) => f.endsWith(".md")).map((file) => {
    const raw = fs.readFileSync(path.join(dir, file), "utf-8");
    const { data } = matter(raw);
    return { file, ...data };
  });
}
