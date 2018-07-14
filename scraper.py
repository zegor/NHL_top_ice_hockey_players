# Python scraper on morph.io (https://morph.io)

# Import libraries
import scraperwiki
import lxml.html

# Scrape source
html = scraperwiki.scrape("http://www.espn.com/nhl/statistics")

# Parse HTML
root = lxml.html.fromstring(html)
groupings = root.cssselect("table.tablehead")
categories = groupings.cssselect("tr.colhead")
category_names = categories.cssselect("td")

# Print
print(category_names)

# Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=["column1"], data={"column1": column1}, table_name="data")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
