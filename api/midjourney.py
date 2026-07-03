from _common import get_api_key

API_NAME = "MIDJOURNEY"


def imagine(prompt: str, aspect_ratio: str = "16:9", stylize: int = 100) -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel Midjourney API (via Discord ou service tiers)
    return {
        "platform": "midjourney",
        "status": "queued",
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "stylize": stylize,
        "job_id": "stub_mj_job_id",
    }


def upscale(job_id: str, variant: int = 1) -> dict:
    return {"platform": "midjourney", "status": "upscaled", "job_id": job_id, "variant": variant}
