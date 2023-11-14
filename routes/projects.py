from fastapi import APIRouter, UploadFile, File, Form, Request

from models import Project
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
async def post_project(proj: Project):
    newInst = project_collection.insert_one(dict(proj))
    theNew = project_collection.find_one(newInst.inserted_id)
    return project_single(theNew)

@projects.put("/{id}")
async def put_project(id: str, proj: Project):
    project_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(proj)})
    theUpdated = project_collection.find_one(ObjectId(id))
    return project_single(theUpdated)

@projects.delete("/{id}")
async def delete_project(id: str):
    project_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "deletion success"}



# file uploads
@projects.post("/upload-file")
async def upFile(file: UploadFile):
    data = await file.read()
    save_to = 'static/videos/' + str(uuid.uuid4()) + '.' + str(file.filename).split(".")[1]
    with open(save_to, 'wb') as f:
        f.write(data)
