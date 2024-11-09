def raise_detail_message(title: str, status: int, detail: str) -> dict:
    return {
        "title": title,
        "status": status,
        "detail": detail
    }