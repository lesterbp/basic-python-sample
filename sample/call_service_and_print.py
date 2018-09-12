import sys
from sample_service import SampleService


def call_service_and_print(id):
    try:
        host = "https://jsonplaceholder.typicode.com"
        service = SampleService(host)
        result = service.get_todo(id)
        print("Todo Title: {}".format(result["title"]))
    except Exception as e:
        print("call_service_and_print: Error: {}. Exit code 1.".format(str(e)))
        sys.exit(1)


call_service_and_print(sys.argv[1])
