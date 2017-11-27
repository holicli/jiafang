#include <stdio.h>
int main()
{
    int a=3;
    int b=8;
    int count =0;
    // scanf("请输入月份%d", &a);
    // scanf("请输入日期%d\n", &b);
    printf("月份%d 日期%d\n", a, b);
    count = (a -1)*2;
    if(b >=8){
        count++;
    }
    if(b>=18){
        count++;
    }
    printf("3count = %d\n", count);
    switch(count%3){
        case 1:printf("白班 乙， 中班 丙， 夜班 甲");break;
        case 2:printf("白班 丙， 中班 甲， 夜班 乙");break;
        case 3:printf("白班 甲， 中班 乙， 夜班 丙");break;

    }
}
