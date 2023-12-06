import torch.optim
import torchvision.datasets
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import time

import myloss_fun
from model import *
import torch
from myloss_fun import *

#定义设备
device = torch.device("cpu")

#读取数据
train_data = torchvision.datasets.CIFAR10(root="../data", train=True, transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10(root="../data", train=False, transform=torchvision.transforms.ToTensor(),
                                          download=True)
#获取长度
train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练数据集长度：{}".format(train_data_size))
print("测试数据集长度：{}".format(test_data_size))

#加载数据
train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

#创建模型
tudui = Tudui()
#tudui = tudui.cuda()
tudui = tudui.to(device)

#损失函数
#loss_fn = nn.CrossEntropyLoss()
#loss_fn = loss_fn.cuda()
#loss_fn = loss_fn.to(device)
loss_fn = myloss_fun.CrossEntropyLoss()

#优化器
learning_rate = 0.01
optimizer = torch.optim.SGD(tudui.parameters(), lr=learning_rate)

total_train_step = 0    #记录训练的次数
total_test = 0          #记录测试的次数
epoch = 10              #训练的轮数
writer = SummaryWriter("./logs_train")

start_time = time.time()
for i in range(epoch):
    print("--------第{}轮训练开始----------".format(i+1))
    tudui.train()
    for data in train_dataloader:
        imgs, targets = data
        #imgs = imgs.cuda()
        #targets = targets.cuda()
        imgs = imgs.to(device)
        targets = targets.to(device)
        outputs = tudui(imgs)
        loss = loss_fn(outputs, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_train_step += 1
        if total_train_step % 100 == 0:
            end_time = time.time()
            print(end_time - start_time)
            print("训练次数：{}, Loss:{}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    #测试步骤开始
    tudui.eval()
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            # imgs = imgs.cuda()
            # targets = targets.cuda()
            imgs = imgs.to(device)
            targets = targets.to(device)
            outputs = tudui(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss += loss
            accuracy = (outputs.argmax(1) == targets).sum()
            total_accuracy += accuracy
    print("整体测试集上的Loss：{}".format(total_test_loss))
    print("整体测试集上的正确率：{}".format(total_accuracy/test_data_size))
    writer.add_scalar("test_loss", total_test_loss,total_train_step)
    writer.add_scalar("test_accuracy", total_accuracy/test_data_size, total_train_step)
    total_train_step += 1

    torch.save(tudui, "./models/tudui_{}.pth".format(i))
    print("模型已保存")

writer.close()