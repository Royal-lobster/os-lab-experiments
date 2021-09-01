// USE THE BELOW CODE TO RUN THE FILE
// gcc -pthread -o threads threads.c

#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

void *mythread(void *vargp){
  for (int i = 0; i < 5; i++) {
    printf("Hello Srujan ! \n");
    sleep(1);
  }
  return NULL;
}

int main()
{
  pthread_t tid;
  printf("before thread\n");
  // create thread with thread id 
  pthread_create(&tid,NULL,mythread,NULL);
  // Join the thread to main thread and wait for the thread to complete
  pthread_join(tid,NULL);
  printf("after thread\n");
  exit(0);
}