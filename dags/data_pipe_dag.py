from airflow.decorators import dag, task
import pendulum

from app.Load import Load
from app.Store import Store
from app.Transform import Transform


@dag(
    dag_id="etl_dag",
    schedule=None,
    start_date=pendulum.datetime(2024, 10, 1, tz="UTC"),
    catchup=False
)
def etl_dag():

    @task()
    def load():
        print("Going to read file")
        loader = Load("sample_data.csv")
        return loader.load_file()


    @task
    def transform(df):
        transformer = Transform(df)
        return transformer.transform_df()

    @task
    def store(df):
        store_obj = Store(df, "updated_data.csv")
        store_obj.store_df()

    store(transform(load()))


etl_dag()

