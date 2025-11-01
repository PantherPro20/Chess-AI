import torch
import torch.nn as nn
import torch.nn.functional as F

class EvaluationNet(nn.Module):
    """
    A simple convolutional neural network for evaluating chess positions.
    """
    def __init__(self):
        super(EvaluationNet, self).__init__()
        self.conv1 = nn.Conv2d(12, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 8 * 8, 256)
        self.fc2 = nn.Linear(256, 1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1, 32 * 8 * 8)
        x = F.relu(self.fc1(x))
        x = torch.tanh(self.fc2(x))
        return x
