#include <stdio.h>
#include <stdlib.h>

int merge(int arr[], int l, int m, int r)
{
    if (r == l)
    {
        return arr[0];
    }

    int n1 = m - l + 1;
    int n2 = r - m;
    int left[n1];
    int right[n2];

    for (int i = 0; i < n1; i++)
    {
        left[i] = arr[l + i];
    }
    for (int j = 0; j < n2; j++)
    {
        right[j] = arr[m + 1 + j];
    }

    int i = 0;
    int j = 0;
    int k = l;

    while ((i < n1) && (j < n2))
    {
        if (left[i] < right[j])
        {
            arr[k++] = left[i++];
        }
        else
        {
            arr[k++] = right[j++];
        }
    }

    while (i < n1)
    {
        arr[k++] = left[i++];
    }

    while (j < n2)
    {
        arr[k++] = right[j++];
    }
}

void mergeSort(int arr[], int l, int r)
{
    if (r > l)
    {
        int mid = l + ((r - l) / 2);

        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);

        merge(arr, l, mid, r);
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
    mergeSort(l, 0, n - 1);
    printArr(l, n);
}