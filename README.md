# Task03-Python-Web-Scraping

<b>Purpose:</b><br/>
This Python script fetches a webpage, extracts the top headlines, and saves them into a text file named Top_HeadLines.txt.<br/>It performs the following steps:<br/>

<b>Imports:</b><br/>
<b>requests:</b> To send HTTP requests and retrieve web page content.<br/>
<b>BeautifulSoup from bs4:</b> To parse HTML content.<br/>
<b>os:</b> To interact with the filesystem (check if file exists, get size).<br/>

<b>Send HTTP Request:</b><br/>
Uses the requests library to send a GET request to the specified URL.<br/>
If the request is successful (status_code == 200), proceeds to parse the page content.<br/>
Otherwise, prints an error message and exits.<br/>

<b>Parse HTML Content:</b><br/>
Uses BeautifulSoup from the bs4 library to parse the HTML content of the webpage.<br/>

<b>Extract Headlines:</b><br/>
Finds all `<h2>` tags on the page. For each `<h2>`, it searches for an `<a>` tag inside it.<br/>
If found, extracts the text of the <a> tag (the headline) and writes it to the output file, each headline on a new line.<br/>


<b>Save and Verify File:</b><br/>
Checks if the file Top_HeadLines.txt exists and whether it contains any data.<br/>
If the file exists and is not empty, confirms that the headlines have been saved successfully.<br/>
If the file is empty or does not exist, it displays an appropriate message.<br/>

<b>Usage Notes:</b><br/>
Replace the placeholder #enter url with the actual URL of the webpage you want to scrape.<br/>
Ensure you have the requests and beautifulsoup4 libraries installed (pip install requests beautifulsoup4).<br/>

Programming language & libraries: Python, BeautifulSoup<br/>
Tools: PyCharm<br/>

<strong>*** Disclaimer ***</strong><br/>
**Always check the website's `robots.txt` file before scraping.**<br/>  
Respect the crawling policies specified by the website owner. Ignoring `robots.txt` directives may violate the website’s terms of service and legal regulations. Use this tool responsibly and ethically.<br/>

for example: append /robots.txt after the webpage you want to scrape.<br/>
Review the directives in this file to see which pages or sections are disallowed for crawling. Respect these rules to ensure ethical scraping practices.
