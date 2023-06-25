import random
import requests
from concurrent.futures import ThreadPoolExecutor


def do_request(iterations):
    thread_id = random.randint(1000, 9999)

    session = requests.Session()
    headers = {"Content-Type": "application/json"}
    serialized_data = {}

    for _ in range(iterations):
        url = "https://music-pro-api.herokuapp.com/api/get_productos"
        response = session.request(method="GET", url=url, headers=headers)
        if response.status_code == 200:
            serialized_data = response.json()

    result = {
        "threadId": thread_id,
        "iterations": iterations,
        "data": serialized_data
    }

    return result

def run_load_test(threads=5, iterations=10):
    try:
        thread_data = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for i in range(threads):
                thread_data.append(executor.submit(do_request, iterations))            

        results = []
        for thread in thread_data:
            result = thread.result()
            results.append(result)

        return results
    except Exception as e:
        print(str(e))
