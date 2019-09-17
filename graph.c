#include <stdio.h>
#include <stdlib.h>

typedef struct Neighbour{
    int val;
    struct Neighbour* next;
}neighbour;

typedef struct Node{
    int val;
    struct Node* next;
    struct Neighbour* link;
}node;

node* headNode;

node* findNode(node* head,int key){
    node* temp = (node*)malloc(sizeof(node));
    return temp;
}

node* newNode(int key){
    node* temp;
    temp = (node*)malloc(sizeof(node));
    temp->val = key;
    temp->next = NULL;
    temp->link = NULL;
    return temp;
}

neighbour* newNeighbour(int key){
    neighbour* temp;
    temp = (neighbour*)malloc(sizeof(neighbour));
    temp->next = NULL;
    temp->val = key;
    return temp;
}

node* insertNode(node* temp_a,int key){
    // temp_a = insertNode(temp_a,key)
    if (temp_a == NULL){
        return newNode(key);
    }
    node* temp = temp_a;
    while(temp->next){
        temp = temp->next;
    }temp->next = newNode(key);
    return temp_a;
}

void show_node(node* head_a){
    node* head = head_a;
    printf("all nodes are -> ");
    while (head){
        printf("%d ",head->val);
        head = head->next;
    }printf("\n");
}

void show_neighbour(node* temp){
    neighbour* point = temp->link;
    while(point){
        printf("%d ",point->val);
        point = point->next;
    }printf("\n");
}


void show_all(node* head_a){
    node* head = head_a;
    while (head){
        printf("node is %d and its neighbours are -> ",head->val);
        show_neighbour(head);
        head = head->next;
    }printf("\n");
}

node* insertNeighbour(node* temp_a,int key_node,int key){
    // insert neighbour in temp node
    // headNode = insertNeighbour(headNode,key_node,key) -> to use it

    node* head = temp_a;
    node* temp = temp_a;
    while(temp!=NULL){
        if (temp->val == key_node){
            break;
        }temp = temp->next;
    }
    if (temp!=NULL){
        // printf("node found %d\n",temp->val);
        neighbour* insertLink = temp->link;
        if (insertLink == NULL){
            temp->link = newNeighbour(key);
        }else{
            while (insertLink->next!=NULL){
                insertLink = insertLink->next;
            }
            insertLink->next = newNeighbour(key);
        }
        // printf("insertion succes the neighbours of %d are : \n",temp->val);
        // show_neighbour(temp);
    }else{
        printf("node not found\n");
    }

    return head;
}

int main(){
    node* headNode;
    headNode = insertNode(headNode,1);
    headNode = insertNode(headNode,2);
    headNode = insertNode(headNode,3);
    headNode = insertNode(headNode,4);
    headNode = insertNode(headNode,6);
    headNode = insertNode(headNode,5);
    show_node(headNode);

    // insertion of node
    headNode = insertNeighbour(headNode,1,3);
    headNode = insertNeighbour(headNode,1,4);
    headNode = insertNeighbour(headNode,2,1);
    headNode = insertNeighbour(headNode,2,2);
    headNode = insertNeighbour(headNode,2,3);
    headNode = insertNeighbour(headNode,3,2);
    headNode = insertNeighbour(headNode,3,5);
    headNode = insertNeighbour(headNode,4,1);
    headNode = insertNeighbour(headNode,5,3);
    headNode = insertNeighbour(headNode,5,4);
    headNode = insertNeighbour(headNode,5,5);
    headNode = insertNeighbour(headNode,5,6);
    show_all(headNode);
    
}



