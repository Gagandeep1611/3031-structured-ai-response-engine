from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.aws_help import services

router = APIRouter()


@router.post("/stream_chat")
async def aws_stream_help(prompt: str):
    return StreamingResponse(
        services.get_help_streaming(prompt), media_type="text/plain"
    )


@router.post("/chat")
def aws_help(prompt: str):
    return services.get_help(prompt)
