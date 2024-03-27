import random

# Упражнение 1:
def generate_and_reverse_list():
    int_list = random.sample(range(-100, 100), 10) 
    print(f"Original list: {int_list}")
    int_list_reversed = int_list[::-1]
    print(f"Reversed list: {int_list_reversed}")
    return int_list, int_list_reversed

# Упражнение 2: 
def merge_even_odd_index_elements():
    list_one = random.sample(range(-100, 100), 10)
    list_two = random.sample(range(-100, 100), 10)
    print(f"First list: {list_one}")
    print(f"Second list: {list_two}")
    merged_list = list_one[::2] + list_two[1::2]
    print(f"Merged list: {merged_list}")
    return list_one, list_two, merged_list

# Упражнение 3: 
def remove_duplicates():
    random_elements = [random.choice([random.randint(-10, 10), random.uniform(-10, 10), random.choice('abcdefgh')]) for _ in range(15)]
    print(f"Original list with duplicates: {random_elements}")
    unique_elements = list(set(random_elements))
    print(f"List without duplicates: {unique_elements}")
    return random_elements, unique_elements

# Упражнение 4:
def dictionary_to_tuples():
    keys = [f"key{i}" for i in range(5)]
    values = [random.choice([random.randint(-10, 10), random.uniform(-10, 10)]) for _ in range(5)]
    dictionary = dict(zip(keys, values))
    print(f"Original dictionary: {dictionary}")
    unique_values = set(dictionary.values())
    value_to_keys_tuples = [(value, [k for k, v in dictionary.items() if v == value]) for value in unique_values]
    print(f"Tuples list: {value_to_keys_tuples}")
    return dictionary, value_to_keys_tuples

# Упражнение 5: 
def find_intersection_and_create_new_dict():
    keys_one = [f"key{i}A" for i in range(5)]
    values_one = [random.choice([random.randint(1, 10), random.uniform(1, 10)]) for _ in range(5)]
    dict_one = dict(zip(keys_one, values_one))
    
    keys_two = [f"key{i}B" for i in range(5)]
    values_two = [random.choice([random.randint(1, 10), random.uniform(1, 10)]) for _ in range(5)]
    dict_two = dict(zip(keys_two, values_two))
    
    print(f"First dictionary: {dict_one}")
    print(f"Second dictionary: {dict_two}")
    
    intersection = set(dict_one.values()) & set(dict_two.values())
    
    new_dict = {k: v for d in [dict_one, dict_two] for k, v in d.items() if v in intersection}
    print(f"New dictionary with intersection: {new_dict}")
    return dict_one, dict_two, new_dict

# Выполнение всех упражнений
results = {}
results['exercise_1'] = generate_and_reverse_list()
results['exercise_2'] = merge_even_odd_index_elements()
results['exercise_3'] = remove_duplicates()
results['exercise_4'] = dictionary_to_tuples()
results['exercise_5'] = find_intersection_and_create_new_dict()
results
