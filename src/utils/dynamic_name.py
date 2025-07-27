def add_text(text:str, cond:bool = True) -> str:
    return text if cond else ''

def path_index(path_list_1:list, path_list_2:list, index:int, cond:bool = True):
    return path_list_1[index] if cond else path_list_2[index]