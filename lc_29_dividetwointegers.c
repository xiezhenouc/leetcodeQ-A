#include<stdio.h>
#include<limits.h>

/*
 * above all, I try it slowest method, it is time limited.
 * this idea is similar to 10 to 2 
 * for example:
 * 	100(10) -> xxx(2)
 * 	1 2 4 8 16 32 64 128
 * 	0 0 1 0 0  1  1  0
 * firstly, almost there, then get off it, and do again
 */
long long mydivide(long long a, long long b)
{
	if(b == 0)  	return INT_MAX;
	if(a < b)	return 0;
	if(a == b)	return 1;

	long long sum = b;
	long long multi = 1;
	while(sum + sum <= a)
	{
		sum += sum;
		multi += multi;
	}
	return multi + mydivide(a - sum, b);
}

/*
 *  I made a serious mistake here
 *  	1 that is sizeof(int) = 4, but sizeof(long) = 4, sizeof(long long) = 8
 *  	2 abs() return is int, if abs(a(-INT_MAX-1)) = -INT_MAX-1, a is integer;
 *	3 return range is [-INT_MAX-1, INT_MAX], it's sure
 */
int divide(int acopy, int bcopy)
{
	long long a = acopy;
	long long b = bcopy;

	if(b == 0)	return INT_MAX;

	int flag = 1;
	if(a > 0 && b < 0 || a < 0 && b > 0)
	{
		flag = -1;
	}

	long long anew = a > 0 ? a : (0 - a); 
	long long bnew = b > 0 ? b : (0 - b); 
        printf("%lld, %lld\n", anew, bnew);
	if(anew == 0 || anew < bnew)	return 0;

	long long result = mydivide(anew, bnew);
        result = flag == 1 ? result : (0 - result);
	
        if(-INT_MAX-1 <= result && result <= INT_MAX)    return (int)result;
	else						 return INT_MAX;
}

int main()
{
	int a[6] = {1, 2, 3, 4, INT_MAX, -INT_MAX-1};
	int b[6] = {0, 2, 1, 2, 1, 1};
	int i;
	for(i = 0; i < 6; i++)
	{
		printf("%d / %d = %d\n", a[i], b[i], divide(a[i], b[i]));
	}
	//printf("%d\n", sizeof(long));
	//printf("%d\n", sizeof(long long));

	return 0;
}
