import json

# Load the JSON data from the 'scores' file
with open('scores.json', 'r') as json_file:
    input_data = json.load(json_file)

# Create a dictionary to store the converted data
scores_data = {}

# Iterate through the JSON data and convert it
for utt_id, utt_data in input_data.items():
    scores_data[utt_id] = {
        'text': utt_data['text'],
        'accuracy': utt_data['accuracy'],
        'completeness': utt_data['completeness'],
        'fluency': utt_data['fluency'],
        'prosodic': utt_data['prosodic'],
        'total': utt_data['total'],
        'words': []
    }
    
    for word_data in utt_data['words']:
        scores_data[utt_id]['words'].append({
            'accuracy': word_data['accuracy'],
            'stress': word_data['stress'],
            'total': word_data['total'],
            'text': word_data['text'],
            'phones': word_data['phones'],
            'phones-accuracy': word_data['phones-accuracy']
        })

# Save the converted data as a Python file
with open('scores_data.py', 'w') as py_file:
    py_file.write('scores_data = ')
    json.dump(scores_data, py_file, indent=4)
