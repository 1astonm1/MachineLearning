from numpy import random


def split_data(data, M, k, seed):   # 把数据随机分成测试集和训练集
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return test, train
