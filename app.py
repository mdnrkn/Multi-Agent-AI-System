import streamlit as st
import threading
from src.pipelines.pipelines import run_research_pipeline

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 AI Research Assistant")
st.write("Multi-agent research system powered by Google Gemini.")

st.divider()

topic = st.text_input(
    "Research Topic",
    placeholder="Enter your research topic..."
)

if st.button("🚀 Run Research", type="primary", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a research topic.")

    else:
        # Agent status placeholders
        st.subheader("Agent Execution Status")

        search_status = st.empty()
        reader_status = st.empty()
        writer_status = st.empty()
        critic_status = st.empty()

        statuses = [
            (search_status, "Search Agent"),
            (reader_status, "Reader Agent"),
            (writer_status, "Writer Chain"),
            (critic_status, "Critic Chain")
        ]

        for placeholder, name in statuses:
            placeholder.info(f"⏳ {name} — Waiting...")

        result_container = {}
        error_container = {}

        # Run pipeline in background
        def execute_pipeline():
            try:
                result_container["result"] = run_research_pipeline(topic)
            except Exception as e:
                error_container["error"] = str(e)

        thread = threading.Thread(target=execute_pipeline)
        thread.start()

        # Display sequential progress
        agent_names = [
            "Search Agent",
            "Reader Agent",
            "Writer Chain",
            "Critic Chain"
        ]

        placeholders = [
            search_status,
            reader_status,
            writer_status,
            critic_status
        ]

        current_step = 0

        while thread.is_alive():
            # Show current stage based on console output is not possible
            # without changing the pipeline.
            # Keep the interface responsive and wait for completion.
            thread.join(timeout=0.5)

        # Check execution result
        if "error" in error_container:
            st.error(f"Research failed: {error_container['error']}")

        else:
            # Mark all agents completed after pipeline finishes
            for placeholder, name in statuses:
                placeholder.success(f"✅ {name} — Completed")

            result = result_container["result"]

            st.success("Research completed successfully!")

            st.divider()

            with st.expander("🔎 Search Results"):
                st.markdown(result["search_result"])

            with st.expander("📄 Scraped Content"):
                st.markdown(result["scraped_content"])

            st.subheader("📝 Final Research Report")
            st.markdown(result["report"])

            st.divider()

            st.subheader("📊 Critic Evaluation")
            st.markdown(result["feedback"])

st.divider()

st.caption("Powered by LangChain | Google Gemini | Streamlit")
