import pandas as pd


class Channel:
    """
    simple processing for *.dat to *.csv
    """

    def __init__(self):
        self.origin_path = 'E:\Download\dataset\ml-1m\ml-1m\{}'

    def process(self):
        print('Process user data...')
        self._process_user_data()
        print('Process movies data...')
        self._process_movies_date()
        print('Process rating data...')
        self._process_rating_data()
        print('End.')

    def _process_user_data(self, file='users.dat'):
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python',
                          names=['userID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
        f.to_csv(self.origin_path.format('users.csv'), index=False)

    def _process_rating_data(self, file='ratings.dat'):
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python',
                          names=['UserID', 'MovieID', 'Rating', 'Timestamp'])
        f.to_csv(self.origin_path.format('ratings.csv'), index=False)

    def _process_movies_date(self, file='movies.dat'):
        f = pd.read_table(self.origin_path.format(file), sep='::', engine='python',
                          names=['MovieID', 'Title', 'Genres'])
        f.to_csv(self.origin_path.format('movies.csv'), index=False)


if __name__ == '__main__':
    Channel().process()
