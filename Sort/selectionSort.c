#include <stdio.h>
#include <stdlib.h>

void selectionSort(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min])
            {
                min = j;
            }
        }
        if (min != i)
        {
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
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
    selectionSort(l, n);
    printArr(l, n);
}