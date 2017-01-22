import socket, random, time
from enum import Enum

def rec_fields(data):
    """
    Enthält das Spielfeld für den Client
    :param data: Bytes
    :return: True or False
    """
    if not data:
        print("Connection closed")
        return True
    if len(data) == 50:
        print(data[0:10])
        print(data[10:20])
        print(data[20:30])
        print(data[30:40])
        print(data[40:50])
    elif len(data) == 18:
        print(data[0:6])
        print(data[6:12])
        print(data[12:18])
    elif len(data) == 98:
        print(data[0:14])
        print(data[14:28])
        print(data[28:42])
        print(data[42:56])
        print(data[56:70])
        print(data[70:84])
        print(data[84:98])
    else:
        # Lose / Win
        print(data)
        return True

    return False

class CommandType(Enum):
    """
    Bestimmt die Richtung
    """
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    try:
        # Verbindung herstellen (Gegenpart: accept() )
        clientsocket.connect(('localhost', 5050))
        msg = input("Name?")
        # Nachricht schicken
        clientsocket.send(msg.encode())
        # Antwort empfangen
        data2 = clientsocket.recv(1024).decode()
        if not data2:
            # Schließen, falls Verbindung geschlossen wurde
            clientsocket.close()
        else:
            while True:
                data = clientsocket.recv(1024).decode()

                if rec_fields(data):
                    break

                lake = "L"
                #bombe = "B"
                while True:
                    randomDir = random.randint(0,3)
                # Der Versuch irgendwas hinzubekommen
                #     #WALD
                #     if len(data) == 18 and bombe in data[1:18]:
                #         if bombe == data[9]:
                #             break
                #
                #         if bombe in data[1:6] and not data[2] == lake:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #         elif bombe in data[1:6] and not data[10] == lake:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #
                #         if bombe == data[11]:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #
                #         if bombe in data[13:18] and not data[14] == lake:
                #             clientsocket.send(CommandType.DOWN.value.encode())
                #             break
                #         elif bombe in data[13:18] and not data[10] == lake:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #
                #         if bombe == data[7]:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                #     #WIESE
                #     if len(data) == 50 and bombe in data[0:50]:
                #         if bombe == data[25]:
                #             break
                #
                #         if (bombe in data[1:4] or bombe in data[11:14]) and not data[22] == lake:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                #         elif (bombe in data[1:4] or bombe in data[11:14]) and not data[14] == lake:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #
                #         if bombe == data[15]:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #
                #         if bombe == data[5] and not data[14] == lake:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #         elif bombe == data[5] and not data[26] == lake:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #
                #         if (bombe in data[7:10] or bombe in data[17:20]) and not data[26] == lake:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #         elif (bombe in data[7:10] or bombe in data[17:20]) and not data[14] == lake:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #
                #         if bombe in data[21:24] and not data[22] == lake:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                #         elif bombe in data[21:24] and not data[14] == lake:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #
                #         if bombe in data[31:34] and not data[22] == lake:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                #         elif bombe in data[31:34] and not data[34] == lake:
                #             clientsocket.send(CommandType.DOWN.value.encode())
                #             break
                #
                #         if bombe == data[35]:
                #             clientsocket.send(CommandType.DOWN.value.encode())
                #             break
                #
                #         if bombe == data[45] and not data[34] == lake:
                #             clientsocket.send(CommandType.DOWN.value.encode())
                #             break
                #         elif bombe == data[45] and not data[22] == lake:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                #
                #
                #         if bombe in data[27:30]:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #         if bombe in data[31:50]:
                #             clientsocket.send(CommandType.DOWN.value.encode())
                #             break
                #         if bombe in data[21:24]:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                #
                #     if len(data) == 98 and bombe in data[0:98]
                #         if bombe == data[48]:
                #             break
                #         if bombe in data[1:42]:
                #             clientsocket.send(CommandType.UP.value.encode())
                #             break
                #         if bombe in data[51:56]:
                #             clientsocket.send(CommandType.RIGHT.value.encode())
                #             break
                #         if bombe in data[57:98]:
                #             clientsocket.send(CommandType.DOWN.value.encode())
                #             break
                #         if bombe in data[43:48]:
                #             clientsocket.send(CommandType.LEFT.value.encode())
                #             break
                    # Nach oben gehen und Teich ausweichen
                    if randomDir == 0:
                        if len(data) == 18 and not data[2] == lake \
                                or len(data) == 50 and not data[14] == lake \
                                or len(data) == 98 and not data[34] == lake:
                            clientsocket.send(CommandType.UP.value.encode())
                            #time.sleep(0.01)
                            break

                    # Nach rechts gehen und Teich ausweichen
                    if randomDir == 1:
                        if len(data) == 18 and not data[10] == lake \
                                or len(data) == 50 and not data[26] == lake \
                                or len(data) == 98 and not data[50] == lake:
                            clientsocket.send(CommandType.RIGHT.value.encode())
                            #time.sleep(0.01)
                            break

                    # Nach unten gehen und Teich ausweichen
                    if randomDir == 2:
                        if len(data) == 18 and not data[14] == lake \
                                or len(data) == 50 and not data[34] == lake \
                                or len(data) == 98 and not data[62] == lake:
                            clientsocket.send(CommandType.DOWN.value.encode())
                            #time.sleep(0.01)
                            break

                    # Nach links gehen und Teich ausweichen
                    if randomDir == 3:
                        if len(data) == 18 and not data[6] == lake \
                                or len(data) == 50 and not data[22] == lake \
                                or len(data) == 98 and not data[46] == lake:
                            clientsocket.send(CommandType.LEFT.value.encode())
                            #time.sleep(0.01)
                            break
    except socket.error as serr:
        print("Socket error: " + serr.strerror)

