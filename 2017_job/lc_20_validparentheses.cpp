#include<iostream>
#include<stack>

using namespace std;

int isValid(string s)
{
	stack<char> backet;
        int i;
	for(i = 0; i < s.length(); i++)
	{
		if(s[i] == '{' || s[i] == '[' || s[i] == '(')
		{
			cout << "in:" << s[i] << " ";
			backet.push(s[i]);
		}
		else if(!backet.empty())
		{
			if(backet.top() == '{' && s[i] == '}' || backet.top() == '[' && s[i] == ']' || backet.top() == '(' && s[i] == ')')
			{
				cout << "out:" << s[i] << " ";
				backet.pop();
			}
			else
			{
				return 0;
			}
		}
		else if(backet.empty())
		{
			return 0;
		}
	}

	if(backet.size() == 0)    return 1;
	else			  return 0;
}

int main()
{
	string s = "{[}]";
        cout << isValid(s);	
	cout << endl;
	return 0;
}
