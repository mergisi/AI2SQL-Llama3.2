import streamlit as st
from embedchain import App

def embedchain_bot():
    return App.from_config(
        config={
            "llm": {"provider": "ollama", "config": {"model": "llama3.2:latest", "max_tokens": 250, "temperature": 0.5, "stream": True, "base_url": 'http://localhost:11434'}},
            "embedder": {"provider": "ollama", "config": {"model": "llama3.2:latest", "base_url": 'http://localhost:11434'}},
        }
    )

st.title("AI2SQL Lite: Text to SQL Converter (Powered by Llama 3.2)")
st.write("Try our lite version! For full features, become an AI2SQL paid user.")

# Initialize the app
if 'app' not in st.session_state:
    st.session_state.app = embedchain_bot()

# Simplified schema
schema = {
    "users": ["id", "name", "email", "registration_date"],
    "orders": ["id", "user_id", "total", "order_date"]
}

st.sidebar.title("Sample Database Schema")
st.sidebar.json(schema)

# Format schema for the prompt
def format_schema():
    schema_str = "Database Schema:\n"
    for table, columns in schema.items():
        schema_str += f"Table: {table}\n"
        schema_str += f"Columns: {', '.join(columns)}\n\n"
    return schema_str

# Sample prompts
sample_prompts = [
    "Show me all users who registered in the last month",
    "What's the total value of orders for each user?",
    "List the top 5 users by order total",
    "Find users who haven't placed any orders"
]

selected_prompt = st.selectbox("Choose a sample prompt or write your own:", [""] + sample_prompts)
prompt = st.text_input("Enter your query in natural language:", value=selected_prompt)

if st.button("Generate SQL"):
    if prompt:
        with st.spinner("Generating SQL..."):
            schema_prompt = format_schema()
            full_prompt = f"{schema_prompt}\nGenerate a SQL query for the following request: {prompt}\nPlease use the provided schema to ensure the query is accurate."
            response = st.session_state.app.chat(full_prompt)
            
            # Extract the SQL query from the response
            sql_query = response.split("```sql")[1].split("```")[0].strip() if "```sql" in response else response
            
            st.code(sql_query, language="sql")
    else:
        st.warning("Please enter a query or select a sample prompt.")

st.markdown("---")
st.subheader("Upgrade to AI2SQL Pro for More Features!")
st.write("- Support for multiple database types (MySQL, SQL Server, PostgreSQL)")
st.write("- Custom schema import from your own databases")
st.write("- Query history and saved queries")
st.write("- Advanced error handling and query optimization suggestions")
st.write("- Regular updates and new features")

st.markdown("---")
st.subheader("How It Works")
st.write("""
1. Choose a sample prompt or enter your own query in natural language.
2. Click 'Generate SQL' to see the AI-generated SQL query.
3. The app uses Llama 3.2 to understand your request and generate appropriate SQL.
4. Try different queries to explore the capabilities!
""")

st.markdown("---")
st.write("Note: This is a demo version with a simplified schema. The full version supports complex schemas and multiple database types.")
