/*
 * 25 reverse nodes in k groups
 * 206 reverse linked list
 */
#include<stdio.h>
#include<stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head, int n) {
	struct ListNode *start = (struct ListNode *)malloc(sizeof(struct ListNode));
	start->val = -1;
	start->next = NULL;

	struct ListNode *p = head, *old;

	int count = 0;
	while(p != NULL && count < n)
	{
		old = p->next;
		p->next = start->next;
		start->next = p;
		p = old;
		count += 1;
	}

	p = start->next;
	free(start);
	return p;    
}
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
 	if(k <= 1)	return head;

	struct ListNode *p = head, *start, *move, *end, *before = NULL, *after = NULL, *output;
	int i = 0;

	while(p)
	{
		start = p;
	 	move = p;
		
		i = 0;
		while(i < k - 1 && move)
		{
			move = move->next;
			i += 1;
		}			
		if(i == k - 1 && move)
		{
			end = move;
			
			if(start && end)	printf("start: %d end: %d \n", start->val, end->val);

			if(end)	
			{
				after = end->next;
			}
			else
			{
				after = NULL;
			}
			output = reverseList(start, k);

			if(before)
			{
				printf("before:%d\n", before->val);
                                before->next = output;
			}
			else
			{
				head = output;
				printf("head:%d\n", head->val);
			}
                        before = start;
			p = after;
		}
		else
		{
			if(before)
			{
				before->next = start;
			}
			break;
		}
	}	

	return head;
}
int main()
{
 	struct ListNode a1, a2, a3, a4;
	a1.val = 1; a1.next = &a2;
	a2.val = 2; a2.next = NULL;
	a3.val = 3; a3.next = &a4;
	a4.val = 4; a4.next = NULL;

	struct ListNode *p = reverseKGroup(&a1, 3);
	//struct ListNode *p = reverseList(&a1, 3);

 	while(p)
	{
		printf("%d ", p->val);
		p = p->next;
	}
	printf("\n");
	return 0;
}
