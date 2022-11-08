import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;

public class boj_2665{

	// set static variables
	static int n;

	public static void main(String[] args) throws IOException{

		// set needed variables
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		int[] dx = {0, 1, 0, -1};
		int[] dy = {-1, 0, 1, 0};

		// get map
		char[][] map = new char[n][n];
		for (int i = 0; i < n; i++){
			map[i] = br.readLine().toCharArray();
		}
		
		// set variables for dijkstra
		boolean[][] visited = new boolean[n][n];
		Queue<Loc> q = new LinkedList<>();
		q.add(new Loc(0, 0));
		int[][] count = new int[n][n];
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				count[i][j] = Integer.MAX_VALUE;
			}
		}
		count[0][0] = 0;

		// do dijkstra
		while (!q.isEmpty()){

			Loc tmp = q.poll();
			if (tmp.x == n-1 && tmp.y == n-1) continue;
			int cx = tmp.x;
			int cy = tmp.y;

			for (int i = 0; i < 4; i++){
				int nx = cx + dx[i];
				int ny = cy + dy[i];
				if (inRange(nx, ny) && !visited[nx][ny]){
					// black room
					if (map[nx][ny] == '0'){
						if (count[cx][cy] + 1 < count[nx][ny]){
							count[nx][ny] = count[cx][cy] + 1;
							q.add(new Loc(nx, ny));
						}
					}
					// white room
					else{
						if (count[cx][cy] < count[nx][ny]){
							count[nx][ny] = count[cx][cy];
							q.add(new Loc(nx, ny));
						}
					}
				}
			}
		}

		// print answer and end program
		System.out.print(count[n-1][n-1]);
		br.close();
		return;
	}

	// check location is in map
	private static boolean inRange(int x, int y){
		return (0<=x && x<n && 0<=y && y<n);
	}
}

// location class
class Loc{
	int x;
	int y;
	public Loc(int x, int y){
		this.x = x;
		this.y = y;
	}
}