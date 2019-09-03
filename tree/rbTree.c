#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int value;
    int color; // 0 red 1 black
    struct Node* left;
    struct Node* right;
    struct Node* parent;
}node;

node* head; // header node;

int getColor(node *temp){
    if (temp == NULL)
        return 1; // null node is considered black
    return temp->color;
}

void changeColor(node* temp){
    if (temp){
        if (temp->color==0)
            temp->color=1;
        else
            temp->color=0;
    }
}

int checkDoubleRed(node* temp){
    if (temp->color == 1)
        return 0; // no problem at black node
    if (temp->left && temp->left->color==0)
        return 1; // problem
    if (temp->right && temp->right->color == 0)
        return 1; // problem
    if (temp->parent && temp->parent->color == 0)
        return 1; // problem
    return 0; // all nodes are black in proximity
}

// node* leftRotation(node* node_x){
//     // to apply node_x = leftRotation(node_x)
    
//     // changing parents
//     node_x->right->parent = node_x->parent;
//     node_x->parent = node_x->right;

//     // swaping
//     node* temp1 = node_x->right->left;
//     node_x->right->left = node_x;
//     node* temp2 = node_x->right;
//     node_x->right = temp1;
//     return temp2;
// }

// node* rightRotation(node* node_x){
//     // to apply node_x = rightRotation(node_x)

//     // changing parents
//     node_x->left->parent = node_x->parent;
//     node_x->parent = node_x->left;

//     // swaping
//     node* temp = node_x->left->right;
//     node_x->left->right = node_x;
//     node* temp2 = node_x->left;
//     node_x->left = temp;
//     return temp2;
// }

void LeftRotate(node **root, node *x)
{
    //y stored pointer of right child of x
    node *y = x->right;

    //store y's left subtree's pointer as x's right child
    x->right = y->left;

    //update parent pointer of x's right
    if (x->right != NULL)
        x->right->parent = x;

    //update y's parent pointer
    y->parent = x->parent;

    // if x's parent is null make y as root of tree
    if (x->parent == NULL)
        (*root) = y;

    // store y at the place of x
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;

    // make x as left child of y
    y->left = x;

    //update parent pointer of x
    x->parent = y;
}

// Right Rotation (Similar to LeftRotate)
void rightRotate(node **root, node *y)
{
    node *x = y->left;
    y->left = x->right;
    if (x->right != NULL)
        x->right->parent = y;
    x->parent = y->parent;
    if (x->parent == NULL)
        (*root) = x;
    else if (y == y->parent->left)
        y->parent->left = x;
    else
        y->parent->right = x;
    x->right = y;
    y->parent = x;
}

node* newNode(int key,int col){
    node* temp = (node*)malloc(sizeof(node));
    temp->value = key;
    temp->color = col;
    temp->left = NULL;
    temp->right = NULL;
    temp->parent = NULL;
    return temp;
}

node* doChecks(node* root,node* kid){
    node* other = NULL;
    while (kid->parent && kid->parent->color==0){
        if (kid->parent == kid->parent->parent->left){
            other = kid->parent->parent->right;
            if (getColor(other)==0){
                changeColor(kid->parent);
                changeColor(other);
                changeColor(kid->parent->parent);
                kid = kid->parent->parent;  // kid is now grand parent
            }
            else{
                if (kid==kid->parent->right){
                    kid = kid->parent;
                    LeftRotate(&root,kid);
                }
                kid->parent->color = 1;
                kid->parent->parent->color = 0;
                rightRotate(&root,kid->parent->parent);
            }
        }else{
            other = kid->parent->parent->left;
            if (getColor(other) == 0)
            {
                changeColor(kid->parent);
                changeColor(other);
                changeColor(kid->parent->parent);
                kid = kid->parent->parent; // kid is now grand parent
            }
            else
            {
                if (kid == kid->parent->left)
                {
                    kid = kid->parent;
                    rightRotate(&root,kid);
                }
                kid->parent->color = 1;
                kid->parent->parent->color = 0;
                LeftRotate(&root,kid->parent->parent);
            }
        }
    }
    while(kid->parent){
        kid=kid->parent;
    }
    kid->color = 1;
    return kid; // by the end kid is the root // kid's grown up
}

node* insert(node* temp,int key){
    if (temp==NULL){
        // parent is by default black;
        return newNode(key,1);
    }
    node* tempHead = temp;

    node *tempNext = temp;
    node *tempParent = tempNext->parent;

    // moving down
    while(tempNext){
        tempParent = tempNext;
        if (tempNext->value > key){
            tempNext = tempNext->left;
        }
        else{
            tempNext = tempNext->right;
        }
    }

    if (tempParent->value > key){
        tempParent->left = newNode(key,0);
        tempParent->left->parent = tempParent;
        tempHead = doChecks(tempHead,tempParent->left);
    }
    else{
        tempParent->right = newNode(key, 0);
        tempParent->right->parent = tempParent;
        tempHead = doChecks(tempHead,tempParent->right);
    }

    return tempHead;
}



void inorder(node* temp){
    if (temp==NULL) return ;
    inorder(temp->left);
    printf("%d-%d-%d ",temp->value,temp->color,checkDoubleRed(temp));
    inorder(temp->right);
}

void allBlackHeight(node* temp,int count){
    if (temp==NULL){
        printf("%d ",count);
        return ;
    }
    if (temp->color == 1)   count++;
    allBlackHeight(temp->left,count);
    allBlackHeight(temp->right,count);
}

int main(){

    int l[15] = {15,21,5,49,3,6,73,8,9,0,11,25,45,78,68};
    for(int i=0;i<15;i++){
        head = insert(head,l[i]);
    }

    printf("node-color-doublered\n");
    inorder(head); printf("\n");
    allBlackHeight(head,0); printf("\n");printf("\n");    
}