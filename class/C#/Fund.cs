using System;

class Fund{
    public static void Main(string[] args){
        InputIO.output("Hello World");
        InputIO.input("Enter your name"); 
        TypesAndLoops.myArrays();
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
    public static string readFile(string filepath){
        return "Not implemented";
    }
    public static bool writeToFile(string filepath){
        return false;
    }

    //private methods
    private void fileExists(string filepath){
        InputIO.output("Not implemented");
    }

}