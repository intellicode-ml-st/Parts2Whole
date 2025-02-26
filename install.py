import subprocess
import sys
from pathlib import Path

def main():
    """Just create directories and run original download script"""
    base_path = Path(__file__).parent.absolute()
        
    # Use original download script
    subprocess.run([sys.executable, "download_weights.py"], cwd=base_path)

if __name__ == "__main__":
    main() 