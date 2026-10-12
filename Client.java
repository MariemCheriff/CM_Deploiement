import java.rmi.*;

public class Client {

    public static void main(String[] args) throws Exception {

        // il faut rechercher l'objet distant enregistré sur le serveur
        // Naming.lookup() récupère l'objet associé au nom "Hello"à l'adresse rmi://localhost/Hello
        // Le résultat est converti en type Hello (interface distante)
        Hello stub = (Hello) Naming.lookup("rmi://localhost/Hello");

        // On appelle la méthode distante sayHello() en envoyant "Samir"
        // serveur renvoie le résultat
        // résultat est ensuite affiché
        System.out.println(stub.sayHello("Meriem"));
    }
}