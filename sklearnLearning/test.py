from sklearn import datasets
import matplotlib.pyplot as plt
# 自带的数据集
iris = datasets.load_iris() # load_digital
test_X = iris.data
test_y = iris.target
feat_name = iris.feature_names

# 计算机产生的数据集
# 产生样本量为100，特征维数为2，有相关关系的特征维数为2，的分类数据集
X, y = datasets.make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=2, random_state=22)
# 产生样本量为100，特征维数为2，有相关关系的特征维数为2，分类数为1，噪声为0的分类数据集
X, y = datasets.make_regression(n_samples=100, n_features=2, n_informative=2, n_targets=1, noise=0.0, random_state=22)
# 可视化
plt.scatter(X, y)
plt.show()
