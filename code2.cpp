#include<iostream>
#include<vector>
using namespace std;
void swap(vector<int> &array,int i,int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}
void display(vector<int> &array,int size){
    for (int i = 0; i < size; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;
    
}
void permutation(vector<int> &array,int pos,int size){
    if(pos==size){
        display(array,size);
        return;
    }
    for (int i = pos; i <size; i++){
        // swap(array,i,pos);
        permutation(array,i+1,size);
        // swap(array,i,pos);
    }
    
}
int main(){
    vector<int> array = {1,2,3,4};
    int size = array.size();
    permutation(array,0,size);

    return 0;
}