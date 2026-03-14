from fastapi import FastAPI
from database import Base,engine

from routes.interaction_routes import router as interaction_router
from routes.voice_routes import router as voice_router

Base.metadata.create_all(bind=engine)

app=FastAPI(title="AI First CRM")

app.include_router(interaction_router)

app.include_router(voice_router)


@app.get("/")

def root():

    return{"message":"AI First CRM Running"}