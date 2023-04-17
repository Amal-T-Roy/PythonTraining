CC = gcc
CFLAGS = -I/usr/include/python3.8
LDFLAGS =  -lcrypto -lpython3.8
test_my_program: final.c
	$(CC) $(CFLAGS) final.c -o TEST $(LDFLAGS) 

.PHONY: clean
clean:
	rm -f TEST



