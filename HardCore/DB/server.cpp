#include<iostream>
#include<sys/socket.h>
#include<netinet/in.h>
using namespace std;

class Connect{
    Connect(){
        int server_fd,new_socket,valread;
        struct server
        {
            int opt=1;
            char buffer[1024]={0};
            char *hello="Hello From Server";
        };
        
    }
    int newConn(){
        cout<<"Receiving Connection"<<endl;
        return 0;
    }
};
int main(){
    cout<<"Server Running on POrt"<<endl;
    return 0;
}