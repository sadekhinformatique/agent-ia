from _common import get_api_key

API_NAME = "CANVA"


def create_design(template_id: str, modifications: dict) -> dict:
    key = get_api_key(API_NAME)
    if not key:
        return {"error": f"{API_NAME}_API_KEY not configured"}
    # TODO: implémenter l'appel Canva API
    # https://www.canva.com/developers/
    return {
        "platform": "canva",
        "status": "created",
        "design_id": "stub_canva_design_id",
        "url": "https://canva.com/design/stub",
    }


def export_pdf(design_id: str) -> dict:
    return {"platform": "canva", "status": "exported", "format": "pdf", "design_id": design_id}
