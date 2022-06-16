#include<iostream>
using namespace std;
void swap(int* &array,int i,int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}
void display(int* &array,int size){
    for (int i = 0; i < size; i++){
        cout<<array[i]<<" ";
    }
    cout<<endl;
    
}
void permutation(int* &array,int pos,int size){
    if(pos==size){
        display(array,size);
        return;
    }
    for (int i = pos; i < size; i++){
        swap(array,i,i+1);
        permutation(array,i+1,size);

        //backtraking step
        //reverting changes
        swap(array,i,i+1);
    }
    
}
int main(){
    int arr[] = {1,2,3};
    int size = 3;
    int * array = arr;

    permutation(array,0,size);

    return 0;
}