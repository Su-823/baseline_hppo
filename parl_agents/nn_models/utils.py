import torch


def initialize_parameters(m):
    """ From https://github.com/ikostrikov/pytorch-a2c-ppo-acktr/blob/master/model.py """
    class_name = m.__class__.__name__
    if class_name.find('Linear') != -1:
        m.weight.data.normal_(0, 1)
        m.weight.data *= 1 / torch.sqrt(m.weight.data.pow(2).sum(1, keepdim=True))
        if m.bias is not None:
            m.bias.data.fill_(0)