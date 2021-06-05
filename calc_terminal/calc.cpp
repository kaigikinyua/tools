#include<iostream>
#include<string>
using namespace std;

class InputOutPut{
public:
  static string getString(string message){
    cout<<message<<endl;
    string input="";
    cin>>input;
    return input;
  }
};
/*class Operators{
  float addition(){return 0.0}
  float subtraction(){return 0.0}
  float multiplication(){return 0.0}
  float division(){return 0.0}
};
class Operations{
public:
  string problem;
  int stack[1000];
  int currElemOnStack=0;
  Operations(string problem){
    this.problem=problem;
  }
  void digestProblem(){
    string currValue;
    for(int i=0;i<=problem.length();i++){
      if(problem[i]=='+' || problem[i]=='*'){
        stack[currElemOnStack]=problem[i];
      }else{
      //go through the elements appending the numbers toggetther
      try{
          stoi(problem[i]);
          stack[currElemOnStack]=problem[i]
      }catch(...){
        cout<<"Could not convert "<<ans<<" to integer"<<endl;
      }
    }
    }
  }

};
*/
int main(){
  cout<<"Hello World"<<endl;
  string ans=InputOutPut::getString("Enter a mathematical problem");
  cout<<ans.length()<<endl;
  return 0;
}
