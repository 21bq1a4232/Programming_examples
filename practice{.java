class Abc{
    int a;
    int b;
    int c;
    void Abc(int x, int y){
        this.a=x;
        this.b=y;
        this.c=this.b-this.a;
    }
    int b(){
        return c;
    }
}
class TestMe(){
    public static void main(String args[]){
        Abc a=new Abc();
        a.Abc(10,20);
        int z=a.b();
        System.out.println(z);
        
    }
}