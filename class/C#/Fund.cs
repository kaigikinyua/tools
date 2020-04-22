using System;
using System.IO;
class Fund{
    public static void Main(string[] args){
        InputIO.readFile("filepath");
        InputIO.writeToFile("filepath");
    }
}

class TypesAndLoops{
    public static void myArrays(){
        int[] myarray=new int[10];//int[] myArray;
        //initialization : string[] arrayName ={'C#','C++'}
        for(int i=0;i<10;i++){
            myarray[i]=i*32;
        }
        bool stop=false;int j=0;
        while(stop==false){
            Console.WriteLine("Value at index {0} is {1}",j,myarray[j]);
            if(j>8){
                stop=true;
            }
            j++;
        }
    }
}


class InputIO{
    //console io
    public static void output(string message){
        Console.WriteLine("Output {0}",message);
    }
    public static string input(string message){
        Console.WriteLine(message);
        string userInput=Console.ReadLine();
        Console.WriteLine("User Input: {0}",userInput);
        InputIO.parser(userInput);
        return userInput;
    }
    public static void parser(string data){
        //conditional parsing
        int intValue;
        bool parseState=Int32.TryParse(data, out intValue);
        Console.WriteLine(parseState?"The number is "+intValue:"Value is not int");
    }
    //files io
    public static void readFile(string filepath){
        StreamReader read=new StreamReader("sample.txt");
        string line=read.ReadLine();//read.ReadToEnd();
        int lineNum=0;
        while(line!=null){
            lineNum++;
            Console.WriteLine(line);
            line=read.ReadLine();
        }
        read.Close();
    }
    public static void writeToFile(string filepath){
        StreamWriter writter=new StreamWriter("fileIO.txt");
        string[] lines={"line one","abceefasdf","faeafgava"};
        for(int i=0;i<3;i++){
            writter.WriteLine(lines[i]);
        }
        writter.Close();
    }

    //private methods
    private void fileExists(string filepath){
        InputIO.output("Not implemented");
    }

}