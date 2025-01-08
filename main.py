import threading
from queue import Queue
from spider import Spider
from domain import get_domain_name
from general import file_to_set


PROJECT_NAME = 'spotify'
HOMEPAGE = 'https://www.spotify.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = f"{PROJECT_NAME}/queue.txt"
CRAWLED_FILE = f"{PROJECT_NAME}/crawled.txt"
NUMBER_OF_THREADS = 8

queue = Queue()


Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def create_threads():
 
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True  
        t.start()

def work():
 
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_jobs():

    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()  
    crawl()  

def crawl():
  
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(f"Links Left: {len(queue_links)}")
        create_jobs()


create_threads()
crawl()
