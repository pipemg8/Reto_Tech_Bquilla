from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.routes import router
from app.infra.db import init_db
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="OrderService API")

@app.on_event("startup")
async def on_startup():
    await init_db()
    logger.info("Database initialized")

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": f"Internal error: {str(exc)}"}
    )

app.include_router(router)
