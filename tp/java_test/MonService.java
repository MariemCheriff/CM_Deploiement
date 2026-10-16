package tp.java_test;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService(targetNamespace = "http://institutgalilee.fr")
public class MonService {

    @WebMethod(operationName = "affichage")
    public String bonjour(){
        return "Bonjour !";
    }

    @WebMethod
    public double somme(double a, double b){
        return a+b;
    }
}
 