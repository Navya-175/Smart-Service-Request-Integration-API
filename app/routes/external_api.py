from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_current_user
from ..models import User
from ..services.external_service import fetch_post

router = APIRouter(prefix="/api/v1/external", tags=["External API"])

@router.get("/posts/{post_id}")
async def external_post(post_id: int, _: User = Depends(get_current_user)):
    try:
        return await fetch_post(post_id)
    except Exception:
        raise HTTPException(status_code=502, detail="External API could not be reached")
