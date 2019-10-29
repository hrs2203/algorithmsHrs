#include <bits/stdc++.h>
using namespace std;

// void belmanFormAdjListAlgo(vector<pair<int,int> >adjList[],int start,int nodes){
//     int dist[nodes];
//     for (int i = 0; i < nodes; i++)
//         dist[i]=2e8;    //setting distance to inf.
//     dist[start-1]=0;  //setting start to 0

//     int edgeCount = 0;
//     int nbr,wt;

//     int nochange=1;

//     for (int x = 0; x < nodes; x++){
//         // if no changes happen then no need to proceed
//         if (nochange==1){
//             nochange = 0;
//             // for each edge
//             for (int i = 0; i < nodes; i++){
//                 edgeCount = adjList[i].size();
//                 // checking all neighbours
//                 for (int j = 0; j < edgeCount; j++){
//                     nbr = adjList[i].at(j).first;
//                     wt  = adjList[i].at(j).second;
//                     if (dist[nbr-1] > dist[i]+wt){
//                         dist[nbr-1] = dist[i]+wt;
//                         nochange = 1;
//                     }
//                 }
//             }
//         }
//     }

//     // check for negative cycle
//     nochange = 0;
//     for (int i = 0; i < nodes; i++){
//         edgeCount = adjList[i].size();
//         for (int j = 0; j < edgeCount; j++){
//             nbr = adjList[i].at(j).first;
//             wt  = adjList[i].at(j).second;
//             if (dist[nbr-1] > dist[i]+wt){
//                 dist[nbr-1] = dist[i]+wt;
//                 nochange = 1;
//             }
//         }
//     }

//     if (nochange==1){
//         cout << "negative cycle detected" << endl;
//     }
    
//     else{
//         for (int i = 0; i < nodes; i++){
//             cout << dist[i] << ' ';
//         }cout << endl;
//     }
// }

void belmanFordAlgo(vector< int > edgeInp[],int edges,int nodes ,int start){
    int dist[nodes];
    for (int i = 0; i < nodes; i++)
        dist[i]=2e8;    //setting distance to inf.
    dist[start-1]=0;  //setting start to 0

    int a,b,w;

    for (int x = 0; x < nodes; x++){
        for (int i = 0; i < edges; i++){
            a = edgeInp[i].at(0)-1; //from
            b = edgeInp[i].at(1)-1; //to
            if (dist[b] > dist[a]+edgeInp[i].at(2)){
                dist[b] = dist[a]+edgeInp[i].at(2);
            }
        }   
    }
    
    for (int i = 0; i < nodes; i++){
        cout << dist[i] << ' ';
    }cout << endl;


}

int main(){
    int nodes,edges,a,b,w;
    cin >> nodes >> edges;
    vector< pair<int,int> > adjList[nodes];
    
    vector< int > edgeInp[edges];
    
    for (int i = 0; i < edges; i++){
        cin >> a >> b >> w;
        
        edgeInp[i].push_back(a);
        edgeInp[i].push_back(b);
        edgeInp[i].push_back(w);

        // edgeInp[edges+i].push_back(b);
        // edgeInp[edges+i].push_back(a);
        // edgeInp[edges+i].push_back(w);
        
        adjList[a-1].push_back(make_pair(b,w));
        adjList[b-1].push_back(make_pair(a,w));
    }
    int startPoint;
    cout << "enter the start point: ";
    cin >> startPoint;

    belmanFordAlgo(edgeInp,edges,nodes,startPoint);

}