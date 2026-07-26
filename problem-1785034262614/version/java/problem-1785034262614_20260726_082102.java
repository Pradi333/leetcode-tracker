// Last updated: 7/26/2026, 8:21:02 AM
1class Solution {
2    public int largestInteger(int n, int s) {
3      if(s>9*n){
4          return-1;
5      }
6      if(s==0){
7          return 0;
8      }
9      int result=0;   
10      for(int i=0;i<n;i++){
11          int digit=Math.min(9,s);
12          result=result*10+ digit;
13          s-=digit;
14      }
15      return result;
16    
17    }
18}