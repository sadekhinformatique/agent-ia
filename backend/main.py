from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="NAIOM Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class CarouselRequest(BaseModel):
    text: str


class ReportRequest(BaseModel):
    analytics: dict


class PromptRequest(BaseModel):
    prompt: str
    aspect_ratio: str = "16:9"


@app.get("/health")
def health():
    return {"status": "ok", "service": "naiom-backend"}


@app.post("/api/carousels/generate")
def generate_carousel(req: CarouselRequest):
    return {"status": "generated", "slides": 8, "text": req.text}


@app.post("/api/reports/generate")
def generate_report(req: ReportRequest):
    return {"status": "generated", "format": "pdf-visual"}


@app.post("/api/nano-banana/generate")
def generate_image(req: PromptRequest):
    return {"status": "generated", "prompt": req.prompt, "url": "stub_gemini_url"}


@app.post("/api/integrations/{platform}/sync")
def sync_integration(platform: str):
    return {"platform": platform, "status": "synced"}


if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
