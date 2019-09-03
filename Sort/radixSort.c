#include <stdio.h>

void radixSort(int n,int m,int l[n][m],int level,int start,int end){
	if (level<m){
		int i=start;
		int j=end;
		while(i<=j){
			if (l[i][level]==0)
				i++;
			if (l[j][level]==1)
				j--;
			if (i>j)
				break;
			if (l[i][level]==1 && l[j][level]==0){
				//swaping 2 1Xm arrays
				int temp[m];
				for(int k=0;k<m;k++){
					temp[k]=l[i][k];
				}
				for(int k=0;k<m;k++){
					l[i][k]=l[j][k];
				}
				for(int k=0;k<m;k++){
					l[j][k]=temp[k];
				}
				// changing pointers
				i++;
				j--;
			}
		}
		radixSort(n,m,l,level+1,start,j);
		radixSort(n,m,l,level+1,i,end);
	}
}

int main(){
	int n; scanf("%d",&n);
	int m; scanf("%d",&m);
	int l[n][m];
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			scanf("%d",&l[i][j]);
		}
	}

	radixSort(n,m,l,0,0,n-1);
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			printf("%d ",l[i][j]);
		}printf("\n");
	}
}