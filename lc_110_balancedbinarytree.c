#include<stdio.h>
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};
int myMax(int a, int b)
{
	return a > b? a : b;
}
int depthTree(struct TreeNode *root)
{
	if(root == NULL)	return 0;

	return myMax(depthTree(root->left), depthTree(root->right)) + 1;
}
int isBalanced(struct TreeNode* root) {
	if(root == NULL)	return 1;

	int temp = depthTree(root->right) - depthTree(root->left);

	if(temp < -1 || temp > 1)	return 0;
	else						return isBalanced(root->left) && isBalanced(root->right);
}

int isBalancedNew(struct TreeNode *root)
{
	if(root == NULL)	return 0;

	int left = isBalancedNew(root->left);
	int right = isBalancedNew(root->right);

	if(left < 0 || right < 0 || abs(left-right) > 1)	return -1;

	return myMax(left,right)+1;
}
int isBalance(struct TreeNode *root)
{
	return isBalancedNew(root) >= 0;
}

int main()
{
	struct TreeNode a, b, c;
	a.left = NULL;
	a.right = &b;
	b.left = &c;
	b.right = NULL;
	c.left = NULL;
	c.right = NULL;
		
	printf("%d\n", isBalancedNew(&a));
	return 0;
}
