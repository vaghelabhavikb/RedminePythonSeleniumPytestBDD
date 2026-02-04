import json

def get_features_list(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return list(data['createFeatures'])

def get_stories_map(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data["createStories"]
    
