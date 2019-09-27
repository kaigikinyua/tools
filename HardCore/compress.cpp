#include<iostream>
using namespace std;
string fill(string str){
    int i=0;
    string empt=" *";
    while(i<str.length()){
        if(str[i]==empt[0]){
            str[i]=empt[1];
        }
        i++;
    }
    return str;
}
string compress(string str){
    int i=0;string comp="";
    while(i<(str.length()-1)){
        if(str[i]==str[i+1]){
            string fi=str[i]+".";
            comp+=fi;
            cout<<"found match"<<endl;
        }
     i++;
    }
    return comp;
}
int main(){
    cout<<"Enter a string"<<endl;
    string name;std::getline(cin,name);cout<<"\n";
    string fi;fi=compress(fi);
    cout<<fi<<endl;
}