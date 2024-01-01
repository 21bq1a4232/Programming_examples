import java.util.Scanner;
class SpeedConverter{
    public double toMilesPerHour(double kilometersPerHour){
        if(kilometersPerHour<0){
            return -1;
        }
        else{
            long r=Math.round(kilometersPerHour*1.609);
            return r;
        }
    }
}
class U extends SpeedConverter{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the distance in miles:");
        double x = sc.nextDouble();
        SpeedConverter s = new SpeedConverter();
        System.out.println(s.toMilesPerHour(x));
    }
}