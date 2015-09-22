#include<stdio.h>
/**
 *  * Definition for a binary tree node.
 *   * struct TreeNode {
 *    *     int val;
 *     *     struct TreeNode *left;
 *      *     struct TreeNode *right;
 *       * };
 *        */
#define bool int
#define true 1
#define false 0

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
	//NULL NULL true
	if(!p && !q)				return true;
	//!NULL NULL false
	else if(!p && q || p && !q)	return false;

	//!NULL !NULL val different
	else if(p->val != q->val)	return false;

	return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);


}
int main()
{
	return 0;
}
