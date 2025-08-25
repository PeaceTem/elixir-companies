# 🧩 Elixir Companies Scraper

A Selenium + Python scraper that collects data from [Elixir Companies](https://elixir-companies.com/en/companies).  
It automatically scrolls through the infinite page, extracts company details, and saves them into **CSV** and **Excel** files for easy analysis.

---

## ✨ Features
- 🔄 Handles **infinite scrolling** to load all companies  
- 🏢 Extracts **company name, type, location, description, and links**  
- 💾 Exports clean data into:
  - `companies.csv`  
  - `companies.xlsx`  
- 📊 Ready for further **data analysis or visualization**  

---

## ⚡️ Tech Stack
- **Python 3**
- **Selenium WebDriver** (Edge/Chrome/Firefox supported)
- **Pandas** for exporting data

---

## 📥 Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/elixir-companies-scraper.git
cd elixir-companies-scraper
pip install -r requirements.txt
