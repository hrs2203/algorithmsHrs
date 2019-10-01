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
    int isVisited;
} node;

node *headNode;

void makeAllUnvisited(node** temp_a){
    node* tempHead = *temp_a;
    node* temp = *temp_a;
    while(temp){
        temp->isVisited = 0;
        temp = temp->next;
    }
    *temp_a = tempHead;
}

node *newNode(int key)
{
    node *temp;
    temp = (node *)malloc(sizeof(node));
    temp->val = key;
    temp->next = NULL;
    temp->prev = NULL;
    temp->link = NULL;
    temp->isVisited = 0;
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

// dfs

void DFS(node* temp,node* temp_a){
    if (temp == NULL)
        return ;
    if (temp->isVisited == 0){
        temp->isVisited = 1;
        printf("%d ",temp->val);
        neighbour* target = temp->link;
        while(target){
            node* tempS = getNode(temp_a,target->val);
            DFS(tempS,temp_a);
            target = target->next;
        }
    }
}

void DFS_head(node* temp_a){
    printf("enter the node to search from : ");
    int n;
    scanf("%d",&n);
    node* temp = getNode(temp_a,n);
    if (temp==NULL){
        printf("Node does not exist\n");
    }else{
        DFS(temp,temp_a);
    }
}

typedef struct QueueNode{
    int value;
    struct QueueNode* next;
} que ;

que* getNewQueNode(int val){
    que* temp = (que*)malloc(sizeof(que));
    temp->next = NULL;
    temp->value = val;
    return temp;
}

void printAllQue(que* head){
    while(head){
        printf("%d ",head->value);
        head = head->next;
    }
}

void insertInQueue(que** head,int val){
    que* tempHead = *head;
    que* temp = *head;
    
    if (tempHead == NULL){
        tempHead = getNewQueNode(val);
    }else{
        if (temp->value == val){
            return ;
        }
        while (temp->next){
            if (temp->value == val){
                // printf("Match found %d \n",val);
                return ; // no addition needed
            }else{
                temp = temp->next;
            }
        }
        if (temp->value == val){
            return ;
        }
        temp->next = getNewQueNode(val);
    }
    *head = tempHead;
}
    
void BFS(node* temp,node* temp_a){
    // we will start from temp;
    // temp_a is the main header of our node DataStructure
    // our queue will be a linked list
    que* HeadRunPoint = getNewQueNode(temp->val);
    que* HeadPoint = HeadRunPoint;
    while(HeadPoint){
        neighbour* tempNode = getNode(temp_a,HeadPoint->value)->link;
        while (tempNode){
            insertInQueue(&HeadRunPoint,tempNode->val);
            tempNode = tempNode->next;
        }
        HeadPoint = HeadPoint->next;
    }
    printAllQue(HeadRunPoint);
}

void BFS_head(node* temp_a){
    printf("enter the node to search from : ");
    int n;
    scanf("%d",&n);
    node* temp = getNode(temp_a,n);
    if (temp==NULL){
        printf("Node does not exist\n");
    }else{
        BFS(temp,temp_a);
    }
}


int main()
{
    node *headNode = NULL;
    insertNode(&headNode,1);
    insertNode(&headNode,2);
    insertNode(&headNode,3);
    insertNode(&headNode,4);
    insertNode(&headNode,5);
    insertNode(&headNode,6);
    insertNode(&headNode,7);
    
    show_node(headNode);

    // insertion of node
    insertNeighbour(&headNode, 1, 2);
    insertNeighbour(&headNode, 2, 1);
    insertNeighbour(&headNode, 1, 3);
    insertNeighbour(&headNode, 3, 1);
    insertNeighbour(&headNode, 1, 4);
    insertNeighbour(&headNode, 4, 1);
    insertNeighbour(&headNode, 2, 5);
    insertNeighbour(&headNode, 5, 2);
    insertNeighbour(&headNode, 3, 6);
    insertNeighbour(&headNode, 6, 3);
    insertNeighbour(&headNode, 3, 4);
    insertNeighbour(&headNode, 4, 3);
    insertNeighbour(&headNode, 4, 7);
    insertNeighbour(&headNode, 7, 4);
    insertNeighbour(&headNode, 6, 7);
    insertNeighbour(&headNode, 7, 6);
    
    
    show_all(headNode);

    DFS_head(headNode);
    printf("\n");

    BFS_head(headNode);
    printf("\n");
    BFS_head(headNode);
    printf("\n");

    return 0;
}
