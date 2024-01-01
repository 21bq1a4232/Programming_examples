import java.util.Scanner;
import java.util.Random;
public class Length{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the name of the movie:");
        String movie=sc.nextLine();
        System.out.println("enter the number of persons (>6):");
        int n=sc.nextInt();
        String[] Person= new String[n];
        if (n>=6){
            for (int i=0;i<n;i++){
                System.out.println("Enter the name of the person"+(i+1));
                String name=sc.nextLine();
                Person[i].add(name);
            }
            System.out.println("select your budget:");
            System.out.println("1-30 seats costs 70/- per head");
            System.out.println("31-70 seats costs 150/- per head");
            System.out.println("71-100 seats costs 300/- per head");
            int x=sc.nextInt();
            int[] Place=new int[n];
            if (x<=30){
                Random r=new Random(1,100);
                for (int i=0;i<n;i++){
                    int p=r.nextInt();
                    Place[i].add(r);
                }
                System.out.println(movie+" is the movie you have booked for");
                System.out.println("the persons are:");
                for (int i=0;i<n;i++){
                    System.out.println(Person[i]);
                }
                int f=n*70;
                System.out.println("the total fare is "+f);
            }
            else if (x<=100){
                Random r=new Random(31,70);
                for (int i=0;i<n;i++){
                    p=r.nextInt();
                    Place[i].add(r);
                }
                System.out.println(movie+" is the movie you have booked for");
                System.out.println("the persons are:");
                for (int i=0;i<n;i++){
                    System.out.println(Person[i]);
                }
                int f=n*150;
                System.out.println("the total fare is "+f);
            }
            else{
                Random r=new Random(71,100);
                for (int i=0;i<n;i++){
                    p=r.nextInt();
                    Place[i].add(r);
                }
                System.out.println(movie+" is the movie you have booked for");
                System.out.println("the persons are:");
                for (int i=0;i<n;i++){
                    System.out.println(Person[i]);
                }
                int f=n*300;
                System.out.println("the total fare is "+f);
            }
        }
    }   
}