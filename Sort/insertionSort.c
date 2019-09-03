#include <stdio.h>
#include <stdlib.h>

void insertionSort(int arr[], int n)
{
    for (int i = 0; i < (n - 1); i++)
    {
        int j = i + 1;
        while ((arr[j] < arr[j - 1]) && (j > 0))
        {
            //swap them
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[--j] = temp;
        }
    }
}

void printArr(int l[], int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("%d ", l[i]);
    }
    printf("\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    int l[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &l[i]);
    }
    printArr(l, n);
    insertionSort(l, n);
    printArr(l, n);
}