package byteToString;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.io.IOException;  
import java.nio.charset.StandardCharsets;  


public class GenerateSignature {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException {
	   byte[] B = {48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102};
	   String str=args[0];
	   System.println(str);
	   byte[] bArr=str.getBytes("utf-8");		
	   MessageDigest instance = MessageDigest.getInstance("MD5");
       instance.update(bArr, 0, bArr.length);
       bArr=instance.digest();
       StringBuilder sb = new StringBuilder(bArr.length);
       for (byte b : bArr) {
            int i = b & 255;
            byte[] bArr2 = B;
            sb.append((char) bArr2[i >>> 4]);
            sb.append((char) bArr2[i & 15]);
        }
       String r=sb.toString();
       System.out.println(r);
    }
}
