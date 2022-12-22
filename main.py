from typing import Union
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.sessions import SessionMiddleware
from starlette_csrf import CSRFMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics, optional_metrics

from src.core.db.db import init_database, shutdown_database
from src.api.v1.auth import auth_router
from src.api.v1.info import info_router
from src.core.settings import settings
from src.api.v1.lessons import lessons_router

app = FastAPI()


app.add_middleware(SessionMiddleware, secret_key="some-random", https_only=True)
app.add_middleware(
  PrometheusMiddleware,
  app_name=settings.app_name,
  prefix=settings.app_name,
  optional_metrics=[optional_metrics.response_body_size, optional_metrics.request_body_size],
  group_paths=True,
  buckets=[0.1, 0.25, 0.5, 1],
  skip_paths=['/health'],
  always_use_int_status=False)
app.add_route("/metrics", handle_metrics)

app.include_router(auth_router)
app.include_router(info_router)

app.include_router(lessons_router)

@app.on_event("startup")
async def init_config():
    init_database()


@app.on_event("shutdown")
async def shutdown():
    shutdown_database()

handler = Mangum(app=app)
