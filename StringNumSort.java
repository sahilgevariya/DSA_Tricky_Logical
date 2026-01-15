public class Main {
    public static void main(String[] args) {
        List<String> numbers = Arrays.asList(
                "10.5", "-2.3", "-1.5", "-1.2", "-1.20",
                "2.50", "2", "2.5", "2.1234",
                "-10", "0.5", "-0.25",
                "85", "83", "0", "-0"
        );

        numbers.sort(Main::compareNumericStrings);
        System.out.println(nums);
}
    
    public static int compareNumericStrings(String a, String b) {
        // System.out.println(a + " > " + b);
        
        boolean negA = a.charAt(0) == '-';
        boolean negB = b.charAt(0) == '-';
        
        // If any of the num is negative then comparison is easy
        if (negA && !negB) return -1;
        if (!negA && negB) return 1;
        
        // Now both number can either positive or negative
        if (negA) a = a.substring(1);
        if (negB) b = b.substring(1);
        
        String[] partA = a.split("\\.", 2);
        String[] partB = b.split("\\.", 2);
        
        // If INT part's length is not equals then comparison is easy
        if (partA[0].length() != partB[0].length()) {
            int isAbigger = partA[0].length() - partB[0].length();
            return negA ? -isAbigger : isAbigger;
        }
        
        // If equals then check if INT part is same, if not then comparison is easy
        int isEqual = partA[0].compareTo(partB[0]);
        if (isEqual != 0) return negA ? -isEqual : isEqual;
        
        // Now we sure that INT part is same, so compare FRAC part
        String fracA = partA.length > 1 ? partA[1] : "0";
        String fracB = partB.length > 1 ? partB[1] : "0";
        
        // We can use compareTo directly as for fraction,
           // If prefix is not equal then compareTo does char-by-char comparison 
           // and if its then based on length of string
        /* 
        // Normalize lengths: "5" vs "123" -> "500" vs "123"
        int maxLen = Math.max(fracA.length(), fracB.length());
        while (fracA.length() < maxLen) fracA += "0";
        while (fracB.length() < maxLen) fracB += "0";
        */
        
        int isAbigger = fracA.compareTo(fracB);
        return negA ? -isAbigger : isAbigger;
    }
}
