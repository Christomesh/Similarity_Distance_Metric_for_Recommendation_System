import csv

# list of features to retrive from the dataset
features_to_retrieve = ['acousticness', 'artists', 'danceability', 'energy', 'id', 'liveness',
                            'loudness', 'name', 'popularity', 'speechiness', 'tempo','valence']


def load_dataset():
    """
    This fuction loads the dataset.csv and stores it in a dictionary,
    the dataset column names and its values being used as key-value pair in dictionary
    return:
        a dictionary format of the dataset
    """
    def get_mulList(*args):
        return map(list, zip(*args))

    csv_data = open("data.csv", encoding='utf-8')
    data = list(csv.reader(csv_data))
    data_dict = dict(zip(data[0], get_mulList(*data[1:])))
    for key in list(data_dict.keys()):
        if key not in features_to_retrieve:
            del data_dict[key]
    return data_dict

# load the dataset
data_dict = load_dataset()


def artist_music_func():
    """
    This function returns artist music dictionary contains artists name, music name, and corresponding features
    """
    artist_music_dict = {}
    artist_music_features = ['artists', 'name', 'id', 'acousticness', 'danceability', 'energy', 'liveness',
                             'loudness', 'popularity', 'speechiness', 'tempo', 'valence']
    for key, value in data_dict.items():
        if key in artist_music_features:
            artist_music_dict[key] = value
    return artist_music_dict

def music_features_func():
    """
    This fuction returns  music_features dictionary contains music id, and their respective features.
    """
    music_features_dict = {}
    music_features = ['id', 'acousticness', 'danceability', 'energy', 'liveness',
                             'loudness', 'popularity', 'speechiness', 'tempo', 'valence']
    for key, value in data_dict.items():
        if key in music_features:
            music_features_dict[key] = value
    return music_features_dict

