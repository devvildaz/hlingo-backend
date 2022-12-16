import email
from fastapi import APIRouter
from src.core.schemas.AppUser import AppUser
from src.api.v1.contracts.auth import ClassicLoginUser, ClassicUserPost,ModifyUserPost
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
from src.utils import token,auth_bearer
from src.api.v1.middleware.auth_middleware import find_user_by_email
from fastapi import Depends
import json

auth_router = APIRouter(prefix="/v1")

@auth_router.post('/register/email')
async def register_via_email(user: ClassicUserPost):
    new_user = AppUser(name=user.name, password=user.password, issuer="localhost", email=user.email)
    new_user.save()

    return JSONResponse({
        "name": new_user.name,
        "email": new_user.email,
        "issuer": new_user.issuer,
    }, status_code=201)

@auth_router.post('/login/email')
async def login_via_email(user:ClassicLoginUser):
    target=find_user_by_email(user.email)
    result = target.val_password(user.password)
    if result:
        return JSONResponse({
                'user':{
                    'id':str(target.id),
                    'name':target.name,
                    'email':target.email,
                    'score': target.score,
                },
                'token':token.create_access_token(user)          
            },status_code=200)
    else:
        return JSONResponse({
            'message': 'user no authenticated'
        }, status_code=401)


@auth_router.get('/user')
def get_users():
    return json.loads(AppUser.objects().to_json())


@auth_router.post('/user/edit')
def update_users(user: ModifyUserPost):
    modified_user = AppUser.objects(id=user.id).first()
    modified_user.name = user.name
    modified_user.score = user.score
    modified_user.update()
    return JSONResponse(
        {
            'id':str(modified_user.id),
            'name':modified_user.name,
            'email':modified_user.email,
            'score': modified_user.score,
        }
    )

@auth_router.get('/testapi')
async def test(request: Request):
    return request


@auth_router.get('/validate/token', dependencies=[Depends(auth_bearer.JWTBearer())])
def validate_token():
    return JSONResponse({
        'message':'valid token'
    })

@auth_router.get('/user/current')
def get_current_user(token_str:str =Depends(auth_bearer.JWTBearer()) ):
    payload = token.decode_jwt(token_str) 
    target=find_user_by_email(payload.get("sub"))
    return JSONResponse({
                    'id':str(target.id),
                    'name':target.name,
                    'email':target.email,
                    'score': target.score,
                },
                status_code=200)
