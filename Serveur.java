import java.rmi.registry.*;
import java.rmi.*;;

public class Serveur {

    public static void main(String[] args) throws Exception {

        // 1. Créer une instance de l'objet distant
        // HelloImpl implémente l'interface distante Hello
        HelloImpl obj = new HelloImpl();

        // 2. Créer le registre RMI sur le port 1099
        // Le registre permet aux clients de retrouver
        // l'objet distant grâce à son nom
        LocateRegistry.createRegistry(1099);

        // 3. Enregistrer l'objet distant dans le registre
        // L'objet sera accessible sous le nom "Hello"
        // à l'adresse rmi://localhost/Hello
        Naming.rebind("rmi://localhost/Hello", obj);

        // 4. Afficher un message indiquant que le serveur
        // est prêt à recevoir les appels des clients
        System.out.println("Serveur prêt !");
    }
}