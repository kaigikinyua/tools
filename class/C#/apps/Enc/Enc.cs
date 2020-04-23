using System;
using System.IO;
public class Files{
    public static void readFile(string filePath){
        StreamReader reader=new StreamReader("keys.txt");
        string data=reader.ReadLine();
        while(data!=null){
            Console.WriteLine(data);
            Console.WriteLine(data[3]);
            data=reader.ReadLine();
        }
        reader.Close();
    }
    public static void writeToFile(string filePath){

    }
    
}



public class Enc{
    public string encrypt(string message){
        Console.WriteLine("Encrypting......");
        return message;
    }
    public string decode(string message){
        Console.WriteLine("Decrypting......");
        return message;
    }
    public string flip(string message){
        return message;
    }

    public static void Main(string[] args){
        Files.readFile("/home");
    }
}