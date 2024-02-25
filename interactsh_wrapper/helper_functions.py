import pandas as pd


def empty_file(file_path):
    try:
        open(file_path, 'w').close()
    except Exception as e:
        # Log the error or handle it appropriately
        pass


def read_and_store_data(file_path, interaction_data):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.replace('\x00','')
                line = line[:-1]
                data_in_list = line.split(' ')

                link = data_in_list[0][1:-1]
                datestamp = data_in_list[-2]
                timestamp = data_in_list[-1]

                new_data = {'datetime': pd.to_datetime(datestamp + " " + timestamp), 'value': ' '.join(data_in_list[1:])}
                interaction_data[link] = pd.concat([interaction_data[link], pd.DataFrame([new_data])], ignore_index=True)

    except  Exception as e:
        # Log the error or handle it appropriately
        pass

    empty_file(file_path)


def query_data(start_time, end_time, df):
    mask = (df['datetime'] >= start_time) & (df['datetime'] <= end_time)
    result = df[mask]
    return result
