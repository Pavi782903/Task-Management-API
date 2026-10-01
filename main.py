from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.database import Base, engine
from app.routes.tasks import router as task_router


# Create database tables automatically
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Task Management API",
    description=(
        "REST API for managing tasks using "
        "FastAPI, Pydantic, SQLAlchemy and SQLite."
    ),
    version="1.0.0"
)


# Global validation exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation error.",
            "errors": exc.errors()
        }
    )


# Global database exception handler
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(
    request: Request,
    exc: SQLAlchemyError
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Database operation failed."
        }
    )


@app.get(
    "/",
    tags=["Root"]
)
def root():
    return {
        "message": "Task Management API is running."
    }


app.include_router(task_router)