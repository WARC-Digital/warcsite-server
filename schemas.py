def project_single(proj) -> dict:
    return {
        "id": str(proj["_id"]),
        "title": proj["title"],
        "description": proj["description"],
        "client": proj["client"]
    }

def projects_multi(projs) -> list:
    return [project_single(proj) for proj in projs]