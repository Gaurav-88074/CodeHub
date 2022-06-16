#include<iostream>
using namespace std;
bool isPalindrome(string s,int start,int end){
    if(start>end){
        return true;
    }
    else if(s[start]!=s[end]){
        return false;
    }
    else{
        return isPalindrome(s,start+1,end-1);
    }
}
int main(){
    string s = "hello";

    if (isPalindrome(s,0,s.length()-1)){
        cout<<s<<" is palindrome"<<endl;
    }
    else{
        cout<<s<<" isn't palindrome"<<endl;
    }
    
    return 0;
}