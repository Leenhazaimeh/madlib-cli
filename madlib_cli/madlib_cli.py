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
        print(" Pleaes make sure that you are entr the correct path")
        raise



def parse_template(text):
    parse = re.findall(r'\{(.*?)\}', text)
    for word in parse:
        text = text.replace(word, '', 1) 
    return (text,tuple(parse))


def user_input(q):
    inputs=[]
    for i in q:
      ask = input(f"please insert a word:  {i} ")
      inputs.append(ask)
    return inputs

def merge(text, parse):
    new_text = text.format(*parse)
    with open('assests/parse_merge.text', 'w') as output:
        output.write(new_text)
    return new_text