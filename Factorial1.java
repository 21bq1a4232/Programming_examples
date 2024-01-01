class Factorial{
    int fact;
    int factorial(int n){
        if(n==1){
            return 1;
        }
        else{
            fact=n*factorial(n-1);
        }
        return fact;
    }
}