import pandas as pd

def read_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def get_record_by_id(file_path: str, record_id: int):
    df = read_csv(file_path)
    record = df[df['id'] == record_id]
    if not record.empty:
        return record.to_dict('records')[0]
    return None