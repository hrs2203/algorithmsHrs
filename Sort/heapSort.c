#include <stdio.h>

void printArr(int arr[], int l, int r){
    for (int i = l; i <= r; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void swap(int arr[],int i,int j){
    int temp = arr[j];
    arr[j] = arr[i];
    arr[i] = temp;
}

void heapify(int arr[],int n,int i){
    int largest=i;
    int left=2*i+1;
    int right=2*i+2;

    if (left<n && arr[left]>arr[largest])
        largest = left;
    
    if (right<n && arr[right]>arr[largest])
        largest = right;

    if (largest!=i){
        // swaping
        swap(arr,i,largest);
        // recurse
        heapify(arr,n,largest);
    }
}

void heapSort(int arr[],int n){
    for(int i=n/2 -1;i>=0;i--){
        heapify(arr,n,i);
        // printArr(arr,0,n-1);
    }
    for(int i=n-1;i>=0;i--){
        swap(arr,0,i);
        heapify(arr,i,0);
        // printArr(arr, 0, n - 1);
    }
}

int main(){
    int n; scanf("%d",&n);
    int l[n];
    for(int i=0;i<n;i++){
        scanf("%d", &l[i]);
    }
    heapSort(l,n);
    printArr(l, 0, n - 1);
}