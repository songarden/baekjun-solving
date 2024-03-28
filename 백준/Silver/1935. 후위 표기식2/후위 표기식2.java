import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Map<Character,Double> dict = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String task = sc.next();
        for (int i=0;i<n;i++){
            dict.put((char)(65+i),(double)sc.nextInt());
        }
        Stack<Double> stack = new Stack<>();
        for (int i=0;i<task.length();i++){
            if (Character.isAlphabetic(task.charAt(i))){
                double num = dict.get(task.charAt(i));
                stack.push(num);
            } else{
                double b = stack.pop();
                double a = stack.pop();
                if(task.charAt(i) == '+'){
                    stack.push(a+b);
                }
                else if (task.charAt(i) == '-'){
                    stack.push(a-b);
                }
                else if(task.charAt(i) == '*'){
                    stack.push(a*b);
                } else if (task.charAt(i) == '/') {
                    stack.push(a/b);
                }
            }
        }
        String answer = String.format("%.2f",stack.pop());
        System.out.println(answer);
    }
}
