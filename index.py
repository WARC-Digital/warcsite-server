from fastapi import FastAPI
from configs.db import db, conn
from routes.projects import projects

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(projects)






if __name__ == "__main__":
    try:
        db.command('ping')
        print('pinged, success!!')
    except Exception as e:
        print(e)