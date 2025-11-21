'''
手写 语义分割 Softmax + Cross Entropy Loss（多分类）
'''

import torch
# import torch.nn.functional as F


def softmax(logits):
    """
    logits: (N, 5, H, W)
    return: softmax probabilities (same shape)
    """
    # 手写 softmax（不调用 F.softmax）
    max_vals, _ = torch.max(logits, dim=1, keepdim=True)
    '''
    为了数值稳定性，减去每行的最大值, 避免 exp() 过大溢出 
    softmax函数具有平移不变性，即对于输入向量 x 和任意常数 c，有 softmax(x) = softmax(x + c)。
    通过减去每行的最大值，可以防止指数函数计算时出现数值溢出的问题，从而提高计算的稳定性。
    '''
    exp_x = torch.exp(logits - max_vals)
    probs = exp_x / torch.sum(exp_x, dim=1, keepdim=True)#将dim=1 （channel，类别）维度的值相加，保持维度不变
    return probs


def cross_entropy_loss(logits, targets):
    """
    手写 cross entropy loss（与 nn.CrossEntropyLoss 等价）

    logits: (N, 5, H, W)
    targets: (N, H, W)   每个像素是 0~4 的类别标签

    return: 标量 loss
    """

    N, C, H, W = logits.shape

    # ---- 1. softmax ----
    probs = softmax(logits)  # shape: (N,5,H,W) 经过softmax变为概率分布

    # ---- 2. 展平方便计算 ----
    probs = probs.permute(0, 2, 3, 1).reshape(-1, C)  # (N*H*W, 5)  #将类别维度放到最后，再展平
    '''
    [[probs[0,0],probs[0,1],...,probs[0,c-1],
    [probs[1,0],probs[1,1],...,probs[1,c-1],
    ...
    [probs[N*H*W-1,0],probs[N*H*W-1,1],...,probs[N*H*W-1,c-1]]]
    '''
    
    targets = targets.reshape(-1)  # (N*H*W) #展平标签
    '''
    [target[0],target[1],...,target[N*H*W-1]]
    '''

    # ---- 3. 选择对应的类别概率 ----
    #
    correct_probs = probs[torch.arange(probs.size(0)), targets]
    # correct_probs shape: (N*H*W,)
    #行号是每个像素点的索引，列号是对应的类别标签，从而选出每个像素点对应类别的概率值
    '''
    [probs[0,target[0]],probs[1,target[1]],...,probs[N*H*W-1,target[N*H*W-1]]]
    '''

    # ---- 4. 交叉熵：-log(p) ----
    loss = -torch.log(correct_probs + 1e-12) 
    # 对于每个类别
    # 预测错误时，实际标签为0，loss=-0*log(p错误)=0，所以不会对loss有贡献
    # 预测正确时，实际标签为1，loss=-1*log(p正确)=-log(p正确)，p正确越大，loss越小

    return loss.mean()


# ------------------------- 测试 -------------------------
if __name__ == "__main__":
    logits = torch.randn(2, 5, 4, 4)  # batch=2, 5 类, 4x4 图像
    targets = torch.randint(0, 5, (2, 4, 4))  # 随机标签

    loss = cross_entropy_loss(logits, targets)
    print("CE loss =", loss.item())
