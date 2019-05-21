#include <iostream>
#include <pthread.h>
#include <string.h>
#include <unistd.h>
#include <cstdlib>

using namespace std;

class Customer {
	public:
	string name;
	int hamburger;
	int fries;
	int soda;
	void run();

	Customer(int x) {
		hamburger = 0;
		fries = 0;
		soda = 0;
	}
};

class Chef {
	void getRand(int arr[]);
};

void Customer::run(){
	cout << "Customer " << name << "is eating..." << endl;
	usleep(1000);
	cout << "Customer " << name << "has finished eating." << endl;
}

void Chef::getRand(int arr[]) {
	int x, y;
	x = rand() % 2 + 1;
	y = rand() % 2 + 1;
	while(x == y)
		y = rand() % 2 + 1;
}

int main(){
	int c1_count = 0;
	int c2_count = 0;
	int c3_count = 0;
	pthread_t customer1(Customer(), 1);
	pthread_t customer2(Customer(), 2);
	pthread_t customer3(Customer(), 3);
	customer1.hamburger = 1;
	customer2.fries = 1;
	customer3.soda = 1;
	return 0;
}
