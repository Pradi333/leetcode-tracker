// Last updated: 7/19/2026, 8:37:42 AM
1class Solution {
2    public boolean canReach(int[] start, int[] target) {
3        int[][]dirs={
4            {2,1},{2,-1},{-2,1},{-2,-1},{1,2},{1,-2},{-1,2},{-1,-2}
5        };
6        boolean[][]visited=new boolean[8][8];
7        Queue<int[]> q= new LinkedList<>();
8        q.offer(new int[]{start[0],start[1],0});
9        visited[start[0]][start[1]]=true;
10
11        while(!q.isEmpty()){
12            int[]cur=q.poll();
13            int x=cur[0];
14            int y=cur[1];
15            int dist=cur[2];
16
17            if(x==target[0]&&y==target[1]){
18                return dist%2==0;
19            }
20            for(int[]d:dirs){
21                int nx=x+d[0];
22                int ny=y+d[1];
23
24                if(nx>=0 && nx<8 && ny>=0 &&ny<8 && !visited[nx][ny]){
25                    visited[nx][ny]=true;
26                    q.offer(new int[]{nx,ny,dist+1});
27                }
28            }
29        }
30        
31    return false;
32    }
33}