import os

def create_app(directory):
    current_path = os.getcwd()
    path = os.path.join(current_path, directory)
    os.mkdir(path)

    with open(os.path.join(path, "__init__.py"), "w") as f:
        pass

    with open(os.path.join(path, "models.py"), "w") as f:
        f.write("from server.connection import Base\n")
        f.write("# Add model to migrations/env.py\n\n")

    with open(os.path.join(path, "schemas.py"), "w") as f:
        f.write("from pydantic import BaseModel\n\n")

    with open(os.path.join(path, "router.py"), "w") as f:
        f.write("# Add this router to main.py\n\n")

    with open(os.path.join(path, f"test_{directory}.py"), "w") as f:
        f.write("from fastapi.testclient import TestClient\n\n")
        f.write("from ..main import app\n\n")
