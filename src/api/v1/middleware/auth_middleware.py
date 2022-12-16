from src.core.schemas.AppUser import AppUser
from src.api.v1.contracts.auth import ClassicLoginUser, ClassicUserPost,ModifyUserPost
from starlette.responses import JSONResponse
from fastapi import Request, HTTPException

def find_user_by_email(email_q:str)->AppUser:
    target = AppUser.objects.get(email=email_q)
    if target is None: 
        raise HTTPException(status_code=404, detail="Email not found")
    else:
        return target
    