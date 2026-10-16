package tp.java_test;

import javax.xml.ws.Endpoint;

public class Application {

    public static void main(String[] args) {
        String url = "http://localhost:8081/";
        Endpoint.publish(url, new MonService());
        System.out.println("service accessible à :" + "http://localhost:8081/?wsdl" );

    }
}
 
