#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int key;
    struct Node* left;
    struct Node* right;
}node;

void printArr(int arr[], int l, int r){
    for (int i = l; i <= r; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

node* head; //defining header

node* newNode(int key){
    // allocating memory in the first line
    node* temp = (node*)malloc(sizeof(node));
    temp->key = key;
    temp->left = NULL; temp->right = NULL;
    return temp;
}

node* insert(node* point, int key){
    if (point==NULL)
        return newNode(key);
    // travel down the line
    if (point->key >= key )
        point->left = insert(point->left,key);
    else if (point->key < key)
        point->right = insert(point->right, key);
}

int ind=0;

void inorderInsertion(int arr[],node* point){
    if (point != NULL){
        inorderInsertion(arr,point->left);
        arr[ind++]=point->key;
        inorderInsertion(arr,point->right);
    }
}

void inorderTraversal(node* point){
    if (point!=NULL){
        inorderTraversal(point->left);
        printf("%d ",point->key);
        inorderTraversal(point->right);
    }
}

void BSTsort(int arr[],int n){
    head = insert(head,arr[0]);
    for(int i=1;i<n;i++){
        insert(head, arr[i]);
    }
    inorderInsertion(arr,head);
}

int main(){
    int n; scanf("%d", &n);
    int l[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &l[i]);

    // sorting 
    BSTsort(l,n);
    
    // printing the result
    printArr(l,0,n-1);
}