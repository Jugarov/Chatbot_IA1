# from Chatbot import Chatbot
# from Server import Server

# if __name__ == "__main__":
#     GustaVOT = Chatbot()
#     #server = Server("25.69.81.47", 2620, GustaVOT)
#     server = Server("localhost", 8554, GustaVOT)

#     try:
#         while True:
#             server.listen()

#     except Exception as ex:
#         print("ERROR:", ex)

#     except KeyboardInterrupt:
#         pass

#     finally:
#         server.close()

from Chatbot import Chatbot
from Server import Server

if __name__ == "__main__":
    GustaVOT = Chatbot()
    server = Server("25.69.81.47", 2620, GustaVOT)

    try:
        server.listen()

    except Exception as ex:
        print("ERROR:", ex)

    except KeyboardInterrupt:
        pass

    finally:
        server.close()