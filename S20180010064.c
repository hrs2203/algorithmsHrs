#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define sizelimit 26
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')

typedef struct EmpNode{
    int lev;
    int charLen;
    char empName[100];
    struct EmpNode *nextNode;
    struct EmpNode *childNode;
    struct EmpNode *parentNode;
} empNode;

empNode *newEmpNode(int lenName,char empname[]){
    empNode *temp = (empNode *)malloc(sizeof(empNode));
    temp->charLen = lenName;
    // for(int i= 0; i < lenName; i++){
    //     temp->empName[i] = empname[i];
    // }
    // temp->empName[lenName] = NULL;
    strcpy(temp->empName,empname);
    temp->lev = 0;
    temp->nextNode = NULL;
    temp->parentNode = NULL;
    temp->childNode = NULL;
    return temp;
}

// only lowercase input is allowed
typedef struct trieNode
{
    struct trieNode *childs[sizelimit];
    empNode *address;
    // in general node will be null
    // at the end it will be pointer as defined
} trie;

trie *newTrie(){
    trie *temp = (trie *)malloc(sizeof(trie));
    for (int i = 0; i < sizelimit; i++)
        temp->childs[i] = NULL;
    temp->address = NULL;
    return temp;
}

void insertTrie(trie **root, int lenStr, char charInp[], empNode* newAddress){
    trie *tempRoot = *root;
    trie *tempTrie = *root;

    for (int i = 0; i < lenStr; i++){
        int index = CHAR_TO_INDEX(charInp[i]);
        if (tempTrie->childs[index] == NULL){
            // printf("memory allocated for %c\n",charInp[i]);
            tempTrie->childs[index] = newTrie();
        }
        tempTrie = tempTrie->childs[index];
    }
    tempTrie->address = newAddress; // change this to pointer
    *root = tempRoot;
}

empNode *searchTrie(trie *root, int lenStr, char charInp[]){
    trie *tempNode = root;
    for (int i = 0; i < lenStr; i++)
    {   
        // printf("%c",charInp[i]);
        int index = CHAR_TO_INDEX(charInp[i]);
        if (tempNode->childs[index]==NULL)
        {   
            // printf("->");
            // printf("Node not found\n");
            return NULL;
        }
        tempNode = tempNode->childs[index];
    }
    // printf("-> Node is found\n");
    return tempNode->address;
}

// for searching employees we will use searhTrie

void insertEmpNode(empNode** rootEmpNode,trie** rootTrie,int lenChild,char childName[],int lenBoss,char bossName[]){
    if (searchTrie(*rootTrie,lenChild,childName)){
        printf("node exists\n");
        return ;
    }
    empNode* CEO = *rootEmpNode;
    empNode* bossPointer = searchTrie(*rootTrie,lenBoss,bossName);
    if (bossPointer == NULL){
        printf("the boss is not found\n");
        return ;
    }
    empNode* bossChild = bossPointer->childNode;
    empNode* tempNewNode = newEmpNode(lenChild,childName);
    tempNewNode->nextNode = bossChild;
    tempNewNode->parentNode = bossPointer;
    bossPointer->childNode = tempNewNode;

    tempNewNode->lev = bossPointer->lev + 1;

    insertTrie(rootTrie,lenChild,childName,tempNewNode);
    
    printf("addition of %s is succesfull\n",childName);
    *rootEmpNode = CEO;
}

void deleteNameInTrie(trie **root, int lenStr, char charInp[]){
    // delete by derefrencing address node
    trie* tempRoot = *root;
    trie* tempNode = *root;
    for (int i = 0; i < lenStr; i++)
    {   
        int index = CHAR_TO_INDEX(charInp[i]);
        if (tempNode->childs[index]==NULL)
        {   
            // printf("->");
            // printf("Node not found\n");
            return ;
        }
        tempNode = tempNode->childs[index];
    }
    printf("-> Node is found and deleted\n");
    tempNode->address = NULL;
    *root = tempRoot;
}

void printAllChild(empNode* temp){
    if (temp && temp->childNode)
    {
        empNode* tempc = temp->childNode;
        while(tempc){
            printf("%s ",tempc->empName);
            tempc = tempc->nextNode;
        }printf("\n");
    }
}

void deleteEmployee(empNode** rootEmp,trie** rootTrie,int firstNameLength,char firstName[],int secondNameLength,char secondName[]){
    empNode* tempEmpRoot = *rootEmp;
    trie* tempTrieRoot = *rootTrie; 
    empNode* firstNode = searchTrie(tempTrieRoot,firstNameLength,firstName);
    empNode* secondNode = searchTrie(tempTrieRoot,secondNameLength,secondName);

    if ( firstNode==NULL || secondNode==NULL ){
        printf("input employee pair is invalid\n");
        return ;
    }

    if (firstNode == secondNode){
        printf("deletion of same node is invalid\n");
        return ;
    }

    if (firstNode->lev != secondNode->lev){
        printf("deletion b/w diffrent levels is not allowed\n");
        return ;
    }

    // also check for same level

    empNode* firstNodeChild = firstNode->childNode;
    empNode* secondNodeChild = secondNode->childNode;

    // transfer of child nodes
    if (firstNodeChild){
        while(firstNodeChild->nextNode){
            // this will exclude the last child
            firstNodeChild->parentNode = secondNode;
            // printf("%s-",firstNodeChild->empName);
            firstNodeChild = firstNodeChild->nextNode;
        }
        firstNodeChild->parentNode = secondNode;
        // printf("%s\n",firstNodeChild->empName);

        firstNodeChild->nextNode = secondNodeChild;
        
        secondNode->childNode = firstNode->childNode;
        firstNode->childNode = NULL;
    }

    // printAllChild(secondNode);
    // printAllChild(firstNode);

    // deleting the node itself
    empNode* parentNode = firstNode->parentNode;
    if (parentNode->childNode == firstNode){
        parentNode->childNode = firstNode->nextNode;
    }
    else{
        empNode* prevTempNode = parentNode->childNode;
        while(prevTempNode->nextNode != firstNode){
            prevTempNode = prevTempNode->nextNode;
        }
        prevTempNode->nextNode = firstNode->nextNode;
    }
    
    // delete from trie
    deleteNameInTrie(&tempTrieRoot,firstNameLength,firstName);
    
    *rootTrie = tempTrieRoot;
    *rootEmp = tempEmpRoot;
}

void printByLevel(empNode* head,trie* headTrie){
    if (head==NULL){
        return ;
    }
    empNode* tempChild = NULL;
    empNode *tempHead = NULL;
    while(head){
        printf("%s ",head->empName);
        empNode* hc = head->childNode;
        if (hc == NULL){
            // printf("NUll found at %s\n",head->empName);
        }
        else{
            if (tempChild == NULL){
                tempChild = newEmpNode(hc->charLen,hc->empName);
                tempChild->childNode = searchTrie(headTrie, hc->charLen, hc->empName)->childNode;
                // printf("%s-added ", hc->empName);
                tempHead = tempChild;
                hc = hc->nextNode;
            }
            
            while (hc){
                tempChild->nextNode = newEmpNode(hc->charLen, hc->empName);
                tempChild->nextNode->childNode = searchTrie(headTrie, hc->charLen, hc->empName)->childNode;
                // printf("%s added ", hc->empName);
                hc = hc->nextNode;
                tempChild = tempChild->nextNode;
            }
        }
        head = head->nextNode;
    }
    printf("\n");
    // printf("\n passing %s \n",tempHead->empName);

    printByLevel(tempHead,headTrie);
}


int main()
{
    // creating the sudo boss;
    int bossNameLength;
    // printf("enter the boss name length: ");
    // scanf("%d",&bossNameLength);
    char bossName[bossNameLength];
    printf("Enter the boss name : ");
    scanf("%s",bossName);
    bossNameLength = strlen(bossName);
    
    trie *trieRoot = newTrie(); // root for trie
    empNode *empRoot = newEmpNode(bossNameLength,bossName); // employee storage root node
    empNode* testSearch; // used for searhing

    insertTrie(&trieRoot,bossNameLength,bossName,empRoot);

    int choice = 1; // defalut value
    // 1: add | 2: delete | 3: lowest common boss | 4: print by layer | 5: search perations | 0: exit
    printf("you have the following options now \n");
    printf("1 to add a new employee \n");
    printf("2 to delete a employee \n");
    printf("3 to print lowest common boss for employees \n");
    printf("4 to print employees by layer \n");
    printf("5 to search employees by name \n");
    printf("0 to quit all \n");

    // test insertion cases
    insertEmpNode(&empRoot, &trieRoot, 1, "b", 1, "a");
    insertEmpNode(&empRoot, &trieRoot, 1, "c", 1, "a");
    insertEmpNode(&empRoot, &trieRoot, 1, "d", 1, "a");
    printByLevel(empRoot,trieRoot);
    insertEmpNode(&empRoot, &trieRoot, 1, "e", 1, "b");
    insertEmpNode(&empRoot, &trieRoot, 1, "f", 1, "b");
    insertEmpNode(&empRoot, &trieRoot, 1, "g", 1, "c");
    insertEmpNode(&empRoot, &trieRoot, 1, "h", 1, "c");
    insertEmpNode(&empRoot, &trieRoot, 1, "i", 1, "c");
    printByLevel(empRoot, trieRoot);
    insertEmpNode(&empRoot, &trieRoot, 1, "j", 1, "e");
    insertEmpNode(&empRoot, &trieRoot, 1, "k", 1, "e");
    insertEmpNode(&empRoot, &trieRoot, 1, "l", 1, "f");
    insertEmpNode(&empRoot, &trieRoot, 1, "o", 1, "g");
    printByLevel(empRoot, trieRoot);
    insertEmpNode(&empRoot, &trieRoot, 1, "m", 1, "l");
    insertEmpNode(&empRoot, &trieRoot, 1, "n", 1, "l");
    printByLevel(empRoot, trieRoot);
    insertEmpNode(&empRoot, &trieRoot, 1, "p", 1, "n");
    insertEmpNode(&empRoot, &trieRoot, 1, "q", 1, "n");
    printAllChild(searchTrie(trieRoot,1,"n"));
    printByLevel(empRoot, trieRoot);

    while( choice!=0 ){
        printf("Enter you choice : ");
        scanf("%d",&choice);

        if (choice == 1){
            // employee details
            int NameLength;
            // printf("enter the employee name length: ");
            // scanf("%d",&NameLength);
            
            char Name[100];
            printf("Enter the employee name : ");
            scanf("%s",Name);
            NameLength = strlen(Name);
            
            // boss details
            int bossNameLength;
            // printf("enter the boss name length: ");
            // scanf("%d",&bossNameLength);
            
            char bossName[100];
            printf("Enter the boss name : ");
            scanf("%s",bossName);
            bossNameLength = strlen(bossName);
            
            // insertion time
            insertEmpNode(&empRoot,&trieRoot,NameLength,Name,bossNameLength,bossName);

            printf("\n");
        }
        else if (choice == 2){
            // deletion
            printf("We will be deleting first employee\n");
            int emp_1_name_len;            
            // printf("Enter the first employee name lenght : ");
            // scanf("%d",&emp_1_name_len);
            char emp_1_name[100];
            printf("Enter the first employees name : ");
            scanf("%s",emp_1_name);
            emp_1_name_len = strlen(emp_1_name);

            int emp_2_name_len;
            // printf("Enter the second employee name lenght : ");
            // scanf("%d",&emp_2_name_len);
            char emp_2_name[100];
            printf("Enter the second employees name : ");
            scanf("%s",emp_2_name);
            emp_2_name_len = strlen(emp_2_name);

            // deleteNameInTrie(&trieRoot,emp_1_name_len,emp_1_name); // -> deletes from trie

            deleteEmployee(&empRoot,&trieRoot,emp_1_name_len,emp_1_name,emp_2_name_len,emp_2_name);

        }
        else if (choice == 3){
            // lowest common boss
            int emp_1_name_len;
            // printf("Enter the first employee name lenght : ");
            // scanf("%d",&emp_1_name_len);
            char emp_1_name[100];
            printf("Enter the first employees name : ");
            scanf("%s", emp_1_name);
            emp_1_name_len = strlen(emp_1_name);

            int emp_2_name_len;
            // printf("Enter the second employee name lenght : ");
            // scanf("%d",&emp_2_name_len);
            char emp_2_name[100];
            printf("Enter the second employees name : ");
            scanf("%s", emp_2_name);
            emp_2_name_len = strlen(emp_2_name);

            empNode* firstEmp = searchTrie(trieRoot,emp_1_name_len,emp_1_name);
            empNode* secondEmp = searchTrie(trieRoot,emp_2_name_len,emp_2_name);

            if ( firstEmp==NULL || secondEmp==NULL ){
                printf("input employee pair is invalid\n");
            }

            else{
                if (firstEmp->lev != secondEmp->lev){
                    // if diffrence in level move up;
                    // printf("level diff\n");
                    while (firstEmp->lev > secondEmp->lev){
                        // printf("%d moving first from %d to ",secondEmp->lev, firstEmp->lev);
                        firstEmp = firstEmp->parentNode;
                        // printf("%d\n",firstEmp->lev);
                    }
                    while (firstEmp->lev < secondEmp->lev){
                        // printf("%d moving second from %d to ",firstEmp->lev,secondEmp->lev);
                        secondEmp = secondEmp->parentNode;
                        // printf("%d\n",secondEmp->lev);
                    }       
                }
                while(firstEmp != secondEmp){
                    firstEmp = firstEmp->parentNode;
                    secondEmp = secondEmp->parentNode;
                }
                printf("there common least important boss in %s\n",firstEmp->empName);
            }
        }
        else if (choice == 4){
            // level wise printing
            printByLevel(empRoot, trieRoot);
        }
        else if (choice == 5){
            // employee details
            int NameLength;
            // printf("enter the employee name length: ");
            // scanf("%d",&NameLength);
            
            char Name[100];
            printf("Enter the employee name : ");
            scanf("%s",Name);
            NameLength = strlen(Name);

            testSearch = NULL;
            testSearch = searchTrie(trieRoot,NameLength,Name);
            if (testSearch){
                printf("%s %d ",testSearch->empName,testSearch->lev);
                empNode* parent = testSearch->parentNode;
                while(parent){
                    printf("%s %d ",parent->empName,parent->lev);
                    parent = parent->parentNode;    
                }
            }else
                printf("employee not found");
            printf("\n");
        }
        else if (choice == 6){
            int emp_1_name_len;            
            // printf("Enter the first employee name lenght : ");
            // scanf("%d",&emp_1_name_len);
            char emp_1_name[100];
            printf("Enter the employees name : ");
            scanf("%s",emp_1_name);
            emp_1_name_len = strlen(emp_1_name);

            printAllChild(searchTrie(trieRoot,emp_1_name_len,emp_1_name));
        }
        else if (choice == 0){
            printf("Exit\n");
        }
        else{
            printf("Invalide input\n");
        }
    }

    return 0;
}
