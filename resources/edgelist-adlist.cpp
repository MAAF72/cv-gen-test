#include <bits/stdc++.h>
using namespace std;
typedef vector <int> VI;
typedef vector <VI> MI;
typedef long long LL;
typedef vector<LL> VL;
typedef vector<VL> ML;
typedef vector<char> VC;
typedef vector<VC> MC;
typedef vector<pair<int,int>> VPII;

int n, m; // n is the number of vertices, m is the number of edges

void addedges(VI adj[], int u, int v){
	adj[u].push_back(v);
	sort(adj[u].begin(),adj[u].end());
	adj[v].push_back(u);
	sort(adj[v].begin(),adj[v].end());
}

void printadj(VI adj[], int n){
	for (int v = 1; v <= n; v++){
		cout << adj[v].size() << " ";
		for (auto x: adj[v])
			cout << x << " ";
		cout << "\n";
	}
}

int main(){
	cin >> n >> m;
	VPII edges; // vector of pair for edges
	int init, end;
	for (int i = 0; i < m; i++){
		cin >> init >> end;
		edges.push_back({init,end});
	}
	sort(edges.begin(),edges.end());
	/* cout << "\n";
	for (int i = 0; i < m; i++){
		cout << edges[i].first << " "<< edges[i].second << "\n";
	} */
	VI adj[n+1]; // adjacency list
	for (int i = 0; i < m; i++){
		addedges(adj,edges[i].first, edges[i].second);
	}
	printadj(adj,n);
	return 0;
}