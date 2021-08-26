import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from api.config import get_config
from api.public import api as public_api
from api.utils.logger import logger_config
from api.db import db


logger = logger_config(__name__)

settings = get_config()
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    docs_url="/",
    # openapi_tags=tags_metadata, # to provide custom information on the swagger
)

app.include_router(public_api)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prometheus metrics: https://prometheus.io/
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)


logger.info(
    "FastAPI Mongo Async API has been launched for %s environment!",
    settings.ENVIRONMENT,
)


# here comes fastapi magic
@app.on_event("startup")
async def startup():
    logger.info("db connection startup")
    await db.connect_to_database(path=settings.DB_URI)


@app.on_event("shutdown")
async def shutdown():
    logger.info("db connection startup")
    await db.close_database_connection()
