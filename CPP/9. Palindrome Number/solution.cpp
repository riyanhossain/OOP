#include <iostream>
#include <string>

class Solution
{
public:
    bool isPalindrome(int x)
    {
        int r = false;
        if (x <= -1)
            return r;
        else
        {
            int len = std::to_string(x).length();
            std::string nx = std::to_string(x);

            if (len == 1)
            {
                r = true;
                return r;
            }

            for (int i = 0; i < len / 2; i++)
            {
                if (nx[i] == nx[len - i - 1])
                {
                    r = true;
                }
                else
                {
                    r = false;
                    break;
                }
            }
        }

        return r;
    }
};

int main()
{
    Solution s;
    std::cout << s.isPalindrome(0);
    return 0;
}