#include <stdio.h>
#define SIZE 5

void print_array(int[], int);
void increment(int [], int);
float stat_values(int [], int, int *, int *);
int main(void) {
  int values[SIZE] = {-17, 8, 9, 0, 44}; 
  int num = SIZE; 
  int max, min; 
  float average; 
  average = stat_values(values, num, &max, &min);
  printf("Max. value = %d\n", max); printf("Min. value = %d\n", min);
  printf("Average = %6.1f\n", average);
  
  printf("\nBefore the call to function increment:\n");
  print_array(values, num);

  
  increment(values, num);
  printf("\nAfter the call to function increment:\n");
  print_array(values, num);
  return 0 ;
}  
 
void print_array(int x[], int n) {
  
  int j; 
  
  for (j = 0; j < n; j++)
    printf("%5d", x[j]);
  
  printf("\n");
}

void increment(int x[], int n) {
  
  int j; 
  for (j = 0; j < n; j++)
    x[j]++;
} 
float stat_values (int x[], int n, int *max, int *min) {
  
  int sum; 
  int j; 
  
  *min = *max = x[0]; 
  sum = x[0];
  
  for (j = 1; j < n; j++) {
    
    if (*max < x[j]) *max = x[j];
    
    if (*min > x[j]) *min = x[j];
    
    sum += x[j];
  } 
  
  return (float)sum/(float)n;
} 


