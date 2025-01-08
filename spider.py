from urllib.request import urlopen
from link_finder import LinkFinder
from general import create_project_dir, create_data_files, file_to_set, set_to_file


class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
   
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = f"{Spider.project_name}/queue.txt"
        Spider.crawled_file = f"{Spider.project_name}/crawled.txt"
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
    
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(spider_name, page_url):

        if page_url not in Spider.crawled:
            print(f"{spider_name} now crawling: {page_url}")
            print(f"Queue: {len(Spider.queue)} | Crawled: {len(Spider.crawled)}")
            links = Spider.gather_links(page_url)
            if links:
                Spider.add_links_to_queue(links)
            Spider.queue.discard(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):

        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
            return finder.page_links()
        except Exception as e:
            print(f"Error: Cannot crawl page {page_url}. {e}")
            return set()

    @staticmethod
    def add_links_to_queue(links):

        for url in links:
            if url in Spider.queue or url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():

        set_to_file(Spider.queue_file, Spider.queue)
        set_to_file(Spider.crawled_file, Spider.crawled)
