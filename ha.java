import java.util.Random;
import java.util.Scanner;
class Thread1 implements Runnable{
    Thread t;
    int x;
    String name;
    Thread1(int n,String z){
        x=n;
        name=z;
        t = new Thread(this,name);
    }
    public void run(){
        System.out.println("the name my thread is : " + name);
        try{
            for(int j=1;j<x;j++){
                if(x%j==0){
                    System.out.println(j);
                    t.sleep(1000);
                }
            }
        }catch(InterruptedException e){
            System.out.println(e);
        }
    }
}
class Thread2 implements Runnable{
    Thread t;
    int g;
    String name;
    Thread2(int n,String na){
        g=n;
        name=na;
        t = new Thread(this,name);
    }
    public void run(){
        System.out.println("the name my thread is : " + name);
        try{
            for(int e=1;e<g;e++){
                if(g%e==0){
                    System.out.println(e);
                    t.sleep(1000);
                }
            }
        }catch(InterruptedException e){
            System.out.println(e);
        }
    }
}
class ha{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        Thread t;
        System.out.println("enter the range to print the even and odd numbers : ");
        int n = sc.nextInt();
        for(int i =0;i<n;i++){
            int f = r.nextInt(n);
            Thread1 t1 = new Thread1(f,"Even");
            t1.t.start();
            Thread2 t2 = new Thread2(f,"Odd");
            t2.t.start();
        }
    }
}