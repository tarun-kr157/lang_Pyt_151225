/*public class Test{
    public static void main(String[] args) {
        System.out.println("Hello world");
    }

}8*/
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Hello, Tarun! Java is running successfully.");
        System.out.print("Enter your age: ");

        int age = sc.nextInt();
        System.out.println("You will be " + (age + 1) + " next year.");

        sc.close();
    }
}

