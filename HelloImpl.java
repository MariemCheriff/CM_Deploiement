import java.rmi.server.*;
import java.rmi.*;

// 2eme etape: implémenter l'interface Hello 
//UnicastRemoteObject permet à l'objet d'etre exporté au réseau
public class HelloImpl extends UnicastRemoteObject implements Hello {
    public HelloImpl() throws RemoteException {
        super();
    }
    //Implémentation de la méthode sayHello
    public String sayHello(String name) throws RemoteException {
        return "Bonjour " + name + "!";
    }
}
