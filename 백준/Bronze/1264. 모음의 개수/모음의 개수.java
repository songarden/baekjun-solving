import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Queue<String> sentence = new LinkedList<>();
        String str = new String();
        while(true){
            str = sc.nextLine();
            if(str.equals("#")){
                break;
            }
            sentence.offer(str);
        }


        int moem;
        while(!sentence.isEmpty()) {
            moem = 0;
            str = sentence.poll();
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == 'a' || str.charAt(j) == 'e' || str.charAt(j) == 'i' || str.charAt(j) == 'o' || str.charAt(j) == 'u' || str.charAt(j) == 'A' || str.charAt(j) == 'E' || str.charAt(j) == 'I' || str.charAt(j) == 'O' || str.charAt(j) == 'U') {
                    moem++;
                }
            }
            System.out.println(moem);
        }
    }
}