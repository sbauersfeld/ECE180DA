import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def GetData(google_sheet="Graduation Localization Form (Responses)", sheet_key="../../ece180-a1520813da23.json"):
    '''
        Get data from google form responses
        PARAMETERS:
        google_sheet - google sheet to get data from, the sheet must be shared with the email in the sheet_key
        sheet_key - the json file containing the oauth2 information needed to connect with google sheets api
        RETURNS:
        data - pandas dataframe containing google sheet data
    '''
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(sheet_key, scope)
    gc = gspread.authorize(credentials)
    wks = gc.open(google_sheet).sheet1

    data = pd.DataFrame(wks.get_all_records())

    # these column names must be updated to match any changes to the google form
    column_names = {'Timestamp': 'timestamp',
                    'What is your ID?': 'id',
                    'What is the ID of the person sitting in front of you? Use 0 if the person in front of you is not participating or if there is no one sitting there.': 'front',
                    'What is the ID of the person sitting to the right of you? Use 0 if the person to the right of you is not participating or if there is no one sitting there.': 'right',
                    'What is the ID of the person sitting behind you? Use 0 if the person behind you is not participating or if there is no one sitting there.': 'behind',
                    'What is the ID of the person sitting to the left of you? Use 0 if the person to the left of you is not participating or if there is no one sitting there.': 'left',
                    }

    row_names = {}
    for index, row in data.iterrows():
        row_names[index] = row['What is your ID?']

    data.rename(columns=column_names, index=row_names, inplace=True)
    data.timestamp = pd.to_datetime(data.timestamp)
    print(data.head())
    return data

def GetCoords(data, start_idx=0):
    '''
        Get localization info from google form responses
        PARAMETERS:
        data - pandas dataframe containing google form data
        start_idx - row index of dataframe to begin search from, comparing results from different starting points can help validate data
        RETURNS:
        localization_info - map of pi ids to coordinates in seating arrangement
        num_rows - number of rows in seating arrangement
        num_cols - number of columns in seating arrangement
    '''
    localization_info = {}

    depth, width, min_depth, min_width = 0, 0, 0, 0
    next_id = data.iloc[start_idx, :]['id']
    stack = [next_id]
    localization_info[next_id] = [depth, width]
    visited = set()
    while len(stack) != 0:
        cur_id = stack[-1]
        stack.pop()
        neighbors = data.loc[cur_id, ['front', 'right', 'behind', 'left']]
        for idx, next_id in enumerate(neighbors):
            if next_id != 0 and next_id not in visited:
                new_depth = localization_info[cur_id][0]
                new_width = localization_info[cur_id][1]
                if idx == 0: # TODO: add check to ensure that information is consistent here
                    new_depth -= 1
                elif idx == 1:
                    new_width += 1
                elif idx == 2:
                    new_depth += 1
                else:
                    new_width -= 1
                min_depth = min(min_depth, new_depth)
                min_width = min(min_width, new_width)
                localization_info[next_id] = [new_depth, new_width]
                stack.append(next_id)
        visited.add(cur_id)

    num_rows = 0
    num_cols = 0

    for key in localization_info:
        localization_info[key][0] -= min_depth
        localization_info[key][1] -= min_width
        num_rows = max(num_rows, localization_info[key][0])
        num_cols = max(num_cols, localization_info[key][1])

    return localization_info, num_rows, num_cols

def main():
        data = GetData()
        localization_info, num_rows, num_cols = GetCoords(data)
        print(localization_info)
        print(num_rows)
        print(num_cols)

if __name__ == '__main__':
    main()