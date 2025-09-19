**Finance Stock Report Automation**

This project automates fetching stock market data from Yahoo Finance and sending a daily report via email.

**Features**

      Scrapes live stock data (Amazon, Google, Microsoft by default).
      
      Saves stock info into a CSV file named with today’s date.
      
      Automatically emails the report as an attachment.

**Project Files**

      stock_scraper.py → Scrapes stock data from Yahoo Finance and writes it into a CSV.
      
      send_mail.py → Sends the generated CSV file as an email attachment.

**Data Collected**

      For each stock:
      
      Stock Name
      
      Current Price
      
      Previous Close
      
      Open Price
      
      Bid
      
      Ask
      
      Day Range
      
      52-Week Range
      
      Volume
      
      Average Volume

⚙️ **Setup Instructions**
      **Install dependencies**
      pip install requests beautifulsoup4 lxml
      
      **Gmail setup**
      
      Since Gmail blocks less-secure apps, you need to create an App Password:
      
      Enable 2FA in your Gmail account.
      
      Generate an App Password from Google Account → Security → App Passwords
      .
      
      Replace the password in send_mail.py:
      
      server.login(from_add, 'your_app_password_here')
      
      **Run the scraper**
      python stock_scraper.py
      
      
      This will create a CSV file named like 2025-09-19.csv.
      
      **Send the report**
      python send_mail.py

**Example Email**
      
      Subject: Finance Stock Report
      
      Body: Includes a short message
      
      Attachment: CSV file with stock data
