package java_rmi;
import java.rmi.registry.*;
import java.rmi.*;;

public class Serveur {

    public static void main(String[] args) throws Exception {

        // HelloImpl implémente l'interface distante Hello
        HelloImpl obj = new HelloImpl();

        // Le registre permet aux clients de retrouver l'objet distant
        LocateRegistry.createRegistry(1099);

        // On enregistre l'objet distant dans le registre
        // L'objet sera accessible sous le nom "Hello" à rmi://localhost/Hello
        Naming.rebind("rmi://localhost/Hello", obj);

        // On affiche un message indiquant que le serveur est prêt à recevoir les appels des clients
        System.out.println("Serveur prêt !");
    }
}