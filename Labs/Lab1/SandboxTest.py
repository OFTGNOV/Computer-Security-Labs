import os
from pathlib import Path
import subprocess

def main():
    desktop_path = Path.home() / "Desktop" / "SandboxTestFile.txt"
    try:
        with open(desktop_path, 'w') as f:
            f.write("This file was created inside the sandbox.")
        print("Test file created on Desktop.")
    except Exception as e:
        print(f"Error creating file: {e}")
    print()

    print("Now attempting to clear the Recycle Bin...")
    try:
        subprocess.run(
            ["powershell", "-Command", "Clear-RecycleBin -Force"],
            check=True,
            shell=True
        )
        print("Recycle Bin clearance command executed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
