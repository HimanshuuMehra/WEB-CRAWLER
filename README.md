# 🌐 Web Crawler with GUI Integration

A Python-based web crawler that systematically extracts links from websites, organizes them, and presents the data through a user-friendly graphical interface. This project is perfect for anyone looking to automate web data collection or learn more about the inner workings of web crawlers.


## 🚀 Features

- **Multi-threaded Crawling**: Efficiently crawl websites using multiple threads for faster data extraction.  
- **Domain-Specific Filtering**: Restrict crawling to specific domains for focused data collection.  
- **Data Management**: Automatically organizes links into `queue.txt` (to be crawled) and `crawled.txt` (already crawled).  
- **Interactive GUI**: Easily start, monitor, and manage crawling tasks through an intuitive Tkinter-based interface.  
- **Extensibility**: Modular code structure allows for easy integration of additional features like content analysis or export options.


## 🛠️ Project Structure

The project is divided into modular Python scripts for better organization and reusability:

1. general.py  
   Handles file operations and manages project directories.

2. domain.py 
   Extracts domain and subdomain names from URLs.

3. link_finder.py  
   Parses HTML content to extract links using Python’s `HTMLParser`.

4. spider.py 
   Core crawler logic that manages the crawling process, including queue and file updates.

5. web_crawler_gui.py
   A Tkinter-based graphical interface for user-friendly interaction.


## 🖥️ How to Run

### **Prerequisites**
- Python 3.8 or higher
- Basic understanding of Python and web crawling concepts

### **Steps**
1. Clone this repository:
   
   git clone https://github.com/yourusername/web-crawler-with-gui.git
   cd web-crawler-with-gui
   
2. Install required libraries (if any).
3.   
   For example:
   pip install -r requirements.txt
   *(Note: Add a `requirements.txt` file if necessary)*

4. Run the GUI:
5. 
   python web_crawler_gui.py

6. Input:
   - **Project Name**: A folder name for organizing results (e.g., `spotify`).
   - **Homepage URL**: The starting URL to crawl (e.g., `https://www.spotify.com`).

7. View results in the generated project folder:
   - queue.txt: Links to be crawled.
   - crawled.txt: Links already crawled.



## 📂 Example Output

### Directory Structure:

spotify/
├── queue.txt
├── crawled.txt


### Sample Data:
- **`queue.txt`**:
  ```
  https://www.spotify.com/about/
  https://www.spotify.com/premium/
  ```
- **`crawled.txt`**:
  ```
  https://www.spotify.com/
  ```

## 📈 Future Enhancements

- **Dynamic Content Crawling**: Support for JavaScript-heavy websites using tools like Selenium.  
- **Data Analysis**: Extract and analyze page content, such as keywords or sentiment.  
- **Visualization**: Add graphical reports for crawled data.  
- **Export Options**: Save data in formats like CSV or JSON for further processing.


## 🙋‍♂️ Author

**Himanshu Mehra[(https://github.com/HimanshuuMehra)]**  
Aspiring developer passionate about automation, AI, and web technologies.

---

Let me know if you'd like to personalize any section further!
