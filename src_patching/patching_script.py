import subprocess
import sys
from pathlib import Path

# Edit these to change to different model/data
language_folder = "belebele_mexa"
dataset = "belebele"
model = "Llama3.1"

# Data location
path = Path(__file__).resolve().parent.parent  / "data" / language_folder

# Find the stems of all txt files in the data location
file_stems = [f.stem for f in path.iterdir() if f.is_file() and f.suffix == ".txt"]

print("Running...")

# Execute code on stem 
for f in file_stems:
    print("Working on " + f)
    
    command = [
    sys.executable, str(Path(__file__).resolve().parent / "mcqa_evaluator.py"),
    "--dataset", dataset,
    "--lang", f,
    "--llm_name", model,
    "--mc_key", "ABCD",
    "--save_dir", "results/patching"
    ]
    
    output = subprocess.run(command)

