import java.util.*;
class LastString{
    public static void main(String args[]){
        String string='';
        Scanner in=new Scanner(System.in)
        System.out.println("enter a string:");
        string=in.nextLine();
        System.out.println("Last string is:"+string.substring(string.lastIndexOf(''),string.length());
    }

}