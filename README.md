This script automates the process of logging into LinkedIn, performing a search for people with the title "CIO" in a specific region, and scraping their contact details such as name, designation, city, and LinkedIn profile URL. The scraped data is then saved into a CSV file for further analysis.

Prerequisites

Before you run the script, ensure you have the following installed:

1. Python 3.x
2. Google Chrome
3. Required Python packages (listed in requirements.txt):

   3.1 selenium

   3.2 pandas

   3.3 chromedriver_py

Setup
1. Install Required Packages:
Run the following command to install the required packages:
pip install -r requirements.txt

2. LinkedIn Credentials:
Replace the placeholders for USERNAME and PASSWORD in the script with your actual LinkedIn credentials or load them from an external configuration file (Config.py).

3. Configure Web Driver:
  3.1 The script uses chromedriver_py to manage the ChromeDriver binary path. Ensure the correct version of ChromeDriver is installed and compatible with your version of Google Chrome.
  3.2 The script also uses Selenium for browser automation, which requires the ChromeDriver executable.

Script Breakdown
1. Import Statements:
  1.1 The script imports various libraries required for browser automation (selenium), data handling (pandas), and other utilities.

2. WebDriver Initialization:
  2.1 The script initializes the Chrome WebDriver with specified options such as maximizing the window and ignoring SSL certificate errors.

3. LinkedIn Login:
  3.1 The script navigates to LinkedIn’s login page and uses your credentials to log in automatically.

4. Data Storage:
  4.1 A dictionary named data is created to store the scraped information: contact person’s name, designation, city, and LinkedIn profile URL.

5. Scraping Loop:
  5.1 The script iterates through multiple pages of search results (20 pages in this case). For each page, it scrapes the first 10 profiles and extracts the desired information.
  5.2 If any element is not found (due to LinkedIn’s dynamic content), a NoSuchElementException is caught and an error message is printed.

6. Pagination:
  6.1 After scraping each page, the script clicks the “Next” button to navigate to the next set of search results. The loop continues until all specified pages are processed.

7. Data Export:
  7.1 Once all the data is collected, it is saved into a CSV file named linkedin_results.csv using the pandas library.

8. Clean Up:
  8.1 The script closes the browser window by calling driver.quit() once the scraping is complete.

Running the Script
1. Clone the repository and navigate to the project directory.
2. Ensure you have set up your LinkedIn credentials in the script or an external configuration file.
3. Run the script:
python linkedin_scraper.py
4. The script will log in to LinkedIn, perform the search, and start scraping the information. The results will be saved in linkedin_results.csv.

Notes
1. Compliance: Please make sure that you comply with LinkedIn’s terms of service when using this script.
2. Dynamic Content: LinkedIn’s page structure can change frequently. If the script fails due to changes in the webpage layout, you may need to update the XPath expressions accordingly.
