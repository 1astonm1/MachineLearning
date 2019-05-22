import time
import os
from RecommendSystem.lfm.lfm import LFM, Corpus


def run():
    dataset_1m = 'F:\Download\dataset\ml-1m/ratings.csv'
    assert os.path.exists(dataset_1m), \
        'File not exists in path, run preprocess.py before this.'
    print('Start..')
    start = time.time()
    if not os.path.exists('data/lfm_items.dict'):
        Corpus.pre_process()
    if not os.path.exists('data/lfm.model'):
        LFM().train()
    movies = LFM().predict(user_id=1)
    for movie in movies:
        print(movie)
    print('Cost time: %f' % (time.time() - start))


if __name__ == '__main__':
    run()
