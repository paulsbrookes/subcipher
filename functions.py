import numpy as np
from key import Key
import itertools

default_alpha = 'abcdefghijklmnopqrstuvwxyz '

def remove_duplicates(values):
    list_form = [x.tolist() for x in values]
    list_form.sort()
    filtered_list = list(list_form for list_form,_ in itertools.groupby(list_form))
    filtered_arrays = [np.array(x) for x in filtered_list]
    return filtered_arrays

def proliferation_generator(number):
    def proliferator(input_keys):
        dt = np.dtype(object)
        key_list = [x.array_cycle(number) for x in input_keys]
        map_list = []
        for list in key_list:
            for key in list:
                map_list.append(key.map)
        filtered_map_list = remove_duplicates(map_list)
        filtered_key_list = [Key(x) for x in filtered_map_list]
        return filtered_key_list
    return proliferator

def key_proliferation(input_keys, number):
    dt = np.dtype(object)
    key_list = [x.array_cycle(number) for x in input_keys]
    map_list = []
    for list in key_list:
        for key in list:
            map_list.append(key.map)
    filtered_map_list = remove_duplicates(map_list)
    filtered_key_list = [Key(x) for x in filtered_map_list]
    return filtered_key_list

def key_proliferation_swap(input_keys):
    dt = np.dtype(object)
    key_list = [x.array_swap() for x in input_keys]
    map_list = []
    for list in key_list:
        for key in list:
            map_list.append(key.map)
    filtered_map_list = remove_duplicates(map_list)
    filtered_key_list = [Key(x) for x in filtered_map_list]
    return filtered_key_list

def key_proliferation3(input_keys):
    dt = np.dtype(object)
    key_list = [x.array_cycle() for x in input_keys]
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
    if number_returned > len(ranking) - 1:
        number_returned = len(ranking) - 1
    top_key_list = [key_list[x] for x in ranking[0:number_returned]]
    return top_key_list

def metric_function(decryption_attempt, natural_sample):
    decryption_attempt.triplet_frequencies()
    difference = abs(natural_sample.rates - decryption_attempt.rates)
    difference = np.absolute(difference) + 1e-12
    metric = -np.sum(1/difference)
    return metric

def metric_function2(decryption_attempt, natural_sample):
    decryption_attempt.quadruplet_frequencies()
    difference = abs(natural_sample.rates - decryption_attempt.rates)
    difference = np.absolute(difference) + 1e-16
    metric = -np.sum(1/difference)
    return metric

def closeness(map):
    differences = [abs(x-i) for i, x in enumerate(map)]
    return np.sum(differences)

def triplet_dictionary_metric(decryption_attempt, natural_sample, alpha=default_alpha):
    decryption_attempt.triplet_frequency_dictionary()
    metric = 0
    for group in decryption_attempt.rate_dictionary:
        indices = tuple([alpha.find(group[i]) for i in range(3)])
        metric += 1/(natural_sample.triplet_rates[indices]+1e-12)
    return metric

def quadruplet_dictionary_metric(decryption_attempt, natural_sample, alpha=default_alpha):
    decryption_attempt.quadruplet_frequency_dictionary()
    metric = 0
    for group in decryption_attempt.rate_dictionary:
        indices = tuple([alpha.find(group[i]) for i in range(4)])
        if natural_sample.rates[indices] == 0:
            metric += 1
    return metric

def dict_metric_generator(number, epsilon=5e-6, alpha=default_alpha):
    def dict_metric(decryption_attempt, natural_sample):
        decryption_attempt.frequency_dictionary(number)
        metric = 0
        for group in decryption_attempt.rate_dictionary:
            indices = tuple([alpha.find(group[i]) for i in range(number)])
            metric += 1/(natural_sample.rates[indices]+epsilon)
        return metric
    return dict_metric
