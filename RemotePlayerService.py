__author__ = 'matt and tony'
import rpyc


class RPYCPlayerService(rpyc.Service):
    def on_connect(self):
        print("Connected to server")

    def on_disconnect(self):
        print("Disconnected from server")

    def exposed_get_name(self, player):
        return player.get_name()

    def exposed_play(self):
        return None

    def exposed_notify(self):
        return None

    def exposed_get_player(self):
        return None

    def exposed_start_player_service(self):
        return None

# if __name__ == "__main__" :
# from rpyc.utils.server import ThreadedServer
#     server = ThreadedServer(RemotePlayerService,port=12345,protocol_config={'allow_public_attrs':True})
#     server.start()

