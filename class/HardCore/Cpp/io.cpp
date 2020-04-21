#include <iostream>
#include "io.h"
using namespace std;

//contructor
IO::IO(){

}

char* IO::keyboard_input(char value[]){  
    cout<<value<<endl;
    char *p=&value[0];
    return p;
}

/*void IO::output(char output){
    string f_output=string(output);
    cout<<output<<endl;
}*/