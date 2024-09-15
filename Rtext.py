import string
import random
import hashlib
import time
from random_word import RandomWords
class AnyType(str):

    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

class RText:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": '', "multiline": True}),
            }
        }

    RETURN_TYPES = (any_type,"STRING",)
    #RETURN_NAMES = ("image_output_name",)
    RETURN_NAMES = ("randomtext","show_help",)
    FUNCTION = "text_random"
    CATEGORY = "Example"
    
    def text_random(self, text):
     rw = RandomWords()
     random_words = [rw.get_random_word() for _ in range(4)]
     random_string = ' '.join(random_words)
     show_help = "you need CLIP Text Encode (Prompt). it's green for some reason."
     text = random_string
     return (text, show_help,)   

    @classmethod
    def IS_CHANGED(s, text):
            #always update
            m = hashlib.sha256().update(str(time.time()).encode("utf-8"))
            return m.digest().hex()
    
# Add custom API routes, using router
from aiohttp import web
from server import PromptServer

@PromptServer.instance.routes.get("/hello")
async def get_hello(request):
    return web.json_response("hello")

NODE_CLASS_MAPPINGS = {
    "RText": RText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RText": "RText Node"
}
