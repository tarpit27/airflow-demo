#### Steps for local setup
- python3 -m venv airflow-env
- source airflow-env/bin/activate
- pip install -r requirements.txt
- airflow db migrate
- Navigate to ~/airflow/airflow.cfg
  - Update dags_folder to the local path of dags folder in the repo
- To start local server: airflow standalone(username and password logged in the console)
- To run DAG on local server: airflow dags test etl_dag 2024-11-06

#### File where sequence of tasks(DAG) is defined for the worflow
- dags/data_pipe_dag.py
