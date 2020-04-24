using System;
using System.IO;
public class Files{
    public static string readFile(string filePath){
        StreamReader reader=new StreamReader(filePath);
        string data=reader.ReadLine();
        while(data!=null){
            Console.WriteLine(data);
            data=reader.ReadLine();
        }
        reader.Close();
        return data;
    }
    public static void writeToFile(string filePath){

    }
    
}



public class Enc{
    public static string encrypt(string message){
        Console.WriteLine("Encrypting......");
        //flip message
        //encrypt
        Enc e=new Enc();
        string encMessage=e.flip(message);
        string keys=e.getKeys();
        return encMessage;
    }
    public string decode(string message){
        Console.WriteLine("Decrypting......");
        //decrypt
        //flip message
        Enc e=new Enc();
        string decMessage=e.flip(message);
        string keys=e.getKeys();
        return decMessage;
    }
    //flip messages
    public string flip(string message){
        int len=message.Length;
        //char [] messagedup=new char[len+1];
        string messagedup="";
        while(len>0){
            messagedup+=message[len-1];
            Console.WriteLine(messagedup);
            len--;
        }
        return messagedup;
    }

    private string getKeys(){
        string keys=Files.readFile("keys.txt");
        Console.WriteLine(keys);
        return keys;
    }
    public static void Main(string[] args){
        Enc.encrypt("Hello World");
    }
}