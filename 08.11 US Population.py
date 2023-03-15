// Header files

#include<iostream>

#include<iomanip>

#include<fstream>

#include<cmath>

using namespace std;

// function.

double Avg_chng(long arr[], int len){

// Declare variables.

long val = 0;

// for loop

for(int i=0; i<len-i; i++){

val += abs(arr[i]-arr[i+1]);

}

// return value

return val/(len-1);

}

// function.

int great_inc(long arr[], int len){

// Declare variables.

int ind_val = 0;

long res = arr[1]-arr[0];

// for loop

for(int i=1; i<len; i++){

// Check condition

if((arr[i]-arr[i-1])>res){

ind_val = i;

res = arr[i]-arr[i-1];

}

}

// return value

return 1950+ind_val;

}

// function.

int small_inc(long arr[], int len){

// Declare variables.

int ind_val = 0;

long res = arr[1]-arr[0];

// for loop

for(int i=1; i<len; i++){

// Check condition

if((arr[i]-arr[i-1])<res){

ind_val = i;

res = arr[i]-arr[i-1];

}

}

// return value

return 1950+ind_val;

}

// function.

int main(){

// Declare variables.

long pop_arr[50];

int i = 0;

// open file

ifstream input("USPopulation.txt");

// check condition for error

if(!input){

cout<<"Error";

return 1;

}

// input values in array

while(input>>pop_arr[i]){

i++;

}

input.close();

cout<<setprecision(2)<<fixed<<showpoint;

// Display result.

cout<<"The average annual change in population during the period from 1950 through 1990 is: " << Avg_chng(pop_arr,i) << endl;

cout<<"The year with the greatest increase in population during the period from 1950 through 1990 is: " << great_inc(pop_arr,i)<<endl;

cout<<"The year with the smallest increase in population during the period from 1950 through 1990 is: " << small_inc(pop_arr,i)<<endl;

return 0;

}