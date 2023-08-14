package javaapplication6;
import java.security.SecureRandom;
import java.util.UUID;

public class JavaApplication6 
    {
    public static void main(String[] args)
        {
        System.out.println(generar().toString());
        }
     public static String generar(){
        String l = Long.toString(System.currentTimeMillis());
        SecureRandom secureRandom = new SecureRandom();
        String valor = new UUID(secureRandom.nextLong() ^ System.currentTimeMillis(), secureRandom.nextLong()).toString();
        return valor;
        } 
    }