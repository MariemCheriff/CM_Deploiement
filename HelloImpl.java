import java.rmi.server.*;
import java.rmi.*;

public class HelloImpl extends UnicastRemoteObject implements Hello {
    public HelloImpl() throws RemoteException {
        super();
    }

    public String sayHello(String name) throws RemoteException {
        return "Bonjour " + name + "!";
    }
}
