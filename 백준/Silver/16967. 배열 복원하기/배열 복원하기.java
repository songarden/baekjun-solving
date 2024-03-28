
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int w = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();
        int[][] array = new int[h+x][w+y];

        for(int i=0;i<h+x;i++){
            for(int j=0;j<w+y;j++){
                array[i][j] = sc.nextInt();
            }
        }

        int[][] newArray = new int[h][w];

        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                if (i<x || j<y) {
                    newArray[i][j] = array[i][j];
                }
                else{
                    newArray[i][j] = array[i][j] - newArray[i-x][j-y];
                }
            }
        }

        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                System.out.print(newArray[i][j] + " ");
            }
            System.out.println();
        }
    }
}
