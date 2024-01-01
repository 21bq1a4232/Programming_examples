class Test{
    public static void main(String args[]){
        Stack st1=new Stack();
        for(int i=0;i<10;i++){
            st1.push(i);
        }
        for(int i=0;i<10;i++){
            System.out.println(st1.pop());
        }
        
    }
}
