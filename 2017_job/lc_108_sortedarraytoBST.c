#include<stdio.h>
#include<stdlib.h>
/**
 *  * Definition for a binary tree node.
 *   * struct TreeNode {
 *    *     int val;
 *     *     struct TreeNode *left;
 *      *     struct TreeNode *right;
 *       * };
 *        */
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};
void myInsert(struct TreeNode **p_addr, int *nums, int left, int right)
{
	if(left > right)	return;
	/*if(left == right)	
	{
		struct TreeNode *temp = (struct TreeNode *)malloc(sizeof(struct TreeNode));
		temp->val = nums[left];
		temp->left = NULL;
		temp->right = NULL;

		*p_addr = temp;

		return ;
	}*/
	/*if(left+1 == right)
	{
		struct TreeNode *temp1 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
		struct TreeNode *temp2 = (struct TreeNode *)malloc(sizeof(struct TreeNode));
		temp2->val = nums[right];
		temp2->left = NULL;
		temp2->right = NULL;

		temp1->val = nums[left];
		temp1->left = NULL;
		temp1->right = temp2;

		*p_addr = temp1;

		return ;
	}*/
	
	int mid = (left+right)/2;
	struct TreeNode *tempMid = (struct TreeNode *)malloc(sizeof(struct TreeNode));
	tempMid->val = nums[mid];
	tempMid->left = NULL;
	tempMid->right = NULL;

	*p_addr = tempMid;

	myInsert(&tempMid->left, nums, left, mid-1);
	myInsert(&tempMid->right, nums, mid+1, right);
}
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
	struct TreeNode *p = NULL;

	myInsert(&p, nums, 0, numsSize-1);

	return p;
}
void traversal(struct TreeNode *p)
{
		if(p == NULL)	return ;

		if(p->left)		traversal(p->left);

		printf("%d ", p->val);

		if(p->right)	traversal(p->right);
}

int main()
{
	int nums[8] = {1, 2, 3, 4, 5, 6, 7, 8};

	struct TreeNode *p = sortedArrayToBST(nums, 8);

	traversal(p);

	printf("\n");

	return 0;
}
