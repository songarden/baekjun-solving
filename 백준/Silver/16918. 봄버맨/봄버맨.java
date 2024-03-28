import java.util.*;


public class Main {
    static int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int n = sc.nextInt();

        char [][] arr = new char [r][c];
        int [][] cntArr = new int[r][c];

        for (int i=0;i<r;i++){
            String a = sc.next();
            for (int j=0;j<c;j++){
                arr[i][j] = a.charAt(j);
                if (arr[i][j] == 'O') {
                    cntArr[i][j] = 1;
                }
            }
        }
        int i = 1;
        while(i <= n){
            for (int j=0;j<r;j++){
                for(int k=0;k<c;k++){
                    if(cntArr[j][k] == 3) {
                        arr[j][k] = '.';
                        cntArr[j][k] = 0;
                        for(int[] dir : dirs){
                            if(j+dir[0]>=0 && j+dir[0]<r && k+dir[1]>=0 && k+dir[1]<c){
                                if ((dir[0]>0 || dir[1]>0) && cntArr[j+dir[0]][k+dir[1]] == 3){
                                    continue;
                                }
                                arr[j+dir[0]][k+dir[1]] = '.';
                                cntArr[j+dir[0]][k+dir[1]] = 0;
                            }
                        }
                    } else if (arr[j][k] == 'O') {
                        cntArr[j][k] += 1;
                    }
                }
            }
            if(i%2 == 0){
                for(int j=0;j<r;j++){
                    for(int k=0;k<c;k++){
                        if(arr[j][k] != 'O'){
                            arr[j][k] = 'O';
                            cntArr[j][k] = 1;
                        }
                    }
                }
            }
            i++;
        }

        for(char [] array : arr){
            for(char spot : array){
                System.out.print(spot);
            }
            System.out.println();
        }
    }
}
