#include <stdio.h>

int new_function(void){
	printf("in new_function");
	return 10;
}

int main(void){

	int a = 5;

	if(a == 5){
		printf("a equals 5"); }

	else{
		printf("a does not equal 5"); }

	for(int index = 0; index != a; index++ ){
		printf("index is at %i.\n", index); }

	int b = a << 2;
	char * char_point = "char_pointer";
	char array[] = "array";

	printf("Using char pointer %s\n", char_point);
	printf("Using array address %s\n", array);
	printf("b has the the value of %i\n", b);



	return 0;

		



}
