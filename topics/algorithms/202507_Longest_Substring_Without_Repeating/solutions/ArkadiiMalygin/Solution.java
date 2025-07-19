public class Solution {
    public static int subString( String str) {
        int maxLength = 0;
        StringBuilder subString = new StringBuilder();
        for (char c : str.toCharArray()) {
            int indexThere = subString.indexOf(String.valueOf(c));
            if (indexThere != -1) {
                subString = new StringBuilder(subString.substring(indexThere + 1));
            }
            subString.append(c);
            maxLength = Math.max(maxLength, subString.length());
        }
        return maxLength;

    }
}