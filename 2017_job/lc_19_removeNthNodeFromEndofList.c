#include<stdio.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
	struct ListNode *p = head, *pre = NULL, *rm = head;
	int i = 0;

	while(i < n && rm)
	{
		rm = rm->next;
		i += 1;
	}
	//printf("\n%d\n", rm->val);

	while(rm)
	{
		pre = p;
		p = p->next;
		rm = rm->next;
	}

	if(pre)
	{
		pre->next = p == NULL ? NULL: p->next;
 		return head;	
	}
	else
	{
		return head == NULL ? head : head->next;
	}

}

int main()
{
	struct ListNode *p;
	struct ListNode a, b, c, d, e;

	a.val = 1; a.next = &b;
	b.val = 2; b.next = &c;
	c.val = 3; c.next = &d;
	d.val = 4; d.next = &e;
	e.val = 5; e.next = NULL;

	printf("start:\n");
	for(p = &a; p != NULL; p = p->next)
	{
		printf("%d ", p->val);
	}
	printf("\n");

        p = removeNthFromEnd(NULL, 1);

	printf("after:\n");
	for(; p != NULL; p = p->next)
	{
		printf("%d ", p->val);
	}
	printf("\n");

	return 0;
}
