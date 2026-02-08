import os
from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    ".idea",
    ".vscode",
    ".cursor",
    "logs",
    "build",
    "dist",
    "node_modules",
    "docs",
    "db",
}
INCLUDE_EXT = {".py", ".toml", ".md", ".yml", ".yaml", ".Dockerfile", ".ts", ".tsx", ".json"}
IGNORE_FILES = {"uv.lock", "poetry.lock", "yarn.lock", "package-lock.json", "history.db"}


def generate_context() -> None:
    output_path = Path("autopostbot_context.txt")

    with output_path.open("w", encoding="utf-8") as outfile:
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

            for file in files:
                if file in IGNORE_FILES:
                    continue

                path = Path(root) / file
                if path.suffix in INCLUDE_EXT or file == "Dockerfile":
                    outfile.write(f"\n{'=' * 20}\nFILE: {path}\n{'=' * 20}\n")

                    try:
                        with path.open(encoding="utf-8") as infile:
                            outfile.write(infile.read())
                    except OSError as e:
                        outfile.write(f"Error reading file: {e}")

    print(f"Ready. File {output_path} created.")


if __name__ == "__main__":
    generate_context()
