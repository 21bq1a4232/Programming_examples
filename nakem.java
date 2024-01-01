import java.util.*;
class Even implements Runnable{
    String name;
    Thread t;
    int y;
    Even(int x,String s){
        y=x;
        name=s;
        t = new Thread(this,name);
    }
    public void run(){
        try{
            System.out.println("thread name " + name);
            System.out.println(y*y);
            Thread.sleep(1000);
        }
        catch(InterruptedException e){
            System.out.println(e);
        }
    }
}
class Odd implements Runnable{
    String na;
    Thread t;
    int a;
    Odd(int x,String u){
        a=x;
        na=u;
        t = new Thread(this,na);
    }
    public void run(){
        try{
            System.out.println("thread name:" + na);
            System.out.println(a*a*a);
            Thread.sleep(1000);
        }
            catch(InterruptedException q){
            System.out.println(q);
        }
    }
}
class nakem{
    public static void main(String []args){
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        Thread t;
        System.out.println("enter the range:");
        int n = sc.nextInt();
        for(int i=1;i<=n;i++){
            int q = r.nextInt(n);
            if(q%2==0){
                Even e =new Even(q,"even");
                e.t.start();
            }
            else{
                Odd o = new Odd(q,"Odd");
                o.t.start();
            }
        }
    }
}