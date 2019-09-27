#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;

string enc(string name){
	string enc="";
	char keys[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	for(int i=0;i<name.length();i++){
		for(int j=0;j<sizeof(keys);j++){
			if(name[i]==keys[j]){
				int offset=j+10;
				if (offset>(sizeof(keys)-1)){
					cout<<offset<<endl;
					offset=offset-25;
				}
				enc+=keys[offset];
			}else{
				if(j==sizeof(keys)-1){
					enc+=name[i];
				}
			}
		}
	}
	return enc;
}
string rvs(string name){
	string rvs="";
	for (int i=name.length();i>=0;i--){
		rvs+=name[i];
	}
	rvs=enc(rvs);
	return rvs;
}
int main(){
	cout<<"Hello World"<<endl;
	string name;cin>>name;cout<<endl;
	cout<<rvs(name)<<endl;
}