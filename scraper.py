# Python scraper on morph.io (https://morph.io)

# Import libraries
import scraperwiki
import lxml.html

# Clear database data table
print("Action: Dropping table 'data'.")
try:
  scraperwiki.sqlite.execute("DROP TABLE 'data'")
  print("Result: Table 'data' dropped.")
except:
  print("Result: Table 'data' does not exist.")

# Scrape source
html = scraperwiki.scrape("http://www.espn.com/nhl/statistics")

# Parse HTML
root = lxml.html.fromstring(html)

groupings = root.cssselect("table.tablehead")

for group in range(6):
  categories = groupings[group].cssselect("tr.colhead")
  players = groupings[group].cssselect("tr.oddrow")
  players.extend(groupings[group].cssselect("tr.evenrow"))
  
  for category in categories:
    category_name = category.cssselect("td")
    print(category_name[0].text_content())
  
  for player in range(5):
    player_name = players[player].cssselect("td")
    if player > 0:
      player_name_text = player_name[0].text_content()
    else:
      player_name_text = player_name[1].text_content()
    player_name_text = player_name_text.split(",",0)[0]

# Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=["column1"], data={"column1": column1}, table_name="data")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
