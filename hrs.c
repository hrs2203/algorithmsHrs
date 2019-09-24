#include <stdio.h>
#include <stdlib.h>

typedef struct Neighbour
{
    int val;
    struct Neighbour *next;
    struct Neighbour *prev;
} neighbour;

typedef struct Node
{
    int val;
    struct Node *next;
    struct Node *prev;
    struct Neighbour *link;
} node;

node *headNode;

node *newNode(int key)
{
    node *temp;
    temp = (node *)malloc(sizeof(node));
    temp->val = key;
    temp->next = NULL;
    temp->prev = NULL;
    temp->link = NULL;
    return temp;
}

neighbour *newNeighbour(int key)
{
    neighbour *temp;
    temp = (neighbour *)malloc(sizeof(neighbour));
    temp->next = NULL;
    temp->prev = NULL;
    temp->val = key;
    return temp;
}

void show_node(node *head_a)
{
    node *head = head_a;
    printf("all nodes are -> ");
    while (head)
    {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

void show_neighbour(node *temp)
{
    neighbour *point = temp->link;
    while (point)
    {
        printf("%d ", point->val);
        point = point->next;
    }
    printf("\n");
}

void show_all(node *head_a)
{
    node *head = head_a;
    while (head)
    {
        printf("node is %d and its neighbours are -> ", head->val);
        show_neighbour(head);
        head = head->next;
    }
    printf("\n");
}

node* getNode(node* temp,int key){
    // search node with value=key
    while(temp){
        if (temp->val == key){
            return temp;
        }temp=temp->next;
    }
    return temp;
}

void show_rev(node *head_a)
{
    node *head = getNode(head_a, 1);
    printf("all nodes are -> ");
    while (head)
    {
        printf("%d ", head->val);
        head = head->prev;
    }
    printf("\n");
}

node *insertNode(node **temp_a, int key){
    node* home = *temp_a;
    node *temp = newNode(key);
    temp->next = home;
    if (home){
        home->prev = temp;
    }
    // return temp;
    *temp_a = temp;
}

neighbour* getNeighbour(node* temp_a,int key_node,int key_neighbour){
    // search neighbour with value=key_neighbour
    node* head = temp_a;
    node* parentNode = getNode(head,key_node);
    neighbour* neighbourNode = parentNode->link;
    while (neighbourNode){
        if (neighbourNode->val = key_neighbour){
            return neighbourNode;
        }neighbourNode = neighbourNode->next;
    }return neighbourNode;
}

node *insertNeighbour(node **temp_a, int key_node, int key){
    node *head = *temp_a;
    node* temp = getNode(head,key_node);
    if (temp){
        neighbour *insertLink = temp->link;
        temp->link = newNeighbour(key);
        temp->link->next = insertLink;
        if (insertLink)
            temp->link->next->prev = temp->link;
    }
    else
        printf("node not found\n");

    *temp_a = head;
}

void deleteNode(node** temp_a,int node_val){
    node* tempHead = *temp_a;
    node* temp = *temp_a;
    while(temp){
        if (temp->val == node_val){
            // deleting the parent node itself
            if (temp == tempHead){
                // if header
                tempHead = temp->next;
                tempHead->prev = NULL;
            }else{
                temp->prev->next = temp->next;
                if (temp->prev->next)
                    temp->prev->next->prev = temp->prev; // if not null
            }
        }else{
            // deleting if found as neighbour
            neighbour* tempChild = temp->link;
            if (tempChild!=NULL){
                while (tempChild){
                    if (tempChild->val == node_val){
                        if (tempChild == temp->link){
                            temp->link = tempChild->next;
                            if (temp->link)
                                temp->link->prev = NULL;
                        }else{
                            tempChild->prev->next = tempChild->next;
                            if (tempChild->prev->next)
                                tempChild->prev->next->prev = tempChild->prev;
                        }
                        break;
                    }
                    tempChild = tempChild->next;
                }
            }
        }
        temp = temp->next;
    }
    *temp_a = tempHead;
}

int main()
{
    node *headNode = NULL;
    insertNode(&headNode,1);
    insertNode(&headNode,2);
    insertNode(&headNode,3);
    insertNode(&headNode,4);
    insertNode(&headNode,5);
        
    show_node(headNode);
    // show_rev(headNode);

    // insertion of node
    insertNeighbour(&headNode, 1, 3);
    insertNeighbour(&headNode, 1, 4);
    insertNeighbour(&headNode, 2, 1);
    insertNeighbour(&headNode, 2, 2);
    insertNeighbour(&headNode, 2, 3);
    insertNeighbour(&headNode, 3, 2);
    insertNeighbour(&headNode, 3, 5);
    insertNeighbour(&headNode, 4, 5);
    insertNeighbour(&headNode, 5, 3);
    insertNeighbour(&headNode, 5, 4);
    insertNeighbour(&headNode, 5, 5);
    show_all(headNode);

    // deletion of node3
    deleteNode(&headNode,3);
    show_all(headNode);

    deleteNode(&headNode,1);
    show_all(headNode);

    deleteNode(&headNode,5);
    show_all(headNode);

    deleteNode(&headNode,5);
    show_all(headNode);

    return 0;
}
