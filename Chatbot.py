from llama_index import VectorStoreIndex, SimpleDirectoryReader
import openai
openai.api_key = ''

class Chatbot():
    
    def __init__ (self):

        #Call to method readDataBase
        self.readDataBase()


    #Methods
    def readDataBase(self):
        self.documents = SimpleDirectoryReader('data').load_data()
        self.index = VectorStoreIndex.from_documents(self.documents)
        self.query_engine = self.index.as_query_engine()

    def sendPrompt(self,message):
        #Query and Answer
        return self.query_engine.query(message)
         

gustaVOT=Chatbot()

#Prompt input
prompt=input("Enter prompt")
print(gustaVOT.sendPrompt(prompt))


    