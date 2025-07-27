def incremental_index(saved_file:str) -> int:
    try:
        with open (saved_file, "r") as f:
            row_index = f.readlines()
            range_start = int(row_index[-1])
    except:
        range_start = 0

    return range_start