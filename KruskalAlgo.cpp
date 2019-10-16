#include <bits/stdc++.h>
using namespace std;

bool comp( const pair< int,pair< int,int > > &a , const pair< int,pair< int , int > > &b ){
    return ( a.first < b.first );
}

pair<int,int> heightNode(int arr[],int node){
    int count = 0;
    int root = node;
    while( arr[node]!=node ){
        count++;
        node = arr[node];
        root = node;
    }return make_pair(root,count);
}

void KruskalAlgo( vector<pair<int,int> > graph[] , int nodes ){
    vector< pair<int,pair<int,int> > > tempVal;
    int a;
    int b;
    int w;

    for(int i=0;i<nodes;i++){
        for(int j=0;j<graph[i].size();j++){
            a = i+1;
            b = graph[i].at(j).first;
            w = graph[i].at(j).second;
            tempVal.push_back( make_pair( w , make_pair( a , b ) ) );
        }
    }

    // sort
    sort(tempVal.begin(),tempVal.end() , comp);

    int tempLen = tempVal.size();

    int sumVal = 0;
    
    vector< pair<int,int> > path;
    
    int group[nodes]; // stores the root
    for(int i=0;i<nodes;i++){
        group[i]=i;
    }

    // cout << "path for KruskalAlgo is " << endl;
    for(int i=0;i<tempLen;i++){
        a = tempVal.at(i).second.first-1;
        b = tempVal.at(i).second.second-1;

        pair<int,int> ha,hb;
        ha=heightNode(group,a);
        hb=heightNode(group,b);
        
        if ( ha.first!=hb.first ){
            // finding the height of a and b
            
            if (ha.second>hb.second){
                group[hb.first]=ha.first;
            }else{
                group[ha.first]=hb.first;
            }
            path.push_back(make_pair(a+1,b+1));
            sumVal += tempVal.at(i).first;

            // for (int j = 0; j < nodes; j++)
            // {
            //     cout << group[j] << " ";
            // }
            // cout << endl;
        }
    }

    // cout << "pairs are -> " ;
    // for(int i=0;i<path.size();i++){
    //     cout << " (" << path.at(i).first << "," << path.at(i).second <<") ";
    // }cout << endl;
    cout << sumVal << endl;

}

int main(){
    int nodes,vertices;
    cin >> nodes >> vertices;
    // implementing weighed graph
    vector<pair<int,int> > graph[nodes];

    int a,b,w;

    for(int i=0;i<vertices;i++){
        cin >> a >> b >> w;
        graph[a-1].push_back(make_pair(b,w));
        graph[b-1].push_back(make_pair(a,w)); // creating directed graph
    }

    // cout << "created graph as \nnode -> neighbour,pair" << endl;
    // for(int i=0;i<nodes;i++){
    //     cout << i+1 << " -> ";
    //     for (int j = 0; j < graph[i].size(); j++)
    //         cout << graph[i].at(j).first << "," << graph[i].at(j).second << " ";
    //     cout << endl;
    // }

    // cout << endl ;

    KruskalAlgo(graph,nodes);

}