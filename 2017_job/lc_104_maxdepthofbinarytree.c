#include<stdio.h>
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
int maxDepth(struct TreeNode* root) {
	int maxleft = 0, maxright = 0;

	if(root == NULL)				
	{
		return 0;
	}
	
	maxleft = maxDepth(root->left) + 1;
	maxright = maxDepth(root->right) + 1;
	
	return maxleft > maxright ? maxleft : maxright;
}
int main()
{
	return 0;
}
