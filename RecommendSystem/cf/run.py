import time
import os
from RecommendSystem.cf.CollaborativeFiltering import UserCf


def run():
    dataset_1m = 'E:\Download\dataset\ml-1m/ratings.csv'
    dataset_20m = 'E:\Download\dataset\ml-20m\ml-20m/ratings.csv'
    assert os.path.exists(dataset_1m), \
        'File not exists in path, run preprocess.py before this.'
    print('Start..')
    start = time.time()
    movies = UserCf().calculate()
    for movie in movies:
        print(movie)
    print('Cost time: %f' % (time.time() - start))


if __name__ == '__main__':
    run()


