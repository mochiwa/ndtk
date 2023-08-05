import uvicorn
from fastapi import FastAPI

from app.rest import projects_router
from container import Container


def create_app(container: Container) -> FastAPI:
    app = FastAPI()
    app.container = container
    container.file_manager.provided().create_dir('projects')
    app.include_router(projects_router)
    return app


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    application = create_app(Container())
    uvicorn.run(application, port=8080)