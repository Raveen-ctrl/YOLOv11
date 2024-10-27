
import torch
from models.custom_model import YourModel  # replace with actual model import

def custom(path):
    # Function to load your custom YOLOv11 model
    model = YourModel()  # replace with model initialization
    model.load_state_dict(torch.load(path))
    model.eval()
    return model
