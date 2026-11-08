from src.tools.tools import web_search, scrape_url

search = web_search.invoke("latest advancements in AI technology")
print(search)

# scrape = scrape_url.invoke({
#     "url": "https://en.wikipedia.org/wiki/Nikola_Tesla"
# })
# print(scrape)