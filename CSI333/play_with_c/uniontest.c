#include<stdio.h>

int main(void) {
  enum l_type { VALUE };
  struct booster {
    int ason;
    double bson;
    enum l_type valis;
    union {
      int a;
      int b;
    }param;
  }oneix,tunix;

oneix.param.a= 4;
oneix.param.b = 1;
 printf("%d",oneix.param.a);
 printf("%d",oneix.param.b);
     return 0;
}
