This script automates the process of logging into LinkedIn, performing a search for people with the title "CIO" in a specific region, and scraping their contact details such as name, designation, city, and LinkedIn profile URL. The scraped data is then saved into a CSV file for further analysis.

Prerequisites
Before you run the script, ensure you have the following installed:

Python 3.x
Google Chrome
Required Python packages (listed in requirements.txt):
selenium
pandas
chromedriver_py
Setup
Install Required Packages:

Run the following command to install the required packages:

bash
Copy code
pip install -r requirements.txt
LinkedIn Credentials:

Replace the placeholders for USERNAME and PASSWORD in the script with your actual LinkedIn credentials or load them from an external configuration file (Config.py).

Configure Web Driver:

The script uses chromedriver_py to manage the ChromeDriver binary path. Ensure the correct version of ChromeDriver is installed and compatible with your version of Google Chrome.
The script also uses Selenium for browser automation, which requires the ChromeDriver executable.
Script Breakdown
Import Statements:

The script imports various libraries required for browser automation (selenium), data handling (pandas), and other utilities.
WebDriver Initialization:

The script initializes the Chrome WebDriver with specified options such as maximizing the window and ignoring SSL certificate errors.
LinkedIn Login:

The script navigates to LinkedIn’s login page and uses your credentials to log in automatically.
Data Storage:

A dictionary named data is created to store the scraped information: contact person’s name, designation, city, and LinkedIn profile URL.
Scraping Loop:

The script iterates through multiple pages of search results (20 pages in this case). For each page, it scrapes the first 10 profiles and extracts the desired information.
If any element is not found (due to LinkedIn’s dynamic content), a NoSuchElementException is caught and an error message is printed.
Pagination:

After scraping each page, the script clicks the “Next” button to navigate to the next set of search results. The loop continues until all specified pages are processed.
Data Export:

Once all the data is collected, it is saved into a CSV file named linkedin_results.csv using the pandas library.
Clean Up:

The script closes the browser window by calling driver.quit() once the scraping is complete.
Running the Script
Clone the repository and navigate to the project directory.
Ensure you have set up your LinkedIn credentials in the script or an external configuration file.
Run the script:
bash
Copy code
python linkedin_scraper.py
The script will log in to LinkedIn, perform the search, and start scraping the information. The results will be saved in linkedin_results.csv.
Notes
Compliance: Please make sure that you comply with LinkedIn’s terms of service when using this script.
Dynamic Content: LinkedIn’s page structure can change frequently. If the script fails due to changes in the webpage layout, you may need to update the XPath expressions accordingly.
