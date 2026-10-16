package java_rmi;

// Java rmi permet d'appeler objet situé sur une autre machine
import java.rmi.*;
//1ere étape consiste à créer l'interface distance
// Remote permet de créer l'interface distante

public interface Hello extends Remote {
    //on définit juste la signature de la méthode
    //RemoteException permet de lever les exceptions
    String sayHello (String name) throws RemoteException;
}


