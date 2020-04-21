using System;

public class Files{
    private bool fileExists(){
        return false;
    }
    public static string readFile(string filePath){
        return "Opened File";
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
    public static void Main(string[] args){
        Console.WriteLine("Starting");
        Enc enc=new Enc();
        enc.encrypt("Message");
        enc.decode("Message");
    }
}