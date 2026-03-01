// Version 1 (Official):
// javac Warmup-1/sleep_in/Main.java
// java -cp Warmup-1/sleep_in Main

public class Main {
    public static boolean sleepIn(boolean weekday, boolean vacation) {
        if (!weekday || vacation) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        // Example test cases
        System.out.println(sleepIn(false, false)); // true
        System.out.println(sleepIn(true, false));  // false
        System.out.println(sleepIn(false, true));  // true
    }
}