import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

project_name = "Text-Summarization"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components.py/__init__.py",
    f"src/{project_name}/utils.py/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    file_path = Path(filepath)
    file_dir, filename = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for the file {filename}")

    if (not os.path.exists(file_path) or (os.path.getsize(file_path) == 0)):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path} and is not empty.")
