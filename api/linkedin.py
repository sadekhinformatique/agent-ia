from _common import get_api_key

API_NAME = "LINKEDIN"


def post_content(text: str, image_urls: list[str] = None) -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel LinkedIn API v2
    # https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/
    return {
        "platform": "linkedin",
        "status": "posted",
        "post_id": "stub_linkedin_post_id",
        "text_length": len(text),
        "image_count": len(image_urls or []),
    }


def delete_post(post_id: str) -> dict:
    return {"platform": "linkedin", "status": "deleted", "post_id": post_id}
