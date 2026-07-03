from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="NAIOM Backend", version="0.1.0")


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
    uvicorn.run(app, host="0.0.0.0", port=8000)
