# Create .venv then run the following command to install dependencies
# pip install -q torch transformers datasets nnsight bitsandbytes accelerate numpy pandas kaggle

#setup the Kaggle API credentials
import kaggle

kaggle.api.authenticate()
