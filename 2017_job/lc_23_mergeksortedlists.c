#include<stdio.h>
#include<stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
};
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
	struct ListNode *p,  *p1 = l1, *p2 = l2;
	struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
	head->val = -1;
	head->next = NULL;

	p = head;
	while(p1 && p2)
	{
		if(p1->val <= p2->val)
		{
			p->next = p1;
			p1 = p1->next;
		}
		else
		{
			p->next = p2;
			p2 = p2->next;
		}
		p = p->next;
	}

	if(p1)	p->next = p1;
	if(p2)	p->next = p2;

	p = head->next;
	free(head);
	return p;
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
 	struct ListNode **p = lists;

	if(listsSize <= 0)	return NULL;

	if(listsSize == 1)	return lists[0];

	int i, k = listsSize;

	struct ListNode *p1 = mergeKLists(p, k / 2);

	for(i = 0; i < k / 2; i++)
	{
		p += 1;
	}

	struct ListNode *p2 = mergeKLists(p, k - k / 2);

	return mergeTwoLists(p1, p2);

}
int main()
{
	struct ListNode a, b, c, d, e, f;
        struct ListNode *lists1 = &a;
	struct ListNode *lists2 = &e;
 	struct ListNode **lists;
        lists = &lists1;
	lists += 1;
	lists = &lists2;

	a.val = 1; a.next = &b;
	b.val = 3; b.next = &c;
	c.val = 4; c.next = NULL;

	e.val = 2; e.next = &d;
	d.val = 5; d.next = &f;
	f.val = 8; f.next = NULL;
	
	struct ListNode *p = mergeKLists(&lists1, 2);

	while(p != NULL)
	{
		printf("%d ",p->val);
		p = p->next;
	}
	printf("\n");
	return 0;
}
