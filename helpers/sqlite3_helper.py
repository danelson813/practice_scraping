import sqlite3
import pandas as pd


def to_sqlite(df: pd.DataFrame) -> None:
    conn = sqlite3.connect('data/Movie_Info.db')

    c = conn.cursor()
    df.to_sql(name='movies', con=conn, if_exists='replace', index=False)
    conn.commit()
    print('The database has been filled.')

