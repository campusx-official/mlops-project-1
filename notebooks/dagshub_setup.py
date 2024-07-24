import dagshub
import mlflow

dagshub.init(repo_owner='campusx-official', repo_name='mlops-project-1', mlflow=True)
mlflow.set_tracking_uri('https://dagshub.com/campusx-official/mlops-project-1.mlflow')

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)