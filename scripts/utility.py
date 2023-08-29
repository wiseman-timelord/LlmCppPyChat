# utility.py

# imports
import yaml
import glob
import os
from scripts import model as model_module 


# function to list all available models
def list_available_models():
    return glob.glob("./models/*.bin")

# function to read from YAML file
def read_yaml(file_path='./cache/config.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# function to write to YAML file
def write_to_yaml(key, value, file_path='./cache/config.yaml'):
    data = read_yaml(file_path)
    if value is None:
        value = "Empty"
    data[key] = value
    ordered_keys = [
        'human_name', 'human_current',
        'model_name', 'model_role', 'model_current', 
        'model_previous1', 'model_previous2', 'model_previous3',
        'model_motivation', 'scenario_location', 'session_history'
    ]
    ordered_data = {k: data.get(k, "Empty") for k in ordered_keys}
    with open(file_path, 'w') as file:
        yaml.dump(ordered_data, file)

# shift responses for the model only
def shift_responses():
    data = read_yaml()
    data['model_previous3'] = data['model_previous2']
    data['model_previous2'] = data['model_previous1']
    data['model_previous1'] = data['model_current']
    write_to_yaml('model_previous3', data['model_previous3'])
    write_to_yaml('model_previous2', data['model_previous2'])
    write_to_yaml('model_previous1', data['model_previous1'])


# function to summarize responses and update session history
def summarize_responses(data):
    data = read_yaml()
    
    # Determine which summarize prompt to use based on the conversation state
    if data['human_previous'] == "Empty" and data['model_previous'] == "Empty":
        summarize_file = "./prompts/summarize1.txt"
    elif data['session_history'] == "Empty":
        summarize_file = "./prompts/summarize2.txt"
    else:
        raise ValueError("Invalid state for summarization")
    
    summarized_text = model_module.summarize(data['human_previous'], data['model_previous'], summarize_file)
    
    write_to_yaml('recent_statements', summarized_text)
    consolidated_history = model_module.consolidate(data['session_history'], summarized_text)
    write_to_yaml('session_history', consolidated_history)
    
    if consolidated_history == "Empty":
        consolidated_history = summarized_text.strip()
    if data['model_current'] is None:
        data['model_current'] = ""
    if data['human_current'] is None:
        data['human_current'] = ""
        
    updated_session_history = consolidated_history + " " + data['model_current'] + " " + data['human_current']
    write_to_yaml('session_history', updated_session_history)

# function to clear all keys to "Empty" at the start of the program
def clear_keys():
    print(" Resetting config.yaml...")
    if os.path.exists('./cache/config.yaml'):
        print(" ...config.yaml keys wiped.\n\n")
        keys_to_clear = ['human_name', 'human_current', 'human_previous', 'model_name', 'model_role', 'model_current', 'model_previous', 'recent_statements', 'session_history']
        for key in keys_to_clear:
            write_to_yaml(key, "Empty")
    else:
        print(" File config.yaml missing!\n")