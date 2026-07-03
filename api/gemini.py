from _common import get_api_key

API_NAME = "GEMINI"


def generate_image(prompt: str, aspect_ratio: str = "16:9") -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel Gemini API
    return {
        "platform": "gemini",
        "status": "generated",
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "url": "https://storage.googleapis.com/stub/gemini_image.png",
    }
