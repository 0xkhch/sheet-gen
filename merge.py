import json
import os

dictionary_path = "resources/dictionary.txt"
dictionary = {}

with open(dictionary_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        json_character = json.loads(line.strip())
        current_character = json_character.get('character')

        # remove character from json object and use it as the key in dict
        json_character.pop('character', None)  
        dictionary[current_character] = json_character

graphics_path = "resources/graphics.txt"
with open(graphics_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        json_stroke = json.loads(line.strip())
        stroke_character = json_stroke.get('character')
        json_stroke.pop('character', None)

        # append stroke order to correct character 
        character_object = dictionary.get(stroke_character)
        combined_object = {**character_object, **json_stroke}
        dictionary[stroke_character] = combined_object 

merged_path = os.path.join("resources/", "merged.json")
with open(merged_path, 'w') as file:
    json.dump(dictionary, file, ensure_ascii=False)

assert open(merged_path, 'r') != None
print("Successfully merged files!")
