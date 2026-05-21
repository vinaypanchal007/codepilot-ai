import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

REPOSITORIES = os.getenv("REPOSITORIES").split(",")

BASE_DIR = "./repos"