#include <iostream>
using namespace std;

int main() {
	cout << "Number of courses: ";
	float courses; cin >> courses;

	float total_points{};
	float total_hours{};

	for (short i = 0; i < courses; i++) {
		cout << "Enter your grade and Credit hours separated by a space" << endl;
		float grade, credit_hour;
		cin >> grade >> credit_hour;

		total_points += (grade * credit_hour);
		total_hours += credit_hour;
	}

	printf("Your GPA is %.2f \n", total_points / total_hours);
}