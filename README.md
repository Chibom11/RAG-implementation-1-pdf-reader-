PDF Q&A with RAG using LangChain, OpenAI, and Qdrant
This project demonstrates a simple Retrieval-Augmented Generation (RAG) system that allows you to ask questions about a PDF document and receive answers based on its content. The system uses LangChain to orchestrate the process, OpenAI for embeddings and language modeling, and Qdrant as a vector database to store and retrieve relevant text chunks.

Project Structure
The project is divided into two main Python scripts:

indexer.py: This script is responsible for:

Loading a PDF document (react.pdf).

Splitting the document into smaller, manageable text chunks.

Generating embeddings for each chunk using OpenAI's text-embedding-3-large model.

Storing these chunks and their corresponding vector embeddings in a Qdrant vector database collection named learning_rag.

main.py: This is the user-facing script that:

Takes a user's question as input.

Generates an embedding for the user's query.

Performs a similarity search in the Qdrant database to find the most relevant text chunks from the PDF.

Constructs a detailed prompt for the OpenAI chat model, including the retrieved context (the relevant chunks).

Sends the prompt to the gpt-5 model to generate a natural language answer based only on the provided context.

Prints the final answer to the console.

How It Works
The core idea is to leverage a vector database to find the most relevant parts of a large document before asking a Large Language Model (LLM) to generate an answer. This approach is more efficient and accurate than feeding the entire document to the LLM, as it focuses the model's attention on the specific information needed to answer the user's query.

Technologies Used
LangChain: A framework for developing applications powered by language models. It helps in chaining together different components like document loaders, text splitters, and models.

OpenAI: Used for generating high-quality text embeddings and for the final answer generation with their powerful chat models.

Qdrant: An open-source vector database used to store and efficiently search through high-dimensional vector embeddings.

Python: The programming language used for the entire project.

Prerequisites
Before you can run this project, you need to have the following installed and set up:

Python 3.8+

Qdrant: You must have a Qdrant instance running. The easiest way is to use Docker:

docker run -p 6333:6333 qdrant/qdrant

This will start a Qdrant container and expose it on localhost:6333.

OpenAI API Key: You need an API key from OpenAI.

Setup and Installation
Clone the repository:

git clone <your-repository-url>
cd <your-repository-directory>

Install the required Python packages:

pip install -r requirements.txt

Note: If you don't have a requirements.txt file, you can create one with the following content or install the packages manually.

langchain-community
langchain-text-splitters
langchain-openai
langchain-qdrant
python-dotenv
qdrant-client
openai
pypdf

Then run pip install -r requirements.txt.

Create an environment file:
Create a file named .env in the root of your project directory and add your OpenAI API key:

OPENAI_API_KEY="your_openai_api_key_here"

Add your PDF:
Place the PDF file you want to query in the same directory as the scripts and name it react.pdf, or update the pdf_path variable in indexer.py to point to your file.

How to Run
You need to run the scripts in two steps:

Step 1: Index the Document

First, run the indexer.py script to process your PDF and store its content in the Qdrant database.

python indexer.py

You should see the output Indexing of documents done.... upon successful completion. You only need to run this script once for each new or updated PDF.

Step 2: Ask a Question

Now you can run the main.py script to start asking questions.

python main.py

The script will prompt you to enter your question.

👤:Ask Something

Type your question and press Enter. The script will then retrieve the relevant context and generate an answer.

Example Interaction:

👤:Ask SomethingWhat is React?
🤖: Based on the document, React is a JavaScript library used for building user interfaces. For more details, you can refer to the information on page 1 of the provided PDF file located at react.pdf.

Customization
Change the PDF: To use a different PDF, simply change the file path in indexer.py. Remember to delete your existing Qdrant collection or use a new collection name to avoid mixing contexts.

Change Models: You can easily swap out the embedding model or the chat model by changing the model names in indexer.py and main.py.

Adjust Chunking: Modify the chunk_size and chunk_overlap parameters in RecursiveCharacterTextSplitter within indexer.py to fine-tune how the document is split.    


<img width="1427" height="401" alt="image" src="https://github.com/user-attachments/assets/776c8117-ffa0-41ca-9ac6-f875b470d169" />
