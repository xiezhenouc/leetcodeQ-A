#include<stdio.h>

//O(n^2) not good 
void changeZeroPosition(int a[], int n)
{
    //start from last one
    int i = n - 1;    
    int k, tmp;
 
    while(i >= 0)
    {
        if(a[i] == 0)
        {
            k = i - 1;
            //find first not zero element
            while(k >= 0)
            {
                if(a[k] != 0) break;
                k--;
            }
            //find it!
            if(k >= 0 && a[k] != 0)
            {
                tmp = a[k];
                a[k] = a[i];
                a[i] = tmp;   
            }
        }
        i--;
    }
}
//O(n) good one
void changeZeroGood(int a[], int n)
{
    //two pointers
    //src:source  
    //dst:destination
    int src = n - 1;
    int dst = n - 1;
 
    while(src >= 0)
    {
        if(a[src] != 0)
        {
            a[dst] = a[src];
            dst--;
        }
        src--;
    }
    //dst means sum of 0
    while(dst >= 0)
    {
        a[dst--] = 0;
    }
}
int main()
{
    int a[8] = {4, 0, 1, 7, 2, 0, 0, 3};
    int i = 0;

    //changeZeroPosition(a, 8);
    changeZeroGood(a, 8);

    for(i = 0; i < 8; i++)
    {
        printf("%d ", a[i]);
    }   
    printf("\n");
    return 0;
}
