#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
void *mythread1(void *vargp)
{
    printf("Start [Thread 1] \n");
    for (int i = 1; i <= 10; i++)
        printf("[Thread 1] : %d \n", i);
    printf("Exit from [Thread 1] \n");
    return NULL;
}
void *mythread2(void *vargp)
{
    printf("Start [Thread 2] \n");
    for (int j = 1; j <= 10; j++)
        printf("[Thread 1] : %d \n", j);
    printf("Exit from [Thread 2]\n");
    return NULL;
}
int main()
{
    pthread_t tid1;
    pthread_t tid2;
    printf("before thread\n");
    pthread_create(&tid1, NULL, mythread1, NULL);
    pthread_join(tid1, NULL);
    pthread_create(&tid2, NULL, mythread2, NULL);
    pthread_join(tid2, NULL);
    exit(0);
}
