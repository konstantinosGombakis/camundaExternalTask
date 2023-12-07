import logging
from concurrent.futures.thread import ThreadPoolExecutor

from camunda.external_task.external_task_worker import ExternalTaskWorker
from examples.task_handler_example import handle_task
from camunda.external_task.external_task import ExternalTask
from camunda.utils.log_utils import log_with_context


logger = logging.getLogger(__name__)

default_config = {
    "maxTasks": 1,
    "lockDuration": 10000,
    "asyncResponseTimeout": 3000,
    "retries": 3,
    "retryTimeout": 5000,
    "sleepSeconds": 30,
    "isDebug": True,
    "httpTimeoutMillis": 3000,
}



def generic_task_handler(task: ExternalTask):
    log_context = {"WORKER_ID": task.get_worker_id(),
                   "TASK_ID": task.get_task_id(),
                   "TOPIC": task.get_topic_name()}
    temperature = task.get_variable("temperature")
    temperature=temperature+1
    print("Raising temperature to: ", temperature)
    # log_with_context("executing generic task handler", log_context)
    # return task.complete(Python dictionary)  
    # return task.failure(Python dictionary)  
    # task.bpmn_error
    return task.complete({"temperature": temperature})

def main():
    # configure_logging()
    topics = ["setting_temperature"]
    executor = ThreadPoolExecutor(max_workers=len(topics))
    for index, topic in enumerate(topics):
        executor.submit(ExternalTaskWorker(worker_id=index, config=default_config).subscribe, topic, generic_task_handler)
    print("Finish")


def configure_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                        handlers=[logging.StreamHandler()])


if __name__ == '__main__':
    main()
