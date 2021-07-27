import re
from typing import Text

print(
    
     """
     
     
     
     Welcome to Madlib game, 
     
     
     
     
      """
     
     
     )



def read_template(path):
    try:
        with open(path, "r") as file:
            file = file.read()
        return file.strip()
    except FileNotFoundError:
        raise



    def parse_template(text):
    parse = re.findall(r'\{(.*?)\}', text)
    for word in parse:
        text = text.replace(word, '', 1)
    return (text, tuple(parse))


    def merge(text, parse):
    new_text = text.format(*parse)
    with open('assets/parse_merge.text', 'w') as output:
        output.write(new_text)
    return new_text