List of https://github.com/camunda-community-hub/awesome-camunda-7-external-clients
https://docs.camunda.org/manual/7.20/user-guide/process-engine/external-tasks/

## How it works
Fom camunda docs
![archtecture](./visual/external-task-pattern.png)


- Process Engine: Creation of an external task instance
- External Worker: Fetch and lock external tasks
- External Worker & Process Engine: Complete external task instance

When the process engine encounters a service task that is configured to be externally handled, it creates an external task instance and adds it to a list of external tasks (step 1). 

The task instance receives a topic ('someTopic') that identifies the nature of the work to be performed. At a time in the future, an external worker may fetch and lock tasks for a specific set of topics (step 2, 'someTopic').

To prevent one task being fetched by multiple workers at the same time, a task has a timestamp-based lock that is set when the task is acquired. Only when the lock expires, another worker can fetch the task again. When an external worker has completed the desired work, it can signal the process engine to continue process execution after the service task (step 3).

## For python

1. Run Camunda and deploy the externalRaiseTemperature.bpmn
2. Run [externalRaiseTemperature.py](./python/externalRaiseTemperature.py)
3. see the temperature raise

See it in action:  ![externalRaiseTemperature.gif](./visual/externalRaiseTemperature.gif)

https://github.com/camunda-community-hub/camunda-external-task-client-python3
