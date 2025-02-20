import os
from config import client

def translate_text(stanza, commentaries):
    prompt = f"""
    Translate the following Tibetan stanza into English. Return only the translation of the stanzas in stanza format.
    
    Stanza:
    {stanza}
    
    {commentaries}
    """
    
    response = client.chat.completions.create(
        model="gpt-4o",
        max_tokens=2048,
        messages=[
                {
                "role": "system",
                "content": "You will be provided with a Tibetan stanza and its commentaries, and your task is to translate the stanza into English. You can refer to the commentaries to understand the meaning of the stanza."
            },
                {"role": "user", "content": prompt},
                  ],
        temperature=0.1
    )
    return response.choices[0].message.content 

stanza = "ཇི་ལྟར་མཐོང་ཐོས་ཤེས་པ་དག །\nའདིར་ནི་དགག་པར་བྱ་མིན་ཏེ། །\nའདིར་ནི་སྡུག་བསྔལ་རྒྱུར་གྱུར་པ། །\nབདེན་པར་རྟོག་པ་བཟློག་བྱ་ཡིན། །"
commentaries = """Commentaries:  
    Commentary 1:
    ཇི་ལྟར་མཐོང་ཐོས་དང་ཤེས་པ་འདི་དག་མ་བརྟག་ཉམ་དགའ་ཙམ་གྱི་དབང་དུ་བྱས་ཏེ་བརྗོད་ན་ནི།འདིར་ནི་དགག་པར་བྱ་བ་མིན་ཏེ་དེ་དག་དགག་མི་ནུས་ལ་དགག་ཀྱང་མི་དགོས་པའི་ཕྱིར། འོ་ན་ཅི་ཞིག་འགོག་ཅེ་ན། འདིར་ནི་སྔུག་བསྔལ་གྱི་རྒྱུར་གྱུར་པ་དངོས་པོ་ཀུན་ལ་དེར་ཞེན་གྱི་བདེན་པར་རྟོག་པ་བཟློག་བྱ་ཡིན་ནོ། །འདིར་མཐོང་བ་མངོན་སུམ་དང༌། ཐོས་པ་གང་ཟག་གཞན་ལས་དང༌། ཤེས་པ་རྗེས་དཔག་ཚད་མའི་སྒོ་ནས་བཞག་པའི་ཐ་སྙད་ལ་འགྲེལ་ བས་བཤད་དོ། །
    Commentary 2:
    འདི་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། མཐོང་བ་དང་ཐོས་པ་ལ་སོགས་པ་ཀུན་རྫོབ་ནི་འདིར་མི་འགོག་པའི་ཕྱིར་དང་། འོ་ན་འདིར་ཅི་ཞིག་འགོག་སྙམ་པ་ལ། འདིར་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདི་ནི་སྡུག་བསྔལ་ཐམས་ཅད་འབྱུང་བའི་རྒྱུ་དངོས་པོར་ཞེན་པ་དགག་པའི་ཕྱིར། ཡང་དག་པའི་རང་བཞིན་འགོག་གོ་སྙམ་དུ་བསམས་པའོ།
    Commentary 3:
    གལ་ཏེ་དེ་ལྟར་ན་ཡང་ཤེས་པ་རིག་པ་མེད་ན་དེ་ཇི་ལྟར་མཐོང་ངོ་འདི་ཐོས་སོ་འདི་ཤེས་སོ་ཞེས་བྱ་བའི་ཐ་སྙད་དུ་འགྱུར་རོ་ཞེ་ན། ཇི་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། ། མཐོང་བ་ལ་སོགས་པའི་ཐ་སྙད་དག་འཇིག་རྟེན་འདིར་དགག་པར་བྱ་བ་མ་ཡིན་པ་དེ་ཁོ་ནའོ། ། འོན་ཀྱང་འདིར་ནི་འཁོར་བའི་སྡུག་བསྔལ་མ་ལུས་པའི་རྒྱུར་འགྱུར་བའི་དངོས་པོར་ཀུན་རྟོག་པ་ནི་གདོན་ཆེན་པོས་བདེན་པ་ཉིད་དུ་སྒྲོ་བཏགས་པ་བྱས་པ་གང་ཡིན་པ་དེ་དགག་པར་བྱ་བ་ཡིན་པས་སྐྱོན་མེད་དོ། ། གཞན་ཡང་ཁྱོད་ཀྱིས་ཇི་སྐད་དུ། གལ་ཏེ་འཁྲུལ་པ་ཡང་མེད་ན། ། ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་པ་དེ་ལ་ཡང་བརྗོད་པར་བྱ་སྟེ།"""



translation = translate_text(stanza, commentaries)
print(translation)
