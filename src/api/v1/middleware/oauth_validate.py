from fastapi import FastAPI, Request
from starlette.types import ASGIApp, Scope, Receive, Send
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


urls = [
    
]

class ValidateMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
    
    async def dispatch(self, request : Request, call_next):
        session = request.cookies['session']
        print(request.url.path)
        response = await call_next(request)
        #return JSONResponse({'hellp': 'world'}, status_code=200)
        return response