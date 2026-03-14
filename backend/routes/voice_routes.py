from fastapi import APIRouter,UploadFile
from tools.voice_transcribe import transcribe_voice

router=APIRouter()

@router.post("/voice")

async def voice(file:UploadFile):

    path=f"temp_{file.filename}"

    with open(path,"wb") as f:
        f.write(await file.read())

    text=transcribe_voice(path)

    return{"transcript":text}