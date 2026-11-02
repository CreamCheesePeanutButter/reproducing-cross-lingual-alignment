# reproducing-cross-lingual-alignment

## Setup the python virtual environment

### For Windows

#### Requirement

uv : can get using winget `winget install astral-sh.uv`

#### Steps

Setup the venv

- `uv venv --python 3.10.14`
- `.\.venv\Scripts\Activate.ps1`

  **For running datavis**

- `pip install datasets pandas matplotlib seaborn jupyter`

  **For running experiment 2: Activation patching**

- `uv pip install transformers datasets nnsight accelerate scipy jupyter python-dotenv huggingface_hub`

<!-- ### For arch linux (ignore this)

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
2. Run the file /notebook/activation_patching -->
