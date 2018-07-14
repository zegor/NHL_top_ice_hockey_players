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
    category_name_text = category_name[0].text_content()
  
  for player in range(5):
    player_row = players[player].cssselect("td")
    if player > 0:
      player_row_text = player_row[0].text_content()
    else:
      player_row_text = player_row[1].text_content()
    player_rank_text = player_row_text.split(". ",1)[0]
    player_name_text = player_row_text.split(". ",1)[1].split(", ",1)[0]
    
    # Write out to the sqlite database using scraperwiki library
    ID = 1
    scraperwiki.sqlite.save(unique_keys="ID",data={"ID":ID, "Category":category_name_text, "Player Rank":player_rank_text, "Player Name":player_name_text}, table_name="data")
    ID += 1

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
