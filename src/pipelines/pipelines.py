from src.agents.agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic: str) -> dict:

    state = {}

    # Step 1: Search Agent
    print("\n"+" ="*50)
    print("Step 1: Search Agent is working...")
    print("="*50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })

    state["search_result"] = search_result['messages'][-1].content
    print("\n Search result: ", state['search_result'])

    
    # Step 2: Reader Agent
    print("\n"+" ="*50)
    print("Step 2: Reader Agent is working...")
    print("="*50)

    reader_agent = build_reader_agent()
    scrape_result = reader_agent.invoke({
        "messages": [("user", 
            f"Based on the following search results about: '{topic}',"
            f"pick the most relevant URL and scrape it for deeper insights. \n\n"
            f"Search Results: \n{state['search_result'][:800]}"
        )]
    })

    state['scraped_content'] = scrape_result['messages'][-1].content
    print("\n Scraped content: ", state['scraped_content'])


    # Step 3: Writer Chain
    print("\n"+" ="*50)
    print("Step 3: Writer Chain is drafting the report...")
    print("="*50)

    research_combined = (
        f"Search Results: \n{state['search_result']} \n\n"
        f"Detailed Scraped Content: \n{state['scraped_content']}"
    )

    state['report'] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report: ", state['report'])


    # Step 4: Critic Chain
    print("\n"+" ="*50)
    print("Step 4: Critic Chain is evaluating the report...")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })

    print("\n Critic Report: ", state['feedback'])

    return state