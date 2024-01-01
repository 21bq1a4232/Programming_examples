class Stack{
    int stk[]=new int[10];
    int c;
    Stack(){
        c=-1;
    }
    void push(int i){
        if(c==9){
            System.out.println("full");
        }
        else{
            stk[++c]=i;
        }
    }
    int pop(){
        if (c<0){
            System.out.println("empty");
            return 0;
        }
        else{
            return stk[c--];
        }


    }


}