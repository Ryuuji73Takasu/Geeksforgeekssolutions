//https://practice.geeksforgeeks.org/problems/break-numbers0435/1
//Given a large number N, write a program to count the ways to break it into three whole numbers such that they sum up to the original number.

// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function Template for C++

class Solution{
public:
    long long countWays(long long N){
        // code here
        return int(((N+1)*(N+2))/2);
    }
};

// { Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        long long N;
        cin>>N;

        Solution ob;
        cout<<ob.countWays(N)<<endl;
    }
    return 0;
}  // } Driver Code Ends