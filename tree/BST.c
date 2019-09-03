#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int value;
    struct Node *left;
    struct Node *right;
} node;

node *head; // header node;

node *newNode(int key){
    node *temp = (node *)malloc(sizeof(node));
    temp->value = key;
    temp->left = NULL;  temp->right = NULL;
    return temp;
}

node *insert(node *temp, int key){
    if (temp == NULL)   return newNode(key);
    if (temp->value > key)  temp->left = insert(temp->left, key);
    else    temp->right = insert(temp->right, key);
    return temp;
}

void inorder(node *temp){
    if (temp == NULL)
        return;
    inorder(temp->left);
    printf("%d ", temp->value);
    inorder(temp->right);
}

void fillPoint(node* temp,int len,int l[len][2*len +1],int a,int b){
    if (temp==NULL){
        return ;
    }
    l[a][b]=temp->value;

    fillPoint(temp->left ,len, l, a+1, b-1);
    fillPoint(temp->right,len, l, a+1, b+1);
}

void prettyPrint(node* temp,int len){
    // len is the number of elements in BST
    // temp will be head by default

    int val[len][2*len + 1];
    for(int i=0;i<len;i++){
        for(int j=0;j<(2*len +1);j++){
            val[i][j]=NULL;
        }
    }

    int a=0;
    int b=len;

    fillPoint(temp, len, val, a, b);

    for (int i = 0; i < len; i++){
        for (int j = 0; j < (2 * len + 1); j++){
            if (val[i][j] == NULL){
                printf("-");
            }else{
                printf("%d",val[i][j]);
            }
        }printf("\n");
    }
}

int main(){
    int maxI = 3;
    // int l[7] = {4,2,6,1,3,5,7};
    // int l[13]={7,6,5,4,3,2,1,8,9,10,11,12,13};
    int l[3]={8,3,4};
    for (int i = 0; i < maxI; i++)
        head = insert(head, l[i]);
    inorder(head);
    printf("\n");
    prettyPrint(head,maxI);
    printf("\n");
}