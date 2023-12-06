import numpy as np
import torch
from torch import nn

class CrossEntropyLoss(nn.Module):
    def __init__(self, weight=None, ignore_index=-100):
        super().__init__()
        self.weight = weight
        self.ignore_index = ignore_index

    def forward(self, logits, labels):
        C = logits.shape[1]

        offset_logits = logits - logits.max(dim=1, keepdim=True).values
        s = offset_logits.exp().sum(dim=1, keepdim=True)
        log_prob = offset_logits - s.log()
        if self.weight != None:
            weight = self.weight.view(1, C, 1).repeat(logits.shape[0], 1, logits.shape[2])
            log_prob *= weight
            if self.ignore_index in range(0, C):
                weight[:, self.ignore_index] = 0

            w_y = torch.gather(weight, dim=1, index=labels.unsqueeze(1))
            print(w_y)
            print(w_y.view(-1))
            weightSum = w_y.view(-1).sum()

        if self.ignore_index in range(0, C):
            log_prob[:, self.ignore_index] = 0

        l = - torch.gather(log_prob, dim=1, index=labels.unsqueeze(1)).squeeze()
        if self.weight == None:
            loss = l.view(-1).mean()
        else:
            loss = l.view(-1).sum() / weightSum
        return loss

B = 2
N = 2
C = 4
logits = torch.randn(B,C,N)+1000000000000 # 大正数用来测试logSoftmax溢出
labels= torch.randint(0,C,(B,N))
weights = torch.randn(C)
ignore_index = torch.randint(0,C,()).item()

loss1 = nn.CrossEntropyLoss(weight=weights,ignore_index=ignore_index)
print(loss1(logits,labels))
loss3 = CrossEntropyLoss(weight=weights,ignore_index=ignore_index)
print(loss3(logits,labels))
# tensor(1.1413)
# tensor(1.1413)