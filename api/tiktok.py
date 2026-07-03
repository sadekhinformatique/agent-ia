from _common import get_api_key

API_NAME = "TIKTOK"


def upload_video(video_path: str, description: str) -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel TikTok Business API
    # https://developers.tiktok.com/
    return {
        "platform": "tiktok",
        "status": "uploaded",
        "video_id": "stub_tiktok_id",
        "description_length": len(description),
    }
