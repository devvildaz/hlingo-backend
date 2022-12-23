from typing import Union
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.sessions import SessionMiddleware
from starlette_csrf import CSRFMiddleware

from src.core.db.db import init_database, shutdown_database
from src.api.v1.auth import auth_router
from src.api.v1.info import info_router
from src.core.settings import settings
from src.api.v1.lessons import lessons_router
from prometheus_fastapi_instrumentator import Instrumentator, metrics

app = FastAPI()

instrumentator=Instrumentator()
app.add_middleware(SessionMiddleware, secret_key="some-random", https_only=True)
instrumentator.add(metrics.latency(buckets=(1, 2, 3,)))
instrumentator.add(
    metrics.request_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_namespace="request_size",
        metric_subsystem="hlingo",
    )
).add(
    metrics.response_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_namespace="response_size",
        metric_subsystem="hlingo",
    )
)
app.include_router(auth_router)
app.include_router(info_router)

app.include_router(lessons_router)

@app.on_event("startup")
async def init_config():
    init_database()
    instrumentator.instrument(app).expose(app)


@app.on_event("shutdown")
async def shutdown():
    shutdown_database()

handler = Mangum(app=app)

