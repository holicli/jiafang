import java.util.Scanner;

public class date{
    public static void main(String args[]){
    int a;
    int b;
    int count =0;
    // scanf("请输入月份%d", &a);
    // scanf("请输入日期%d\n", &b);
   Scanner in =  new Scanner(System.in);
    a = in.nextInt();
    b = in.nextInt();
    System.out.println("月份"+a+"日期"+b);
    count = (a -1)*2;
    if(b >=8){
        count++;
    }
    if(b>=18){
        count++;
    }
    switch(count%3){
        case 1:System.out.println("白班 乙， 中班 丙， 夜班 甲");break;
        case 2:System.out.println("白班 丙， 中班 甲， 夜班 乙");break;
        case 3:System.out.println("白班 甲， 中班 乙， 夜班 丙");break;
        default:
            System.out.println("白班 甲， 中班 乙， 夜班 丙");
    }
    }
}
