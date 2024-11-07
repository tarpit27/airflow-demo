# Steps for local setup
- python3 -m venv airflow-env
- source airflow-env/bin/activate
- pip install -r requirements.txt
- airflow db migrate
- Navigate to ~/airflow/airflow.cfg
  - Update dags_folder to the local path of dags folder in the repo
