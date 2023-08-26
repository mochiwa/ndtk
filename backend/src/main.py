import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.rest import projects_router
from app.rest.exception_handler import add_exception_handler
from container import Container


def create_app(container: Container) -> FastAPI:
    app = FastAPI()
    app.container = container
    container.file_manager.provided().create_dir('')
    app.include_router(projects_router)
    add_exception_handler(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Location"]
    )
    return app


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    application = create_app(Container())
    uvicorn.run(application, port=8080)
