// Main class
public class myClass {

    // Main driver method
    public static void main(String[] args)
    {
        int nm = 5;
        int x = 0;
        for (int i = 1; i <= nm; i++)
        {
            x = i - 1;
            for (int j = i; j <= nm - 1; j++)
            {

                // First Number Space
                System.out.print(" ");

                // Space between Numbers
                System.out.print("  ");
            }

            for (int j = 0; j <= x; j++)
                System.out.print((i + j) < 10
                                     ? (i + j) + "  "
                                     : (i + j) + " ");

            for (int j = 1; j <= x; j++)
                System.out.print((i + x - j) < 10
                                     ? (i + x - j) + "  "
                                     : (i + x - j) + " ");

            // By now we reach end for one row, so
            // new line to switch to next
            System.out.println();
        }
    }
}