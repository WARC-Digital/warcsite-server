from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated

from models import Project, hostURL
from schemas import projects_multi, project_single
from configs.db import project_collection
from bson import ObjectId

import uuid

projects = APIRouter()

# CRUDs
@projects.get("/")
async def get_projects():
    projects = projects_multi(project_collection.find())
    return projects

@projects.post("/")
async def post_project(
        title: Annotated[str, Form()],
        description: Annotated[str, Form()],
        client: Annotated[str, Form()],
        file: Annotated[UploadFile, File()],
    ):
    data = await file.read()
    save_to = 'static/videos/' + str(uuid.uuid4()) + '.' + str(file.filename).split(".")[1]
    with open(save_to, 'wb') as f:
        f.write(data)

    vidLink: str = hostURL + save_to
    proj = {
        "title": title,
        "description": description,
        "client": client,
        "videoLink": vidLink
    }
    print(proj)
    newInst = project_collection.insert_one(proj)
    theNew = project_collection.find_one(newInst.inserted_id)
    return project_single(theNew)

@projects.put("/{id}")
async def update_project(id: str, proj: Project):
    project_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(proj)})
    theUpdated = project_collection.find_one(ObjectId(id))
    return project_single(theUpdated)

@projects.delete("/{id}")
async def delete_project(id: str):
    project_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "deletion success"}
