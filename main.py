import os
from src.tools import get_system_resume

version = os.getenv('VERSION',1.0)

print(get_system_resume())
print(f"Version : {version}")

