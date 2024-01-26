from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai
openai.api_key = ''

class Chatbot():
    def __init__ (self):
        # Load file information into the agent on startup
        self.readDataBase()

    def readDataBase(self):
        self.documents = SimpleDirectoryReader('../data/IA_CURSO').load_data()
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine()

    def ask(self, message):
        return self.query_engine.query(message)
