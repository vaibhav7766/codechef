//https://www.codechef.com/problems/S100
#include <stdio.h>

void solve(int n, char word[n]){
    int flag=n;
    for(int i=0;i<n-2;i++){
        if(word[i]=='1'){
            flag=i;
            break;
        }
    }
    for(int k=flag+1;k<n;k++){
        word[k]='0';
    }
    printf("%s",word);
}

int main(void) {
	int t;
	scanf("%d",&t);
	for(int j=0;j<t;j++){
	    int n;
	    scanf("%d",&n);
	    char arr[n];
	    scanf("%s",arr);
	    solve(n,arr);
	    printf("\n");
	}
	return 0;
}

