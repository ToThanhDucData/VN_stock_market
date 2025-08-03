def get_cond(cond:bool):
    return cond

def add_text(text:str, cond:bool = True) -> str:
    return text if cond else ''