#include<stdio.h>
/*
 *  first idea is good, but not think more
 *  if I can think more about time limit, I will get good answer
 *  what I doubt is "" "" is not strStr, because, their lengths equals to 0
 */
int strStr(char* haystack, char* needle)
{
	char *p = haystack, *q = needle;
	
	if(p == NULL || q == NULL)	return -1;

	int needlelen = 0;
        while(q[needlelen] != '\0')
	{
		needlelen += 1;
	}
	int haystacklen = 0;
	while(p[haystacklen] != '\0')
	{
		haystacklen += 1;
	}
        
	if(needlelen == 0 && haystacklen == 0)	return 0;
	int count = 0;
	int pindex = 0;
	int qindex = 0;
	//add tail limit
	while(p[count] != '\0' && count + needlelen <= haystacklen)
	{
		pindex = count;
		qindex = 0;
		while(p[pindex] != '\0' && q[qindex] != '\0' && p[pindex] == q[qindex])
		{
			pindex += 1;
			qindex += 1;
		}	
		if(q[qindex] == '\0')
		{
			return count;
		}
		count += 1;
	}
	return -1;
}
int main()
{
	char *haystack = ""; 
        char *needle = ""; 

	printf("%d\n", strStr((char *)haystack, (char *)needle));

	return 0;
}
