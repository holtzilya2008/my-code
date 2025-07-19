import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @Test
    void subString_empty_zero() {
        var str = "";
        assertEquals(0, Solution.subString(str));
    }

    @Test
    void subString_allDifferent_5() {
        var str = "abcde";
        assertEquals(5, Solution.subString(str));
    }

    @Test
    void subString_dupcicate_5() {
        var  str = "ababcdecde";
        assertEquals(5, Solution.subString(str));
    }

    @Test
    void subString_dupcicateSpacesDigits_5() {
        var  str = " a a 2de2de";
        assertEquals(5, Solution.subString(str));
    }

    @Test
    void subString_UpperLowerCase_2() {
        String str = "Aa";
        assertEquals(2, Solution.subString(str));
    }
}