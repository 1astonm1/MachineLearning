import time
import os
from RecommendSystem.cf.CollaborativeFiltering import UserCf

def run():
    dataset_1m = 'F:\Download\dataset\MovieLens\ml-1m/ratings.csv'
    dataset_20m = 'F:\Download\dataset\ml-20m/ratings.csv'
    assert os.path.exists(dataset_1m), \
        'File not exists in path, run preprocess.py before this.'
    print('Start..')
    start_all = time.time()
    for i in range(1, 20):
        start = time.time()
        print("user %d: " % i)
        movies = UserCf().calculate(i, 10)
        for movie in movies:
            print(movie)
        print('Cost time: %f' % (time.time() - start))
    alltime = time.time() - start_all
    print("All time: {0}" .format(alltime))
    print("Average Time:{0}".format(alltime/19))


if __name__ == '__main__':
    run()


