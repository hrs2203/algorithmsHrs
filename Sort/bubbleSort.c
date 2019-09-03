#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < (n - 1 - i); j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
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
    bubbleSort(l, n);
    printArr(l, n);
}