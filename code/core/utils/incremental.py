def incremental_index(saved_file):
    try:
        with open (saved_file, "r") as f:
            row_index = f.readlines()
            range_start = int(row_index[-1])
    except Exception as e:
        range_start = 0

    return range_start