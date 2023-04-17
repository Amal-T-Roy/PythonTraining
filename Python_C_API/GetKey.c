 #include<stdio.h>
 #include<stdlib.h>
 
 char GeneratedKey[32] = {0};
 char OriginalKey[16] = {0};
 
 void main()
 {
	 FILE *file; /*Pointer to the file struct*/
	 file = fopen("/home/amalr/Desktop/PythonTraining/Python_C_API/key.txt", "r"); /*Open text file*/
	 fgets(GeneratedKey, 256, file); /*Read 128 bits from file*/
	 for(int i = 0;i < 32;i++) {
	 	printf("%d ",GeneratedKey[i]);
	 }
	 printf("\n ");
	 
	 for (int i = 0;i < 32; i++) {
		if(GeneratedKey[i] > 96) {
			GeneratedKey[i] = GeneratedKey[i] - 'a' + 10; /*ASCII to decimal  conversion*/
		}
		 else if(GeneratedKey[i] >= 48 && GeneratedKey[i] < 58) {
			GeneratedKey[i] = GeneratedKey[i] - '0'; /*ASCII to decimal  conversion*/
		}
		else {
			printf("Error\n");
		}
    	}
        printf("To int:\n");
        for(int i=0;i<32;i++) {
	 	printf("%d ",GeneratedKey[i]);
	 }
	 printf("\n ");
        
        
        int current = 0;
        for (int i = 0;i < 32; i += 2) {
        	OriginalKey[current++] = (int)(GeneratedKey[i] << 4 | GeneratedKey[i+1]) & 0xFF;
        	printf("%02x ",OriginalKey[i]);
        }
         printf("\n ");
        printf("Final:\n");
        for(int i = 0;i < 16;i++) {
	 	printf("%02x ",OriginalKey[i] & 0xFF);
	 }
	 printf("\n ");
        
    printf("\n");
 }
