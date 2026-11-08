from src.tools.tools import web_search, scrape_url
from src.pipelines.pipelines import run_research_pipeline

# search = web_search.invoke("latest advancements in AI technology")
# print(search)

# scrape = scrape_url.invoke({
#     "url": "https://en.wikipedia.org/wiki/Nikola_Tesla"
# })
# print(scrape)

topic = "The impact of AI on the job market in the next decade"
run_research_pipeline(topic)