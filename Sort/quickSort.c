#include <stdio.h>

void printArr(int arr[],int l,int r){
    for(int i=l;i<=r;i++){
        printf("%d ",arr[i]);
    }printf("\n");
}

void swap(int arr[],int i,int j){
	int temp=arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}

int quickSort(int arr[],int low,int high){
	if (low>=high)
		return arr[low];
	
	int i=low; // finds the higher value
	int j=high-1; // finds the lower value
	int pivot=arr[high]; // last element is the pivot

	while(i<=j){
		// printf("%d %d\n",i,j);
		if (arr[i]<=pivot)
			i++;
		if (arr[j]>=pivot)
			j--;
		if (i>j)
			break;
		if (arr[i]>pivot && arr[j]<pivot){
			swap(arr,i,j);
			i++;
			j--;
		}
	}swap(arr,i,high);

	printArr(arr,low,high);

	// pivot at index i
	quickSort(arr,low,i-1);
	quickSort(arr,i+1,high);

}

int main(){
	int n; scanf("%d", &n);
	int l[n];
	for (int i = 0; i < n; i++){
		scanf("%d", &l[i]);
	}
	quickSort(l,0,n-1);
	printArr(l,0,n-1);
}