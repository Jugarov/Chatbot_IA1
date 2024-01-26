from Client import Client

if __name__ == "__main__":
    client = Client("localhost", 8554)

    try:
        while True:
            client.read()
            client.listen()

    except Exception as ex:
        print("ERROR:", ex)

    except KeyboardInterrupt:
        pass

    finally:
        client.close()