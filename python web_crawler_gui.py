import tkinter as tk
from tkinter import messagebox, scrolledtext
from spider import Spider
from domain import get_domain_name
from general import file_to_set

class WebCrawlerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Crawler GUI")

        tk.Label(root, text="Domain").grid(row=0, column=0, padx=10, pady=5)
        self.project_name_entry = tk.Entry(root, width=30)
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Domain's website").grid(row=1, column=0, padx=10, pady=5)
        self.homepage_entry = tk.Entry(root, width=30)
        self.homepage_entry.grid(row=1, column=1, padx=10, pady=5)


        tk.Button(root, text="Start Crawling", command=self.start_crawling).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="View Queue", command=self.view_queue).grid(row=3, column=0, pady=5)
        tk.Button(root, text="View Crawled", command=self.view_crawled).grid(row=3, column=1, pady=5)


        tk.Label(root, text="Output:").grid(row=4, column=0, columnspan=2)
        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
        self.output_area.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def start_crawling(self):
    
        project_name = self.project_name_entry.get().strip()
        homepage = self.homepage_entry.get().strip()

        if not project_name or not homepage:
            messagebox.showerror("Input Error", "Please enter both Project Name and Homepage URL.")
            return

        try:
            domain_name = get_domain_name(homepage)
            Spider(project_name, homepage, domain_name)
            self.output_area.insert(tk.END, f"Crawling started for project '{project_name}' with homepage '{homepage}'.\n")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_queue(self):
    
        project_name = self.project_name_entry.get().strip()
        if not project_name:
            messagebox.showerror("Input Error", "Please enter the Project Name to view the queue.")
            return

        try:
            queue_file = f"{project_name}/queue.txt"
            queue_links = file_to_set(queue_file)
            self.output_area.insert(tk.END, f"Queue URLs ({len(queue_links)}):\n")
            self.output_area.insert(tk.END, "\n".join(queue_links) + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_crawled(self):
     
        project_name = self.project_name_entry.get().strip()
        if not project_name:
            messagebox.showerror("Input Error", "Please enter the Project Name to view the crawled URLs.")
            return

        try:
            crawled_file = f"{project_name}/crawled.txt"
            crawled_links = file_to_set(crawled_file)
            self.output_area.insert(tk.END, f"Crawled URLs ({len(crawled_links)}):\n")
            self.output_area.insert(tk.END, "\n".join(crawled_links) + "\n")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WebCrawlerGUI(root)
    root.mainloop()

