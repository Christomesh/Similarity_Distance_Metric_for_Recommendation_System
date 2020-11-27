import numpy as np #if not install use "pip install numpy"
from load_dataset_module import artist_music_func, music_features_func

def helper_func(data_dict):
    """
    This function helps modified the data_dict
    such that the id which is unique for each entry of the dataset is now set as the keys of the dictionary,
    while the corresponding features are now values of the dictionary

    return:
            a dictionary where the id is the key and others set as value.
    """
    numeric_features = ['acousticness', 'danceability', 'energy', 'liveness',
                        'loudness', 'popularity', 'speechiness', 'tempo', 'valence']
    numerical_feature_values = []
    for key in data_dict.keys():
        if key in numeric_features:
            numerical_feature_values.append(data_dict[key])
    numerical_feature_values = np.array(numerical_feature_values, dtype=float).T    
    id_and_numeric_features_dict = dict(zip(data_dict['id'], numerical_feature_values))
    return id_and_numeric_features_dict

def euclidean_similarity(data_dict, id_1, id_2):
    """
    Compute Eculidean similarity between two ids using their numerical values
    and returns the result
    """
    id_value_1 = data_dict[id_1]
    id_value_2 = data_dict[id_2]
    euc_sim = np.linalg.norm(id_value_1 - id_value_2)
    return euc_sim


def cosine_similarity(data_dict, id_1, id_2):
    """
    Compute Cosine similarity between two ids using their numerical values
    and returns the result
    """
    id_value_1 = data_dict[id_1]
    id_value_2 = data_dict[id_2]
    cos_sim = np.dot(id_value_1, id_value_2) / (np.linalg.norm(id_value_1) * np.linalg.norm(id_value_2))
    return cos_sim

def pearson_similarity(data_dict, id_1, id_2):
    """
    Compute Pearson similarity between two ids using their numerical values
    and returns the result
    """
    id_value_1 = data_dict[id_1]
    id_value_2 = data_dict[id_2]
    ps_sim = np.corrcoef(id_value_1, id_value_2)[0, 1]
    return ps_sim

def jaccard_similarity(data_dict, id_1, id_2):
    """
    Compute Jaccard similarity between two ids using their numerical values
    and returns the result
    """
    id_value_1 = data_dict[id_1]
    id_value_2 = data_dict[id_2]
    intersection = len(list(set(id_value_1).intersection(id_value_2)))
    union = (len(id_value_1) + len(id_value_2)) - intersection
    return float(intersection) / union

def manhattan_similarity(data_dict, id_1, id_2):
    """
    Compute Manhattan similarity between two ids using their numerical values
    and returns the result
    """
    id_value_1 = data_dict[id_1]
    id_value_2 = data_dict[id_2]
    mah_sim = np.abs(id_value_1 - id_value_2).sum()
    return mah_sim


artist_music_dict = artist_music_func()
music_features_dict = music_features_func()

def compute_similarity(id_1, id_2, similarity_func):
    """
    This functions take two ids and the a similarity metric
    then carries out mathematical computation using the numerical values of the ids
    using the similarity metric pass and return the result.
    """
    ids_as_keys_dict = helper_func(music_features_dict)
    list_of_ids = ids_as_keys_dict.keys()
    if (id_1 in list_of_ids) and (id_2 in list_of_ids):
        result = similarity_func(ids_as_keys_dict, id_1, id_2)
        return result
    else:
        print("Ids not found")
    


def main():
    id1 = input("Enter the first music_id or artist_id: ")
    id2 = input("Enter the second music_id or artist_id: ")
    metric_choice = input("What similarity metric to use?\n\
                          Enter 1 for euclidean_similarity\n\
                          Enter 2 for cosine_similarity\n\
                          Enter 3 for pearson_similarity\n\
                          Enter 4 for jaccard_similarity\n\
                          Enter 5 for manhattan_similarity\n")

    metric_dict = {"1":euclidean_similarity, "2":cosine_similarity, 
                    "3": pearson_similarity, "4":jaccard_similarity, "5":manhattan_similarity}
    if metric_choice in metric_dict.keys():
        final_value = compute_similarity(id1, id2, metric_dict[metric_choice])
        if final_value:
            display_sim = ['##','euclidean_similarity','cosine_similarity', 'pearson_similarity', 'jaccard_similarity', 'manhattan_similarity']
            print("The {} between music_id: {} and music_id: {} is {}".format(display_sim[int(metric_choice)], id1, id2, final_value))
            
if __name__ == "__main__":
    main()


