#include </usr/include/python3.8/Python.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    Py_Initialize();
    printf("After initialisation\n");
    PyObject* pModule = PyImport_ImportModule("test");
    if (pModule == NULL) {
    PyErr_Print();
    fprintf(stderr, "Failed to load mymodule\n");
    return 1;
}
    printf("After calling module\n");
    printf("Before fetching function\n");
    PyObject* pFunc = PyObject_GetAttrString(pModule,"foo");
    PyErr_Print();
    if (pFunc == NULL || !PyCallable_Check(pFunc)) {
    PyErr_Print();
    fprintf(stderr, "Failed to get func attribute\n");
    Py_DECREF(pModule);
    return 1;
}
    printf("After fetching function\n");
    
    printf("Before calling function\n");
    PyObject* pResult = PyObject_CallObject(pFunc, NULL);
    if (pResult == NULL) {
    PyErr_Print();
    fprintf(stderr, "Failed to call function\n");
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    return 1;
}
    printf("After calling function\n");
    
    //Get result
    long result = 0;
    result = (int) PyLong_AsLong(pResult);
    
    printf("Result = %ld\n",result);
    
    //Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);
    //Py_DECREF(pResult);
    Py_Finalize();

    return 0;
}

