from _common import get_api_key

API_NAME = "INSTAGRAM"


def post_image(image_path: str, caption: str) -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel Instagram Graph API
    # https://developers.facebook.com/docs/instagram-api/
    return {
        "platform": "instagram",
        "status": "posted",
        "media_id": "stub_ig_media_id",
        "caption_length": len(caption),
    }


def post_carousel(media_paths: list[str], caption: str) -> dict:
    return {
        "platform": "instagram",
        "status": "posted",
        "type": "carousel",
        "media_count": len(media_paths),
        "media_ids": [f"stub_ig_media_{i}" for i in range(len(media_paths))],
    }
