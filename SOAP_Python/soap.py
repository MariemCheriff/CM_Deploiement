from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


# On va définir le service Web SOAP
# ServiceBase est la classe de base des services Spyne
class HelloService(ServiceBase):

    # On déclare une opération SOAP qui renvoie une chaîne de caractères
    @rpc(_returns=Unicode)
    def say_hello(ctx):
        # On renvoie la réponse au client
        return "Bonjour"


application = Application(
    [HelloService],

    tns='spyne.examples.hello',

    in_protocol=Soap11(validator='lxml'),

    out_protocol=Soap11()
)


wsgi_app = WsgiApplication(application)


if __name__ == '__main__':

    # On crée le serveur HTTP sur le port 8000
    server = make_server('0.0.0.0', 8000, wsgi_app)

    # On affiche un message pour indiquer que le serveur est prêt
    print("Service SOAP démarré sur http://localhost:8000")

    # On maintient le serveur actif pour recevoir les requêtes
    server.serve_forever()


# Et on va tester DU SERVICE WEB AVEC SOAPUI et on vérifie que la réponse contient "Bonjour".
