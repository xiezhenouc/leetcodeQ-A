#include<stdio.h>
#include<stdlib.h>

/**
 *  * Definition for singly-linked list.
 *   * struct ListNode {
 *    *     int val;
 *     *     struct ListNode *next;
 *      * };
 *       */
struct ListNode {
	int val;
	struct ListNode *next;
};
struct ListNode* swapPairs(struct ListNode* head) {
	if(head == NULL)	return NULL;

	struct ListNode *beforeHead, *p, *p1, *p2, *old;

	beforeHead = (struct ListNode *)malloc(sizeof(struct ListNode));
	beforeHead->val = -1;
	beforeHead->next = NULL;

	p = beforeHead;	p1 = head; p2 = p1->next;

	while(p1 && p2)
	{
		//memory it 
		old = p1;
		
		//new list now p = p2
		p->next = p2;
		p = p->next;

		//move to new place p2 important!
		p1 = p2->next;
		 
		//get memory must be here! 
		p->next = old;
		p = p->next;
		
		if(p1 == NULL)	break;
		p2 = p1->next;
	}

	//last node next = NULL
	if(p1)	p->next = p1;
	else	p->next = NULL;

	p = beforeHead->next;
	free(beforeHead);

	return p;
}
int main()
{
	struct ListNode a, b, c, d;
	a.val = 1; a.next = &b;
	b.val = 2; b.next = &c;
	c.val = 3; c.next = &d;
	d.val = 4; d.next = NULL;

	struct ListNode *p = swapPairs(&a);

	while(p != NULL)
	{
		printf("%d\n", p->val);
		p = p->next;
	}

	printf("\n");
	return 0;
}

