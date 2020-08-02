from azureml import core
from azureml.core import Workspace

import mlflow

workspace = Workspace.from_config()  
mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

config = {"COMPUTE": "cpu-cluster"}

submitted_run = mlflow.projects.run(uri="MlflowProjectNotebooks\examples\tenserflow\tf1",
                                        experiment_name = "tensorflow",
                                        backend = "azureml",
                                        backend_config = config)