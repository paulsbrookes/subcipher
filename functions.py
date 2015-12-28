import numpy as np
from key import Key

def remove_duplicates(values):
    output = []
    seen = []
    for value in values:
        if not np.any([np.all(value == x) for x in seen]):
            output.append(value)
            seen.append(value)
    return output

def key_proliferation(input_keys):
    dt = np.dtype(object)
    key_list = [x.array_swap() for x in input_keys]
    map_list = []
    for list in key_list:
        for key in list:
            map_list.append(key.map)
    filtered_map_list = remove_duplicates(map_list)
    filtered_key_list = [Key(x) for x in filtered_map_list]
    return filtered_key_list

def best_keys(key_list, encrypted_message, natural_sample, number_returned = 10):
    metric_list = []
    for key in key_list:
        decryption_attempt = encrypted_message.map(key)
        metric = metric_function(decryption_attempt, natural_sample)
        metric_list.append(metric)
    ranking = np.argsort(metric_list)
    top_key_list = [key_list[x] for x in ranking[0:number_returned]]
    return top_key_list

def best_keys_fast(key_list, encrypted_message, natural_sample, number_returned = 10):
    metric_list = []
    for key in key_list:
        decryption_attempt = encrypted_message.map(key)
        metric = metric_function_fast(decryption_attempt, natural_sample)
        metric_list.append(metric)
    ranking = np.argsort(metric_list)
    top_key_list = [key_list[x] for x in ranking[0:number_returned]]
    return top_key_list

def metric_function(decryption_attempt, natural_sample):
    decryption_attempt.triplet_frequencies()
    difference = abs(natural_sample.rates - decryption_attempt.rates)
    difference = np.absolute(difference) + 1e-10
    metric = -np.sum(1/difference)
    return metric

def metric_function2(decryption_attempt, natural_sample):
    decryption_attempt.triplet_frequencies()
    difference = abs(natural_sample.rates - decryption_attempt.rates)
    difference = np.absolute(difference)
    metric = -np.sum(difference)
    return metric
