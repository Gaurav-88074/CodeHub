#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> compute(vector<int> &array){
    sort(array.begin(),array.end());
    for(int i =1 ; i<=array.size() ;i++ ){
        if (array[i-1]!=i){
            return {array[i-1],i};
        }
    }
    return {};
}
int main(){
    
    vector<int> array = {3,1,2,5,3};

    vector<int> res = compute(array);

    cout<<res[0]<<" "<<res[1]<<endl;

    return 0;
}