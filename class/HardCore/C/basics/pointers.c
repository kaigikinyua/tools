#include<stdio.h>
//function prototypes

void assign_p();

int main(){
    printf("------Refresher-----\n");
}

void assign_p(){
    int age=10;
    int *age_p=&age;
    printf("%d\n --original variable\n",age);
    printf("%d\n --using memory\n",*age_p);
    //&age --age memory age--value of age
    //*pointer_variable contains the value
}