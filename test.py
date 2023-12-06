import torch
import torchvision.transforms
from PIL import Image
from torch import nn

image_path = "./imgs/dog.png"
image = Image.open(image_path)
image = image.convert('RGB')

transfrom = torchvision.transforms.Compose([torchvision.transforms.Resize((32,32)),
                                            torchvision.transforms.ToTensor()])
image = transfrom(image)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3,32,5,1,2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,32,5,1,2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,64,5,1,2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64*4*4,64),
            nn.Linear(64,10)
        )
    def forward(self,x):
        x = self.model(x)
        return x

model = torch.load("./models/tudui_19.pth", map_location=torch.device('cpu'))

image = torch.reshape(image, (1,3,32,32))
model.eval()
with torch.no_grad():
    output = model(image)
print(output)
print(output.argmax(1))
