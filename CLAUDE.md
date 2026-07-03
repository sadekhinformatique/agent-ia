# NAIOM — Plateforme Multi-Agent Marketing

## Architecture

Un orchestrateur (Claude Code) route vers 5 agents métier spécialisés + 3 agents support.
L'orchestrateur n'écrit jamais de livrable — il route, consolide, enchaîne.

## Roster des agents

| Agent | Modèle | Rôle |
|-------|--------|------|
| Stratège | Opus | Briefs, positionnement, stratégie éditoriale |
| Créateur | Sonnet | Posts, carrousels, scripts, hooks |
| Designer | Sonnet | Prompts images, visuels, miniatures |
| Analyste | Opus | Analytics, reporting, recommandations |
| Présentateur | Sonnet | Deck PDF, pitch prospects |
| Gmail (support) | Sonnet | Intégration email |
| Fireflies (support) | Sonnet | Notes de réunion |
| CV (support) | Sonnet | CVthèque |

## Arborescence

```
briefs/          ← livrables du Stratège
content/         ← livrables du Créateur
prompts-images/  ← livrables du Designer
analytics/       ← livrables de l'Analyste
decks/           ← livrables du Présentateur
clients/{client}/
  brand.md       ← charte, ton, palette, interdits
  icp.md         ← client idéal, personas
  historique.md  ← historique des campagnes
api/             ← stubs Python (LinkedIn, YouTube, etc.)
dashboard/       ← Next.js 16 (interface web)
backend/         ← FastAPI (port 8000)
```

## Conventions transverses

1. Chaque livrable a un frontmatter YAML obligatoire :
   ```yaml
   ---
   client: string
   campagne: string
   agent: string
   date: YYYY-MM-DD
   version: semver
   statut: brouillon|relecture|final
   ---
   ```
2. Tout agent doit lire `clients/{client}/brand.md` avant de produire.
3. Interdictions de marque = bloquantes. Si violées, le livrable est rejeté.
4. Les livrables sont versionnés dans leurs dossiers respectifs.
5. L'orchestrateur ne produit jamais de contenu — il délègue toujours.
