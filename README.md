# reproducing-cross-lingual-alignment

## How to run the code
1. Setup the venv
   - `python3 -m venv venv`
   - `./venv/Script/activate` (for window only)
   - `pip install datasets pandas matplotlib seaborn jupyter`

## How to run the code for experiment 2: Activation patching
### For arch linux
#### Requirement
- base-devel
- pyenv
#### Steps
1. Setup venv for running activation patching experiment
   ```bash
   pyenv install 3.10.14
   ~/.pyenv/versions/3.10.14/bin/python -m venv exp2_venv
   pip install -q transformers datasets nnsight accelerate scipy jupyter
   ```
2. Run the file /notebook/activation_patching






