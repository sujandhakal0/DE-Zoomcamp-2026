import pandas as pd
from sqlalchemy import create_engine
import click

@click.command()
@click.option('--pg-user', default='root')
@click.option('--pg-pass', default='root')
@click.option('--pg-host', default='localhost')
@click.option('--pg-db', default='ny_taxi')
@click.option('--pg-port', default=5432, type=int)
@click.option('--target-table', default='zones')
def run(pg_user, pg_pass, pg_host, pg_db, pg_port, target_table):

    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

    engine = create_engine(
        f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    )

    df = pd.read_csv(url)

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists='replace',
        index=False
    )

    print("Zones table loaded successfully.")

if __name__ == '__main__':
    run()
