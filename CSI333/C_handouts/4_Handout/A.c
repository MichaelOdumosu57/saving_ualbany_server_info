#include <stdio.h>
#include <string.h>

#define MAX_NAME_LEN 25
#define MAX_EMPLOYEES 1000

struct employee {
char name[MAX_NAME_LEN]; int age; float salary;
};

typedef struct employee EmpRec;

void print_record (EmpRec[]);
void employee_search (EmpRec [], int, char []);
void raise_salary (EmpRec [], int, float);

void print_record (EmpRec x[]) {
int i = 0;  
for (i = 0; i < sizeof(EmpRec)/(sizeof(EmpRec[1])); i++) {
    
printf("s name = %s\n", x[i].name);
printf("s age = %d\n", x[i].age);
printf("s salary = %f\n", x[i].salary);
} 
}
void employee_search (EmpRec division[], int num_emp, char emp_name[]) {
int i = 0;  
for (i = 0; i < num_emp; i++) {
if (strcmp(division[i].name, emp_name) == 0) {
  
print_record(division); return;
}
} 
printf("There is no employee with name: %s\n", emp_name);
} 


void raise_salary (EmpRec division[], int num_emp, float percent_raise) {
  
  int i; 
  float raise_factor; 
raise_factor = 1.0 + percent_raise/100.0;
for (i = 0; i < num_emp; i++) {
  
division[i].salary *= raise_factor;
} 
} 

int main(void){

  EmpRec Google[25];
  int i;
  for( i =0; i <= sizeof(Google)/sizeof(Google[0]); i++){
    printf("%d\n",i);
    Google[i].salary =255.09;  
      }
raise_salary(Google,25, 78);
print_record(Google);    
}
