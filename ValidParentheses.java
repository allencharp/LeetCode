import java.util.*;

/**
 * Created by allen on 2016/10/22.
 */
public class ValidParentheses {

    public boolean isValid(String s) {

        Stack<Character> stack = new Stack<Character>();

        for(int i = 0; i < s.length(); i++)
        {
            char charVal = s.charAt(i);

            if (charVal == '(')
                stack.push(charVal);
            else if(charVal == '{')
                stack.push(charVal);
            else if(charVal == '[')
                stack.push(charVal);

            if(!stack.isEmpty() && charVal == ')') {
                Character re = stack.pop();
                if(re != '(')
                    return false;
            }
            else if(stack.isEmpty() && charVal == ')')
                return false;
            else if(!stack.isEmpty() && charVal == '}') {
                Character re = stack.pop();
                if(re != '{')
                    return false;
            }
            else if(stack.isEmpty() && charVal == '}')
                return false;
            else if(!stack.isEmpty() && charVal == ']') {
                Character re = stack.pop();
                if (re != '[')
                    return false;
            }
            else if(stack.isEmpty() && charVal == ']')
                return false;

        }

        if(stack.size()!=0)
            return false;

        return true;
    }
}
