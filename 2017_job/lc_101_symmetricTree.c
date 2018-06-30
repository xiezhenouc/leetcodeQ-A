#include<stdio.h>
#define bool char
#define true 1
#define false 0

struct TreeNode
{
	int val;
	struct TreeNode *left, *right;
};
bool myTraversal(struct TreeNode *root1, struct TreeNode *root2)
{
	if(!root1 && !root2)	return true;
	if((!root1 && root2) || (root1 && !root2))	return false;

	printf("1\n");
	return (root1->val == root2->val) && myTraversal(root1->left, root2->right) && myTraversal(root1->right, root2->left);	
}
bool isSymmetric(struct TreeNode *root)
{
	return myTraversal(root, root);
}
int main()
{
	struct TreeNode a;
	a.val = 1;
	a.left = NULL;
	a.right = NULL;
	printf("%d\n", isSymmetric(&a));

	return 0;
}
