# AI2SQL: Advanced Text to SQL Conversion with Llama 3.2

Welcome to the AI2SQL Llama 3.2 Demo repository! This project showcases our powerful text-to-SQL conversion capabilities, leveraging Llama 3.2 for advanced natural language processing to transform your queries into accurate SQL statements.

## Lite Version

![AI2SQL Lite Version Screenshot](/images/lite_version_screenshot.png)
*AI2SQL Lite: Simple interface for quick text-to-SQL conversion*

Try our lite version to experience the core functionality of AI2SQL:
- Text to SQL conversion powered by Llama 3.2
- Sample schema for demonstration
- Easy-to-use Streamlit interface
- Sample prompts to get you started

## Pro Version

![AI2SQL Pro Version Screenshot](/images/pro_version_screenshot.png)
*AI2SQL Pro: Advanced features including custom schema import and query optimization*

Upgrade to the Pro version for advanced features:
- Support for multiple database types (MySQL, SQL Server, PostgreSQL)
- Custom schema import from your own databases
- Query history and saved queries
- Comprehensive error handling and query optimization suggestions
- Regular updates and new features

## Key Features of Llama 3.2

AI2SQL leverages the power of Llama 3.2, which offers:

- **Multiple Model Sizes**: From 1B to 90B parameters, optimized for various tasks.
- **On-Device Processing**: Enhances privacy and speed by running locally.
- **Multimodal Capabilities**: Larger models can understand and reason with visual data.
- **Competitive Performance**: Outperforms many leading models in various NLP tasks.
- **Enhanced Safety**: Includes features like Llama Guard to reduce harmful outputs.

These capabilities allow AI2SQL to provide accurate, fast, and secure text-to-SQL conversions.

## Getting Started

To try out the lite version:

1. Clone this repository
2. Install the required packages: `pip install -r requirements.txt`
3. Install Ollama from https://ollama.ai/
4. Pull the Llama 3.2 model: `ollama pull llama3.2:latest`
5. Run the Streamlit app: `streamlit run ai2sql_lite.py`

## Sample Prompts

The lite version includes some sample prompts to help you get started:

- Show me all users who registered in the last month
- What's the total value of orders for each user?
- List the top 5 users by order total
- Find users who haven't placed any orders

Feel free to try these or enter your own natural language queries!

## Upgrade to Pro

Ready to experience the full power of AI2SQL? Visit [our website](https://ai2sql.io) to become a paid user and unlock all features!

## Contact

For any questions or support, please contact us at support@ai2sql.io.

## License

This demo version is provided under the MIT License. The full version is subject to our commercial license terms.
