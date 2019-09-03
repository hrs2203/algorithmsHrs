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

int noOfkid(node* temp){
    int count=0;
    if (temp){
        if (temp->left){
            count++;
        }
        if (temp->right){
            count++;
        }
    }
    return count;
}

int search(node* temp,int key){
    if (temp==NULL){
        return 0;
    }
    printf("%d %d\n",key,temp->value);
    if (temp->value == key){
        return 1;
    }
    else if (temp->value > key)
        search(temp->left,key);
    else
        search(temp->right,key);
}

node* delete(node* temp,int key){
    node* root = temp;
    node* parent=temp;
    node* kid =temp;
    if (parent){
        while(kid && kid->value!=key){
            parent=kid;
            if (parent->value > key){
                kid=parent->left;
            }else{
                kid=parent->right;
            }
        }if (kid==NULL){
            printf("not found\n");
            return root;
        }else{
            if (noOfkid(kid)==0){
                // leaf node
                if (kid==parent->left){
                    parent->left=NULL;
                }else{
                    parent->right=NULL;
                }
            }else{
                if (noOfkid(kid)==1){
                    if (kid==parent->left){
                        node* t = kid->left;
                        if (t==NULL)
                            t=kid->right;
                        parent->left = t;
                    }else{
                        node* t = kid->left;
                        if (t==NULL)
                            t=kid->right;
                        parent->left = t;
                    }
                }else{
                    // no of kid == 2
                    if (kid == parent->left){
                        node* t = kid->right;
                        node* p = kid;
                        while(t->left){
                            p=t;
                            t=t->left;
                        }
                        kid->value = t->value;
                        p->right = t->right;
                    }else{
                        node* t = kid->left;
                        node* p = kid;
                        while(p->right){
                            p=t;
                            p=p->right;
                        }
                        kid->value = t->value;
                        p->left = t->left;
                    }
                }
            }
            return root;
        }
    }  
}

void inorder(node *temp){
    if (temp == NULL)
        return;
    inorder(temp->left);
    printf("%d-%d ", temp->value,noOfkid(temp));
    inorder(temp->right);
}

int main(){
    int maxI = 4;
    // int l[7] = {4,2,6,1,3,5,7};
    // int l[13]={7,6,5,4,3,2,1,8,9,10,11,12,13};
    int l[4]={8,3,4,1};
    for (int i = 0; i < maxI; i++)
        head = insert(head, l[i]);
    inorder(head);
    printf("\n");
    head=delete(head,3);
    inorder(head);
    printf("\n");
    // prettyPrint(head,maxI);
    // printf("\n");
    // for (int i = 0; i < maxI; i++)
    //     printf("%d-%d\n",l[i],search(head,l[i]));
}