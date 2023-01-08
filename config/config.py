import os
import json
from pathlib import Path
from typing import Optional
def get_token(key:str,default_valye: Optional[str] = None):
    """ 토큰 추출 """
    BASE_DIR = ".discord-token/.token.json"
    with open(BASE_DIR,'r') as fp:
        secret = json.loads(fp.read())
    try:
        return secret[key]
    except EnvironmentError:
        if default_valye:
            return default_valye
        raise EnvironmentError(f'Set the {key}')