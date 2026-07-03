from _common import get_api_key

API_NAME = "IDEOGRAM"


def generate_image(prompt: str, style: str = "auto", aspect_ratio: str = "1:1") -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel Ideogram API
    # https://docs.ideogram.ai/
    return {
        "platform": "ideogram",
        "status": "generated",
        "style": style,
        "aspect_ratio": aspect_ratio,
        "url": "https://ideogram.ai/stub/image.png",
    }
