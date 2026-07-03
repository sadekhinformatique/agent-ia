from _common import get_api_key

API_NAME = "YOUTUBE"


def upload_video(file_path: str, title: str, description: str, tags: list[str] = None) -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel YouTube Data API v3
    # https://developers.google.com/youtube/v3/docs/videos/insert
    return {
        "platform": "youtube",
        "status": "uploaded",
        "video_id": "stub_youtube_id",
        "title": title,
    }


def update_metadata(video_id: str, title: str = None, description: str = None) -> dict:
    return {"platform": "youtube", "status": "updated", "video_id": video_id}
