import java.util.Scanner;
class Employee{
    double bp,da,hra,pf,scf, gs, ns;
    Scanner sc=new Scanner(System.in);
    Scanner scs=new Scanner(System.in);
    String emp_name,emp_id,address,mail_id;
    long mobileno;
    void getdata(){
        System.out.println("enter employee name:");
        emp_name=scs.next();
         System.out.println("enter employee id:");
        emp_id=scs.next();
         System.out.println("enter employee address:");
        address=scs.next();
         System.out.println("enter employeee mailid:");
        mail_id=scs.next();
         System.out.println("enter employee mobileno:");
        mobileno=sc.nextLong();
    }
    void cal() {
        System.out.println("enter basicpay of employee:");
        bp=sc.nextDouble();
        da=(97/100)*bp;
        hra=(10/100)*bp;
        pf=(12/100)*bp;
        scf=(0.1/100)*bp;
        gs=bp+da+hra+pf;
        ns=gs-pf-scf;
    }
    void payslip1() {
        System.out.println("Programmer name:"+emp_name);
        System.out.println("Programmer id:"+emp_id);
        System.out.println("Programmer address:"+address);
        System.out.println("Programmer mail id:"+mail_id);
        System.out.println("Programmer mobileno:"+mobileno);
        System.out.println("Programmer da:"+da);
        System.out.println("Programmer hra:"+hra);
        System.out.println("Programmer pf:"+pf);
        System.out.println("Programmer scf:"+scf);
        System.out.println("Programmer grossalary:"+gs);
        System.out.println("Programmer netsalary:"+ns);
    }
    void payslip2() {
        System.out.println("Assistant Professor name:"+emp_name);
        System.out.println("Assistant Professor id:"+emp_id);
        System.out.println("Assistant Professor address:"+address);
        System.out.println("Assistant Professor mail id:"+mail_id);
        System.out.println("Assistant Professor mobileno:"+mobileno);
        System.out.println("Assistant Professor da:"+da);
        System.out.println("Assistant Professor hra:"+hra);
        System.out.println("Assistant Professor pf:"+pf);
        System.out.println("Assistant Professor scf:"+scf);
        System.out.println("Assistant Professor grossalary:"+gs);
        System.out.println("Assistant Professor netsalary:"+ns);
    }
    void payslip3()  {
        System.out.println("Associate professor name:"+emp_name);
        System.out.println("Associate professor id:"+emp_id);
        System.out.println("Associate professor address:"+address);
        System.out.println("Associate professor mail id:"+mail_id);
        System.out.println("Associate professor mobileno:"+mobileno);
        System.out.println("Associate professor da:"+da);
        System.out.println("Associate professor hra:"+hra);
        System.out.println("Associate professor pf:"+pf);
        System.out.println("Associate professor scf:"+scf);
        System.out.println("Associate professor grossalary:"+gs);
        System.out.println("Associate professor netsalary:"+ns);
    }
    void payslip4(){
        System.out.println("Professor name:"+emp_name);
        System.out.println("Professor id:"+emp_id);
        System.out.println("Professor address:"+address);
        System.out.println("Professor mail id:"+mail_id);
        System.out.println("Professor mobileno:"+mobileno);
        System.out.println("Professor da:"+da);
        System.out.println("Professor hra:"+hra);
        System.out.println("Professor pf:"+pf);
        System.out.println("Professor scf:"+scf);
        System.out.println("Professor grossalary:"+gs);
        System.out.println("Professor netsalary:"+ns);
    }
}
class Programmer extends Employee{
    Programmer(){
        getdata();
        cal();
        payslip1();
    }
    }
class AssistantProfessor extends Employee{
    AssistantProfessor(){
    getdata();
        cal();
        payslip2();
    }
}
class AssociateProfessor extends Employee{
    AssociateProfessor(){
    getdata();
        cal();
        payslip3();
    }
}
class Professor extends Employee{
     Professor(){
    getdata();
        cal();
        payslip4();
    }
}
public class Lab8
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
	Employee in=new Employee();
	int choice;
	do {
	System.out.println("###menu for type of employee###");
	System.out.println("1.Programmer\n2.Assistant proffesor\n3.Associate professor\n4.Professor");
	System.out.println("enter your choice:");
	choice=sc.nextInt();
	switch(choice) {
	case 1:
	System.out.println("Programmer details");
	Programmer p=new Programmer();
	break;
	case 2:
	System.out.println("Assistant proffesor details");
	AssistantProfessor a=new AssistantProfessor();
	break;
	case 3:
	System.out.println("Assosiate professor details");
	AssociateProfessor b=new AssociateProfessor();
	break;
	case 4:
	System.out.println("Professor details");
	Professor c=new Professor();
	}
	}while(choice!=5);
	}
}
