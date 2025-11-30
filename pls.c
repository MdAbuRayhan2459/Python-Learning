#include<stdio.h>
int main()
{
int marks;
printf("Enter the marks (0-100) :");
scanf("%d", &marks);
if(marks >=0 && marks <=30)
{  printf("FAIL\n");
}
else{
printf("PASS\n");
}
return 0;
}
